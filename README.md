# File Organizer Script

A Python automation script that scans a directory and sorts files into
categorized subfolders based on their file extension.

## Features
- Automatically sorts files into Images, Videos, Documents, Audio, Archives, Data, and Others
- Dry-run mode to preview changes before actually moving files
- Collision handling — never overwrites existing files (renames to file_1, file_2...)
- Logging — every moved file is recorded in organizer.log with a timestamp

## Modules Used
- os — folder scanning, path building, directory creation
- shutil — moving files
- logging — recording moved files with timestamps

## How to Run
python file_organizer.py

## Usage
Enter the directory path to organize: C:/Users/YourName/Downloads
Dry run? (y/n): y
