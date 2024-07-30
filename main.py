import GUI_for_fs as gui
import customtkinter as Ctk

# Główna funkcja tworząca okno aplikacji
def create_main_window():
    Ctk.set_appearance_mode("System")
    Ctk.set_default_color_theme("dark-blue")

    root = Ctk.CTk()
    root.title("File sorter")
    root.resizable(0, 0)

    input_frame, path_entry, key_entry, date_entry = gui.create_input_frame(root)
    input_frame.grid(column=0, row=0, padx=20, pady=20)

    button_frame = gui.create_button_frame(root, path_entry, key_entry, date_entry)
    button_frame.grid(column=0, row=1, padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()
