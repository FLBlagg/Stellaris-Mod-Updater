import os
import re

def find_stellaris_mod_folder():
    # Check common locations for the Stellaris mod directory
    possible_paths = [
        os.path.expanduser(r'~/Documents/Paradox Interactive/Stellaris/mod'),
        os.path.expanduser(r'~/OneDrive/Documents/Paradox Interactive/Stellaris/mod')
    ]

    for path in possible_paths:
        if os.path.isdir(path):
            return path

    # If no path was found, prompt the user for the path
    return input("Stellaris mod folder not found. Please enter the path to your Stellaris mod folder: ")

# Find the Stellaris mod folder path
mod_folder_path = find_stellaris_mod_folder()
print(f"Using Stellaris mod folder path: {mod_folder_path}")

# Regular expression pattern to find and capture the folder name in the path
path_pattern = re.compile(r'path="workshop/content/\d+/(\d+)/"')
# Regular expression pattern to check if "path=mod/" already exists in the file
mod_path_pattern = re.compile(r'path="mod/[^"]+"')

def modify_file_path(file_path):
    print(f"Processing file: {file_path}")

    # Open the .mod file and read its content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Print the current content for debugging purposes
    print("Current file content:")
    print(content)

    # Check if "path=mod/" already exists
    if not mod_path_pattern.search(content):
        print("Mod path not found. Attempting to replace or add path.")

        # Function to replace the path in the file content
        def replacement(match):
            folder_name = match.group(1)  # Extract the folder name
            print(f"Found workshop path with folder name: {folder_name}")
            return f'path="mod/{folder_name}"'

        # Replace the path using the replacement function
        modified_content = re.sub(path_pattern, replacement, content)

        # If no replacement was made, add the path attribute
        if modified_content == content:
            print("No workshop path found. Adding mod path.")
            folder_name = os.path.basename(file_path).replace('.mod', '')
            modified_content += f'\npath="mod/{folder_name}"'

        # Print the modified content for debugging purposes
        print("Modified file content:")
        print(modified_content)

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        print(f"Updated path in {file_path}")
    else:
        print(f"No update needed for {file_path}")

# Iterate over all files in the specified directory
for filename in os.listdir(mod_folder_path):
    # Check if the file is a .mod file
    if filename.endswith('.mod'):
        # Construct the full file path
        file_path = os.path.join(mod_folder_path, filename)
        # Modify the file path within the .mod file
        modify_file_path(file_path)

print("All .mod files have been checked and updated if necessary.")

# Add this line to keep the console window open
input("Press Enter to exit...")
