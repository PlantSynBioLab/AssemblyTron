'''AssemblyTron Paths Writer Script

This script guides the user through finding and recording the AssemblyTron working directory and the Rscript.exe file. The pathswriter module records working directory and enables protocol setup scripts to navigate accurately. The pathswriter.py must be run in the AssemblyLine working directory so that the correct path is generated, and the paths.csv file is saved in the proper location. 

The script does not require any input files, however it saves the paths as strings in a CSV. 

This script requires that `pandas` be installed in the python environment where the script is run. 

This file can also be run as a module by calling `AssemblyTron.pathswriter`

'''
if __name__ == '__main__':
    import os
    import pandas as pd

    path = os.getcwd()

    df = pd.DataFrame({'opentrons_repo': [path]})

    # df.to_csv("paths.csv")


    # from tkinter import filedialog
    # from tkinter import *

    # def browse_button():
    #     # Allow user to select a directory and store it in global var
    #     # called folder_path
    #     global folder_path
    #     global name
    #     filename = filedialog.askdirectory()
    #     folder_path.set(filename)
    #     print(filename)
    #     name = filename

    # root = Tk()
    # root.geometry("800x200")
    # folder_path = StringVar()
    # lbl1 = Label(master=root,textvariable=folder_path)
    # lbl1.grid(row=0, column=1)
    # button2 = Button(text="Browse", command=browse_button)
    # button2.grid(row=0, column=3)

    # label_extra1 = Label(text='Navigate to the folder containing your Rscript.exe',font=('Helvatical bold',14))
    # label_extra1.place(relx=0,rely=0.2)

    # label_extra1 = Label(text='Example: C:/Users/opentrons/AppData/Local/Programs/R/R-4.2.1/bin/Rscript.exe',font=('Helvatical bold',14))
    # label_extra1.place(relx=0,rely=0.4)

    # def Close():
    #     root.destroy()
    
    
    # # Button for closing
    # exit_button = Button(root, text="Confirm", command=Close)
    # #exit_button.pack(pady=20)
    # exit_button.place(relx=.5,rely=.6)

    # mainloop()

    # df['r_path'] = name

    # print(df)

    df.to_csv("paths.csv")
