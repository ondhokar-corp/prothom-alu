import os
from datetime import datetime
import re

# Define the base directory where posts will be saved
BASE_DIR = os.path.expanduser('./')
def slugify(title):
    """
    Converts a string into a slug suitable for URLs and filenames:
    - Converts to lowercase
    - Replaces spaces and non-word characters with hyphens
    - Strips out leading/trailing hyphens
    """
    title = title.lower()  # Convert to lowercase
    title = re.sub(r'[^\w\s-]', '', title)  # Remove non-alphanumeric characters
    title = re.sub(r'\s+', '-', title)  # Replace spaces with hyphens
    return title.strip('-')  # Strip leading/trailing hyphens

def create_post_file():
    # Get inputs from user
    title = input("Enter the title: ")
    author = input("Enter the author: ")

    # Display category options
    print("Select a category:")
    categories = {
        1: ('national', 'জাতীয়'),
        2: ('international', 'আন্তর্জাতিক'),
        3: ('sports', 'খেলা'),
        4: ('tech', 'প্রযুক্তি'),
        5: ('editorial', 'সম্পাদকীয়')
    }

    for key, (eng_name, _) in categories.items():
        print(f"{key}. {eng_name.capitalize()}")

    # Get the category selection
    category_choice = int(input("Enter the number corresponding to the category: "))

    # Validate the category choice
    if category_choice not in categories:
        print("Invalid choice, exiting...")
        return

    # Get the Bangla path for the selected category
    category_eng, category_bangla = categories[category_choice]

    # Slugify the title for the filename
    slugified_title = slugify(title)

    # Get the current date for the file name
    today = datetime.now().strftime('%Y-%m-%d')

    # Define the path based on the selected category
    category_path = f'News/{category_bangla}/_posts'

    # Full path to the directory
    full_dir = os.path.join(BASE_DIR, category_path)

    # Create the directory if it does not exist
    os.makedirs(full_dir, exist_ok=True)

    # Define the filename with date and slugified title
    file_name = f'{today}-{slugified_title}.md'
    file_path = os.path.join(full_dir, file_name)

    # Create the markdown file with front matter
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write(f'title: "{title}"\n')
        f.write(f'author: "{author}"\n')
        f.write(f'place: ""\n')
        f.write('---\n\n')

    print(f"Post created: {file_path}")

if __name__ == "__main__":
    create_post_file()

