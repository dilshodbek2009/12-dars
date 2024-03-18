from tkinter import Tk, Menubutton, RAISED, Menu, Scale, Toplevel, Label, Button, colorchooser

from setuptools.logging import configure

window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
center_x = int(width / 2 - 500 / 2)
center_y = int(height / 2 - 450 / 2)
window.geometry(f"{500}x{450}+{center_x}+{center_y}")

window.mainloop()