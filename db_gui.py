import tkinter as tk
from tkinter import ttk


def main_window():

    def ok_cmd():
        print("Patient name: {}".format(patient_name_entry.get()))
        print("Patient id: {}".format(patient_id_entry.get()))
        print("Clicked OK button")

    root = tk.Tk()
    root.title("Blood Donor Database Window")
    root.geometry('600x300')

    ttk.Label(root, text="Blood Donor Database").grid(column=0, row=0,
                                                      columnspan=2)
    ttk.Label(root, text="Name:").grid(column=0, row=1)

    patient_name_entry = tk.StringVar()
    patient_name_entry.set("Enter a name here")
    ttk.Entry(root, width=50, textvariable=patient_name_entry).grid(column=1, row=1)

    ttk.Label(root, text="Id:").grid(column=0, row=2)
    patient_id_entry = tk.StringVar()
    ttk.Entry(root, textvariable=patient_id_entry).grid(column=1,row=2)

    blood_letter_selection = tk.StringVar()
    ttk.Radiobutton(root, text="A", variable=blood_letter_selection,
                    value="A").grid(column=0, row=3)
    ttk.Radiobutton(root, text="B", variable=blood_letter_selection,
                    value="B").grid(column=0, row=4)
    ttk.Radiobutton(root, text="AB", variable=blood_letter_selection,
                    value="AB").grid(column=0, row=5)
    ttk.Radiobutton(root, text="O", variable=blood_letter_selection,
                    value="O").grid(column=0, row=6)

    ttk.Button(root, text="OK", command=ok_cmd).grid(column=1, row=6)
    root.mainloop()


if __name__ == '__main__':
    main_window()
