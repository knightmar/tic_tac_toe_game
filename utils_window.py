import tkinter as tk
from tkinter import ttk


def clear():
    print("clear")


debugWin = tk.Tk()
debugWin.title("test")

clear_btn = ttk.Button(debugWin, text="Clear button", command=clear)
clear_btn.pack()

debugWin.mainloop()
