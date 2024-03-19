import os
import re

# Define the directory containing your .mod files
mod_folder_path = r'C:\Users\Shadow\Documents\Paradox Interactive\Stellaris\mod'

# Regular expression pattern to find and capture the folder name in the path
path_pattern = re.compile(r'path="workshop/content/\d+/(\d+)/"')

def modify_file_path(file_path):
    # Open the .mod file and read its content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Function to replace the path in the file content
    def replacement(match):
        folder_name = match.group(1)  # Extract the folder name
        return f'path="mod/{folder_name}"'
    
    # Replace the path using the replacement function
    modified_content = re.sub(path_pattern, replacement, content)
    
    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

# Iterate over all files in the specified directory
for filename in os.listdir(mod_folder_path):
    # Check if the file is a .mod file
    if filename.endswith('.mod'):
        # Construct the full file path
        file_path = os.path.join(mod_folder_path, filename)
        # Modify the file path within the .mod file
        modify_file_path(file_path)

print("All .mod files have been updated.")