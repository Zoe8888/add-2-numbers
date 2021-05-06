import tkinter as tk

from tkinter import messagebox()


top = tk.Tk()


def hello_callback():
    tk.Message("Test", "Test")


b = tk.Button(top, text="Hello World", command=hello_callback())


b.pack()


top.mainloop()