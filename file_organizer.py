import os
import shutil
import logging
logging.basicConfig(filename = "organizer.log",
                    level = logging.INFO,
                    format = "%(asctime)s - %(message)s",
                    datefmt = "%Y-%m-%d %H:%M:%S")

FILE_CATEGORIES = {
    "Images" : [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos" : [".mp4", ".mov", ".flv", ".mkv", ".avi"],
    "Documents" : [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"],
    "Audio" : [".mp3",".wav",".aac",".flac"],
    "Archives" : [".zip", ".rar", ".tar", ".7z", ".gz"],
    "Data" : [".csv", ".json", ".xml"],
    "Others" : []
}

def organize_files(directory, dry_run):
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    for category in FILE_CATEGORIES:
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok = True)
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isdir(file_path):
            continue

        file_moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                dest_path = os.path.join(directory, category, filename)
                name, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(dest_path):
                    dest_path = os.path.join(directory, category, f"{name}_{counter}{ext}")
                    counter +=1
                if dry_run:
                    print(f"[Dry Run] Would move: {filename} -> {category}/")
                else:
                    shutil.move(file_path, dest_path)
                    logging.info(f"Moved: {filename} -> {category}/")
                    print(f"Moved: {filename} -> {category}/")
                file_moved = True
                break
        if not file_moved:
                if dry_run:
                    print(f"[Dry Run] Would move: {filename} -> Others/")
                else:
                    shutil.move(file_path, os.path.join(directory, "Others", filename))
                    logging.info(f"Moved: {filename} -> Others/")
                    print(f"Moved: {filename} -> Others/")

directory_to_organize = input("Enter the directory path to organize: ")
dry_run = input("Dry run? (y/n): ").strip().lower() == "y"
organize_files(directory_to_organize, dry_run)