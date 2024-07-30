import os
import shutil
from datetime import datetime

def create_folder(path: str, folder_name: str) -> str:
    folder_path: str = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def sort_files(source_path: str, sort_key: str, date_option: str = None) -> None:
    for root_dir, sub_sir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            folder_name: str = ""

            if sort_key == "1":
                folder_name: str = os.path.splitext(filename)[1][1:]
            elif sort_key == "2":
                folder_name: str = filename[0].upper()
            elif sort_key == "3":
                mod_time = os.path.getmtime(file_path)
                if date_option == "Day":
                    folder_name: str = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
                elif date_option == "Month":
                    folder_name: str = datetime.fromtimestamp(mod_time).strftime('%Y-%m')
                elif date_option == "Year":
                    folder_name: str = datetime.fromtimestamp(mod_time).strftime('%Y')

            if folder_name:
                target_folder: str = create_folder(source_path, folder_name)
                target_path: str = os.path.join(target_folder, filename)
                shutil.move(file_path, target_path)

def remove_empty_folders(source_path: str) -> None:
    for root_dir, sub_sir, filenames in os.walk(source_path, topdown=False):
        for current_dir in sub_sir:
            folder_path: str = os.path.join(root_dir, current_dir)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
