
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
root.geometry("800x150")
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=0, column=3)

label_extra1 = Label(text='Navigate to the folder containing your Rspript.exe',font=('Helvatical bold',14))
label_extra1.place(relx=0,rely=0.2)

label_extra1 = Label(text='Example: C:\Users\opentrons\AppData\Local\Programs\R\R-4.2.1',font=('Helvatical bold',14))
label_extra1.place(relx=0,rely=0.2)

def Close():
    root.destroy()
  
  
# Button for closing
exit_button = Button(root, text="Confirm", command=Close)
#exit_button.pack(pady=20)
exit_button.place(relx=.5,rely=.4)

mainloop()
