from pytube import YouTube
from tkinter import Tk, Menubutton, RAISED, Menu, Scale, Toplevel, Label, Button, colorchooser, Entry

from setuptools.logging import configure

# window = Tk()
# width = window.winfo_screenwidth()
# height = window.winfo_screenheight()
# center_x = int(width / 2 - 500 / 2)
# center_y = int(height / 2 - 450 / 2)
# window.geometry(f"{500}x{450}+{center_x}+{center_y}")
#
# def puk():
#     entry.get()
#
#
#
#
# entry = Entry(window)
# entry.pack()
# button = Button(window, text="give", command=puk)
# button.pack()


url = "https://youtu.be/kRDX0v8Aln0?si=2r-nqXNxzmz9E4YM"

yt = YouTube(url)

stream = yt.streams.get_highest_resolution()
stream.download("./nnn/kkk")

# window.mainloop()