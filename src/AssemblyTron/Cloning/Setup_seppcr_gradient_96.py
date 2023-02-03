'''Setup script for Homology Dependent Assembly with 96 tube capacity

This script walks the user through setup of a homology dependent assembly with up to 96 combined primers and templates. This script makes a dated directory in the wd, parses/transfers input files, allows users to customize parameters, runs the gradient PCR optimization algorithm, and performs calculation and tracking steps for parsed design files.

This script requires no arguments, but instead obtains all necessary information and files by user-friendly tkinter pop-up windows.

This script requires `pandas` and `numpy` to be installed in the python environment where running. 

This script can also be called as a module by calling `AssemblyTron.Cloning.Setup_seppcr_gradient_96`.

'''
if __name__ == '__main__':
    
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

label_extra1 = Label(text='Navigate to the folder containing your j5 design.',font=('Helvatical bold',14))
label_extra1.place(relx=0,rely=0.2)

def Close():
    root.destroy()
  
  
# Button for closing
exit_button = Button(root, text="Confirm", command=Close)
#exit_button.pack(pady=20)
exit_button.place(relx=.5,rely=.4)

mainloop()




#name = 'JAB-j5__20210603140838kG6Y-Synthetic-GFP-IAA'

os.getcwd()

def walk_up_folder(path, depth=1):
    _cur_depth = 1        
    while _cur_depth < depth:
        path = os.path.dirname(path)
        _cur_depth += 1
    return path   

paths = pandas.read_csv(walk_up_folder(os.getcwd(), 2)+'\paths.csv')
paths

##########################################################################################################################
###Run R script via python
shutil.copy2(paths.loc[0].at['opentrons_repo']+'/j5_to_csvs.R', name)
goback = os.getcwd() 
os.chdir(name)

retcode = subprocess.call([paths.loc[0].at['r_path']+'/Rscript.exe', '--vanilla', name+'/j5_to_csvs.R'], shell=True)
retcode

os.chdir(goback)
#######################################################################################################################

shutil.copy2(name+'/assembly.csv', paths.loc[0].at['opentrons_repo']+'/Cloning/')
shutil.copy2(name+'/combinations.csv', paths.loc[0].at['opentrons_repo']+'/Cloning/')
#shutil.copy2(name+'/digests.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')
shutil.copy2(name+'/oligo.csv', paths.loc[0].at['opentrons_repo']+'/Cloning/')
shutil.copy2(name+'/pcr.csv', paths.loc[0].at['opentrons_repo']+'/Cloning/')

#########################################################################################################
###Instructions
oligos = pandas.read_csv('oligo.csv')
oligos

#digests = pandas.read_csv('digests.csv')
#digests

pcr = pandas.read_csv('pcr.csv')
pcr.columns = pcr.columns.str.replace("'","")
pcr

names = pandas.DataFrame(pcr['Primary Template'])
names = names.drop_duplicates()
names['location'] = ''
names['pwllocation'] = ''
names['rack'] = ''

combinations = pandas.read_csv('combinations.csv')
combinations


######################################################################################################3
#make instructions file
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


id2well = {}
id2well['0'] = 'A1'
id2well['1'] = 'A2'
id2well['2'] = 'A3'
id2well['3'] = 'A4'
id2well['4'] = 'A5'
id2well['5'] = 'A6'
id2well['6'] = 'A1'
id2well['7'] = 'A2'
id2well['8'] = 'A3'
id2well['9'] = 'A4'
id2well['10'] = 'A5'
id2well['11'] = 'A6'
id2well['12'] = 'B1'
id2well['13'] = 'B2'
id2well['14'] = 'B3'
id2well['15'] = 'B4'
id2well['16'] = 'B5'
id2well['17'] = 'B6'
id2well['18'] = 'B1'
id2well['19'] = 'B2'
id2well['20'] = 'B3'
id2well['21'] = 'B4'
id2well['22'] = 'B5'
id2well['23'] = 'B6'
id2well['24'] = 'C1'
id2well['25'] = 'C2'
id2well['26'] = 'C3'  ############
id2well['27'] = 'C4'
id2well['28'] = 'C5'
id2well['29'] = 'C6'
id2well['30'] = 'C1'
id2well['31'] = 'C2'
id2well['32'] = 'C3'
id2well['33'] = 'C4'
id2well['34'] = 'C5'
id2well['35'] = 'C6'
id2well['36'] = 'D1'
id2well['37'] = 'D2'
id2well['38'] = 'D3'
id2well['39'] = 'D4'
id2well['40'] = 'D5'
id2well['41'] = 'D6'
id2well['42'] = 'D1'
id2well['43'] = 'D2'
id2well['44'] = 'D3'
id2well['45'] = 'D4'
id2well['46'] = 'D5'
id2well['47'] = 'D6'
id2well['48'] = 'A1'
id2well['49'] = 'A2'
id2well['50'] = 'A3'
id2well['51'] = 'A4'
id2well['52'] = 'A5'
id2well['53'] = 'A6'
id2well['54'] = 'A1'
id2well['55'] = 'A2'
id2well['56'] = 'A3'
id2well['57'] = 'A4'
id2well['58'] = 'A5'
id2well['59'] = 'A6'
id2well['60'] = 'B1'
id2well['61'] = 'B2'
id2well['62'] = 'B3'
id2well['63'] = 'B4'
id2well['64'] = 'B5'
id2well['65'] = 'B6'
id2well['66'] = 'B1'
id2well['67'] = 'B2'
id2well['68'] = 'B3'
id2well['69'] = 'B4'
id2well['70'] = 'B5'
id2well['71'] = 'B6'
id2well['72'] = 'C1'
id2well['73'] = 'C2'
id2well['74'] = 'C3'
id2well['75'] = 'C4'
id2well['76'] = 'C5'
id2well['77'] = 'C6'
id2well['78'] = 'C1'
id2well['79'] = 'C2'
id2well['80'] = 'C3'
id2well['81'] = 'C4'
id2well['82'] = 'C5'
id2well['83'] = 'C6'
id2well['84'] = 'D1'
id2well['85'] = 'D2'
id2well['86'] = 'D3'
id2well['87'] = 'D4'
id2well['88'] = 'D5'
id2well['89'] = 'D6'
id2well['90'] = 'D1'
id2well['91'] = 'D2'
id2well['92'] = 'D3'
id2well['93'] = 'D4'
id2well['94'] = 'D5'
id2well['95'] = 'D6'

id2rack = {}
id2rack['0'] = 'deckslot4'
id2rack['1'] = 'deckslot4'
id2rack['2'] = 'deckslot4'
id2rack['3'] = 'deckslot4'
id2rack['4'] = 'deckslot4'
id2rack['5'] = 'deckslot4'
id2rack['6'] = 'deckslot5'
id2rack['7'] = 'deckslot5'
id2rack['8'] = 'deckslot5'
id2rack['9'] = 'deckslot5'
id2rack['10'] = 'deckslot5'
id2rack['11'] = 'deckslot5'
id2rack['12'] = 'deckslot4'
id2rack['13'] = 'deckslot4'
id2rack['14'] = 'deckslot4'
id2rack['15'] = 'deckslot4'
id2rack['16'] = 'deckslot4'
id2rack['17'] = 'deckslot4'
id2rack['18'] = 'deckslot5'
id2rack['19'] = 'deckslot5'
id2rack['20'] = 'deckslot5'
id2rack['21'] = 'deckslot5'
id2rack['22'] = 'deckslot5'
id2rack['23'] = 'deckslot5'
id2rack['24'] = 'deckslot4'
id2rack['25'] = 'deckslot4'
id2rack['26'] = 'deckslot4'
id2rack['27'] = 'deckslot4'
id2rack['28'] = 'deckslot4'
id2rack['29'] = 'deckslot4'
id2rack['30'] = 'deckslot5'
id2rack['31'] = 'deckslot5'
id2rack['32'] = 'deckslot5'
id2rack['33'] = 'deckslot5'
id2rack['34'] = 'deckslot5'
id2rack['35'] = 'deckslot5'
id2rack['36'] = 'deckslot4'
id2rack['37'] = 'deckslot4'
id2rack['38'] = 'deckslot4'
id2rack['39'] = 'deckslot4'
id2rack['40'] = 'deckslot4'
id2rack['41'] = 'deckslot4'
id2rack['42'] = 'deckslot5'
id2rack['43'] = 'deckslot5'
id2rack['44'] = 'deckslot5'
id2rack['45'] = 'deckslot5'
id2rack['46'] = 'deckslot5'
id2rack['47'] = 'deckslot5'
id2rack['48'] = 'deckslot1'
id2rack['49'] = 'deckslot1'
id2rack['50'] = 'deckslot1'
id2rack['51'] = 'deckslot1'
id2rack['52'] = 'deckslot1'
id2rack['53'] = 'deckslot1'
id2rack['54'] = 'deckslot2'
id2rack['55'] = 'deckslot2'
id2rack['56'] = 'deckslot2'
id2rack['57'] = 'deckslot2'
id2rack['58'] = 'deckslot2'
id2rack['59'] = 'deckslot2'
id2rack['60'] = 'deckslot1'
id2rack['61'] = 'deckslot1'
id2rack['62'] = 'deckslot1'
id2rack['63'] = 'deckslot1'
id2rack['64'] = 'deckslot1'
id2rack['65'] = 'deckslot1'
id2rack['66'] = 'deckslot2'
id2rack['67'] = 'deckslot2'
id2rack['68'] = 'deckslot2'
id2rack['69'] = 'deckslot2'
id2rack['70'] = 'deckslot2'
id2rack['71'] = 'deckslot2'
id2rack['72'] = 'deckslot1'
id2rack['73'] = 'deckslot1'
id2rack['74'] = 'deckslot1'
id2rack['75'] = 'deckslot1'
id2rack['76'] = 'deckslot1'
id2rack['77'] = 'deckslot1'
id2rack['78'] = 'deckslot2'
id2rack['79'] = 'deckslot2'
id2rack['80'] = 'deckslot2'
id2rack['81'] = 'deckslot2'
id2rack['82'] = 'deckslot2'
id2rack['83'] = 'deckslot2'
id2rack['84'] = 'deckslot1'
id2rack['85'] = 'deckslot1'
id2rack['86'] = 'deckslot1'
id2rack['87'] = 'deckslot1'
id2rack['88'] = 'deckslot1'
id2rack['89'] = 'deckslot1'
id2rack['90'] = 'deckslot2'
id2rack['91'] = 'deckslot2'
id2rack['92'] = 'deckslot2'
id2rack['93'] = 'deckslot2'
id2rack['94'] = 'deckslot2'
id2rack['95'] = 'deckslot2'


    
temptubes = []

def main():
    f = open('reagent_setup.txt','w+')
    f.write('Date: '+str(date)+' Time: '+str(time)+' \r\n')
    f.write('Absolute Path: '+str(os.getcwd())+' \r\n')

    f.write('Place the coldtuberack in slot 1. \r\n')
    f.write('Put 300uL tips in slot 6 & 9, and 10uL tips in slot 5. \r\n')

    for i, row in oligos.iterrows():
        f.write('Put '+oligos.loc[i].at['Name']+' in '+id2rack[str(oligos.loc[i].at['ID Number'])]+' '+id2well[str(oligos.loc[i].at['ID Number'])]+'\r\n')
    f.close()
    
    Nextslot = len(oligos["ID Number"])
    
    # No digest in this protocol
    # f = open('Golden_Gate_instructions.txt','a+')
    # for i, row in digests.iterrows():
    #     f.write('Put '+digests.loc[i].at['Sequence Source']+' in '+id2well[str(Nextslot)]+'\r\n')
    #     Nextslot = Nextslot+1
    # f.close()
    
    #Nextslot2 = Nextslot + len(digests["Sequence Source"])-1
    
    f = open('reagent_setup.txt','a+')
    
    f.write('NOTE: if a template is listed twice, (ie, pwl106 in B6 and C3) then skip the second position, and move remaining templates up a slot \r\n')
    f.write('This is ok because this setup sheet and df object in the script are both set up from pcr.csv, except df just takes out repeasts.  \r\n')
    
    for i, row in names.iterrows():
        #Nextslot = Nextslot+1
    
        names.loc[i].at['location'] = id2well[str(Nextslot)]
        names.loc[i].at['rack'] = id2rack[str(Nextslot)]
    
    
    
    # for i, row in pcr.iterrows():
        
    #     if i > 0:
    #         if pcr.loc[i].at['Primary Template'] == pcr.loc[i-1].at['Primary Template']:
    #             Nextslot = Nextslot
    #         else:
    #             Nextslot = Nextslot+1
    
        
        
        f.write('Put '+names.loc[i].at['Primary Template']+' in '+id2rack[str(Nextslot)]+' '+id2well[str(Nextslot)]+'\r\n')
        Nextslot = Nextslot+1

    # if len(names) == 1:
    #     names['pwllocation'] = [temppwl1_entry]
    # if len(names) == 2:
    #     names['pwllocation'] = [temppwl1_entry, temppwl2_entry] 
    # if len(names) == 3:
    #     names['pwllocation'] = [temppwl1_entry, temppwl2_entry, temppwl3_entry]
    # if len(names) == 4:
    #     names['pwllocation'] = [temppwl1_entry, temppwl2_entry, temppwl3_entry, temppwl1_entry4]
    # if len(names) == 5:
    #     names['pwllocation'] = [temppwl1_entry, temppwl2_entry, temppwl3_entry, temppwl1_entry4, temppwl5_entry] 
    # if len(names) == 6:
    #     names['pwllocation'] = [temppwl1_entry, temppwl2_entry, temppwl3_entry, temppwl1_entry4, temppwl5_entry, temppwl6_entry]    
    
    
   
    #f.write('Place empty tube in C4 for the T4/BSA mix \r\n')
    
    #f.write('Place T4 ligase in C5 \r\n')

    #f.write('Place 100X BSA in C6 \r\n')
    
    #f.write('Place T4 buffer in D2 \r\n')
    f.write('Place DPNI in D3 \r\n')
    f.write('Place cutsmart buffer in D4 \r\n')
    #f.write('Place BsaI in D5 \r\n')
    f.write('Place Q5 DNA polymerase in D6 \r\n')
    
    
    totaltubes= Nextslot + len(pcr['Primary Template'])
    
    f.write('Place 24 well tuberack in slot 2. Add '+str(totaltubes)+' empty 1.5 mL tubes to the rack in the same positions. \r\n')
    
    
    
    #numfinaltubes = len(combinations['ID Number'])
    #f.write('Place '+str(numfinaltubes)+' tubes in row C of 24 tuberack in slot 2. Start from D6 and go to D'+str(6-numfinaltubes+1)+' \r\n')

    f.close()

if __name__== "__main__":
    main()

os.system("notepad.exe reagent_setup.txt")

# def main():
#     f = open('Golden_Gate_instructions.txt','w+')
#     f.write('Place the coldtuberack in slot 1. \r\n')
#     f.write('put 300uL tips in slot 6 & 9, and 10uL tips in slot 5. \r\n')
#     f.write('put in a fresh pcr plate into thermocycler. \r\n')

#     f.write('Instructions for setting up the coldtuberack: \r\n')
#     for i, row in oligos.iterrows():
#         f.write('Put '+oligos.loc[i].at['Name']+' in '+e2slot[str(oligos.loc[i].at['ID Number'])]+'\r\n')
#     f.close()
    
#     Nextslot = len(oligos["ID Number"])
    
#     f = open('Golden_Gate_instructions.txt','a+')
#     for i, row in digests.iterrows():
#         f.write('Put '+digests.loc[i].at['Sequence Source']+' in '+e2slot[str(Nextslot)]+'\r\n')
#         Nextslot = Nextslot+1
#     f.close()
    
#     Nextslot2 = Nextslot + len(digests["Sequence Source"])-1
    
#     f = open('Golden_Gate_instructions.txt','a+')
#     for i, row in pcr.iterrows():
#         f.write('Put '+pcr.loc[i].at['Primary Template']+' in '+e2slot[str(Nextslot2)]+'\r\n')
#         Nextslot2 = Nextslot2+1
    
#     f.write('Place empty tube in C4 for the T4/BSA mix \r\n')
    
#     f.write('Place T4 ligase in C5 \r\n')

#     f.write('Place 100X BSA in C6 \r\n')
    
#     f.write('Place T4 buffer in D2 \r\n')
#     f.write('Place DPNI in D3 \r\n')
#     f.write('Place cutsmart buffer in D4 \r\n')
#     f.write('Place BsaI in D5 \r\n')
#     f.write('Place Q5 DNA polymerase in D6 \r\n')
    
    
#     totaltubes= Nextslot2 + len(pcr['Primary Template'])
    
#     f.write('Place 24 well tuberack in slot 2. Add '+str(totaltubes)+' empty 1.5 mL tubes to the rack in the same positions. \r\n')
    
    
    
#     numfinaltubes = len(combinations['ID Number'])
#     f.write('Place '+str(numfinaltubes)+' tubes in row C of 24 tuberack in slot 2. Start from D6 and go to D'+str(6-numfinaltubes+1)+' \r\n')

#     f.close()


    
    
# if __name__== "__main__":
#     main()

# os.system("notepad.exe Golden_Gate_instructions.txt")


########################################################################################################


import tkinter as tk
import csv
import pandas as pd

import os
import shutil



#make the run folder of the day
os.chdir(paths.loc[0].at['opentrons_repo']+'/Cloning/')
os.mkdir(date+time+'_IVA')

#copy the temp GoldenGate.py to the new folder
#dst = '/'+date+'IVA'
shutil.copy2(paths.loc[0].at['opentrons_repo']+'/Cloning/IVA_separatepcrruns_gradient.py', paths.loc[0].at['opentrons_repo']+'/Cloning/'+date+time+'_IVA/')
shutil.copy2(paths.loc[0].at['opentrons_repo']+'/Cloning/dilution_96.py', paths.loc[0].at['opentrons_repo']+'/Cloning/'+date+time+'_IVA/')
shutil.copy2(paths.loc[0].at['opentrons_repo']+'/Update_Input.py', paths.loc[0].at['opentrons_repo']+'/Cloning/'+date+time+'_IVA/')

#now rename the script with the date
os.chdir(paths.loc[0].at['opentrons_repo']+'/Cloning/'+date+time+'_IVA')
os.rename('IVA_separatepcrruns_gradient.py', str(3)+'_'+date+time+'_IVA.py')
os.rename('dilution_96.py', str(2)+'_'+date+time+'_dilution_96.py')
os.rename('Update_Input.py', str(1)+'_Update_Input.py')
os.chdir(walk_up_folder(os.getcwd(), 2))

#shutil.move(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/digests.csv',paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+'_GoldenGate/')
shutil.move(paths.loc[0].at['opentrons_repo']+'/Cloning/combinations.csv',paths.loc[0].at['opentrons_repo']+'/Cloning/'+date+time+'_IVA/')
# shutil.move(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/pcr.csv',paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+'_GoldenGate/')
shutil.move(paths.loc[0].at['opentrons_repo']+'/Cloning/assembly.csv',paths.loc[0].at['opentrons_repo']+'/Cloning/'+date+time+'_IVA/')
shutil.move(paths.loc[0].at['opentrons_repo']+'/Cloning/oligo.csv',paths.loc[0].at['opentrons_repo']+'/Cloning/'+date+time+'_IVA/')
shutil.move(paths.loc[0].at['opentrons_repo']+'/Cloning/reagent_setup.txt',paths.loc[0].at['opentrons_repo']+'/Cloning/'+date+time+'_IVA/')


###############################################################################################################################################################################################3
#tkinter window

from tkinter import *

input_csv = tk.Tk()
input_csv.geometry('1920x1080')
input_csv.title('Parameters for Goldengate')


def set_variables():
    global stkprm
    global stkvol
    global dilprm
    global primerconc
    global pcrvol
    global templatengs
    global Q5
    global DPNI
    global DPwater
    global cutsmart
    global Date
    global ngdesired
    global Combinatorial_pcr_params
    global Time
    # global pwldigesttemp
    # global concdigesttemp
    
    global extra1value
    global extra1name
    global extra2value
    global extra2name
    
    if len(names) == 1:
        global temppwl1
        global conc1

    if len(names) == 2:
        global temppwl1
        global temppwl2
        global conc1
        global conc2
    
    if len(names) == 3:
        global temppwl1
        global temppwl2
        global temppwl3
        global conc1
        global conc2
        global conc3

    if len(names) == 4:
        global temppwl1
        global temppwl2
        global temppwl3
        global temppwl4
        global conc1
        global conc2
        global conc3
        global conc4
    
    if len(names) == 5:
        global temppwl1
        global temppwl2
        global temppwl3
        global temppwl4
        global temppwl5
        global conc1
        global conc2
        global conc3
        global conc4
        global conc5

    if len(names) == 6:
        global temppwl1
        global temppwl2
        global temppwl3
        global temppwl4
        global temppwl5
        global temppwl6
        global conc1
        global conc2
        global conc3
        global conc4
        global conc5
        global conc6

    stkprm = float(stkprm_entry.get())
    stkvol = float(stkvol_entry.get())
    dilprm = float(dilprm_entry.get())
    primerconc = float(primerconc_entry.get())
    pcrvol = float(pcrvol_entry.get())
    templatengs = float(templatengs_entry.get())
    Q5 = float(Q5_entry.get())
    DPNI = float(DPNI_entry.get())
    DPwater = float(DPwater_entry.get())
    cutsmart = float(cutsmart_entry.get())
    Date = Date_entry.get()
    ngdesired = float(ngdesired_entry.get())
    Combinatorial_pcr_params = float(Combinatorial_pcr_params_entry.get())
    Time = Time_entry.get()
    # pwldigesttemp = float(pwldigesttemp_entry.get())
    # concdigesttemp = float(concdigesttemp_entry.get())
    
    extra1value = float(extra1value_entry.get())
    extra1name = str(extra1name_entry.get())
    extra2value = float(extra2value_entry.get())
    extra2name = str(extra2name_entry.get())


    if len(names) == 1:
        if temppwl1_entry.get() == '':
            temppwl1 = ''
        else:
            temppwl1 = int(temppwl1_entry.get())     
        
    
        if conc1_entry.get() == '':
            conc1 = ''
        else:
            conc1 = float(conc1_entry.get())
    
    if len(names) == 2:
        if temppwl1_entry.get() == '':
            temppwl1 = ''
        else:
            temppwl1 = int(temppwl1_entry.get())
    
        if temppwl2_entry.get() == '':
            temppwl2 = ''
        else:
            temppwl2 = int(temppwl2_entry.get())
        
        if conc1_entry.get() == '':
            conc1 = ''
        else:
            conc1 = float(conc1_entry.get())
    
        if conc2_entry.get() == '':
            conc2 = ''
        else:
            conc2 = float(conc2_entry.get())
    
    if len(names) == 3:
        if temppwl1_entry.get() == '':
            temppwl1 = ''
        else:
            temppwl1 = int(temppwl1_entry.get())
    
        if temppwl2_entry.get() == '':
            temppwl2 = ''
        else:
            temppwl2 = int(temppwl2_entry.get())
    
        if temppwl3_entry.get() == '':
            temppwl3 = ''
        else:
            temppwl3 = int(temppwl3_entry.get())
        
    
        if conc1_entry.get() == '':
            conc1 = ''
        else:
            conc1 = float(conc1_entry.get())
    
        if conc2_entry.get() == '':
            conc2 = ''
        else:
            conc2 = float(conc2_entry.get())
    
        if conc3_entry.get() == '':
            conc3 = ''
        else:
            conc3 = float(conc3_entry.get())
       
    if len(names) == 4:
        if temppwl1_entry.get() == '':
            temppwl1 = ''
        else:
            temppwl1 = int(temppwl1_entry.get())
    
        if temppwl2_entry.get() == '':
            temppwl2 = ''
        else:
            temppwl2 = int(temppwl2_entry.get())
    
        if temppwl3_entry.get() == '':
            temppwl3 = ''
        else:
            temppwl3 = int(temppwl3_entry.get())
    
        if temppwl4_entry.get() == '':
            temppwl4 = ''
        else:
            temppwl4 = int(temppwl4_entry.get())
        
        
        if conc1_entry.get() == '':
            conc1 = ''
        else:
            conc1 = float(conc1_entry.get())
    
        if conc2_entry.get() == '':
            conc2 = ''
        else:
            conc2 = float(conc2_entry.get())
    
        if conc3_entry.get() == '':
            conc3 = ''
        else:
            conc3 = float(conc3_entry.get())
    
        if conc4_entry.get() == '':
            conc4 = ''
        else:
            conc4 = float(conc4_entry.get())
    
    if len(names) == 5:
        if temppwl1_entry.get() == '':
            temppwl1 = ''
        else:
            temppwl1 = int(temppwl1_entry.get())
    
        if temppwl2_entry.get() == '':
            temppwl2 = ''
        else:
            temppwl2 = int(temppwl2_entry.get())
    
        if temppwl3_entry.get() == '':
            temppwl3 = ''
        else:
            temppwl3 = int(temppwl3_entry.get())
    
        if temppwl4_entry.get() == '':
            temppwl4 = ''
        else:
            temppwl4 = int(temppwl4_entry.get())
    
        if temppwl5_entry.get() == '':
            temppwl5 = ''
        else:
            temppwl5 = int(temppwl5_entry.get())
    
    
        if conc1_entry.get() == '':
            conc1 = ''
        else:
            conc1 = float(conc1_entry.get())
    
        if conc2_entry.get() == '':
            conc2 = ''
        else:
            conc2 = float(conc2_entry.get())
    
        if conc3_entry.get() == '':
            conc3 = ''
        else:
            conc3 = float(conc3_entry.get())
    
        if conc4_entry.get() == '':
            conc4 = ''
        else:
            conc4 = float(conc4_entry.get())
    
        if conc5_entry.get() == '':
            conc5 = ''
        else:
            conc5 = float(conc5_entry.get())
    
    if len(names) == 6:
        if temppwl1_entry.get() == '':
            temppwl1 = ''
        else:
            temppwl1 = int(temppwl1_entry.get())
    
        if temppwl2_entry.get() == '':
            temppwl2 = ''
        else:
            temppwl2 = int(temppwl2_entry.get())
    
        if temppwl3_entry.get() == '':
            temppwl3 = ''
        else:
            temppwl3 = int(temppwl3_entry.get())
    
        if temppwl4_entry.get() == '':
            temppwl4 = ''
        else:
            temppwl4 = int(temppwl4_entry.get())
    
        if temppwl5_entry.get() == '':
            temppwl5 = ''
        else:
            temppwl5 = int(temppwl5_entry.get())
    
        if temppwl6_entry.get() == '':
            temppwl6 = ''
        else:
            temppwl6 = int(temppwl6_entry.get())
        
        
    
        if conc1_entry.get() == '':
            conc1 = ''
        else:
            conc1 = float(conc1_entry.get())
    
        if conc2_entry.get() == '':
            conc2 = ''
        else:
            conc2 = float(conc2_entry.get())
    
        if conc3_entry.get() == '':
            conc3 = ''
        else:
            conc3 = float(conc3_entry.get())
    
        if conc4_entry.get() == '':
            conc4 = ''
        else:
            conc4 = float(conc4_entry.get())
    
        if conc5_entry.get() == '':
            conc5 = ''
        else:
            conc5 = float(conc5_entry.get())
    
        if conc6_entry.get() == '':
            conc6 = ''
        else:
            conc6 = float(conc6_entry.get())

    input_csv.destroy()

label_stkprm = tk.Label(text='stock primer concentration - uM',font=('Helvatical bold',14))
label_stkprm.place(relx=0,rely=0.04)

label_stkvol = tk.Label(text='volume of stock primer to dilute',font=('Helvatical bold',14))
label_stkvol.place(relx=0,rely=0.07)

label_dilprm = tk.Label(text='Desired conc of intermediate primer stocks',font=('Helvatical bold',14))
label_dilprm.place(relx=0,rely=0.095)

label_primerconc = tk.Label(text='Conc of primers in the assembled PCR',font=('Helvatical bold',14))
label_primerconc.place(relx=0,rely=0.12)

label_pcrvol = tk.Label(text='Total volume of PCR',font=('Helvatical bold',14))
label_pcrvol.place(relx=0,rely=0.145)

label_templatengs = tk.Label(text='Conc of template in PCR - ng/uL',font=('Helvatical bold',14))
label_templatengs.place(relx=0,rely=0.17)

label_Q5 = tk.Label(text='Polymerase mastermix to add - uL',font=('Helvatical bold',14))
label_Q5.place(relx=0,rely=0.2)

label_DNP1 = tk.Label(text='Dpn1 to add - uL',font=('Helvatical bold',14))
label_DNP1.place(relx=0,rely=0.225)

label_water = tk.Label(text='Volume water added to DPN1 digest - uL',font=('Helvatical bold',14))
label_water.place(relx=0,rely=0.25)

label_Cutsmart = tk.Label(text='Volume cutsmart added to DPN1 digest - uL',font=('Helvatical bold',14))
label_Cutsmart.place(relx=0,rely=0.275)

label_Date = tk.Label(text='Date',font=('Helvatical bold',14))
label_Date.place(relx=0,rely=0.3)

label_ngdesired = tk.Label(text='Nanograms template added to PCR',font=('Helvatical bold',14))
label_ngdesired.place(relx=0,rely=0.325)

label_Combinatorial_pcr_params = tk.Label(text='Gradient pcr(2) or in OT(1)?',font=('Helvatical bold',14))
label_Combinatorial_pcr_params.place(relx=0,rely=0.350)

label_Time = tk.Label(text='Time',font=('Helvatical bold',14))
label_Time.place(relx=0,rely=0.375)

# label_pwldigesttemp = tk.Label(text='pwldigesttemp',font=('Helvatical bold',14))
# label_pwldigesttemp.place(relx=0,rely=0.35)

# label_concdigesttemp = tk.Label(text='concdigesttemp',font=('Helvatical bold',14))
# label_concdigesttemp.place(relx=0,rely=0.375)

label_extra1 = tk.Label(text='extra1',font=('Helvatical bold',14))
label_extra1.place(relx=0,rely=0.425)

label_extra2 = tk.Label(text='extra2',font=('Helvatical bold',14))
label_extra2.place(relx=0,rely=0.45)

label2 = tk.Label(text="Template - Well & Name",font=('Helvatical bold',12))
label2.place(relx=0.3,rely=0)

label3 = tk.Label(text="Template Concentration",font=('Helvatical bold',12))
label3.place(relx=0.6,rely=0.)

#Text Entries

stkprm_entry = tk.Entry()
stkprm_entry.insert(END, '100')
stkprm_entry.place(relx=0.2,rely=0.05,width=35)

stkvol_entry = tk.Entry()
stkvol_entry.insert(END, '1')
stkvol_entry.place(relx=0.2,rely=0.075,width=35)

dilprm_entry = tk.Entry()
dilprm_entry.insert(END, '2.5')
dilprm_entry.place(relx=0.2,rely=0.1,width=35)

primerconc_entry = tk.Entry()
primerconc_entry.insert(END, '0.1')
primerconc_entry.place(relx=0.2,rely=0.125,width=35)

pcrvol_entry = tk.Entry()
pcrvol_entry.insert(END, '25')
pcrvol_entry.place(relx=0.2,rely=0.15,width=35)

templatengs_entry = tk.Entry()
templatengs_entry.insert(END, '0.5')
templatengs_entry.place(relx=0.2,rely=0.175,width=35)

Q5_entry = tk.Entry()
Q5_entry.insert(END, '0')
Q5_entry.place(relx=0.2,rely=0.2,width=35)

DPNI_entry = tk.Entry()
DPNI_entry.insert(END, '2')
DPNI_entry.place(relx=0.2,rely=0.225,width=35)

DPwater_entry = tk.Entry()
DPwater_entry.insert(END, '18')
DPwater_entry.place(relx=0.2,rely=0.250,width=35)

cutsmart_entry = tk.Entry()
cutsmart_entry.insert(END, '5')
cutsmart_entry.place(relx=0.2,rely=0.275,width=35)

Date_entry = tk.Entry()
Date_entry.insert(END, date)
Date_entry.place(relx=0.2,rely=0.3,width=55)

ngdesired_entry = tk.Entry()
ngdesired_entry.insert(END, '100')
ngdesired_entry.place(relx=0.2,rely=0.325,width=35)

Combinatorial_pcr_params_entry = tk.Entry()
Combinatorial_pcr_params_entry.insert(END, '2')
Combinatorial_pcr_params_entry.place(relx=0.2,rely=0.35,width=35)

Time_entry = tk.Entry()
Time_entry.insert(END, time)
Time_entry.place(relx=0.2,rely=0.375,width=55)

# pwldigesttemp_entry = tk.Entry()
# pwldigesttemp_entry.insert(END, '0')
# pwldigesttemp_entry.place(relx=0.1,rely=0.35,width=35)

# concdigesttemp_entry = tk.Entry()
# concdigesttemp_entry.insert(END, '0')
# concdigesttemp_entry.place(relx=0.1,rely=0.375,width=35)

extra1name_entry = tk.Entry()
extra1name_entry.insert(END, 'variable')
extra1name_entry.place(relx=0.2,rely=0.425,width=50)

extra2name_entry = tk.Entry()
extra2name_entry.insert(END, 'variable')
extra2name_entry.place(relx=0.2,rely=0.45,width=50)

extra1value_entry = tk.Entry()
extra1value_entry.insert(END, '0')
extra1value_entry.place(relx=0.25,rely=0.425,width=35)

extra2value_entry = tk.Entry()
extra2value_entry.insert(END, '0')
extra2value_entry.place(relx=0.25,rely=0.45,width=35)

########################################################################################
#entries for pwl number
if len(names) == 1:
    temppwl1_entry = tk.Entry()
    names['pwllocation'] = [temppwl1_entry]
if len(names) == 2:
    temppwl1_entry = tk.Entry()
    temppwl2_entry = tk.Entry()
    names['pwllocation'] = [temppwl1_entry, temppwl2_entry] 
if len(names) == 3:
    temppwl1_entry = tk.Entry()
    temppwl2_entry = tk.Entry()
    temppwl3_entry = tk.Entry()
    names['pwllocation'] = [temppwl1_entry, temppwl2_entry, temppwl3_entry]
if len(names) == 4:
    temppwl1_entry = tk.Entry()
    temppwl2_entry = tk.Entry()
    temppwl3_entry = tk.Entry()
    temppwl4_entry = tk.Entry()
    names['pwllocation'] = [temppwl1_entry, temppwl2_entry, temppwl3_entry, temppwl1_entry4]
if len(names) == 5:
    temppwl1_entry = tk.Entry()
    temppwl2_entry = tk.Entry()
    temppwl3_entry = tk.Entry()
    temppwl4_entry = tk.Entry()
    temppwl5_entry = tk.Entry()
    names['pwllocation'] = [temppwl1_entry, temppwl2_entry, temppwl3_entry, temppwl1_entry4, temppwl5_entry] 
if len(names) == 6:
    temppwl1_entry = tk.Entry()
    temppwl2_entry = tk.Entry()
    temppwl3_entry = tk.Entry()
    temppwl4_entry = tk.Entry()
    temppwl5_entry = tk.Entry()
    temppwl6_entry = tk.Entry()
    names['pwllocation'] = [temppwl1_entry, temppwl2_entry, temppwl3_entry, temppwl4_entry, temppwl5_entry, temppwl6_entry]    
    

rel_y = .05

for i, row in names.iterrows():
    
    label_extra1 = tk.Label(text=names.loc[i].at['rack']+' '+names.loc[i].at['location']+' '+names.loc[i].at['Primary Template'],font=('Helvatical bold',14))
    label_extra1.place(relx = 0.3, rely = rel_y)
    
    #names.loc[i].at['pwllocation'] = tk.Entry()
    #names.loc[i].at['pwllocation'].insert(END,names.loc[i].at['location']+' '+names.loc[i].at['Primary Template'])
    #names.loc[i].at['pwllocation'].place(relx = 0.3, rely = rel_y, width = 95)

    rel_y = rel_y+.05

# temppwl1_entry = tk.Entry()
# temppwl1_entry.insert(END, '0')
# temppwl1_entry.place(relx=0.3,rely=0.05,width = 35)

# temppwl2_entry = tk.Entry()
# temppwl2_entry.insert(END, '0')
# temppwl2_entry.place(relx=0.3,rely=0.1,width = 35)

# temppwl3_entry = tk.Entry()
# temppwl3_entry.insert(END, '0')
# temppwl3_entry.place(relx=0.3,rely=0.15,width = 35)

# temppwl4_entry = tk.Entry()
# temppwl4_entry.insert(END, '0')
# temppwl4_entry.place(relx=0.3,rely=0.2,width = 35)

# temppwl5_entry = tk.Entry()
# temppwl5_entry.insert(END, '0')
# temppwl5_entry.place(relx=0.3,rely=0.25,width = 35)

# temppwl6_entry = tk.Entry()
# temppwl6_entry.insert(END, '0')
# temppwl6_entry.place(relx=0.3,rely=0.3,width = 35)

#########################################################################################3
#entries for concentration
if len(names) == 1:
    conc1_entry= tk.Entry()
    conc1_entry.insert(END, '0')
    conc1_entry.place(relx=0.6,rely=0.05,width = 35)

if len(names) == 2:
    conc1_entry= tk.Entry()
    conc1_entry.insert(END, '0')
    conc1_entry.place(relx=0.6,rely=0.05,width = 35)

    conc2_entry = tk.Entry()
    conc2_entry.insert(END, '0')
    conc2_entry.place(relx=0.6,rely=0.1,width = 35)


if len(names) == 3:
    conc1_entry= tk.Entry()
    conc1_entry.insert(END, '0')
    conc1_entry.place(relx=0.6,rely=0.05,width = 35)

    conc2_entry = tk.Entry()
    conc2_entry.insert(END, '0')
    conc2_entry.place(relx=0.6,rely=0.1,width = 35)

    conc3_entry = tk.Entry()
    conc3_entry.insert(END, '0')
    conc3_entry.place(relx=0.6,rely=0.15,width = 35)


if len(names) == 4:
    conc1_entry= tk.Entry()
    conc1_entry.insert(END, '0')
    conc1_entry.place(relx=0.6,rely=0.05,width = 35)

    conc2_entry = tk.Entry()
    conc2_entry.insert(END, '0')
    conc2_entry.place(relx=0.6,rely=0.1,width = 35)

    conc3_entry = tk.Entry()
    conc3_entry.insert(END, '0')
    conc3_entry.place(relx=0.6,rely=0.15,width = 35)

    conc4_entry = tk.Entry()
    conc4_entry.insert(END, '0')
    conc4_entry.place(relx=0.6,rely=0.2,width = 35)


if len(names) == 5:
    conc1_entry= tk.Entry()
    conc1_entry.insert(END, '0')
    conc1_entry.place(relx=0.6,rely=0.05,width = 35)

    conc2_entry = tk.Entry()
    conc2_entry.insert(END, '0')
    conc2_entry.place(relx=0.6,rely=0.1,width = 35)

    conc3_entry = tk.Entry()
    conc3_entry.insert(END, '0')
    conc3_entry.place(relx=0.6,rely=0.15,width = 35)

    conc4_entry = tk.Entry()
    conc4_entry.insert(END, '0')
    conc4_entry.place(relx=0.6,rely=0.2,width = 35)

    conc5_entry = tk.Entry()
    conc5_entry.insert(END, '0')
    conc5_entry.place(relx=0.6,rely=0.25,width = 35)


if len(names) == 6:
    conc1_entry= tk.Entry()
    conc1_entry.insert(END, '0')
    conc1_entry.place(relx=0.6,rely=0.05,width = 35)

    conc2_entry = tk.Entry()
    conc2_entry.insert(END, '0')
    conc2_entry.place(relx=0.6,rely=0.1,width = 35)

    conc3_entry = tk.Entry()
    conc3_entry.insert(END, '0')
    conc3_entry.place(relx=0.6,rely=0.15,width = 35)

    conc4_entry = tk.Entry()
    conc4_entry.insert(END, '0')
    conc4_entry.place(relx=0.6,rely=0.2,width = 35)

    conc5_entry = tk.Entry()
    conc5_entry.insert(END, '0')
    conc5_entry.place(relx=0.6,rely=0.25,width = 35)

    conc6_entry = tk.Entry()
    conc6_entry.insert(END, '0')
    conc6_entry.place(relx=0.6,rely=0.3,width = 35)


################################################################
#Legend


confirm_button = tk.Button(text="Confirm",command=set_variables)
confirm_button.place(relx=0.8,rely=0.8)


input_csv.mainloop()

if len(names) == 1:
    
    temppwls = [temppwl1]
    tempconcs = [conc1]

if len(names) == 2:

    temppwls = [temppwl1,temppwl2]
    tempconcs = [conc1,conc2]

if len(names) == 3:
    
    temppwls = [temppwl1,temppwl2,temppwl3]
    tempconcs = [conc1,conc2,conc3]


if len(names) == 4:

    temppwls = [temppwl1,temppwl2,temppwl3,temppwl4]
    tempconcs = [conc1,conc2,conc3,conc4]


if len(names) == 5:

    temppwls = [temppwl1,temppwl2,temppwl3,temppwl4,temppwl5]
    tempconcs = [conc1,conc2,conc3,conc4,conc5]


if len(names) == 6:

    temppwls = [temppwl1,temppwl2,temppwl3,temppwl4,temppwl5,temppwl6]
    tempconcs = [conc1,conc2,conc3,conc4,conc5,conc6]



test = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
lengthd=['frogs','frogs','frogs','frogs','frogs','frogs']

row = [[stkprm,stkvol,dilprm,primerconc,pcrvol,templatengs,Q5,DPNI,DPwater,cutsmart,Date,ngdesired,Combinatorial_pcr_params,Time]]
variables = pd.DataFrame(test,columns=['stkprm','stkvol','dilprm','primerconc','pcrvol','templatengs','Q5','DPNI','DPwater','cutsmart','Date','ngdesired','Combinatorial_pcr_params','Time'],index=range(len(temppwls)))
variables.iloc[0]= [stkprm,stkvol,dilprm,primerconc,pcrvol,templatengs,Q5,DPNI,DPwater,cutsmart,Date,ngdesired,Combinatorial_pcr_params,Time]
variables['template pwl number'] = temppwls
variables['template concentrations'] = tempconcs

if extra1value != 0: 
    variables[extra1name] = ''
    variables.loc[0,extra1name] = extra1value

if extra2value != 0:
    variables[extra2name] = ''
    variables.loc[0,extra2name] = extra2value

variables

variables['section'] = pd.DataFrame(lengthd,index=range(len(lengthd)))

#########################################################################################
#tkinter window to specify which parts of the protocol to run
from tkinter import *

ws = Tk() 
ws.title('Parts to Run') 
ws.geometry('400x300')

var = StringVar()

def showSelected():
    countries = []
    cname = lb.curselection()
    for i in cname:
        op = lb.get(i)
        countries.append(op)
    for val in countries:
        print(val)
    se = pandas.Series(countries)
    variables['section'] = se
    ws.destroy()

show = Label(ws, text = "Choose which parts of protocol to run", font = ("Times", 14), padx = 10, pady = 10)
show.pack() 
lb = Listbox(ws, selectmode = "multiple")
lb.pack(padx = 10, pady = 10, expand = YES, fill = "both") 

x =["Dilution", "PCR Mix", "DPNI Digest", "Combine Fragments"]

for item in range(len(x)): 
	lb.insert(END, x[item]) 
	lb.itemconfig(item, bg="#bdc1d6") 

Button(ws, text="Confirm", command=showSelected).pack()
ws.mainloop() 

##############################################################################################################

#####################################################################################################
##################GRADIENT OPTIMIZER################################################################
if variables.loc[0].at['Combinatorial_pcr_params'] == 2:
    runnumber = 0

    # pcr_plustemplates
    # pcr_plustemplates['Upper_temp'] = pcr_plustemplates['Mean Oligo Tm (3 Only)'] + pcr_plustemplates['Delta Oligo Tm (3Only)']
    # pcr_plustemplates['Lower_temp'] = pcr_plustemplates['Mean Oligo Tm (3 Only)'] - pcr_plustemplates['Delta Oligo Tm (3Only)']
    # pcr_plustemplates

    temps = pcr['Mean Oligo Tm (3 Only)'].values.tolist()
    
    deltaa =  pcr.nsmallest(1,'Delta Oligo Tm (3Only)').reset_index()
    delta_val = deltaa.loc[0].at['Delta Oligo Tm (3Only)'].tolist()
    delta_temp = deltaa.loc[0].at['Mean Oligo Tm (3 Only)'].tolist()
    
    U = delta_temp + delta_val
    L = delta_temp - delta_val

    redo = 1
    
    while redo == 1:

        current = 0
        CV = 0

        num = 100000
        for x in range(num):    
    
            #temps = [59.499,65.4245,67.8095,62.142,62.7575]
            #temps

            one = np.random.uniform(50,70)
            #one = round(numpy.random.uniform(50, 70), 1)
            eight = np.random.uniform(70,90)
            #eight = round(numpy.random.uniform(70, 90), 1)

            two = one +((2-1)/(8-1)) * (eight-one)
            three = one +((3-1)/(8-1)) * (eight-one)
            four = one +((4-1)/(8-1)) * (eight-one)
            five = one +((5-1)/(8-1)) * (eight-one)
            six = one +((6-1)/(8-1)) * (eight-one)
            seven = one +((7-1)/(8-1)) * (eight-one)

            vectorfull = [one,two,three,four,five,six,seven,eight]
            vector = [two,three,four,five,six,seven,eight]

            f = []
            i = 0
            while i < len(vector):
                j = 0
                while j < len(temps):
                    Diff = abs(vector[i]-temps[j])
                    if Diff > 0.4:
                        f.append(100.0)
                    if Diff < 0.4:
                        f.append(Diff)
                    j = j + 1
                i = i + 1
            sum(f)
    
            #if sum(f) < 3505.0 & :
        
            if current == 0:
        
                current = sum(f)
                CV = vector
                FV = vectorfull
    
            else:
                if sum(f) < current:
                    current = sum(f)
                    CV = vector
                    FV = vectorfull
            
        #find upper and lower for lowest range rxn
        #lowest delta -> upper and lower -> check temps
        #U = 65.6955
        #L = 65.1535

        i = 0
        while i < len(FV):
            if L<FV[i]<U:
                print('good')
                start = str(FV[i])
                redo = 2
                break
            else:
                redo = 1
                print(redo)
            i = i + 1
        # i=0
        # while i<len(CV):
        #     if start == '0':
        #         redo = 1
        #         print(redo)
        #     i = i + 1


    gradient = pandas.DataFrame(FV, columns=['temp'])
    wells = ['A1','A2','A3','A4','A5','A6','A7','A8']
    gradient['tube'] = wells
    
    for i, row in pcr.iterrows():
        diffss = []
        for j, row in gradient.iterrows():
            aaa = pcr.loc[i].at['Mean Oligo Tm (3 Only)']
            bbb = gradient.loc[j].at['temp']
            A = abs(aaa - bbb )
            diffss.append(A)
        min_val = min(diffss)
        min_index = diffss.index(min_val)
        pcr.loc[i,'tube'] = gradient.loc[min_index].at['tube']
    pcr

    dupin = {}
    dupin['A1'] = 'B1'
    dupin['A2'] = 'B2'
    dupin['A3'] = 'B3'
    dupin['A4'] = 'B4'
    dupin['A5'] = 'B5'
    dupin['A6'] = 'B6'
    dupin['A7'] = 'B7'
    dupin['A8'] = 'B8'
    dupin['B1'] = 'C1'
    dupin['B2'] = 'C2'
    dupin['B3'] = 'C3'
    dupin['B4'] = 'C4'
    dupin['B5'] = 'C5'
    dupin['B6'] = 'C6'
    dupin['B7'] = 'C7'
    dupin['B8'] = 'C8'
    dupin['C1'] = 'D1'
    dupin['C2'] = 'D2'
    dupin['C3'] = 'D3'
    dupin['C4'] = 'D4'
    dupin['C5'] = 'D5'
    dupin['C6'] = 'D6'
    dupin['C7'] = 'D7'
    dupin['C8'] = 'D8'
    dupin['D1'] = 'E1'
    dupin['D2'] = 'E2'
    dupin['D3'] = 'E3'
    dupin['D4'] = 'E4'
    dupin['D5'] = 'E5'
    dupin['D6'] = 'E6'
    dupin['D7'] = 'E7'
    dupin['D8'] = 'E8'




    duplicate_in_tube = pcr.duplicated(subset=['tube'])
    if duplicate_in_tube.any():
        tes = pcr.loc[duplicate_in_tube]
        index = tes.index
    else:
        index = []
    index
    i = 0
    while i < len(index):
        letter = pcr.loc[index[i]].at['tube']
        pcr.loc[index[i],'tube'] = dupin[letter]
        i = i + 1

    #repeating the duplicate correction step in case there are triple duplicates (this might not be necessary but not sure)
    duplicate_in_tube = pcr.duplicated(subset=['tube'])
    if duplicate_in_tube.any():
        tes = pcr.loc[duplicate_in_tube]
        index = tes.index
    else:
        index = []
    index
    i = 0
    while i < len(index):
        letter = pcr.loc[index[i]].at['tube']
        pcr.loc[index[i],'tube'] = dupin[letter]
        i = i + 1

    #repeating the duplicate correction step in case there are quadruple duplicates (this might not be necessary but not sure)
    duplicate_in_tube = pcr.duplicated(subset=['tube'])
    if duplicate_in_tube.any():
        tes = pcr.loc[duplicate_in_tube]
        index = tes.index
    else:
        index = []
    index
    i = 0
    while i < len(index):
        letter = pcr.loc[index[i]].at['tube']
        pcr.loc[index[i],'tube'] = dupin[letter]
        i = i + 1

    #repeating the duplicate correction step in case there are 5X duplicates (this might not be necessary but not sure)
    duplicate_in_tube = pcr.duplicated(subset=['tube'])
    if duplicate_in_tube.any():
        tes = pcr.loc[duplicate_in_tube]
        index = tes.index
    else:
        index = []
    index
    i = 0
    while i < len(index):
        letter = pcr.loc[index[i]].at['tube']
        pcr.loc[index[i],'tube'] = dupin[letter]
        i = i + 1
    

    pcr.to_csv('pcr.csv')
    shutil.move(paths.loc[0].at['opentrons_repo']+'/Cloning/pcr.csv',paths.loc[0].at['opentrons_repo']+'/Cloning/'+date+time+'_IVA/')
    gradient.to_csv('gradient.csv')
    shutil.move(paths.loc[0].at['opentrons_repo']+'/Cloning/gradient.csv',paths.loc[0].at['opentrons_repo']+'/Cloning/'+date+time+'_IVA/')



######################################################################################################



os.chdir(paths.loc[0].at['opentrons_repo']+'/Cloning/'+date+time+'_IVA')
variables.to_csv('Input.csv')
shutil.copy2(paths.loc[0].at['opentrons_repo']+'/Cloning/'+date+time+'_IVA/Input.csv', paths.loc[0].at['opentrons_repo']+'/Cloning/')

#os.system("notepad.exe IVA_instructions.txt")

##############################################################################################
###############################################################################################
#CSV processing

#variables:
#primer dilutions:
#stkprm = 100 #concentration of the stock primer you are adding
#stkvol = 1 #the volume of stock primer you are adding
#dilprm = 2.5 #this is the concentration in uM that you want your working dilution to be

#pcr reaction
# need to get this from the df##Numprimers = 4 #this is how many primers go in each pcr reaction.
#primerconcentration = 0.1 #this is the concentration you want each primer to be in the pcr reaction
#pcrvol = 25 #this is the total volume of your pcr reaction 
#templatengs = .5 #this is the concentration of template you want in your pcr rxn in ng/uL

#template dilutions tells you what the temps need to be diluted to initially so that you can just add 1 uL of template to the pcr:
#need to fill in stock template values further down the script
#diltemp = (templatengs)*(pcrvol)/1

#total_volume = 25
#Q5 = total_volume - (0.5*(total_volume)) #How much Q5 to add
#DPNI = 1 #How much DPNI to add
#DPwater = 19
#cutsmart = 5

#goldengate param inputs
#ngdesired=100



#first import information from the j5 spreadsheet in order to perform appropriate steps
#import feather
#import pyarrow.feather as ft
import pandas
import numpy as np
import os

 
#for this to work you need to run the python script on the same day that you make the new directory
#today = date.today()
#starter_date = str(today.strftime('%Y%m%d'))
#if folder was created on diff date:
#starter_date = 'typedatehere'
# pwd = str(os.getcwd())

# def walk_up_folder(path, depth=1):
#     _cur_depth = 1        
#     while _cur_depth < depth:
#         path = os.path.dirname(path)
#         _cur_depth += 1
#     return path   

#paths = pandas.read_csv('C:/Users/Public/Documents/opentrons/src/opentrons/paths.csv')
#paths



#Input_values = pandas.read_csv('Input.csv') 
Input_values = pandas.read_csv(paths.loc[0].at['opentrons_repo']+'/Cloning/Input.csv') 
Input_values
# Date = str(int(Input_values.loc[0].at['Date']))
# Date

Q5 = (0.5*Input_values.loc[0].at['pcrvol'])
diltemp = (Input_values.loc[0].at['templatengs'])*(Input_values.loc[0].at['pcrvol'])/1
DMSO = (0.03*Input_values.loc[0].at['pcrvol'])

os.chdir(paths.loc[0].at['opentrons_repo']+'/Cloning/'+date+time+'_IVA')
os.getcwd()
oligos = pandas.read_csv('oligo.csv')
oligos


oligos['ID Number'] = oligos['ID Number'].astype(int)
oligos

if len(oligos.columns) < 9:
    oligos['24well'] = ''
    oligos['rack'] = ''
    oligos['96well'] = ''
    oligos['stock primer concentration'] = ''
    oligos['volume of stock primer to add'] = ''
    oligos['concentration of diluted primer'] = ''
    oligos['volume of diluted primer'] = '' #this is a calculated value
    oligos['how much of the diluted primer is left'] = '' #also a calculated value
oligos

#custom 4x6 well plate dictionary. hardcoded specifically for the labware used. 
#this could easily be replace with another well specification dictionary

id2well = {}
id2well['0'] = 'A1'
id2well['1'] = 'A2'
id2well['2'] = 'A3'
id2well['3'] = 'A4'
id2well['4'] = 'A5'
id2well['5'] = 'A6'
id2well['6'] = 'A1'
id2well['7'] = 'A2'
id2well['8'] = 'A3'
id2well['9'] = 'A4'
id2well['10'] = 'A5'
id2well['11'] = 'A6'
id2well['12'] = 'B1'
id2well['13'] = 'B2'
id2well['14'] = 'B3'
id2well['15'] = 'B4'
id2well['16'] = 'B5'
id2well['17'] = 'B6'
id2well['18'] = 'B1'
id2well['19'] = 'B2'
id2well['20'] = 'B3'
id2well['21'] = 'B4'
id2well['22'] = 'B5'
id2well['23'] = 'B6'
id2well['24'] = 'C1'
id2well['25'] = 'C2'
id2well['26'] = 'C3'  ############
id2well['27'] = 'C4'
id2well['28'] = 'C5'
id2well['29'] = 'C6'
id2well['30'] = 'C1'
id2well['31'] = 'C2'
id2well['32'] = 'C3'
id2well['33'] = 'C4'
id2well['34'] = 'C5'
id2well['35'] = 'C6'
id2well['36'] = 'D1'
id2well['37'] = 'D2'
id2well['38'] = 'D3'
id2well['39'] = 'D4'
id2well['40'] = 'D5'
id2well['41'] = 'D6'
id2well['42'] = 'D1'
id2well['43'] = 'D2'
id2well['44'] = 'D3'
id2well['45'] = 'D4'
id2well['46'] = 'D5'
id2well['47'] = 'D6'
id2well['48'] = 'A1'
id2well['49'] = 'A2'
id2well['50'] = 'A3'
id2well['51'] = 'A4'
id2well['52'] = 'A5'
id2well['53'] = 'A6'
id2well['54'] = 'A1'
id2well['55'] = 'A2'
id2well['56'] = 'A3'
id2well['57'] = 'A4'
id2well['58'] = 'A5'
id2well['59'] = 'A6'
id2well['60'] = 'B1'
id2well['61'] = 'B2'
id2well['62'] = 'B3'
id2well['63'] = 'B4'
id2well['64'] = 'B5'
id2well['65'] = 'B6'
id2well['66'] = 'B1'
id2well['67'] = 'B2'
id2well['68'] = 'B3'
id2well['69'] = 'B4'
id2well['70'] = 'B5'
id2well['71'] = 'B6'
id2well['72'] = 'C1'
id2well['73'] = 'C2'
id2well['74'] = 'C3'
id2well['75'] = 'C4'
id2well['76'] = 'C5'
id2well['77'] = 'C6'
id2well['78'] = 'C1'
id2well['79'] = 'C2'
id2well['80'] = 'C3'
id2well['81'] = 'C4'
id2well['82'] = 'C5'
id2well['83'] = 'C6'
id2well['84'] = 'D1'
id2well['85'] = 'D2'
id2well['86'] = 'D3'
id2well['87'] = 'D4'
id2well['88'] = 'D5'
id2well['89'] = 'D6'
id2well['90'] = 'D1'
id2well['91'] = 'D2'
id2well['92'] = 'D3'
id2well['93'] = 'D4'
id2well['94'] = 'D5'
id2well['95'] = 'D6'

id296well = {}
id296well['0'] = 'A1'
id296well['1'] = 'A2'
id296well['2'] = 'A3'
id296well['3'] = 'A4'
id296well['4'] = 'A5'
id296well['5'] = 'A6'
id296well['6'] = 'A7'
id296well['7'] = 'A8'
id296well['8'] = 'A9'
id296well['9'] = 'A10'
id296well['10'] = 'A11'
id296well['11'] = 'A12'
id296well['12'] = 'B1'
id296well['13'] = 'B2'
id296well['14'] = 'B3'
id296well['15'] = 'B4'
id296well['16'] = 'B5'
id296well['17'] = 'B6'
id296well['18'] = 'B7'
id296well['19'] = 'B8'
id296well['20'] = 'B9'
id296well['21'] = 'B10'
id296well['22'] = 'B11'
id296well['23'] = 'B12'
id296well['24'] = 'C1'
id296well['25'] = 'C2'
id296well['26'] = 'C3'  ############
id296well['27'] = 'C4'
id296well['28'] = 'C5'
id296well['29'] = 'C6'
id296well['30'] = 'C7'
id296well['31'] = 'C8'
id296well['32'] = 'C9'
id296well['33'] = 'C10'
id296well['34'] = 'C11'
id296well['35'] = 'C12'
id296well['36'] = 'D1'
id296well['37'] = 'D2'
id296well['38'] = 'D3'
id296well['39'] = 'D4'
id296well['40'] = 'D5'
id296well['41'] = 'D6'
id296well['42'] = 'D7'
id296well['43'] = 'D8'
id296well['44'] = 'D9'
id296well['45'] = 'D10'
id296well['46'] = 'D11'
id296well['47'] = 'D12'
id296well['48'] = 'E1'
id296well['49'] = 'E2'
id296well['50'] = 'E3'
id296well['51'] = 'E4'
id296well['52'] = 'E5'
id296well['53'] = 'E6'
id296well['54'] = 'E7'
id296well['55'] = 'E8'
id296well['56'] = 'E9'
id296well['57'] = 'E10'
id296well['58'] = 'E11'
id296well['59'] = 'E12'
id296well['60'] = 'F1'
id296well['61'] = 'F2'
id296well['62'] = 'F3'
id296well['63'] = 'F4'
id296well['64'] = 'F5'
id296well['65'] = 'F6'
id296well['66'] = 'F7'
id296well['67'] = 'F8'
id296well['68'] = 'F9'
id296well['69'] = 'F10'
id296well['70'] = 'F11'
id296well['71'] = 'F12'
id296well['72'] = 'G1'
id296well['73'] = 'G2'
id296well['74'] = 'G3'  ############
id296well['75'] = 'G4'
id296well['76'] = 'G5'
id296well['77'] = 'G6'
id296well['78'] = 'G7'
id296well['79'] = 'G8'
id296well['80'] = 'G9'
id296well['81'] = 'G10'
id296well['82'] = 'G11'
id296well['83'] = 'G12'
id296well['84'] = 'H1'
id296well['85'] = 'H2'
id296well['86'] = 'H3'
id296well['87'] = 'H4'
id296well['88'] = 'H5'
id296well['89'] = 'H6'
id296well['90'] = 'H7'
id296well['91'] = 'H8'
id296well['92'] = 'H9'
id296well['93'] = 'H10'
id296well['94'] = 'H11'
id296well['95'] = 'H12'

id2rack = {}
id2rack['0'] = 'deckslot4'
id2rack['1'] = 'deckslot4'
id2rack['2'] = 'deckslot4'
id2rack['3'] = 'deckslot4'
id2rack['4'] = 'deckslot4'
id2rack['5'] = 'deckslot4'
id2rack['6'] = 'deckslot5'
id2rack['7'] = 'deckslot5'
id2rack['8'] = 'deckslot5'
id2rack['9'] = 'deckslot5'
id2rack['10'] = 'deckslot5'
id2rack['11'] = 'deckslot5'
id2rack['12'] = 'deckslot4'
id2rack['13'] = 'deckslot4'
id2rack['14'] = 'deckslot4'
id2rack['15'] = 'deckslot4'
id2rack['16'] = 'deckslot4'
id2rack['17'] = 'deckslot4'
id2rack['18'] = 'deckslot5'
id2rack['19'] = 'deckslot5'
id2rack['20'] = 'deckslot5'
id2rack['21'] = 'deckslot5'
id2rack['22'] = 'deckslot5'
id2rack['23'] = 'deckslot5'
id2rack['24'] = 'deckslot4'
id2rack['25'] = 'deckslot4'
id2rack['26'] = 'deckslot4'
id2rack['27'] = 'deckslot4'
id2rack['28'] = 'deckslot4'
id2rack['29'] = 'deckslot4'
id2rack['30'] = 'deckslot5'
id2rack['31'] = 'deckslot5'
id2rack['32'] = 'deckslot5'
id2rack['33'] = 'deckslot5'
id2rack['34'] = 'deckslot5'
id2rack['35'] = 'deckslot5'
id2rack['36'] = 'deckslot4'
id2rack['37'] = 'deckslot4'
id2rack['38'] = 'deckslot4'
id2rack['39'] = 'deckslot4'
id2rack['40'] = 'deckslot4'
id2rack['41'] = 'deckslot4'
id2rack['42'] = 'deckslot5'
id2rack['43'] = 'deckslot5'
id2rack['44'] = 'deckslot5'
id2rack['45'] = 'deckslot5'
id2rack['46'] = 'deckslot5'
id2rack['47'] = 'deckslot5'
id2rack['48'] = 'deckslot1'
id2rack['49'] = 'deckslot1'
id2rack['50'] = 'deckslot1'
id2rack['51'] = 'deckslot1'
id2rack['52'] = 'deckslot1'
id2rack['53'] = 'deckslot1'
id2rack['54'] = 'deckslot2'
id2rack['55'] = 'deckslot2'
id2rack['56'] = 'deckslot2'
id2rack['57'] = 'deckslot2'
id2rack['58'] = 'deckslot2'
id2rack['59'] = 'deckslot2'
id2rack['60'] = 'deckslot1'
id2rack['61'] = 'deckslot1'
id2rack['62'] = 'deckslot1'
id2rack['63'] = 'deckslot1'
id2rack['64'] = 'deckslot1'
id2rack['65'] = 'deckslot1'
id2rack['66'] = 'deckslot2'
id2rack['67'] = 'deckslot2'
id2rack['68'] = 'deckslot2'
id2rack['69'] = 'deckslot2'
id2rack['70'] = 'deckslot2'
id2rack['71'] = 'deckslot2'
id2rack['72'] = 'deckslot1'
id2rack['73'] = 'deckslot1'
id2rack['74'] = 'deckslot1'
id2rack['75'] = 'deckslot1'
id2rack['76'] = 'deckslot1'
id2rack['77'] = 'deckslot1'
id2rack['78'] = 'deckslot2'
id2rack['79'] = 'deckslot2'
id2rack['80'] = 'deckslot2'
id2rack['81'] = 'deckslot2'
id2rack['82'] = 'deckslot2'
id2rack['83'] = 'deckslot2'
id2rack['84'] = 'deckslot1'
id2rack['85'] = 'deckslot1'
id2rack['86'] = 'deckslot1'
id2rack['87'] = 'deckslot1'
id2rack['88'] = 'deckslot1'
id2rack['89'] = 'deckslot1'
id2rack['90'] = 'deckslot2'
id2rack['91'] = 'deckslot2'
id2rack['92'] = 'deckslot2'
id2rack['93'] = 'deckslot2'
id2rack['94'] = 'deckslot2'
id2rack['95'] = 'deckslot2'






pcr = pandas.read_csv('pcr.csv')
id2pcrrr = pcr.set_index('Reaction ID Number').to_dict()['tube']

#id2pcrrr = {}
#id2pcrrr['0'] = 'B2'
#id2pcrrr['1'] = 'B3'
#id2pcrrr['2'] = 'B4'
#id2pcrrr['3'] = 'B5'
#id2pcrrr['4'] = 'B6'
#id2pcrrr['5'] = 'B7'
#id2pcrrr['6'] = 'B8'
#id2pcrrr['7'] = 'B9'
# id2pcrrr['8'] = 'B10'
# id2pcrrr['9'] = 'B11'
# id2pcrrr['10'] = 'C2'
# id2pcrrr['11'] = 'C3'
# id2pcrrr['12'] = 'C4'
# id2pcrrr['13'] = 'C5'
# id2pcrrr['14'] = 'C6'
# id2pcrrr['15'] = 'C7'
# id2pcrrr['16'] = 'C8'
# id2pcrrr['17'] = 'C9'
# id2pcrrr['18'] = 'C10'
# id2pcrrr['19'] = 'C11'
# id2pcrrr['20'] = 'D2'
# id2pcrrr['21'] = 'D3'
# id2pcrrr['22'] = 'D4'
# id2pcrrr['23'] = 'D5'


for i, row in oligos.iterrows():
    oligos.loc[i,'24well'] = id2well[str(i)] #this only works because the index matces the id number. id number is a floating value
    oligos.loc[i,'96well'] = id296well[str(i)]
    oligos.loc[i,'rack'] = id2rack[str(i)]
    oligos.loc[i,'stock primer concentration'] = Input_values.loc[0].at['stkprm']
    oligos.loc[i,'volume of stock primer to add'] = Input_values.loc[0].at['stkvol']
    oligos.loc[i,'concentration of diluted primer'] = Input_values.loc[0].at['dilprm']

    
for i, row in oligos.iterrows():
    oligos.loc[i,'volume of diluted primer'] = row['stock primer concentration']*row['volume of stock primer to add']/row['concentration of diluted primer']
    

oligos['amount primer to add to frag amplification'] = Input_values.loc[0].at['pcrvol']*Input_values.loc[0].at['primerconc']/oligos['concentration of diluted primer']
oligos


oligos.to_csv('oligo.csv')

###################################################################################################################################################################################
#assembly

#read in assembly pieces as dataframe .... might not need this info
#os.chdir("C:/Users/jonbr/Documents/GitHub/opentrons/Golden_Gate/Part1_PCR_Mason/")
assembly = pandas.read_csv('assembly.csv')
assembly

# for i, row in assembly.iterrows():
#     assembly.loc[i,'pcr_frag_tube'] = id2pcrrr[i]
# assembly

sub = 0
for i, row in assembly.iterrows():
    if assembly.loc[i,'Reaction Type'] == 'PCR':
        assembly.loc[i,'pcr_frag_tube'] = id2pcrrr[i-sub]
    else:
        assembly.loc[i,'pcr_frag_tube'] = np.nan
        sub = sub + 1
assembly

assembly.to_csv('assembly.csv')

##############################################################################################################################################################################################
#digests

# #os.chdir("C:/Users/jonbr/Documents/GitHub/opentrons/Golden_Gate/Part1_PCR_Mason/")
# os.getcwd()
# digests = pandas.read_csv('digests.csv')
# digests
# #digest_conc=138 #automate digest concentration entry with inputs.py
# digest_conc = Input_values.loc[0].at['concdigesttemp']
# digests['digest_conc']=digest_conc
# digests
# startnum = len(oligos['well'])
# for i, row in digests.iterrows():
#     digests.loc[i,'well'] = id2well[str(startnum+ i)]
# digests

# next_startnum = startnum+len(digests['well'])
# digests

# for i, row in digests.iterrows():
#     digests.loc[i,'amount of template to add'] = 1


# for i, row in digests.iterrows():
   
#         digests.loc[i,'concentration of template (ng/uL)'] = diltemp

# digests['volume of dilute template prepared'] = digests['digest_conc']*Input_values.loc[0].at['stkvol']/digests['concentration of template (ng/uL)']

# digests['water to add']= digests['volume of dilute template prepared']-digests['amount of template to add']
# digests

# for i, row in digests.iterrows():
#     digests.loc[i,'frag_pcr_tube'] = id2well[str(i)]
# digests

# digests.to_csv('output_'+Date+'_digests_GoldenGate.csv')

##################################################################################################################################
#pcr

#os.chdir("C:/Users/jonbr/Documents/GitHub/opentrons/Golden_Gate/Part1_PCR_Mason/")
# pcr = pandas.read_csv('pcr.csv')
pcr.columns = pcr.columns.str.replace("'","")
pcr

pcr[['Reaction ID Number','Forward Oligo ID Number','Reverse Oligo ID Number']] = pcr[['Reaction ID Number','Forward Oligo ID Number','Reverse Oligo ID Number']].astype(int)
pcr

#if bumpback > 0:
#    pcr.index = np.arange(1, len(pcr) + 1)
pcr

#here we create an object with each unique template from the
templates = pcr["Primary Template"]
unique_templates = templates.drop_duplicates(keep = 'first', inplace = False)
unique_templates

df = pandas.DataFrame(unique_templates)

df = df.reset_index()
df = df.drop('index', 1)

df['Template Concentration'] = ''
df

#enter template concentrations here
df['Template Concentration'] = Input_values['template concentrations'] #all you have to do is input the template concentrations in the right order

#df = df[df.line_race != 0]


startnum = len(oligos['24well'])

for i, row in df.iterrows():
    df.loc[i,'template_well'] = id296well[str(startnum+i)]
    
for i, row in df.iterrows():
    df.loc[i,'template_origin'] = id2well[str(startnum+i)]
    
for i, row in df.iterrows():
    df.loc[i,'rack'] = id2rack[str(startnum+i)]


for i, row in df.iterrows():
    df.loc[i,'amount of template to add'] = 1


for i, row in df.iterrows():
   
        df.loc[i,'concentration of template (ng/uL)'] = diltemp

df['volume of dilute template prepared'] = df['Template Concentration']*Input_values.loc[0].at['stkvol']/df['concentration of template (ng/uL)']

df['water to add']= df['volume of dilute template prepared']-df['amount of template to add']


#df['volume of dilute template prepared'] = df['volume of dilute template prepared'].astype(float)
#df['concentration of template (ng/uL)'] = df['concentration of template (ng/uL)'].astype(float)
#df['amount of template to add'] = df['amount of template to add'].astype(float)

#df['water to add'] = df['water to add'].astype(int)
#df['concentration of template (ng/uL)'] = df['concentration of template (ng/uL)'].astype(int)
#df['volume of dilute template prepared'] = df['volume of dilute template prepared'].astype(int)
#df['amount of template to add'] = df['amount of template to add'].astype(int)

df['water to add'].astype(np.float32)
df['amount of template to add'].astype(np.float32)
df['concentration of template (ng/uL)'].astype(np.float32)
df['volume of dilute template prepared'].astype(np.float32)

#df['amount of template to add'] = pd.Series.astype(df['amount of template to add'], dtype=float)
#df['concentration of template (ng/uL)'] = pd.Series.astype(df['concentration of template (ng/uL)'], dtype=float)
#df['volume of dilute template prepared'] = pd.Series.astype(df['volume of dilute template prepared'], dtype=float,)
df

#if bumpback > 0:
#    df.index = np.arange(0+bumpback, len(df) + bumpback)
    
df
df.to_csv('templates.csv')

#df.dtypes

#this line of code integrates the template concentrations into the pcr df
pcr_plustemplates = pandas.merge(pcr,df,on='Primary Template')
pcr_plustemplates

if len(pcr_plustemplates.columns) == 17:

    for i, row in pcr_plustemplates.iterrows():
   
        pcr_plustemplates.loc[i,'concentration of template (ng/uL)'] = diltemp

pcr_plustemplates['volume of dilute template prepared'] = pcr_plustemplates['Template Concentration']*Input_values.loc[0].at['stkvol']/pcr_plustemplates['concentration of template (ng/uL)']

pcr_plustemplates

wellinfo = oligos[['ID Number','96well']]
wellinfo

wellinfo = wellinfo.rename(columns={'ID Number':'Forward Oligo ID Number'})
pcr_plustemplates = pcr_plustemplates.merge(wellinfo, on= 'Forward Oligo ID Number')
wellinfo = wellinfo.rename(columns={'Forward Oligo ID Number':'Reverse Oligo ID Number','96well':'96well2'})
pcr_plustemplates = pcr_plustemplates.merge(wellinfo, on= 'Reverse Oligo ID Number')
pcr_plustemplates

pcr_plustemplates['total_water_toadd'] = Input_values.loc[0].at['pcrvol']-Q5-DMSO-1-1-1
pcr_plustemplates

#pcrstart  = len(digests['well'])
for i, row in pcr_plustemplates.iterrows():
    pcr_plustemplates.loc[i,'frag_pcr_tube'] = id2pcrrr[i]
pcr_plustemplates

prvol = pandas.DataFrame()
prvol['96well'] = oligos['96well']
prvol['primervol'] = '' 
prvol['primervol'] = oligos['amount primer to add to frag amplification']
pcr_plustemplates = pcr_plustemplates.merge(prvol, on='96well')
prvol = prvol.rename(columns={'96well':'96well2'})
pcr_plustemplates = pcr_plustemplates.merge(prvol, on='96well2')
pcr_plustemplates

pcr_plustemplates.to_csv('pcr.csv')

#######################################################################################################################################################################################################################
#combinations

#os.chdir("C:/Users/jonbr/Documents/GitHub/opentrons/Golden_Gate/Part1_PCR_Mason/")
os.getcwd()
combinations = pandas.read_csv('combinations.csv')
combinations


if len(combinations.columns) == 5:
    combinations['Part(s) Bin 1'] = 'nan'
    combinations['Assembly Piece ID Number Bin 1'] = 'nan'
    combinations['Part(s) Bin 2'] = 'nan' 
    combinations['Assembly Piece ID Number Bin 2'] = 'nan'
    combinations['Part(s) Bin 3'] = 'nan' 
    combinations['Assembly Piece ID Number Bin 3'] = 'nan'
    combinations['Part(s) Bin 4'] = 'nan' 
    combinations['Assembly Piece ID Number Bin 4'] = 'nan'
if len(combinations.columns) == 7:
    combinations['Part(s) Bin 2'] = 'nan' 
    combinations['Assembly Piece ID Number Bin 2'] = 'nan'
    combinations['Part(s) Bin 3'] = 'nan' 
    combinations['Assembly Piece ID Number Bin 3'] = 'nan'
    combinations['Part(s) Bin 4'] = 'nan' 
    combinations['Assembly Piece ID Number Bin 4'] = 'nan'
if len(combinations.columns) == 9:
    combinations['Part(s) Bin 3'] = 'nan' 
    combinations['Assembly Piece ID Number Bin 3'] = 'nan'
    combinations['Part(s) Bin 4'] = 'nan' 
    combinations['Assembly Piece ID Number Bin 4'] = 'nan'
if len(combinations.columns) == 11:
    combinations['Part(s) Bin 4'] = 'nan' 
    combinations['Assembly Piece ID Number Bin 4'] = 'nan'

if Input_values.loc[0].at['Combinatorial_pcr_params'] == 1:
    pieces = [columns for columns in combinations if columns.startswith('Assembly Piece ID Number Bin ')]
    frame = combinations[pieces]
    #frame2 = frame.transpose()
    frame

    if str(frame.loc[0].at['Assembly Piece ID Number Bin 0']) == 'nan':
        del frame['Assembly Piece ID Number Bin 0']
    if str(frame.loc[0].at['Assembly Piece ID Number Bin 1']) == 'nan':
        del frame['Assembly Piece ID Number Bin 1']
    if str(frame.loc[0].at['Assembly Piece ID Number Bin 2']) == 'nan':
        del frame['Assembly Piece ID Number Bin 2']
    if str(frame.loc[0].at['Assembly Piece ID Number Bin 3']) == 'nan':
        del frame['Assembly Piece ID Number Bin 3']
    if str(frame.loc[0].at['Assembly Piece ID Number Bin 4']) == 'nan':
        del frame['Assembly Piece ID Number Bin 4']
    frame2 = frame.transpose()
    frame

    frame += startnum
    frame
    frame= frame.values.astype(str)
    frame = pandas.DataFrame(frame)
    frame
    result_1 = frame.replace(id2well)
    result_1

    combinations_plustemplocs = pandas.concat([combinations, result_1], axis=1)
    combinations_plustemplocs

    pieces = [columns for columns in combinations if columns.startswith('Assembly Piece ID Number Bin ')]
    frame = combinations[pieces]

    if str(frame.loc[0].at['Assembly Piece ID Number Bin 0']) == 'nan':
        del frame['Assembly Piece ID Number Bin 0']
    if str(frame.loc[0].at['Assembly Piece ID Number Bin 1']) == 'nan':
        del frame['Assembly Piece ID Number Bin 1']
    if str(frame.loc[0].at['Assembly Piece ID Number Bin 2']) == 'nan':
        del frame['Assembly Piece ID Number Bin 2']
    if str(frame.loc[0].at['Assembly Piece ID Number Bin 3']) == 'nan':
        del frame['Assembly Piece ID Number Bin 3']
    if str(frame.loc[0].at['Assembly Piece ID Number Bin 4']) == 'nan':
        del frame['Assembly Piece ID Number Bin 4']
    frame2 = frame.transpose()
    frame2

#need to remove the row of linearized fragments from the digest when calculating pcr parameters
    if assembly.loc[0].at['Reaction Type'] == 'Digest Linearized':
        frame2 = frame2.drop(frame2.index[0])
        frame2 -= 1
    frame2

    pcr_info = [columns for columns in pcr_plustemplates if columns.startswith('Mean Oligo Tm (3')]
    morepcr_info = [columns for columns in pcr_plustemplates if columns.startswith('Delta Oligo Tm (3')]
    anotherpcr_info = [columns for columns in pcr_plustemplates if columns.startswith('Length')]
    pcr_info = pcr_info + morepcr_info + anotherpcr_info
    pcr_info

    for column in frame2:
        listoffrags = frame2[column].to_list()
        listoffrags
    
        tablee = pcr_plustemplates[pcr_info]
        tablee = tablee.iloc[listoffrags, :]
    
        if column == 0:
            params0 = tablee.copy()
        if column == 1:
            params1 = tablee.copy()
        if column == 2:
            params2 = tablee.copy()
        if column == 3:
            params3 = tablee.copy()
        if column == 4:
            params4 = tablee.copy()
        if column == 5:
            params5 = tablee.copy()
        if column == 6:
            params6 = tablee.copy()
        if column == 7:
            params7 = tablee.copy()
        if column == 8:
            params8 = tablee.copy()
        if column == 9:
            params9 = tablee.copy()
        if column == 10:
            params10 = tablee.copy()
        if column == 11:
            params11 = tablee.copy()

        
    params0

#so looks like this script will be limited for finding pcr conditions for just 2 construct. have to update for more


    if len(combinations['ID Number']) == 1:
        Lengthparams0 = params0.nlargest(1,'Length')
        Lengthparams0['Length'] = (Lengthparams0['Length']/1000)*30
        lengthlist = Lengthparams0['Length'].to_list()
        finallengthlist = lengthlist

        params_tables = {'parmx': ['params0']}
        params_tables = pandas.DataFrame(data=params_tables)
        params_tables

        GG_dfs = {'gg#': ['gg1']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)

    if len(combinations['ID Number']) == 2:
        Lengthparams0 = params0.nlargest(1,'Length')
        Lengthparams0['Length'] = (Lengthparams0['Length']/1000)*30
        lengthlist = Lengthparams0['Length'].to_list()

        Lengthparams1 = params1.nlargest(1,'Length')
        Lengthparams1['Length'] = (Lengthparams1['Length']/1000)*30
        lengthlist1 = Lengthparams1['Length'].to_list()
        finallengthlist = lengthlist + lengthlist1 

        params_tables = {'parmx': ['params0','params1']}
        params_tables = pandas.DataFrame(data=params_tables)
        params_tables

        GG_dfs = {'gg#': ['gg1','gg2']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)

    if len(combinations['ID Number']) == 3:
        Lengthparams0 = params0.nlargest(1,'Length')
        Lengthparams0['Length'] = (Lengthparams0['Length']/1000)*30
        lengthlist = Lengthparams0['Length'].to_list()

        Lengthparams1 = params1.nlargest(1,'Length')
        Lengthparams1['Length'] = (Lengthparams1['Length']/1000)*30
        lengthlist1 = Lengthparams1['Length'].to_list()

        Lengthparams2 = params2.nlargest(1,'Length')
        Lengthparams2['Length'] = (Lengthparams2['Length']/1000)*30
        lengthlist2 = Lengthparams2['Length'].to_list()
        finallengthlist = lengthlist + lengthlist1 +lengthlist2

        params_tables = {'parmx': ['params0','params1','params2']}
        params_tables = pandas.DataFrame(data=params_tables)
        params_tables

        GG_dfs = {'gg#': ['gg1','gg2','gg3']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)

    if len(combinations['ID Number']) == 4:
        Lengthparams0 = params0.nlargest(1,'Length')
        Lengthparams0['Length'] = (Lengthparams0['Length']/1000)*30
        lengthlist = Lengthparams0['Length'].to_list()

        Lengthparams1 = params1.nlargest(1,'Length')
        Lengthparams1['Length'] = (Lengthparams1['Length']/1000)*30
        lengthlist1 = Lengthparams1['Length'].to_list()

        Lengthparams2 = params2.nlargest(1,'Length')
        Lengthparams2['Length'] = (Lengthparams2['Length']/1000)*30
        lengthlist2 = Lengthparams2['Length'].to_list()

        Lengthparams3 = params3.nlargest(1,'Length')
        Lengthparams3['Length'] = (Lengthparams3['Length']/1000)*30
        lengthlist3 = Lengthparams3['Length'].to_list()
        finallengthlist = lengthlist + lengthlist1 +lengthlist2 + lengthlist3

        params_tables = {'parmx': ['params0','params1','params2','params3']}
        params_tables = pandas.DataFrame(data=params_tables)
        params_tables

        GG_dfs = {'gg#': ['gg1','gg2','gg3','gg4']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)

#Lengthparams2 = params2.nlargest(1,'Length')
#   Lengthparams2['Length'] = (Lengthparams2['Length']/1000)*60
 #   lengthlist = Lengthparams2['Length'].to_list()
  #  print(lengthlist)

#Lengthparams3 = params0.nlargest(1,'Length')
#Lengthparams0['Length'] = (Lengthparams0['Length']/1000)*60
#lengthlist = Lengthparams0['Length'].to_list()
#print(lengthlist)

#Lengthparams0 = params0.nlargest(1,'Length')
#Lengthparams0['Length'] = (Lengthparams0['Length']/1000)*60
#lengthlist = Lengthparams0['Length'].to_list()
#print(lengthlist)



    combinations['Extension_time_sec'] = finallengthlist
    combinations

    extens = combinations.nlargest(1,'Extension_time_sec')
    extension_final = extens['Extension_time_sec']
    extension_final

#solved the problem of not being able to loop through multiple dataframes

    annealing=[]
    for i, row in params_tables.iterrows():
        x = params_tables.loc[i].at['parmx']
#locals()[x]
        locals()[x]['Upper_temp'] = locals()[x]['Mean Oligo Tm (3 Only)'] + locals()[x]['Delta Oligo Tm (3Only)']
        locals()[x]['Lower_temp'] = locals()[x]['Mean Oligo Tm (3 Only)'] - locals()[x]['Delta Oligo Tm (3Only)']
        HL = locals()[x].nsmallest(1,'Upper_temp').reset_index()#.values.tolist()
        HL = HL['Upper_temp'].values.tolist()
        LH = locals()[x].nlargest(1,'Lower_temp').reset_index()#.values.tolist()
        LH = LH['Lower_temp'].values.tolist()    
        if LH[0] > HL[0]:
            annealing_temp = (LH[0]+HL[0])/2 + ((LH[0]-HL[0])/3)
        if LH[0] < HL[0]:
            annealing_temp = HL[0]
        annealing.append(annealing_temp)

#dfff = np.array(annealing)
    dfff = pandas.DataFrame(annealing)
    dfff = dfff.sum(axis=1)
    avg_annealing = dfff.mean() 
    avg_annealing

    Annealing_and_extension = pandas.DataFrame({'Annealing temp': avg_annealing,
                   'extension time (seconds)': extension_final})
    Annealing_and_extension = Annealing_and_extension.reset_index()
    Annealing_and_extension = Annealing_and_extension.drop(columns = ['index'])
    Annealing_and_extension

    Annealing_and_extension.to_csv('output_'+date+time+'_Annealing_extension.csv')

######################separate pcrrxns####################################
########################################################################
if Input_values.loc[0].at['Combinatorial_pcr_params'] == 2:
    gradient = pandas.read_csv('gradient.csv')
    

    Length = pcr_plustemplates.nlargest(1,'Length')


#if Input_values.loc[0].at['Combinatorial_pcr_params'] == 'Y':
    pieces = [columns for columns in combinations if columns.startswith('Assembly Piece ID Number Bin ')]
    frame = combinations[pieces]
#frame2 = frame.transpose()
    frame
    if str(frame.loc[0].at['Assembly Piece ID Number Bin 0']) == 'nan':
        del frame['Assembly Piece ID Number Bin 0']
    if str(frame.loc[0].at['Assembly Piece ID Number Bin 1']) == 'nan':
        del frame['Assembly Piece ID Number Bin 1']
    if str(frame.loc[0].at['Assembly Piece ID Number Bin 2']) == 'nan':
        del frame['Assembly Piece ID Number Bin 2']
    if str(frame.loc[0].at['Assembly Piece ID Number Bin 3']) == 'nan':
        del frame['Assembly Piece ID Number Bin 3']
    if str(frame.loc[0].at['Assembly Piece ID Number Bin 4']) == 'nan':
        del frame['Assembly Piece ID Number Bin 4']
    partss = frame

#frame += startnum
#frame
    frame= frame.values.astype(str)
    frame = pandas.DataFrame(frame)
    frame
    result_1 = frame.replace(id2well)
    result_1

    combinations_plustemplocs = pandas.concat([combinations, result_1], axis=1)
    combinations_plustemplocs
    fragnumber = 0.5*(len(combinations.iloc[0,:])-3)
    goldengs = len(combinations['ID Number'])
    goldengs
    if goldengs == 1:
        GG_dfs = {'gg#': ['gg1']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)
    if goldengs == 2:
        GG_dfs = {'gg#': ['gg1','gg2']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)
    if goldengs == 3:
        GG_dfs = {'gg#': ['gg1','gg2','gg3']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)
    if goldengs == 4:
        GG_dfs = {'gg#': ['gg1','gg2','gg3','gg4']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)
    if goldengs == 5:
        GG_dfs = {'gg#': ['gg1','gg2','gg3','gg4','gg5']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)
    if goldengs == 6:
        GG_dfs = {'gg#': ['gg1','gg2','gg3','gg4','gg5','gg6']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)
    if goldengs == 7:
        GG_dfs = {'gg#': ['gg1','gg2','gg3','gg4','gg5','gg6','gg7']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)
    if goldengs == 8:
        GG_dfs = {'gg#': ['gg1','gg2','gg3','gg4','gg5','gg6','gg7','gg8']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)
    if goldengs == 9:
        GG_dfs = {'gg#': ['gg1','gg2','gg3','gg4','gg5','gg6','gg7','gg8','gg9']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)
    if goldengs == 10:
        GG_dfs = {'gg#': ['gg1','gg2','gg3','gg4','gg5','gg6','gg7','gg8','gg9','gg10']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)
    if goldengs == 11:
        GG_dfs = {'gg#': ['gg1','gg2','gg3','gg4','gg5','gg6','gg7','gg8','gg9','gg10','gg11']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)
    if goldengs == 12:
        GG_dfs = {'gg#': ['gg1','gg2','gg3','gg4','gg5','gg6','gg7','gg8','gg9','gg10','gg11','gg12']}
        GG_dfs = pandas.DataFrame(data=GG_dfs)
    
    
    
    
    GG_dfs.to_csv('GG_dfs.csv')
    

################################################################################################################################################
#continued combination processing to set up actual Golden Gate assembly dataframes

#os.chdir("C:/Users/jonbr/Documents/Github/opentrons/Golden_Gate/Part2_Assembly_Cam")
#os.getcwd()
#fragments = pandas.read_csv('fragments.csv')
#fragments

#put final goldengate assembly products on row C for good measure

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
id2wellpcr['14'] = 'C6'
id2wellpcr['15'] = 'C7'
id2wellpcr['16'] = 'C8'
id2wellpcr['17'] = 'C9'
id2wellpcr['18'] = 'C10'
id2wellpcr['19'] = 'C11'

combinations
#add in the looping like in IVA here so that the GG loop will work

ID_tube = assembly[['Reaction ID Number','pcr_frag_tube']]

if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 0']) == 'nan':
    ID_tube = ID_tube.rename(columns={'Reaction ID Number':'Assembly Piece ID Number Bin 0'})
    combinations = combinations.merge(ID_tube, on= 'Assembly Piece ID Number Bin 0')
    combs_shor = [columns for columns in combinations if columns.startswith('pcr_frag_tube')]
    combs_short = combinations[combs_shor]
    #combs_short = combinations[['pcr_frag_tube']] #,'pcr_frag_tube_y','pcr_frag_tube'

if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 1']) == 'nan':
    ID_tube = ID_tube.rename(columns={'Assembly Piece ID Number Bin 0':'Assembly Piece ID Number Bin 1'})
    combinations = combinations.merge(ID_tube, on= 'Assembly Piece ID Number Bin 1')
    combs_shor = [columns for columns in combinations if columns.startswith('pcr_frag_tube')]
    combs_short = combinations[combs_shor]
    #combs_short = combinations[['pcr_frag_tube_x','pcr_frag_tube_y']] #,'pcr_frag_tube_y','pcr_frag_tube'

if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 2']) == 'nan':
    ID_tube = ID_tube.rename(columns={'Assembly Piece ID Number Bin 1':'Assembly Piece ID Number Bin 2'})
    combinations = combinations.merge(ID_tube, on= 'Assembly Piece ID Number Bin 2')
    combs_shor = [columns for columns in combinations if columns.startswith('pcr_frag_tube')]
    combs_short = combinations[combs_shor]
    #combs_short = combinations[['pcr_frag_tube_x','pcr_frag_tube_y','pcr_frag_tube']] #,'pcr_frag_tube_y','pcr_frag_tube'

if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 3']) == 'nan':
    ID_tube = ID_tube.rename(columns={'Assembly Piece ID Number Bin 2':'Assembly Piece ID Number Bin 3'})
    combinations = combinations.merge(ID_tube, on= 'Assembly Piece ID Number Bin 3')
    combs_shor = [columns for columns in combinations if columns.startswith('pcr_frag_tube')]
    combs_short = combinations[combs_shor]
    #combs_short = combinations[['pcr_frag_tube_x','pcr_frag_tube_y','pcr_frag_tube']] #,'pcr_frag_tube_y','pcr_frag_tube'
combs_short = combs_short.T.drop_duplicates().T

if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 4']) == 'nan':
    ID_tube = ID_tube.rename(columns={'Assembly Piece ID Number Bin 3':'Assembly Piece ID Number Bin 4'})
    combinations = combinations.merge(ID_tube, on= 'Assembly Piece ID Number Bin 4')
    combs_shor = [columns for columns in combinations if columns.startswith('pcr_frag_tube')]
    combs_short = combinations[combs_shor]
    #combs_short = combinations[['pcr_frag_tube_x','pcr_frag_tube_y','pcr_frag_tube']] #,'pcr_frag_tube_y','pcr_frag_tube'
combs_short = combs_short.T.drop_duplicates().T



combs_short = combs_short.transpose()
combs_short

gg1 = pandas.DataFrame()
gg2 = pandas.DataFrame()
gg3 = pandas.DataFrame()
gg4 = pandas.DataFrame()

dil_tu = {}
dil_tu['A1'] = 'F1'
dil_tu['A2'] = 'F2'
dil_tu['A3'] = 'F3'
dil_tu['A4'] = 'F4'
dil_tu['A5'] = 'F5'
dil_tu['A6'] = 'F6'
dil_tu['A7'] = 'F7'
dil_tu['A8'] = 'F8'
dil_tu['B1'] = 'G1'
dil_tu['B2'] = 'G2'
dil_tu['B3'] = 'G3'
dil_tu['B4'] = 'G4'
dil_tu['B5'] = 'G5'
dil_tu['B6'] = 'G6'
dil_tu['B7'] = 'G7'
dil_tu['B8'] = 'G8'
dil_tu['C1'] = 'H1'
dil_tu['C2'] = 'H2'
dil_tu['C3'] = 'H3'
dil_tu['C4'] = 'H4'
dil_tu['C5'] = 'H5'
dil_tu['C6'] = 'H6'
dil_tu['C7'] = 'H7'
dil_tu['C8'] = 'H8'
dil_tu['D1'] = 'H2'
dil_tu['D2'] = 'H3'
dil_tu['D3'] = 'H4'
dil_tu['D4'] = 'H5'
dil_tu['D5'] = 'H6'
dil_tu['D6'] = 'H7'
dil_tu['D7'] = 'H8'
dil_tu['D8'] = 'H9'
dil_tu['E1'] = 'H3'
dil_tu['E2'] = 'H4'
dil_tu['E3'] = 'H5'
dil_tu['E4'] = 'H6'
dil_tu['E5'] = 'H7'
dil_tu['E6'] = 'H8'
dil_tu['E7'] = 'H9'
dil_tu['E8'] = 'H10'

#dil_tu['B7'] = 'C7'
#dil_tu['B8'] = 'C8'
#dil_tu['B9'] = 'C9'

e = len(combs_short.columns)

#next_tc_tube = len(assembly.index)
#changing next_tc_tube to 6 just to make room for a solid six fragment gradient every time
next_tc_tube = 6


    
for i, row in GG_dfs.iterrows():
    x = GG_dfs.loc[i].at['gg#']
    locals()[x] = combs_short[[i]]
    locals()[x].loc[:,'conc_assumed']= 60

    bps = assembly[['Sequence Length','pcr_frag_tube']]

    bps = bps.rename(columns={'pcr_frag_tube':i})
    locals()[x] = locals()[x].merge(bps, on= i)
    
    backbone_length=locals()[x]["Sequence Length"].max()
    backbone_length
        
    locals()[x] = locals()[x].rename(columns={0:'frag_loc',1:'frag_loc',2:'frag_loc',3:'frag_loc',4:'frag_loc',5:'frag_loc',6:'frag_loc',7:'frag_loc',8:'frag_loc',9:'frag_loc',10:'frag_loc',11:'frag_loc'})
    
       #for i, row in plasmid.iterrows():
       #     plasmid.loc[i,'final tube'] = pcr2final[str(i)]
           
        
    for i, row in locals()[x].iterrows():
        locals()[x].loc[i,'dil_tube'] = dil_tu[locals()[x].loc[i,'frag_loc']]

    for i, row in locals()[x].iterrows():
        locals()[x].loc[i, "final amount to add"] = 50/len(partss.columns)

        locals()[x].loc[i,'location_of_assembly'] = id2wellpcr[str(next_tc_tube)]
    
    locals()[x].to_csv(x+'.csv')

    next_tc_tube = next_tc_tube + 1

combinations.to_csv('combinations.csv')

dt = {'dispense_tube': ['C3','C4','C5','C6']}
dis_tube = pandas.DataFrame(data=dt)

#########################################################################################################################
# #plasmid dataframe object for the digestion
# plasmid = pandas.DataFrame()
# plasmid['Plasmid'] = Input_values['pwldigesttemp']
# plasmid['Concentration'] = Input_values['concdigesttemp']
# #plasmid = pandas.DataFrame(plasmid)
# plasmid

# plasmid['Buffer'] = float('5')
# plasmid['BSA1'] = float('1')
# plasmid['Volume of Plasmid'] = ''
# plasmid['Volume of Water'] = ''

# plasmid['Volume of Plasmid'] = (1/(plasmid['Concentration'])) * 1000 * 1
# plasmid['Volume of Water'] = 50- plasmid['Volume of Plasmid'] - plasmid['Buffer'] - plasmid['BSA1']

# plasmid['total volume'] = float(50)


# #plasmid templates arranged in an "L" formation
# row2well= {}
# row2well['0'] = 'A2'
# row2well['1'] = 'B2'
# row2well['2'] = 'C2'
# row2well['3'] = 'D2'
# row2well['4'] = 'D3'
# row2well['5'] = 'D4'
# row2well['6'] = 'D5'
# row2well['7'] = 'D6'

# plasmid['Plasmid Location'] = ''
# plasmid

# for i, row in plasmid.iterrows():
#     plasmid.loc[i,'Plasmid Location'] = id2well[str(i+startnum)]
# plasmid

# pcr2final= {}
# pcr2final['0'] = 'D6'
# pcr2final['1'] = 'D5'
# pcr2final['2'] = 'D4'
# pcr2final['3'] = 'D3'
# pcr2final['4'] = 'D2'
# pcr2final['5'] = 'D1'
# pcr2final['6'] = 'C6'
# pcr2final['7'] = 'C5'
# pcr2final['8'] = 'C4'

# plasmid['final tube'] = ''

# for i, row in plasmid.iterrows():
#     plasmid.loc[i,'final tube'] = pcr2final[str(i)]
# plasmid


def main():
    f = open('reaction_setup.txt','w+')
    f.write('PCR gradient tube positions: \r\n')
    f.write('Date: '+str(date)+' Time: '+str(time)+' \r\n')
    f.write('Absolute Path: '+str(os.getcwd())+' \r\n')

    for i, row in pcr.iterrows():
        f.write('Put a 100 uL PCR tube in '+str(pcr.loc[i].at['tube'])+'\r\n')
    f.write('Final assembly tube: \r\n')
    
    ggdf2spot = {}
    ggdf2spot['gg1'] = 'B8'
    ggdf2spot['gg2'] = 'B9'
    ggdf2spot['gg3'] = 'B10'
    ggdf2spot['gg4'] = 'B11'
    ggdf2spot['gg5'] = 'B12'
    ggdf2spot['gg6'] = 'C8'
    ggdf2spot['gg7'] = 'C9'
    ggdf2spot['gg8'] = 'C10'
    ggdf2spot['gg9'] = 'C11'
    ggdf2spot['gg10'] = 'C12'
    ggdf2spot['gg11'] = 'D8'

    for i, row in GG_dfs.iterrows():
        f.write('Put a 100 uL PCR tube in '+ggdf2spot[str(GG_dfs.loc[i].at['gg#'])]+'\r\n')
    
    f.close()
if __name__== "__main__":
    main()

#shutil.move(paths.loc[0].at['opentrons_repo']+'/Cloning/reaction_setup.txt',paths.loc[0].at['opentrons_repo']+'/Cloning/'+date+time+'_IVA/')
#os.chdir(paths.loc[0].at['opentrons_repo']+'/Cloning/'+date+time+'_IVA/')
os.system("notepad.exe reaction_setup.txt")

rc = subprocess.call([paths.loc[0].at['opentrons_repo']+'/Copy Cloning.bat'])
rc
