import os
import pandas
import shutil

name = 'JAB-j5__20210603140838kG6Y-Synthetic-GFP-IAA'

os.getcwd()

def walk_up_folder(path, depth=1):
    _cur_depth = 1        
    while _cur_depth < depth:
        path = os.path.dirname(path)
        _cur_depth += 1
    return path   

paths = pandas.read_csv(walk_up_folder(os.getcwd(), 2)+'\paths.csv')
paths

shutil.copy2(paths.loc[0].at['opentrons_repo']+'/j5_files/'+name+'/assembly.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')
shutil.copy2(paths.loc[0].at['opentrons_repo']+'/j5_files/'+name+'/combinations.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')
shutil.copy2(paths.loc[0].at['opentrons_repo']+'/j5_files/'+name+'/digests.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')
shutil.copy2(paths.loc[0].at['opentrons_repo']+'/j5_files/'+name+'/oligo.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')
shutil.copy2(paths.loc[0].at['opentrons_repo']+'/j5_files/'+name+'/pcr.csv', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')

oligos = pandas.read_csv('oligo.csv')
oligos

digests = pandas.read_csv('digests.csv')
digests

pcr = pandas.read_csv('pcr.csv')
pcr

combinations = pandas.read_csv('combinations.csv')
combinations


######################################################################################################3
#make instructions file
e2slot = {}
e2slot['0'] = 'A1'
e2slot['1'] = 'A2'
e2slot['2'] = 'A3'
e2slot['3'] = 'A4'
e2slot['4'] = 'A5'
e2slot['5'] = 'A6'
e2slot['6'] = 'B1'
e2slot['7'] = 'B2'
e2slot['8'] = 'B3'
e2slot['9'] = 'B4'
e2slot['10'] = 'B5'
e2slot['11'] = 'B6'
e2slot['12'] = 'C1'
e2slot['13'] = 'C2'
e2slot['14'] = 'C3'
e2slot['15'] = 'C4'
e2slot['16'] = 'C5'
e2slot['17'] = 'C6'
e2slot['18'] = 'D1'
e2slot['19'] = 'D2'
e2slot['20'] = 'D3'
e2slot['21'] = 'D4'
e2slot['22'] = 'D5'
e2slot['23'] = 'D6'
    
def main():
    f = open('Golden_Gate_instructions.txt','w+')
    f.write('Place the coldtuberack in slot 1. \r\n')
    f.write('put 300uL tips in slot 6 & 9, and 10uL tips in slot 5. \r\n')
    f.write('put in a fresh pcr plate into thermocycler. \r\n')

    f.write('Instructions for setting up the coldtuberack: \r\n')
    for i, row in oligos.iterrows():
        f.write('Put '+oligos.loc[i].at['Name']+' in '+e2slot[str(oligos.loc[i].at['ID Number'])]+'\r\n')
    f.close()
    
    Nextslot = len(oligos["ID Number"])
    
    f = open('Golden_Gate_instructions.txt','a+')
    for i, row in digests.iterrows():
        f.write('Put '+digests.loc[i].at['Sequence Source']+' in '+e2slot[str(Nextslot)]+'\r\n')
        Nextslot = Nextslot+1
    f.close()
    
    Nextslot2 = Nextslot + len(digests["Sequence Source"])-1
    
    f = open('Golden_Gate_instructions.txt','a+')
    for i, row in pcr.iterrows():
        f.write('Put '+pcr.loc[i].at['Primary Template']+' in '+e2slot[str(Nextslot2)]+'\r\n')
        Nextslot2 = Nextslot2+1
    
    f.write('Place empty tube in C4 for the T4/BSA mix \r\n')
    
    f.write('Place T4 ligase in C5 \r\n')

    f.write('Place 100X BSA in C6 \r\n')
    
    f.write('Place T4 buffer in D2 \r\n')
    f.write('Place DPNI in D3 \r\n')
    f.write('Place cutsmart buffer in D4 \r\n')
    f.write('Place BsaI in D5 \r\n')
    f.write('Place Q5 DNA polymerase in D6 \r\n')
    
    
    totaltubes= Nextslot2 + len(pcr['Primary Template'])
    
    f.write('Place 24 well tuberack in slot 2. Add '+str(totaltubes)+' empty 1.5 mL tubes to the rack in the same positions. \r\n')
    
    
    
    numfinaltubes = len(combinations['ID Number'])
    f.write('Place '+str(numfinaltubes)+' tubes in row C of 24 tuberack in slot 2. Start from D6 and go to D'+str(6-numfinaltubes+1)+' \r\n')

    f.close()


    
    
if __name__== "__main__":
    main()

os.system("notepad.exe Golden_Gate_instructions.txt")


import tkinter as tk
import csv
import pandas as pd
from datetime import date
import os
import shutil

today = date.today()

date = str(today.strftime('%Y%m%d'))
date

#make the run folder of the day
os.chdir(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/')
os.mkdir(date+'_GoldenGate')

#copy the temp GoldenGate.py to the new folder
dst = '/'+date+'GoldenGate'
shutil.copy2(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/GoldenGate.py', paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+'_GoldenGate/')

#now rename the script with the date
os.chdir(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+'_GoldenGate')
os.rename('GoldenGate.py', date+'_GoldenGate.py')
os.chdir(walk_up_folder(os.getcwd(), 2))

shutil.move(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/digests.csv',paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+'_GoldenGate/')
shutil.move(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/combinations.csv',paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+'_GoldenGate/')
shutil.move(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/pcr.csv',paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+'_GoldenGate/')
shutil.move(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/assembly.csv',paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+'_GoldenGate/')
shutil.move(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/oligo.csv',paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+'_GoldenGate/')
shutil.move(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/Golden_Gate_instructions.txt',paths.loc[0].at['opentrons_repo']+'/Golden_Gate/'+date+'_GoldenGate/')


###############################################################################################################################################################################################3
#tkinter window

from tkinter import *

csv_root = tk.Tk()
csv_root.geometry("800x800")
csv_root.title("Parameters")

def confirm():
    csv_root.destroy()
    
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
    global pwldigesttemp
    global concdigesttemp
    
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
    Date = float(Date_entry.get())
    ngdesired = float(ngdesired_entry.get())
    pwldigesttemp = float(pwldigesttemp_entry.get())
    concdigesttemp = float(concdigesttemp_entry.get())


    
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
    
    
    csv_root.destroy()
   
    
label1 = tk.Label(text = "stkprm | stkvol | dilprm | primerconc | pcrvol | templatengs |   Q5   |                DPNI | water |         cutsmart |                       Date   | ngdesired  | concdigesttemp")
label1.place(relx=0,rely=0.125)

label2 = tk.Label(text="Template pwl")
label2.place(relx=0.75,rely=0.075)

label3 = tk.Label(text="Temp conc")
label3.place(relx=0.89,rely=0.075)

stkprm_entry = tk.Entry()
stkprm_entry.insert(END, '100')
stkprm_entry.place(relx=0.015,rely=0.1,width=35)

stkvol_entry = tk.Entry()
stkvol_entry.insert(END, '1')
stkvol_entry.place(relx=0.080,rely=0.1,width=35)

dilprm_entry = tk.Entry()
dilprm_entry.insert(END, '2.5')
dilprm_entry.place(relx=0.155,rely=0.1,width=35)

primerconc_entry = tk.Entry()
primerconc_entry.insert(END, '0.1')
primerconc_entry.place(relx=0.250,rely=0.1,width=35)

pcrvol_entry = tk.Entry()
pcrvol_entry.insert(END, '25')
pcrvol_entry.place(relx=0.340,rely=0.1,width=35)

templatengs_entry = tk.Entry()
templatengs_entry.insert(END, '0.5')
templatengs_entry.place(relx=0.425,rely=0.1,width=35)

Q5_entry = tk.Entry()
Q5_entry.insert(END, '0')
Q5_entry.place(relx=0.520,rely=0.1,width=35)

DPNI_entry = tk.Entry()
DPNI_entry.insert(END, '1')
DPNI_entry.place(relx=0.60,rely=0.1,width=35)

DPwater_entry = tk.Entry()
DPwater_entry.insert(END, '19')
DPwater_entry.place(relx=0.65,rely=0.1,width=35)

cutsmart_entry = tk.Entry()
cutsmart_entry.insert(END, '5')
cutsmart_entry.place(relx=0.725,rely=0.1,width=35)

Date_entry = tk.Entry()
Date_entry.insert(END, date)
Date_entry.place(relx=0.75,rely=0.1,width=55)

ngdesired_entry = tk.Entry()
ngdesired_entry.insert(END, '100')
ngdesired_entry.place(relx=0.84,rely=0.1,width=35)

pwldigesttemp_entry = tk.Entry()
pwldigesttemp_entry.insert(END, '0')
pwldigesttemp_entry.place(relx=0.88,rely=0.1,width=35)

concdigesttemp_entry = tk.Entry()
concdigesttemp_entry.insert(END, '0')
concdigesttemp_entry.place(relx=0.89,rely=0.1,width=35)



########################################################################################
#entries for pwl number
temppwl1_entry = tk.Entry()
temppwl1_entry.insert(END, '0')
temppwl1_entry.place(relx=0.9,rely=0.1,width = 35)

temppwl2_entry = tk.Entry()
temppwl2_entry.insert(END, '0')
temppwl2_entry.place(relx=0.9,rely=0.15,width = 35)

temppwl3_entry = tk.Entry()
temppwl3_entry.insert(END, '0')
temppwl3_entry.place(relx=0.9,rely=0.2,width = 35)

temppwl4_entry = tk.Entry()
temppwl4_entry.insert(END, '0')
temppwl4_entry.place(relx=0.9,rely=0.25,width = 35)

temppwl5_entry = tk.Entry()
temppwl5_entry.insert(END, '0')
temppwl5_entry.place(relx=0.9,rely=0.3,width = 35)

temppwl6_entry = tk.Entry()
temppwl6_entry.insert(END, '0')
temppwl6_entry.place(relx=0.9,rely=0.35,width = 35)

#########################################################################################3
#entries for concentration
conc1_entry= tk.Entry()
conc1_entry.insert(END, '0')
conc1_entry.place(relx=0.95,rely=0.1,width = 35)

conc2_entry = tk.Entry()
conc2_entry.insert(END, '0')
conc2_entry.place(relx=0.95,rely=0.15,width = 35)

conc3_entry = tk.Entry()
conc3_entry.insert(END, '0')
conc3_entry.place(relx=0.95,rely=0.2,width = 35)

conc4_entry = tk.Entry()
conc4_entry.insert(END, '0')
conc4_entry.place(relx=0.95,rely=0.25,width = 35)

conc5_entry = tk.Entry()
conc5_entry.insert(END, '0')
conc5_entry.place(relx=0.95,rely=0.3,width = 35)

conc6_entry = tk.Entry()
conc6_entry.insert(END, '0')
conc6_entry.place(relx=0.95,rely=0.35,width = 35)


legend1 = tk.Label(text = "stkprm - concentration of the stock primer you are adding")
legend1.place(relx=0.1,rely=0.5)

legend2 = tk.Label(text = "stkvol - the volume of stock primer you are adding")
legend2.place(relx=0.1,rely=0.55)

legend3 = tk.Label(text = "dilprm - this is the concentration in uM that you want your working dilution to be")
legend3.place(relx=0.1,rely=0.6)

legend4 = tk.Label(text = "primerconc - this is the concentration you want each primer to be in the pcr reaction")
legend4.place(relx=0.1,rely=0.65)

legend5 = tk.Label(text = "pcrvol - this is the total volume of your pcr reaction")
legend5.place(relx=0.1,rely=0.7)

legend6 = tk.Label(text = "templatengs - this is the concentration of template you want in your pcr rxn in ng/uL")
legend6.place(relx=0.1,rely=0.75)

legend7 = tk.Label(text = "Q5 - How much Q5 to add")
legend7.place(relx=0.1,rely=0.8)

legend8 = tk.Label(text = "DPNI - How much DPNI to add")
legend8.place(relx=0.1,rely=0.85)

legend9 = tk.Label(text = "DPwater - How much water goes in your DPNI digestion")
legend9.place(relx=0.1,rely=0.9)

legend10 = tk.Label(text = "cutsmart - How much cutsmart goes in your DPNI digestion")
legend10.place(relx=0.1,rely=0.95)

confirm_button = tk.Button(text="Confirm",command=set_variables)
confirm_button.place(relx=0.8,rely=0.8)

csv_root.mainloop()



# calc for diltemp


#stkprm = 1
#stkvol = 1
#dilprm = 1
#primerconc = 1
#pcrvol = 1
#templatengs = 1
#Q5 = 1
#DNPI = 1
temppwls = [temppwl1,temppwl2,temppwl3,temppwl4,temppwl5,temppwl6]
tempconcs = [conc1,conc2,conc3,conc4,conc5,conc6]
test = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


row = [[stkprm,stkvol,dilprm,primerconc,pcrvol,templatengs,Q5,DPNI,DPwater,cutsmart,Date,ngdesired,pwldigesttemp,concdigesttemp]]
variables = pd.DataFrame(test,columns=['stkprm','stkvol','dilprm','primerconc','pcrvol','templatengs','Q5','DPNI','DPwater','cutsmart','Date','ngdesired','pwldigesttemp','concdigesttemp'],index=range(len(temppwls)))
variables.iloc[0]= [stkprm,stkvol,dilprm,primerconc,pcrvol,templatengs,Q5,DPNI,DPwater,cutsmart,Date,ngdesired,pwldigesttemp,concdigesttemp]
variables['template pwl number'] = temppwls
variables['template concentrations'] = tempconcs

variables

os.chdir('C:/Users/jonbr/Documents/GitHub/opentrons/Golden_Gate/'+date+'_GoldenGate')
variables.to_csv('Input.csv')

os.system("notepad.exe Golden_Gate_instructions.txt")
