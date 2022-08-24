
import os
import pandas as pd

path = os.getcwd()

df = pd.DataFrame({'opentrons_repo': [path]})

df.to_csv("paths.csv")

from tkinter import filedialog
from tkinter import *

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global name
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)
    name = filename

root = Tk()
root.geometry("800x800")
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=0, column=3)



mainloop()