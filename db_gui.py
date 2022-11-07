import tkinter as tk
from tkinter import ttk


def main_window():
    root = tk.Tk()
    root.title("Blood Donor Database Window")
    root.mainloop()
    root.geometry('600x300')

    ttk.Label(root, text="Blood Donor Database").grid(column=0, row=0,
                                                     columnspan=2)
    ttk.Label(root, text="Name:").grid(column=0, row=1)
    ttk.Entry(root, width=0).grid(column=1, row=1)


if __name__ == '__main__':
    main_window()
