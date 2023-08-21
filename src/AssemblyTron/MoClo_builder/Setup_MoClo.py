'''Setup script for Golden Gate Assembly with 24 tube capacity

This script walks the user through setup of a Golden Gate assembly with up to 24 combined primers and templates. This script makes a dated directory in the wd, parses/transfers input files, allows users to customize parameters, runs the gradient PCR optimization algorithm, and performs calculation and tracking steps for parsed design files.

This script requires no arguments, but instead obtains all necessary information and files by user-friendly tkinter pop-up windows.

This script requires `pandas` and `numpy` to be installed in the python environment where running. 

This script can also be called as a module by calling `AssemblyTron.Golden_Gate.Setup_nodigests_seppcr_gradient_24`.

'''
if __name__ == '__main__':
        
    
    import tkinter as tk
    import os
    import pandas
    import shutil
    import numpy as np
    import subprocess

    from datetime import date
    from datetime import datetime



    now = datetime.now()

    time = str(now.strftime('%H%M'))

    today = date.today()

    date = str(today.strftime('%Y%m%d'))
    date

    os.getcwd()

    def walk_up_folder(path, depth=1):
        _cur_depth = 1        
        while _cur_depth < depth:
            path = os.path.dirname(path)
            _cur_depth += 1
        return path   

    paths = pandas.read_csv(walk_up_folder(os.getcwd(), 2)+'\paths.csv')
    paths


    from tkinter import filedialog
    from tkinter import *

    # var = StringVar()

    # def showSelected():
    #     countries = []
    #     cname = lb.curselection()
    #     for i in cname:
    #         op = lb.get(i)
    #         countries.append(op)
    #     for val in countries:
    #         print(val)
    #     se = pandas.Series(countries)
    #     section['parts'] = se
    #     ws.destroy()
##################################################################################################################
    
    #well_location = StringVar()
    #part = StringVar()
    

    
    ################################################################################################################
    #get number of constructs from user
    from tkinter import *

    input_csv = tk.Tk()
    input_csv.geometry('800x180')
    input_csv.title('Input construct number')


    def set_variables():
        #global stkprm
        global number_constructs
    
        number_constructs = float(number_constructs_entry.get())

        #return number_constructs
        
        input_csv.destroy()


    label_number_constructs = tk.Label(text='How many Constructs are you making?',font=('Helvatical bold',14))
    label_number_constructs.place(relx=0.1,rely=0.4)

    #Text Entries

    number_constructs_entry = tk.Entry()
    number_constructs_entry.place(relx=0.5,rely=0.6,width=35)

    confirm_button = tk.Button(text="Confirm",command=set_variables)
    confirm_button.place(relx=0.5,rely=0.8)

    input_csv.mainloop()

    ################################################################################################################
    number_constructs_i = number_constructs
    number=1
    next_tc_tube = 0
    os.mkdir(date+time+'_MoClo')
    shutil.copy2('MoClo_writer.py',paths.loc[0].at['opentrons_repo']+'/MoClo_builder/'+date+time+'_MoClo/')
    while number_constructs > 0:
        parts_and_locs=[]
        color = ""

        root = Tk()
        root.geometry('1920x1080')
        root.title('MoClo parts')

        def ConLS_button():
            #Has a numeric code for the part and location
            global part_and_loc
            global A
            part_and_loc = 0
            parts_and_locs.append(part_and_loc)
            ConLSbutton.configure(bg="red")

        def ConL1_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 1
            parts_and_locs.append(part_and_loc)
            ConL1button.configure(bg="red")

        def ConL2_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 2
            parts_and_locs.append(part_and_loc)
            ConL2button.configure(bg="red")


        def ConL3_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 3
            parts_and_locs.append(part_and_loc)
            ConL3button.configure(bg="red")


        def ConL4_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 4
            parts_and_locs.append(part_and_loc)
            ConL4button.configure(bg="red")


        def ConL5_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 5
            parts_and_locs.append(part_and_loc)
            ConL5button.configure(bg="red")
            

        def ConLSprim_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 6
            parts_and_locs.append(part_and_loc)
            ConLSprimbutton.configure(bg="red")



        def pREV1_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 7
            parts_and_locs.append(part_and_loc)
            pREV1button.configure(bg="red")

        def pRNR2_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 8
            parts_and_locs.append(part_and_loc)
            pRNR2button.configure(bg="red")

        def pRPL18B_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 9
            parts_and_locs.append(part_and_loc)
            pRPL18Bbutton.configure(bg="red")

        def pTDH3_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 10
            parts_and_locs.append(part_and_loc)
            pTDH3button.configure(bg="red")


        def paqCIDO_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 11
            parts_and_locs.append(part_and_loc)
            paqCIDObutton.configure(bg="red")

        def IAA14_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 12
            parts_and_locs.append(part_and_loc)
            IAA14button.configure(bg="red")

        def IAA12_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 13
            parts_and_locs.append(part_and_loc)
            IAA12button.configure(bg="red")


        def tADH1_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 14
            parts_and_locs.append(part_and_loc)
            tADH1button.configure(bg="red")


        def ConR1_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 15
            parts_and_locs.append(part_and_loc)
            ConR1button.configure(bg="red")

        def ConR2_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 16
            parts_and_locs.append(part_and_loc)
            ConR2button.configure(bg="red")

        def ConR3_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 17
            parts_and_locs.append(part_and_loc)
            ConR3button.configure(bg="red")

        def ConR4_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 18
            parts_and_locs.append(part_and_loc)
            ConR4button.configure(bg="red")

        def ConR5_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 19
            parts_and_locs.append(part_and_loc)
            ConR5button.configure(bg="red")

        def ConRE_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 20
            parts_and_locs.append(part_and_loc)
            ConREbutton.configure(bg="red")

        def ConREprim_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 21
            parts_and_locs.append(part_and_loc)
            ConREprimbutton.configure(bg="red")


        def URA3_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 22
            parts_and_locs.append(part_and_loc)
            URA3button.configure(bg="red")

        def LEU2_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 23
            parts_and_locs.append(part_and_loc)
            LEU2button.configure(bg="red")

        def HIS3_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 24
            parts_and_locs.append(part_and_loc)
            HIS3button.configure(bg="red")

        def TRP1_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 25
            parts_and_locs.append(part_and_loc)
            TRP1button.configure(bg="red")


        def CENARS_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 26
            parts_and_locs.append(part_and_loc)
            CENARSbutton.configure(bg="red")


        def AmpColE1_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 27
            parts_and_locs.append(part_and_loc)
            AmpColE1button.configure(bg="red")


        def YFP_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 28
            parts_and_locs.append(part_and_loc)
            YFPbutton.configure(bg="red")


        def paqCIDOb_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 29
            parts_and_locs.append(part_and_loc)
            paqCIDObbutton.configure(bg="red")

        def IAA14b_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 30
            parts_and_locs.append(part_and_loc)
            IAA14bbutton.configure(bg="red")

        def IAA12b_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 31
            parts_and_locs.append(part_and_loc)
            IAA12bbutton.configure(bg="red")


        def ERBVVENUS_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 32
            parts_and_locs.append(part_and_loc)
            ERBVVENUSbutton.configure(bg="red")


        def tADH1b_button():
            #Has a numeric code for the part and location
            global part_and_loc
            part_and_loc = 33
            parts_and_locs.append(part_and_loc)
            tADH1bbutton.configure(bg="red")





        
        #label_1 = tk.Label(text='Assembly Connector (1)',font=('Helvatical bold',14))
        #label_Cutsmart.place(relx=0.625,rely=0.3125)
        label_extra1 = Label(text='Assembly Connector (1)',font=('Helvatical bold',12))
        label_extra1.place(relx=0.0,rely=0.03125)

        label_extra1 = Label(text='Promoter (2)',font=('Helvatical bold',12))
        label_extra1.place(relx=0.125,rely=0.03125)

        label_extra1 = Label(text='CDS (3)',font=('Helvatical bold',12))
        label_extra1.place(relx=0.25,rely=0.03125)

        label_extra1 = Label(text='Terminator (4)',font=('Helvatical bold',12))
        label_extra1.place(relx=0.375,rely=0.03125)

        label_extra1 = Label(text='Assembly Connector (5)',font=('Helvatical bold',12))
        label_extra1.place(relx=0.5,rely=0.03125)

        label_extra1 = Label(text='Yeast Marker (6)',font=('Helvatical bold',12))
        label_extra1.place(relx=0.625,rely=0.03125)

        label_extra1 = Label(text='Yeast Origin (7)',font=('Helvatical bold',12))
        label_extra1.place(relx=0.75,rely=0.03125)

        label_extra1 = Label(text='E. coli marker/ori (8)',font=('Helvatical bold',12))
        label_extra1.place(relx=0.875,rely=0.03125)


        label_extra1 = Label(text='N-terminal \n CDS (3a)',font=('Helvatical bold',12))
        label_extra1.place(relx=0.225,rely=0.53125)

        label_extra1 = Label(text='CDS (3b)',font=('Helvatical bold',12))
        label_extra1.place(relx=0.2875,rely=0.53125)

        label_extra1 = Label(text='C-terminal \n CDS (4a)',font=('Helvatical bold',12))
        label_extra1.place(relx=0.35,rely=0.53125)

        label_extra1 = Label(text='Terminator (4b)',font=('Helvatical bold',12))
        label_extra1.place(relx=0.4125,rely=0.53125)
    ##############################################################################################################

        ConLSbutton = Button(root, text="ConLS",activebackground="magenta",fg="white",  bg="blue", command=ConLS_button)
        ConLSbutton.place(x=50, y=59.375)

        ConL1button = Button(root, text="ConL1",activebackground="magenta",fg="white", bg = "blue",command=ConL1_button)
        ConL1button.place(x=50, y=118.75)

        ConL2button = Button(root, text="ConL2",activebackground="magenta",fg="white", bg = "blue",command=ConL2_button)
        ConL2button.place(x=50, y=178.125)

        ConL3button = Button(root, text="ConL3",activebackground="magenta",fg="white", bg = "blue",command=ConL3_button)
        ConL3button.place(x=50, y=237.475)

        ConL4button = Button(root, text="ConL4",activebackground="magenta",fg="white", bg = "blue",command=ConL4_button)
        ConL4button.place(x=50, y=296.85)

        ConL5button = Button(root, text="ConL5",activebackground="magenta",fg="white", bg = "blue",command=ConL5_button)
        ConL5button.place(x=50, y=356.225)

        ConLSprimbutton = Button(root, text="ConLS'",activebackground="magenta",fg="white", bg = "blue",command=ConLSprim_button)
        ConLSprimbutton.place(x=50, y=415.6)


        pREV1button = Button(root, text="pREV1",activebackground="magenta",fg="white", bg = "green",command=pREV1_button)
        pREV1button.place(x=265, y=59.375)

        pRNR2button = Button(root, text="pRNR2",activebackground="magenta",fg="white", bg = "green",command=pRNR2_button)
        pRNR2button.place(x=265, y=118.75)

        pRPL18Bbutton = Button(root, text="pRPL18B",activebackground="magenta",fg="white", bg = "green",command=pRPL18B_button)
        pRPL18Bbutton.place(x=265, y=178.125)

        pTDH3button = Button(root, text="pTDH3",activebackground="magenta",fg="white", bg = "green",command=pTDH3_button)
        pTDH3button.place(x=265, y=237.475)

        
        paqCIDObutton = Button(root, text="paqCI DO",activebackground="magenta", bg = "yellow", command=paqCIDO_button)
        paqCIDObutton.place(x=475, y=59.375)

        IAA14button = Button(root, text="Aux/IAA 14",activebackground="magenta", bg = "yellow", command=IAA14_button)
        IAA14button.place(x=475, y=118.75)

        IAA12button = Button(root, text="Aux/IAA 12",activebackground="magenta", bg = "yellow", command=IAA12_button)
        IAA12button.place(x=475, y=178.125)


        tADH1button = Button(root, text="tADH1",activebackground="yellow",fg="white", bg = "magenta", command=tADH1_button)
        tADH1button.place(x=750, y=59.375)


        ConR1button = Button(root, text="ConR1",activebackground="magenta",fg="white",  bg="purple", command=ConR1_button)
        ConR1button.place(x=1000, y=59.375)

        ConR2button = Button(root, text="ConR2",activebackground="magenta",fg="white", bg = "purple",command=ConR2_button)
        ConR2button.place(x=1000, y=118.75)

        ConR3button = Button(root, text="ConR3",activebackground="magenta",fg="white", bg = "purple",command=ConR3_button)
        ConR3button.place(x=1000, y=178.125)

        ConR4button = Button(root, text="ConR4",activebackground="magenta",fg="white", bg = "purple",command=ConR4_button)
        ConR4button.place(x=1000, y=237.475)

        ConR5button = Button(root, text="ConR5",activebackground="magenta",fg="white", bg = "purple",command=ConR5_button)
        ConR5button.place(x=1000, y=296.85)

        ConREbutton = Button(root, text="ConRE",activebackground="magenta",fg="white", bg = "purple",command=ConRE_button)
        ConREbutton.place(x=1000, y=356.225)

        ConREprimbutton = Button(root, text="ConRE'",activebackground="magenta",fg="white", bg = "purple",command=ConREprim_button)
        ConREprimbutton.place(x=1000, y=415.6)


        URA3button = Button(root, text="URA3",activebackground="magenta",  bg="orange", command=URA3_button)
        URA3button.place(x=1225, y=59.375)

        LEU2button = Button(root, text="LEU2",activebackground="magenta", bg = "orange",command=LEU2_button)
        LEU2button.place(x=1225, y=118.75)

        HIS3button = Button(root, text="HIS3",activebackground="magenta", bg = "orange",command=HIS3_button)
        HIS3button.place(x=1225, y=178.125)

        TRP1button = Button(root, text="TRP1",activebackground="magenta", bg = "orange",command=TRP1_button)
        TRP1button.place(x=1225, y=237.475)


        CENARSbutton = Button(root, text="CEN6/ARS4",activebackground="magenta",fg="white",  bg="brown", command=CENARS_button)
        CENARSbutton.place(x=1450, y=59.375)


        AmpColE1button = Button(root, text="AmpR-ColE1",activebackground="magenta",fg="white", bg = "grey",command=AmpColE1_button)
        AmpColE1button.place(x=1700, y=59.375)


        YFPbutton = Button(root, text="YFP 3a",activebackground="magenta", bg = "yellow", command=YFP_button)
        YFPbutton.place(x=450, y=610)

        paqCIDObbutton = Button(root, text="paqCI DO 3b",activebackground="magenta", bg = "yellow", command=paqCIDOb_button)
        paqCIDObbutton.place(x=550, y=610)

        IAA14bbutton = Button(root, text="Aux/IAA14 3b",activebackground="magenta", bg = "yellow", command=IAA14b_button)
        IAA14bbutton.place(x=550, y=669.375)

        IAA12bbutton = Button(root, text="Aux/IAA12 3b",activebackground="magenta", bg = "yellow", command=IAA12b_button)
        IAA12bbutton.place(x=550, y=728.75)


        ERBVVENUSbutton = Button(root, text="ERBV-Venus",activebackground="yellow", bg = "magenta", command=ERBVVENUS_button)
        ERBVVENUSbutton.place(x=675, y=610)


        tADH1bbutton = Button(root, text="tADH1 4b",activebackground="yellow", bg = "magenta", command=tADH1b_button)
        tADH1bbutton.place(x=800, y=610)    


        def Close():
            root.destroy()


        # Button for closing
        exit_button = Button(root, text="Confirm", command=Close)
        #exit_button.pack(pady=20)
        exit_button.place(relx=.5,rely=.9)

        root.mainloop()

    

        parts = pandas.DataFrame(parts_and_locs, columns=['ID'])
        

        num2well = {}
        num2well['0'] = 'A1'
        num2well['1'] = 'A2'
        num2well['2'] = 'A3'
        num2well['3'] = 'A4'
        num2well['4'] = 'A5'
        num2well['5'] = 'A6'
        num2well['6'] = 'A7'
        num2well['7'] = 'A8'
        num2well['8'] = 'A9'
        num2well['9'] = 'A10'
        num2well['10'] = 'A11'
        num2well['11'] = 'A12'
        num2well['12'] = 'B1'
        num2well['13'] = 'B2'
        num2well['14'] = 'B3'
        num2well['15'] = 'B4'
        num2well['16'] = 'B5'
        num2well['17'] = 'B6'
        num2well['18'] = 'B7'
        num2well['19'] = 'B8'
        num2well['20'] = 'B9'
        num2well['21'] = 'B10'
        num2well['22'] = 'B11'
        num2well['23'] = 'B12' 
        num2well['24'] = 'C1'
        num2well['25'] = 'C2'
        num2well['26'] = 'C3'
        num2well['27'] = 'C4'
        num2well['28'] = 'C5'
        num2well['29'] = 'C6'
        num2well['30'] = 'C7'
        num2well['31'] = 'C8'
        num2well['32'] = 'C9'
        num2well['33'] = 'C10'

        num2part = {}
        num2part['0'] = 'ConLS'
        num2part['1'] = 'ConL1'
        num2part['2'] = 'ConL2'
        num2part['3'] = 'ConL3'
        num2part['4'] = 'ConL4'
        num2part['5'] = 'ConL5'
        num2part['6'] = 'ConLSprime'
        num2part['7'] = 'pREV1'
        num2part['8'] = 'pRNR2'
        num2part['9'] = 'pRPL18B'
        num2part['10'] = 'pTDH3'
        num2part['11'] = 'paqCIDO'
        num2part['12'] = 'IAA14'
        num2part['13'] = 'IAA12'
        num2part['14'] = 'tADH1'
        num2part['15'] = 'ConR1'
        num2part['16'] = 'ConR2'
        num2part['17'] = 'ConR3'
        num2part['18'] = 'ConR4'
        num2part['19'] = 'ConR5'
        num2part['20'] = 'ConRE'
        num2part['21'] = 'ConREprime'
        num2part['22'] = 'URA3'
        num2part['23'] = 'LEU2' 
        num2part['24'] = 'HIS3'
        num2part['25'] = 'TRP1'
        num2part['26'] = 'CENARS'
        num2part['27'] = 'AmpRColE1'
        num2part['28'] = 'YFP3a'
        num2part['29'] = 'paqCIDO3b'
        num2part['30'] = 'IAA143b'
        num2part['31'] = 'IAA123b'
        num2part['32'] = 'ERBVVenus'
        num2part['33'] = 'tADH1'

        id2wellpcr = {}
        id2wellpcr['0'] = 'B2'
        id2wellpcr['1'] = 'B3'
        id2wellpcr['2'] = 'B4'
        id2wellpcr['3'] = 'B5'
        id2wellpcr['4'] = 'B6'
        id2wellpcr['5'] = 'B7'
        id2wellpcr['6'] = 'B8'
        id2wellpcr['7'] = 'B9'
        id2wellpcr['8'] = 'B10'
        id2wellpcr['9'] = 'B11'
        id2wellpcr['10'] = 'C2'
        id2wellpcr['11'] = 'C3'
        id2wellpcr['12'] = 'C4'
        id2wellpcr['13'] = 'C5'

        parts["well"]=""
        parts["part"]=""
        parts["location_of_assembly"]=""
        
        for i, row in parts.iterrows():
            parts.loc[i,"well"] = num2well[str(parts.loc[i].at["ID"])]
            parts.loc[i,"part"] = num2part[str(parts.loc[i].at["ID"])]
            parts.loc[i,"location_of_assembly"] = id2wellpcr[str(next_tc_tube)]
        next_tc_tube = next_tc_tube + 1
        
        print(parts)
        parts.to_csv('parts'+str(number)+'.csv')

        
        shutil.move('parts'+str(number)+'.csv',paths.loc[0].at['opentrons_repo']+'/MoClo_builder/'+date+time+'_MoClo/')
        

        number_constructs=number_constructs-1
        number=number+1


#######################################################################################################################



    #name = 'JAB-j5__20210603140838kG6Y-Synthetic-GFP-IAA'



    # ##########################################################################################################################
    # ###Run R script via python
    # shutil.copy2(paths.loc[0].at['opentrons_repo']+'/j5_to_csvs.R', name)
    # goback = os.getcwd() 
    # os.chdir(name)

    # retcode = subprocess.call([paths.loc[0].at['r_path']+'/Rscript.exe', '--vanilla', name+'/j5_to_csvs.R'], shell=True)
    # retcode

    # os.chdir(goback)
    # #######################################################################################################################

    # shutil.copy2(name+'/assembly.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')
    # shutil.copy2(name+'/combinations.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')
    # #shutil.copy2(name+'/digests.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')
    # shutil.copy2(name+'/oligo.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')
    # shutil.copy2(name+'/pcr.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')

    # oligos = pandas.read_csv('oligo.csv')
    # oligos

    # #digests = pandas.read_csv('digests.csv')
    # #digests

    # pcr = pandas.read_csv('pcr.csv')
    # pcr.columns = pcr.columns.str.replace("'","")
    # pcr

    # names = pandas.DataFrame(pcr['Primary Template'])
    # names = names.drop_duplicates()
    # names['location'] = ''
    # names['pwllocation'] = ''

    # combinations = pandas.read_csv('combinations.csv')
    # combinations


    # ######################################################################################################3
    # #make instructions file
    # e2slot = {}
    # e2slot['0'] = 'A1'
    # e2slot['1'] = 'A2'
    # e2slot['2'] = 'A3'
    # e2slot['3'] = 'A4'
    # e2slot['4'] = 'A5'
    # e2slot['5'] = 'A6'
    # e2slot['6'] = 'B1'
    # e2slot['7'] = 'B2'
    # e2slot['8'] = 'B3'
    # e2slot['9'] = 'B4'
    # e2slot['10'] = 'B5'
    # e2slot['11'] = 'B6'
    # e2slot['12'] = 'C1'
    # e2slot['13'] = 'C2'
    # e2slot['14'] = 'C3'
    # e2slot['15'] = 'C4'
    # e2slot['16'] = 'C5'
    # e2slot['17'] = 'C6'
    # e2slot['18'] = 'D1'
    # e2slot['19'] = 'D2'
    # e2slot['20'] = 'D3'
    # e2slot['21'] = 'D4'
    # e2slot['22'] = 'D5'
    # e2slot['23'] = 'D6'
        

    # def main():
    #     f = open('reagent_setup.txt','w+')
    #     f.write('Date: '+str(date)+' Time: '+str(time)+' \r\n')
    #     f.write('Absolute Path: '+str(os.getcwd())+' \r\n')

    #     f.write('Place the coldtuberack in slot 1. \r\n')
    #     f.write('Put 300uL tips in slot 6 & 9, and 10uL tips in slot 5. \r\n')

    #     f.write('Instructions for setting up the coldtuberack: \r\n')
    #     for i, row in oligos.iterrows():
    #         f.write('Put '+oligos.loc[i].at['Name']+' in '+e2slot[str(oligos.loc[i].at['ID Number'])]+'\r\n')
    #     f.close()
        
    #     Nextslot = len(oligos["ID Number"])
        
    #     # No digest in this protocol
    #     # f = open('Golden_Gate_instructions.txt','a+')
    #     # for i, row in digests.iterrows():
    #     #     f.write('Put '+digests.loc[i].at['Sequence Source']+' in '+e2slot[str(Nextslot)]+'\r\n')
    #     #     Nextslot = Nextslot+1
    #     # f.close()
        
    #     #Nextslot2 = Nextslot + len(digests["Sequence Source"])-1
        
    #     f = open('reagent_setup.txt','a+')
        
    #     f.write('NOTE: if a template is listed twice, (ie, pwl106 in B6 and C3) then skip the second position, and move remaining templates up a slot \r\n')
    #     f.write('This is ok because this setup sheet and df object in the script are both set up from pcr.csv, except df just takes out repeasts.  \r\n')
    #     for i, row in names.iterrows():
            
    #         # if i > 0:
    #         #     if pcr.loc[i].at['Primary Template'] == pcr.loc[i-1].at['Primary Template']:
    #         #         Nextslot = Nextslot
    #         #     else:
    #         #         Nextslot = Nextslot+1
        
            
            
    #         f.write('Put '+names.loc[i].at['Primary Template']+' in '+e2slot[str(Nextslot)]+'\r\n')
    #         Nextslot = Nextslot+1

    #     f.write('Place empty tube in C4 for the T4/BSA mix \r\n')
        
    #     f.write('Place T4 ligase in C5 \r\n')

    #     f.write('Place 100X BSA in C6 \r\n')
        
    #     f.write('Place T4 buffer in D2 \r\n')
    #     f.write('Place DPNI in D3 \r\n')
    #     f.write('Place cutsmart buffer in D4 \r\n')
    #     f.write('Place BsaI in D5 \r\n')
    #     f.write('Place Q5 DNA polymerase in D6 \r\n')
        
        
    #     totaltubes= Nextslot + len(pcr['Primary Template'])
        
    #     f.write('Place 24 well tuberack in slot 2. Add '+str(totaltubes)+' empty 1.5 mL tubes to the rack in the same positions. \r\n')
        
        
        
    #     #numfinaltubes = len(combinations['ID Number'])
    #     #f.write('Place '+str(numfinaltubes)+' tubes in row C of 24 tuberack in slot 2. Start from D6 and go to D'+str(6-numfinaltubes+1)+' \r\n')

    #     f.close()

    # if __name__== "__main__":
    #     main()

    # os.system("notepad.exe reagent_setup.txt")

    # # def main():
    # #     f = open('Golden_Gate_instructions.txt','w+')
    # #     f.write('Place the coldtuberack in slot 1. \r\n')
    # #     f.write('put 300uL tips in slot 6 & 9, and 10uL tips in slot 5. \r\n')
    # #     f.write('put in a fresh pcr plate into thermocycler. \r\n')

    # #     f.write('Instructions for setting up the coldtuberack: \r\n')
    # #     for i, row in oligos.iterrows():
    # #         f.write('Put '+oligos.loc[i].at['Name']+' in '+e2slot[str(oligos.loc[i].at['ID Number'])]+'\r\n')
    # #     f.close()
        
    # #     Nextslot = len(oligos["ID Number"])
        
    # #     f = open('Golden_Gate_instructions.txt','a+')
    # #     for i, row in digests.iterrows():
    # #         f.write('Put '+digests.loc[i].at['Sequence Source']+' in '+e2slot[str(Nextslot)]+'\r\n')
    # #         Nextslot = Nextslot+1
    # #     f.close()
        
    # #     Nextslot2 = Nextslot + len(digests["Sequence Source"])-1
        
    # #     f = open('Golden_Gate_instructions.txt','a+')
    # #     for i, row in pcr.iterrows():
    # #         f.write('Put '+pcr.loc[i].at['Primary Template']+' in '+e2slot[str(Nextslot2)]+'\r\n')
    # #         Nextslot2 = Nextslot2+1
        
    # #     f.write('Place empty tube in C4 for the T4/BSA mix \r\n')
        
    # #     f.write('Place T4 ligase in C5 \r\n')

    # #     f.write('Place 100X BSA in C6 \r\n')
        
    # #     f.write('Place T4 buffer in D2 \r\n')
    # #     f.write('Place DPNI in D3 \r\n')
    # #     f.write('Place cutsmart buffer in D4 \r\n')
    # #     f.write('Place BsaI in D5 \r\n')
    # #     f.write('Place Q5 DNA polymerase in D6 \r\n')
        
        
    # #     totaltubes= Nextslot2 + len(pcr['Primary Template'])
        
    # #     f.write('Place 24 well tuberack in slot 2. Add '+str(totaltubes)+' empty 1.5 mL tubes to the rack in the same positions. \r\n')
        
        
        
    # #     numfinaltubes = len(combinations['ID Number'])
    # #     f.write('Place '+str(numfinaltubes)+' tubes in row C of 24 tuberack in slot 2. Start from D6 and go to D'+str(6-numfinaltubes+1)+' \r\n')

    # #     f.close()


        
        
    # # if __name__== "__main__":
    # #     main()

    # # os.system("notepad.exe Golden_Gate_instructions.txt")

    # ###########################################################################################################
    # #######################################################################################################
    # ##CSV Processing


    # import tkinter as tk
    # import csv
    # import pandas as pd

    # import os
    # import shutil

    # #today = date.today()

    # #date = str(today.strftime('%Y%m%d'))
    # #date

    # #make the run folder of the day
    # os.chdir(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')
    # os.mkdir(date+time+'_GoldenGate')

    # #copy the temp GoldenGate.py to the new folder
    # dst = '/'+date+'GoldenGate'
    # shutil.copy2(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/GoldenGate_nodigests_separatepcrruns_gradient.py', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+time+'_GoldenGate/')
    # shutil.copy2(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/dilution_24.py', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+time+'_GoldenGate/')
    # shutil.copy2(paths.loc[0].at['opentrons_repo']+'/Update_Input.py', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+time+'_GoldenGate/')

    # #now rename the script with the date
    # os.chdir(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+time+'_GoldenGate')
    # os.rename('GoldenGate_nodigests_separatepcrruns_gradient.py', str(3)+'_'+date+time+'_GoldenGate.py')
    # os.rename('dilution_24.py', str(2)+'_'+date+time+'_dilution_24.py')
    # os.rename('Update_Input.py', str(1)+'_Update_Input.py')
    # os.chdir(walk_up_folder(os.getcwd(), 2))

    # #shutil.move(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/digests.csv',paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+'_GoldenGate/')
    # shutil.move(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/combinations.csv',paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+time+'_GoldenGate/')
    # # shutil.move(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/pcr.csv',paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+'_GoldenGate/')
    # shutil.move(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/assembly.csv',paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+time+'_GoldenGate/')
    # shutil.move(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/oligo.csv',paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+time+'_GoldenGate/')
    # # shutil.move(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/GoldenGate_instructions.txt',paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+'_GoldenGate/')


    ###############################################################################################################################################################################################3
    #tkinter window

    from tkinter import *

    input_csv = tk.Tk()
    input_csv.geometry('600x600')
    input_csv.title('Parameters for Goldengate')


    def set_variables():
        #global stkprm
        global stkvol
        #global dilprm
        #global primerconc
        global pcrvol
        #global templatengs
        #global Q5
        #global DPNI
        #global DPwater
        #global cutsmart
        global Date
        #global ngdesired
        #global Combinatorial_pcr_params
        global Time
        # global pwldigesttemp
        # global concdigesttemp
        
        #global extra1value
        #global extra1name
        #global extra2value
        #global extra2name
        


        #stkprm = float(stkprm_entry.get())
        stkvol = float(stkvol_entry.get())
        #dilprm = float(dilprm_entry.get())
        #primerconc = float(primerconc_entry.get())
        pcrvol = float(pcrvol_entry.get())
        #templatengs = float(templatengs_entry.get())
        #Q5 = float(Q5_entry.get())
        #DPNI = float(DPNI_entry.get())
        #DPwater = float(DPwater_entry.get())
        #cutsmart = float(cutsmart_entry.get())
        Date = Date_entry.get()
        #ngdesired = float(ngdesired_entry.get())
        #Combinatorial_pcr_params = float(Combinatorial_pcr_params_entry.get())
        Time = Time_entry.get()
        # pwldigesttemp = float(pwldigesttemp_entry.get())
        # concdigesttemp = float(concdigesttemp_entry.get())
        
        # extra1value = float(extra1value_entry.get())
        # extra1name = str(extra1name_entry.get())
        # extra2value = float(extra2value_entry.get())
        # extra2name = str(extra2name_entry.get())


  
        input_csv.destroy()

    label_stkvol = tk.Label(text='volume of stock primer to dilute',font=('Helvatical bold',14))
    label_stkvol.place(relx=0,rely=0.07)

    label_pcrvol = tk.Label(text='Total volume of PCR',font=('Helvatical bold',14))
    label_pcrvol.place(relx=0,rely=0.145)

    label_Date = tk.Label(text='Date',font=('Helvatical bold',14))
    label_Date.place(relx=0,rely=0.3)

    label_Time = tk.Label(text='Time',font=('Helvatical bold',14))
    label_Time.place(relx=0,rely=0.375)

    #Text Entries

    stkvol_entry = tk.Entry()
    stkvol_entry.insert(END, '1')
    stkvol_entry.place(relx=0.6,rely=0.075,width=35)

    pcrvol_entry = tk.Entry()
    pcrvol_entry.insert(END, '25')
    pcrvol_entry.place(relx=0.6,rely=0.15,width=35)

    Date_entry = tk.Entry()
    Date_entry.insert(END, date)
    Date_entry.place(relx=0.6,rely=0.3,width=55)

    Time_entry = tk.Entry()
    Time_entry.insert(END, time)
    Time_entry.place(relx=0.6,rely=0.375,width=55)

    confirm_button = tk.Button(text="Confirm",command=set_variables)
    confirm_button.place(relx=0.8,rely=0.8)

    input_csv.mainloop()

    # temppwls = [temppwl1,temppwl2,temppwl3,temppwl4,temppwl5,temppwl6]
    # tempconcs = [conc1,conc2,conc3,conc4,conc5,conc6]
    test = [[0,0,0,0]]
    #lengthd=['frogs','frogs','frogs','frogs','frogs','frogs']

    row = [[stkvol,pcrvol,Date,Time]]
    variables = pandas.DataFrame(test,columns=['stkvol','pcrvol','Date','Time'])
    variables.iloc[0]= [stkvol,pcrvol,Date,Time]

    variables

#####################################################################################################################################


    os.chdir(paths.loc[0].at['opentrons_repo']+'/MoClo_builder/'+date+time+'_MoClo')
    variables.to_csv('Input.csv')
    shutil.copy2(paths.loc[0].at['opentrons_repo']+'/MoClo_builder/'+date+time+'_MoClo/Input.csv', paths.loc[0].at['opentrons_repo']+'/MoClo_builder/')

#################################################################################################################################

    if number_constructs_i == 1:
        parts_dfs = {'part#':['part1']}
        parts_dfs = pandas.DataFrame(data=parts_dfs)
        part1 =pandas.read_csv("parts1.csv")
    if number_constructs_i == 2:
        parts_dfs = {'part#':['part1','part2']}
        parts_dfs = pandas.DataFrame(data=parts_dfs)
        part1 =pandas.read_csv("parts1.csv")
        part2 =pandas.read_csv("parts2.csv")
    if number_constructs_i == 3:
        parts_dfs = {'part#':['part1','part2','part3']}
        parts_dfs = pandas.DataFrame(data=parts_dfs)
        part1 =pandas.read_csv("parts1.csv")
        part2 =pandas.read_csv("parts2.csv")
        part3 =pandas.read_csv("parts3.csv")
    if number_constructs_i == 4:
        parts_dfs = {'part#':['part1','part2','part3','part4']}
        parts_dfs = pandas.DataFrame(data=parts_dfs)
        part1 =pandas.read_csv("parts1.csv")
        part2 =pandas.read_csv("parts2.csv")
        part3 =pandas.read_csv("parts3.csv")
        part4 =pandas.read_csv("parts4.csv")
        
    if number_constructs_i == 5:
        parts_dfs = {'part#':['part1','part2','part3','part4','part5']}
        parts_dfs = pandas.DataFrame(data=parts_dfs)
        part1 =pandas.read_csv("parts1.csv")
        part2 =pandas.read_csv("parts2.csv")
        part3 =pandas.read_csv("parts3.csv")
        part4 =pandas.read_csv("parts4.csv")
        part5 =pandas.read_csv("parts5.csv")
        
    if number_constructs_i == 6:
        parts_dfs = {'part#':['part1','part2','part3','part4','part5','part6']}
        parts_dfs = pandas.DataFrame(data=parts_dfs)
        part1 =pandas.read_csv("parts1.csv")
        part2 =pandas.read_csv("parts2.csv")
        part3 =pandas.read_csv("parts3.csv")
        part4 =pandas.read_csv("parts4.csv")
        part5 =pandas.read_csv("parts5.csv")
        part6 =pandas.read_csv("parts6.csv")


    parts_dfs.to_csv('parts_df.csv')
    

    