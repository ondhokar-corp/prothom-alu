import os
import re
import yaml


def clean_filename(input_string):
    # Keep only the first 40 characters
    trimmed = input_string[:40]
    # Remove unwanted characters (anything not a word character, space, underscore, or hyphen)
    cleaned = re.sub(r'[^\w\s-]', '', trimmed)
    return cleaned

def split_title_into_parts(title, max_length=55):
    parts = []
    while len(title) > max_length:
        # Find the last space within the max_length limit
        split_index = title.rfind(' ', 0, max_length)
        
        if split_index == -1:  # No space found, force split at max_length
            split_index = max_length

        # Append the current part and update the title
        parts.append(title[:split_index].strip())
        title = title[split_index:].strip()

    # Add the remaining part
    if title:
        parts.append(title)

    return parts

# Define the base directory
base_dir = '../p/News/'
import svgwrite
import base64

def generate_svg(title, image):
  # Define dimensions
  width = 1200
  height = 900
  bottom_rect_height = 0.2* height  # 10% of total height
  bottom_rect_y = height - bottom_rect_height  # Position at the bottom
  
  # Define dimensions for the new SVG element
  new_svg_height = 70  # Height of the new SVG element
  new_svg_y = bottom_rect_y - new_svg_height - 5  # Position slightly above the bottom rectangle (5px gap)
  
  # Read and encode the JPG image
  image_path = image  # Ensure this is the correct path to your JPG image
  with open(image_path, "rb") as img_file:
      encoded_image = base64.b64encode(img_file.read()).decode('utf-8')
  
  # Read and encode the SVG file
  svg_file_path = 'logo.png'  # Ensure this is the correct path to your SVG file
  with open(svg_file_path, "rb") as svg_file:
      encoded_svg = base64.b64encode(svg_file.read()).decode('utf-8')
  
  # Create an SVG drawing
  dwg = svgwrite.Drawing(f"{clean_filename(title)}.svg", size=(width, height))
  
  # Add a pattern to the SVG using the base64 encoded image
  pattern = dwg.defs.add(dwg.pattern(id='imgPattern', size=(width, height), patternUnits="userSpaceOnUse"))
  pattern.add(dwg.image(href=f"data:image/jpeg;base64,{encoded_image}", 
                        insert=(0, 0), 
                        size=(width, height), 
                        preserveAspectRatio='xMidYMid slice'))
  
  # Create a rectangle filled with the pattern
  dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill='url(#imgPattern)'))
  
  # Add the new rectangle at the bottom with a lime fill
  dwg.add(dwg.rect(insert=(0, bottom_rect_y), size=(width, bottom_rect_height), fill='#f2afb9'))
  
  # Add text to the bottom rectangle
  text_content = title  # Change this to the desired text
  title_parts = split_title_into_parts(text_content)
  text_x = 32  # Positioning the text 10px from the left
  if len(title_parts) == 1:
    baseline = 120
  else:
    baseline= 60
  text_y = height - baseline
  line_height = 60
  
  # Add the text element with left alignment
  # Loop through the title parts in reverse order
  for part in reversed(title_parts):
      # Add the text to the SVG
      dwg.add(dwg.text(
          part, 
          insert=(text_x, text_y), 
          text_anchor="start",  # Left align the text
          alignment_baseline="middle",  # Center the text vertically
          font_size="48px", 
          fill="black"
      ))
      
      # Move the y_position up for the next part
      text_y -= line_height

  
  # Add the encoded SVG above the bottom rectangle
  new_svg_width = 200  # Width of the new SVG element
  dwg.add(dwg.image(href=f"data:image/png+xml;base64,{encoded_svg}", 
                     insert=((width - new_svg_width) / 2, new_svg_y), 
                     size=(new_svg_width, new_svg_height), 
                     preserveAspectRatio='xMidYMid meet'))  # Center the SVG
  
  # Save the SVG file
  dwg.save()
  

# Function to extract the title from the frontmatter of a markdown file
def get_md_title(md_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Match the frontmatter using regex
        frontmatter = re.search(r'---\n(.*?)\n---', content, re.DOTALL)
        if frontmatter:
            yaml_content = frontmatter.group(1)
            # Parse YAML frontmatter
            data = yaml.safe_load(yaml_content)
            title = data.get('title', 'No title found')
            img = data.get('cover', {}).get('image', 'No cover image found')
            if img == 'No cover image found':
                image = ""
            elif img.startswith("http"):
                image = ""
            else:
                image = os.path.join(os.path.dirname(md_file_path), img)
            return title, image
        return 'No frontmatter found'

# Traverse the directory structure to find markdown files
for root, dirs, files in os.walk(base_dir):
    # Look for _posts directories
    if '_posts' in root:
        for subdir in dirs:
            subdir_path = os.path.join(root, subdir)
            for file in os.listdir(subdir_path):
                if file.endswith('.md'):
                    md_file_path = os.path.join(subdir_path, file)
                    title, image = get_md_title(md_file_path)
                    print(f"Title: {title}, Image: {image}")
                    if image != "":
                      generate_svg(title, image)
