from lxml import etree

def update_svg_title(template_path, title, output_path):
    # Parse the SVG file
    tree = etree.parse(template_path)
    root = tree.getroot()

    # Find the text element by ID
    title_element = root.find(".//*[@id='titleText']")
    
    if title_element is not None:
        # Update the text content
        title_element.text = title
        # Save the modified SVG to the output path
        tree.write(output_path, pretty_print=True, xml_declaration=True, encoding='UTF-8')
        print(f"Updated SVG saved to: {output_path}")
    else:
        print("Title element not found.")

# Example usage
template_svg_path = 'template.svg'  # Path to your template SVG
new_title = 'Dynamic Title Here'     # Title to be inserted
output_svg_path = 'output.svg'       # Output SVG file path

update_svg_title(template_svg_path, new_title, output_svg_path)

