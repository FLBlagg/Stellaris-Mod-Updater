# Stellaris-Mod-Updater
A simple python and batch file that runs a script to rename the "path=steam/common/..." string to "path=mod/..." for correct mod syntax

# GUIDE

1. Place SMPU.py into your Stellaris mod folder
2. Run Stellaris Mod Updater2.bat
3. Follow prompts (if any)

## How to Use the Script

### Step 1: Ensure Python is Installed
- Make sure Python is installed on your computer.
- Check this by running `python --version` in the Command Prompt.
- If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

### Step 2: Download the `.bat` File and Python Script
- Download or clone this repository, which includes the `.bat` file and the `SMPU.py` Python script.

### Step 3: Running the Script
1. **Double-click the `.bat` file**: 
    - Once the `.bat` file is on your desktop or in a convenient location, double-click it to run the script.
    - The script will find your Stellaris mod folder and modify the `.mod` files as needed.

2. **Follow on-screen prompts**: 
    - The script may prompt you to enter the mod folder path if it can't find it automatically.

### Step 4: Modifying the `.bat` File
If you need to adjust the paths, follow these steps:

1. **Edit the `.bat` file**: Right-click the `.bat` file and select "Edit" to open it in Notepad or another text editor.

2. **Update the Python script path**: 
    - Locate the line with `cd "C:/path/to/your/python/script"`.
    - Change `"C:/path/to/your/python/script"` to match the actual path where you stored `SMPU.py`.

3. **Optional - Python Path**: 
    - If Python isn't in your PATH, update the line where Python is called:
    ```bat
    "C:/Python39/python.exe" SMPU.py
    ```
    - Replace the path with the location of your Python installation.

### Step 5: Running the `.bat` File Again
After making changes, double-click the `.bat` file to run it again.
