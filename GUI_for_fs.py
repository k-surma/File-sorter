import file_sorter as fs
import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import TclError, ttk, messagebox


def sort_button_click(path_entry, key_entry):
    source_path = path_entry.get()
    sort_key = key_entry.get()[0]
    if source_path[0]=='"' and source_path[-1]=='"':
        source_path =source_path[1:-1]

    if not os.path.exists(source_path):
        messagebox.showerror("Error", "Invalid path. Please provide a valid path.")
        return
    if sort_key not in ['1', '2', '3']:
        messagebox.showerror("Error", "Invalid sorting key. Please choose 1, 2, or 3.")
        return

    fs.sort_files(source_path, sort_key)
    fs.remove_empty_folders(source_path)
    messagebox.showinfo("Success", "Files sorted successfully.")


def create_input_frame(container):

    frame = ttk.Frame(container)

    ttk.Label(frame, text="Please provide a path to sort: ").grid(column=0, row=0, sticky=tk.W)
    path_entry = ttk.Entry(frame, width=30)
    path_entry.focus()
    path_entry.grid(column=1, row=0, sticky=tk.W)

    ttk.Label(frame, text="Choose sorting key:").grid(column=0, row=1, sticky=tk.W)
    key_entry = ttk.Combobox(frame, values=['1. File Extension', '2. First letter', '3. Modification time'], width=27)
    key_entry.grid(column=1, row=1, sticky=tk.W)
    key_entry.set('Set sorting key')

    for widget in frame.winfo_children():
        widget.grid(padx=10, pady=10)

    return frame


def create_button_frame(container, path_entry, key_entry):

    frame = ttk.Frame(container)
    sort_button = ttk.Button(frame, text='Sort', command=lambda: sort_button_click(path_entry, key_entry))
    sort_button.grid(row=2, padx=10, pady=10)
    return frame




