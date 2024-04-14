import GUI_for_fs as gui
import file_sorter as fs
import tkinter as tk
def create_main_window():

    root = tk.Tk()
    root.title("File sorter")
    root.resizable(0, 0)

    input_frame = gui.create_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = gui.create_button_frame(root, input_frame.winfo_children()[1], input_frame.winfo_children()[3])
    button_frame.grid(column=0, row=1)

    root.mainloop()

    root.destroy()


if __name__ == "__main__":
    create_main_window()