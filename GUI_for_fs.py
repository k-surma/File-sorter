import customtkinter as Ctk
import os
import file_sorter as fs
from tkinter import messagebox


# Funkcja obsługująca kliknięcie przycisku sortowania
def sort_button_click(path_entry, key_entry, date_entry):
    source_path = path_entry.get()
    sort_key = key_entry.get()[0]
    date_option = date_entry.get()

    if source_path[0] == '"' and source_path[-1] == '"':
        source_path = source_path[1:-1]

    if not os.path.exists(source_path):
        messagebox.showerror("Error", "Invalid path. Please provide a valid path.")
        return
    if sort_key not in ['1', '2', '3']:
        messagebox.showerror("Error", "Invalid sorting key. Please choose 1, 2, or 3.")
        return

    fs.sort_files(source_path, sort_key, date_option)
    fs.remove_empty_folders(source_path)
    messagebox.showinfo("Success", "Files sorted successfully.")


# Funkcja aktualizująca stan pola wyboru daty
def update_date_entry_state(event, key_entry, date_entry):
    print(key_entry.get()[0])
    if key_entry.get()[0] == '3':
        date_entry.configure(state='normal')
    else:
        date_entry.configure(state='disabled')


# Funkcja tworząca ramkę wejściową
def create_input_frame(container):
    frame = Ctk.CTkFrame(container)

    Ctk.CTkLabel(frame, text="Please provide a path to sort: ").grid(column=0, row=0, sticky=Ctk.W, padx=10, pady=10)
    path_entry = Ctk.CTkEntry(frame, width=300)
    path_entry.focus()
    path_entry.grid(column=1, row=0, sticky=Ctk.W, padx=10, pady=10)

    Ctk.CTkLabel(frame, text="Choose sorting key:").grid(column=0, row=1, sticky=Ctk.W, padx=10, pady=10)
    key_entry = Ctk.CTkComboBox(frame, values=['1. File Extension', '2. First letter', '3. Modification date'],
                                width=300)
    key_entry.grid(column=1, row=1, sticky=Ctk.W, padx=10, pady=10)
    key_entry.set('Set sorting key')
    key_entry.bind("<<ComboboxSelected>>", command=lambda event: update_date_entry_state(event, key_entry, date_entry))

    Ctk.CTkLabel(frame, text="Date sorting option:").grid(column=0, row=2, sticky=Ctk.W, padx=10, pady=10)
    date_entry = Ctk.CTkComboBox(frame, values=['Day', 'Month', 'Year'], width=300)
    date_entry.grid(column=1, row=2, sticky=Ctk.W, padx=10, pady=10)
    date_entry.set('Day')
    date_entry.configure(state='disabled')

    return frame, path_entry, key_entry, date_entry


# Funkcja tworząca ramkę przycisków
def create_button_frame(container, path_entry, key_entry, date_entry):
    frame = Ctk.CTkFrame(container)
    sort_button = Ctk.CTkButton(frame, text='Sort',
                                command=lambda: sort_button_click(path_entry, key_entry, date_entry))
    sort_button.grid(row=0, padx=10, pady=10)
    return frame
