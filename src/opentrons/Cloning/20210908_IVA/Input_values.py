import tkinter as tk
import csv
import pandas as pd

from tkinter import *

csv_root = tk.Tk()
csv_root.geometry("600x600")
csv_root.title("Parameter's for IVA Assembly")

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
    if temppwl1_entry.get() == '':
        temppwl1 = ''
    else:
        temppwl1 = float(temppwl1_entry.get())
    
    if temppwl2_entry.get() == '':
        temppwl2 = ''
    else:
        temppwl2 = float(temppwl2_entry.get())
    
    if temppwl3_entry.get() == '':
        temppwl3 = ''
    else:
        temppwl3 = float(temppwl3_entry.get())
    
    if temppwl4_entry.get() == '':
        temppwl4 = ''
    else:
        temppwl4 = float(temppwl4_entry.get())
    
    if temppwl5_entry.get() == '':
        temppwl5 = ''
    else:
        temppwl5 = float(temppwl5_entry.get())
    
    if temppwl6_entry.get() == '':
        temppwl6 = ''
    else:
        temppwl6 = float(temppwl6_entry.get())
        
        
    
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
   
    
label1 = tk.Label(text = "stkprm | stkvol | dilprm | primerconc | pcrvol | templatengs |   Q5   | DPNI / water / cutsmart")
label1.place(relx=0,rely=0.125)

label2 = tk.Label(text="Template pwl")
label2.place(relx=0.7,rely=0.075)

label3 = tk.Label(text="Temp conc")
label3.place(relx=0.89,rely=0.075)

stkprm_entry = tk.Entry()
stkprm_entry.place(relx=0.015,rely=0.1,width=35)

stkvol_entry = tk.Entry()
stkvol_entry.place(relx=0.080,rely=0.1,width=35)

dilprm_entry = tk.Entry()
dilprm_entry.place(relx=0.155,rely=0.1,width=35)

primerconc_entry = tk.Entry()
primerconc_entry.place(relx=0.250,rely=0.1,width=35)

pcrvol_entry = tk.Entry()
pcrvol_entry.place(relx=0.340,rely=0.1,width=35)

templatengs_entry = tk.Entry()
templatengs_entry.place(relx=0.425,rely=0.1,width=35)

Q5_entry = tk.Entry()
Q5_entry.place(relx=0.520,rely=0.1,width=35)

DPNI_entry = tk.Entry()
DPNI_entry.place(relx=0.60,rely=0.1,width=35)

DPwater_entry = tk.Entry()
DPwater_entry.place(relx=0.625,rely=0.1,width=35)

cutsmart_entry = tk.Entry()
cutsmart_entry.place(relx=0.65,rely=0.1,width=35)

########################################################################################
#entries for pwl number
temppwl1_entry = tk.Entry()
temppwl1_entry.place(relx=0.7,rely=0.1)

temppwl2_entry = tk.Entry()
temppwl2_entry.place(relx=0.7,rely=0.15)

temppwl3_entry = tk.Entry()
temppwl3_entry.place(relx=0.7,rely=0.2)

temppwl4_entry = tk.Entry()
temppwl4_entry.place(relx=0.7,rely=0.25)

temppwl5_entry = tk.Entry()
temppwl5_entry.place(relx=0.7,rely=0.3)

temppwl6_entry = tk.Entry()
temppwl6_entry.place(relx=0.7,rely=0.35)

#########################################################################################3
#entries for concentration
conc1_entry= tk.Entry()
conc1_entry.place(relx=0.9,rely=0.1)

conc2_entry = tk.Entry()
conc2_entry.place(relx=0.9,rely=0.15)

conc3_entry = tk.Entry()
conc3_entry.place(relx=0.9,rely=0.2)

conc4_entry = tk.Entry()
conc4_entry.place(relx=0.9,rely=0.25)

conc5_entry = tk.Entry()
conc5_entry.place(relx=0.9,rely=0.3)

conc6_entry = tk.Entry()
conc6_entry.place(relx=0.9,rely=0.35)


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
legend9.place(relx=0.1,rely=0.87)

legend10 = tk.Label(text = "cutsmart - How much cutsmart goes in your DPNI digestion")
legend10.place(relx=0.1,rely=0.9)

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
test = [[0,0,0,0,0,0,0,0,0,0]]


row = [[stkprm,stkvol,dilprm,primerconc,pcrvol,templatengs,Q5,DPNI,DPwater,cutsmart]]
variables = pd.DataFrame(test,columns=['stkprm','stkvol','dilprm','primerconc','pcrvol','templatengs','Q5','DPNI','DPwater','cutsmart'],index=range(len(temppwls)))
variables.iloc[0]= [stkprm,stkvol,dilprm,primerconc,pcrvol,templatengs,Q5,DPNI,DPwater,cutsmart]
variables['template pwl number'] = temppwls
variables['template concentrations'] = tempconcs

variables.to_csv('Input_values.csv')