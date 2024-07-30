import os
import shutil
from datetime import datetime

def create_folder(path: str, folder_name: str) -> str:
    folder_path: str = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def get_sorting_key() ->str:
    print("Choose sorting key:")
    print("1. File extension")
    print("2. First letter")
    print("3. Modification time")

    choice: str = input("Enter your choice: ")

    return choice

def sort_files(source_path: str, sort_key: str)->None:
    for root_dir, sub_sir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            folder_name: str = ""

            if sort_key =="1":
                folder_name: str = os.path.splitext(filename)[1][1:]
            elif sort_key == "2":
                folder_name: str = filename[0].upper()
            elif sort_key == "3":
                mod_time = os.path.getmtime(file_path)
                folder_name: str = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')

            if folder_name:
                target_folder: str=create_folder(source_path, folder_name)
                target_path: str=os.path.join(target_folder, filename)
                shutil.move(file_path, target_path)

def remove_empty_folders(source_path: str)->None:
    for root_dir, sub_sir, filenames in os.walk(source_path, topdown=False):
        for current_dir in sub_sir:
            folder_path: str = os.path.join(root_dir, current_dir)

            if not os.listdir(folder_path):
                os.rmdir(folder_path)

def main():

    user_input: str=input("Please provide a path to sort: ")
    while not os.path.exists(path=user_input):
        print("Invalid path. Please provide a valid path.")
        user_input: str = input("Please provide a path to sort: ")

    sort_key: str = get_sorting_key()
    while sort_key not in ["1", "2", "3"]:
        print("Invalid sorting key")

    sort_files(user_input, sort_key)
    remove_empty_folders(source_path=user_input)
    print("Files sorted successfully")

if __name__=="__main__":
    main()
