## Python File Organizer

This is a Python project I built to organize files into different folders based on their file extensions.

The program searches for a folder by name on the available Windows drives. Before organizing, it shows the folder location and the files inside it so the user can confirm the selection.

## How It Works

The program creates five folders: "Document", "Image", "Python", "Web", and "Other".

It moves files into these folders based on their extensions. For example, PDF files go into "Document", images go into "Image", and Python files go into "Python". Files that don't match the listed extensions go into "Other".

The program also handles uppercase extensions such as ".JPG" and ".PDF". Existing subfolders are skipped during file organization.

## Requirements

- Python 3.10 or later
- Windows

## How to Run

1. Download or clone this repository.

2. Make sure Python 3.10 or later is installed.

3. Open a terminal in the project folder.

4. Run the following command:
   
   python file_organizer.py

5. Enter the name of the folder you want to organize.

6. Check the displayed folder path and file list.

7. Type "yes" to start organizing the files.

Technologies Used

- Python
- "os"
- "ctypes"
- "shutil"

## Note

The program moves files from their original locations. Check the selected folder carefully and test with sample files 

The folder search may take some time because the program searches through available drives.

## What I Learned

While building this project, I practiced working with files and directories, searching through drives, handling file extensions, creating folders, and moving files using Python.
