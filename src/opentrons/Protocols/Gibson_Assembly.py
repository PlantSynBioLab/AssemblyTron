#!/usr/bin/env python
# coding: utf-8

# # Opentrons Protocol for Gibosn Assembly

# In[119]:


import sys
get_ipython().system('{sys.executable} -m pip install opentrons')


# In[120]:


from opentrons import protocol_api
metadata = {
'protocolName': 'gibson_assembly',
'author':'Cameron Longmire <camel94@vt.edu>',
'description':'Gibson Assembly protocol for Opentrons',
'apiLevel':'2.2'
}
print(metadata)


# In[2]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install pyarrow')
get_ipython().system('pip install PIL ')
import pandas as pd
import numpy as np
import pyarrow.feather as ft
import tkinter as tk
combinations = ft.read_feather('C:/Users/camdaman/Documents/GitHub/opentrons/Gibson Assembly/combinations.feather')
combinations

combinations[['ID Number','Assembly Piece ID Number Bin 0','Assembly Piece ID Number Bin 1']] = combinations[['ID Number','Assembly Piece ID Number Bin 0','Assembly Piece ID Number Bin 1']].astype(int)
combinations


# In[122]:


#reading in the assembly feather file
assembly = ft.read_feather('C:/Users/camdaman/Documents/GitHub/opentrons/IVA/AFB_epistasis_muts/assembly.feather')
assembly


# In[8]:


from PIL import Image
myImage = Image.open('C:/Users/camdaman/Documents/GitHub/opentrons/Gibson Assembly/concentration_limits.png');
myImage.show();


# In[326]:


from tkinter import * 

window = Tk()

window.geometry("400x100")
window.title("Combination ID number")

entry = Entry(window)
entry.pack()

def confirm():
    label = Label(window,text = entry.get())
    label.pack()
    global IDNumb
    IDNumb = entry.get()
   
    window.destroy()
   
   
    
button = Button(window,text="Enter Combination ID numbers, seperated by commas",command = confirm)
button.pack()


window.mainloop()
IDNumb


# In[327]:


IDNumb=[int(i) for i in IDNumb.split(',')]
IDNumb


# In[328]:


if 0 in IDNumb:    
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global AFB1_V113Aconc
        AFB1_V113Aconc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (AFB1_V113A)",command = confirm)
    button.pack()


    window.mainloop()
    AFB1_V113Aconc
    conc = AFB1_V113Aconc
    if  conc > 50:
        raise Exception('Concentration in ng/ul for this combination should be between 35 and 50. Your concentration value input is : {}'.format(conc))
    if  conc < 35:
        raise Exception('Concentration in ng/ul for this combination should be between 35 and 50. Your concentration value input is : {}'.format(conc))
    AFB1_V113Aconc
else: 
    AFB1_V113Aconc=0


# In[329]:


if 0 in IDNumb: 
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global C_AFB1_V113A2_C2conc
        C_AFB1_V113A2_C2conc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (C)_(AFB1_V113A2)_(C2)",command = confirm)
    button.pack()


    window.mainloop()
    C_AFB1_V113A2_C2conc
    conc = C_AFB1_V113A2_C2conc
    if  conc > 50:
        raise Exception('Concentration in ng/ul for this combination should be between 35 and 50. Your concentration value input is : {}'.format(conc))
    if  conc < 35:
        raise Exception('Concentration in ng/ul for this combination should be between 35 and 50. Your concentration value input is : {}'.format(conc))
    C_AFB1_V113A2_C2conc
else: 
    C_AFB1_V113A2_C2conc=0


# In[330]:


if 1 in IDNumb: 
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global AFB1_G143Dconc
        AFB1_G143Dconc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (AFB1_G143D)",command = confirm)
    button.pack()


    window.mainloop()
    AFB1_G143Dconc
    conc = AFB1_G143Dconc
    if  conc > 55:
        raise Exception('Concentration in ng/ul for this combination should be between 35 and 55. Your concentration value input is : {}'.format(conc))
    if  conc < 35:
        raise Exception('Concentration in ng/ul for this combination should be between 35 and 55. Your concentration value input is : {}'.format(conc))
    AFB1_G143Dconc
else: 
    AFB1_G143Dconc=0


# In[331]:


if 1 in IDNumb:  
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global A2_AFB1_G143D2_C3conc
        A2_AFB1_G143D2_C3conc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (A2)_(AFB1_G143D2)_(C3)",command = confirm)
    button.pack()


    window.mainloop()
    A2_AFB1_G143D2_C3conc
    conc = A2_AFB1_G143D2_C3conc
    if  conc > 55:
        raise Exception('Concentration in ng/ul for this combination should be between 35 and 55. Your concentration value input is : {}'.format(conc))
    if  conc < 35:
        raise Exception('Concentration in ng/ul for this combination should be between 35 and 55. Your concentration value input is : {}'.format(conc))
    A2_AFB1_G143D2_C3conc
else: 
    A2_AFB1_G143D2_C3conc=0


# In[332]:


if 2 in IDNumb: 
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global AFB1_K8Econc
        AFB1_K8Econc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (AFB1_K8E)",command = confirm)
    button.pack()


    window.mainloop()
    AFB1_K8Econc
    conc = AFB1_K8Econc
    if  conc > 45:
        raise Exception('Concentration in ng/ul for this combination should be between 30 and 45. Your concentration value input is : {}'.format(conc))
    if  conc < 30:
        raise Exception('Concentration in ng/ul for this combination should be between 30 and 45. Your concentration value input is : {}'.format(conc))
    AFB1_K8Econc
else: 
    AFB1_K8Econc=0


# In[333]:


if 2 in IDNumb: 
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global G_AFB1_K8E2__c_conc
        G_AFB1_K8E2__c_conc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (G)_(AFB1_K8E2)_(_c_)",command = confirm)
    button.pack()


    window.mainloop()
    G_AFB1_K8E2__c_conc
    conc = G_AFB1_K8E2__c_conc
    if  conc > 45:
        raise Exception('Concentration in ng/ul for this combination should be between 30 and 45. Your concentration value input is : {}'.format(conc))
    if  conc < 30:
        raise Exception('Concentration in ng/ul for this combination should be between 30 and 45. Your concentration value input is : {}'.format(conc))
    G_AFB1_K8E2__c_conc
else: 
    G_AFB1_K8E2__c_conc=0


# In[334]:


if 3 in IDNumb: 
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global AFB1_A460Econc
        AFB1_A460Econc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (AFB1_A460E)",command = confirm)
    button.pack()


    window.mainloop()
    AFB1_A460Econc
    conc = AFB1_A460Econc
    if  conc > 90:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 90. Your concentration value input is : {}'.format(conc))
    if  conc < 40:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 90. Your concentration value input is : {}'.format(conc))
    AFB1_A460Econc
else: 
    AFB1_A460Econc=0
AFB1_A460Econc


# In[335]:


if 3 in IDNumb: 
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global _A__AFB1_A460E2_cconc
        _A__AFB1_A460E2_cconc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (_A_)_(AFB1_A460E2)_(c-)",command = confirm)
    button.pack()


    window.mainloop()
    _A__AFB1_A460E2_cconc
    conc = _A__AFB1_A460E2_cconc
    if  conc > 90:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 90. Your concentration value input is : {}'.format(conc))
    if  conc < 40:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 90. Your concentration value input is : {}'.format(conc))
    _A__AFB1_A460E2_cconc
else: 
    _A__AFB1_A460E2_cconc=0
_A__AFB1_A460E2_cconc


# In[336]:


if 4 in IDNumb:    
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global AFB1_S434Econc
        AFB1_S434Econc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (AFB1_S434E)",command = confirm)
    button.pack()


    window.mainloop()
    AFB1_S434Econc
    conc = AFB1_S434Econc
    if  conc > 90:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 90. Your concentration value input is : {}'.format(conc))
    if  conc < 40:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 90. Your concentration value input is : {}'.format(conc))
    AFB1_S434Econc
else: 
    AFB1_S434Econc=0


# In[337]:


if 4 in IDNumb: 
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global glutamic_acid_AFB1_S434E2_cconc
        glutamic_acid_AFB1_S434E2_cconc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (glutamic_acid)_(AFB1_S434E2)_(-c-)",command = confirm)
    button.pack()


    window.mainloop()
    glutamic_acid_AFB1_S434E2_cconc
    conc = glutamic_acid_AFB1_S434E2_cconc
    if  conc > 90:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 90. Your concentration value input is : {}'.format(conc))
    if  conc < 40:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 90. Your concentration value input is : {}'.format(conc))
    glutamic_acid_AFB1_S434E2_cconc
else: 
    glutamic_acid_AFB1_S434E2_cconc=0


# In[338]:


if 5 in IDNumb: 
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global TIR1_E12Kconc
        TIR1_E12Kconc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (TIR1_E12K)",command = confirm)
    button.pack()


    window.mainloop()
    TIR1_E12Kconc
    conc = TIR1_E12Kconc
    if  conc > 45:
        raise Exception('Concentration in ng/ul for this combination should be between 30 and 45. Your concentration value input is : {}'.format(conc))
    if  conc < 30:
        raise Exception('Concentration in ng/ul for this combination should be between 30 and 45. Your concentration value input is : {}'.format(conc))
    TIR1_E12Kconc
else: 
    TIR1_E12Kconc=0


# In[339]:


if 5 in IDNumb: 
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global A_TIR1_E12K2_cconc
        A_TIR1_E12K2_cconc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (A)_(TIR1_E12K2)_(c)",command = confirm)
    button.pack()


    window.mainloop()
    A_TIR1_E12K2_cconc
    conc = A_TIR1_E12K2_cconc
    if  conc > 45:
        raise Exception('Concentration in ng/ul for this combination should be between 30 and 45. Your concentration value input is : {}'.format(conc))
    if  conc < 30:
        raise Exception('Concentration in ng/ul for this combination should be between 30 and 45. Your concentration value input is : {}'.format(conc))
    A_TIR1_E12K2_cconc
else: 
    A_TIR1_E12K2_cconc=0


# In[340]:


if 6 in IDNumb: 
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global TIR1_M473Aconc
        TIR1_M473Aconc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (TIR1_M473A)",command = confirm)
    button.pack()


    window.mainloop()
    TIR1_M473Aconc
    conc = TIR1_M473Aconc
    if  conc > 95:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 95. Your concentration value input is : {}'.format(conc))
    if  conc < 40:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 95. Your concentration value input is : {}'.format(conc))
    TIR1_M473Aconc
else: 
    TIR1_M473Aconc=0


# In[341]:


if 6 in IDNumb: 
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global C__TIR1_M473A2_C1conc
        C__TIR1_M473A2_C1conc = int(entry.get())
   
    window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (C_)_(TIR1_M473A2)_(C1)",command = confirm)
    button.pack()


    window.mainloop()
    C__TIR1_M473A2_C1conc
    conc = C__TIR1_M473A2_C1conc
    if  conc > 95:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 95. Your concentration value input is : {}'.format(conc))
    if  conc < 40:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 95. Your concentration value input is : {}'.format(conc))
    C__TIR1_M473A2_C1conc
else: 
    C__TIR1_M473A2_C1conc=0


# In[342]:


if 7 in IDNumb: 
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global TIR1_D170Aconc
        TIR1_D170Aconc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (TIR1_D170A)",command = confirm)
    button.pack()


    window.mainloop()
    TIR1_D170Aconc
    conc = TIR1_D170Aconc
    if  conc > 60:
        raise Exception('Concentration in ng/ul for this combination should be between 35 and 60. Your concentration value input is : {}'.format(conc))
    if  conc < 35:
        raise Exception('Concentration in ng/ul for this combination should be between 35 and 60. Your concentration value input is : {}'.format(conc))
    TIR1_D170Aconc
else: 
    TIR1_D170Aconc=0


# In[343]:


if 7 in IDNumb: 
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global c___TIR1_D170A2_cconc
        c___TIR1_D170A2_cconc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (c__)_(TIR1_D170A2)_(c---)",command = confirm)
    button.pack()


    window.mainloop()
    c___TIR1_D170A2_cconc
    conc = c___TIR1_D170A2_cconc
    if  conc > 60:
        raise Exception('Concentration in ng/ul for this combination should be between 35 and 60. Your concentration value input is : {}'.format(conc))
    if  conc < 35:
        raise Exception('Concentration in ng/ul for this combination should be between 35 and 60. Your concentration value input is : {}'.format(conc))
    c___TIR1_D170A2_cconc
else: 
    c___TIR1_D170A2_cconc=0


# In[344]:


if 8 in IDNumb: 
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global AFB1_noflagtagconc
        AFB1_noflagtagconc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (AFB1_noflagtag)",command = confirm)
    button.pack()


    window.mainloop()
    AFB1_noflagtagconc
    conc = AFB1_noflagtagconc
    if  conc > 80:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 80. Your concentration value input is : {}'.format(conc))
    if  conc < 40:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 80. Your concentration value input is : {}'.format(conc))
    AFB1_noflagtagconc
else: 
    AFB1_noflagtagconc=0


# In[345]:


if 8 in IDNumb: 
    from tkinter import * 

    window = Tk()

    window.geometry("300x100")
    window.title("Linearized vector backbone")

    entry = Entry(window)
    entry.pack()

    def confirm():
        label = Label(window,text = entry.get())
        label.pack()
        global AFB1_noflagtag2_cconc
        AFB1_noflagtag2_cconc = int(entry.get())
   
        window.destroy()
   
   
    
    button = Button(window,text="Enter ng/ul of (AFB1_noflagtag2)_(c--)",command = confirm)
    button.pack()


    window.mainloop()
    AFB1_noflagtag2_cconc
    conc = AFB1_noflagtag2_cconc
    if  conc > 80:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 80. Your concentration value input is : {}'.format(conc))
    if  conc < 40:
        raise Exception('Concentration in ng/ul for this combination should be between 40 and 80. Your concentration value input is : {}'.format(conc))
    AFB1_noflagtag2_cconc
else: 
    AFB1_noflagtag2_cconc=0


# In[346]:



concentration = {}
concentration['0'] = AFB1_V113Aconc
concentration['1'] = C_AFB1_V113A2_C2conc
concentration['2'] = AFB1_G143Dconc
concentration['3'] = A2_AFB1_G143D2_C3conc
concentration['4'] = AFB1_K8Econc
concentration['5'] = G_AFB1_K8E2__c_conc
concentration['6'] = AFB1_A460Econc
concentration['7'] = _A__AFB1_A460E2_cconc
concentration['8'] = AFB1_S434Econc
concentration['9'] = glutamic_acid_AFB1_S434E2_cconc
concentration['10'] = TIR1_E12Kconc
concentration['11'] = A_TIR1_E12K2_cconc
concentration['12'] = TIR1_M473Aconc
concentration['13'] = C__TIR1_M473A2_C1conc
concentration['14'] = TIR1_D170Aconc
concentration['15'] = c___TIR1_D170A2_cconc
concentration['16'] = AFB1_noflagtagconc
concentration['17'] = AFB1_noflagtag2_cconc


# In[347]:


#Adding the concnetration values to the feather file

for i, row in assembly.iterrows():
    assembly.loc[i,'concentration'] = concentration[str(i)]
assembly


# In[348]:


assembly['concentration'] = assembly['concentration'].apply(pd.to_numeric)


# In[349]:


assembly['Vector Backbone'] = np.where(assembly['Sequence Length']>3800,'True','False')
assembly


# In[350]:


assembly['backbone ul to add'] = np.where(assembly['Vector Backbone']== 'True',100/assembly['concentration'],assembly['concentration']*0)
assembly


# In[351]:


assemblyuL= {}
assemblyuL['0'] =(assembly.at[0,'Sequence Length']/assembly.at[1,'Sequence Length'])/assembly.at[0,'concentration']*100
assemblyuL['1'] = 0
assemblyuL['2'] =(assembly.at[2,'Sequence Length']/assembly.at[3,'Sequence Length'])/assembly.at[2,'concentration']*100
assemblyuL['3'] = 0
assemblyuL['4'] =(assembly.at[4,'Sequence Length']/assembly.at[5,'Sequence Length'])/assembly.at[4,'concentration']*100
assemblyuL['5'] = 0
assemblyuL['6'] =(assembly.at[6,'Sequence Length']/assembly.at[7,'Sequence Length'])/assembly.at[6,'concentration']*100
assemblyuL['7'] = 0
assemblyuL['8'] =(assembly.at[8,'Sequence Length']/assembly.at[9,'Sequence Length'])/assembly.at[8,'concentration']*100
assemblyuL['9'] = 0
assemblyuL['10'] =(assembly.at[10,'Sequence Length']/assembly.at[11,'Sequence Length'])/assembly.at[10,'concentration']*100
assemblyuL['11'] = 0
assemblyuL['12'] =(assembly.at[12,'Sequence Length']/assembly.at[13,'Sequence Length'])/assembly.at[12,'concentration']*100
assemblyuL['13'] = 0
assemblyuL['14'] =(assembly.at[14,'Sequence Length']/assembly.at[15,'Sequence Length'])/assembly.at[14,'concentration']*100
assemblyuL['15'] = 0
assemblyuL['16'] = 0
assemblyuL['17'] =(assembly.at[17,'Sequence Length']/assembly.at[16,'Sequence Length'])/assembly.at[17,'concentration']*100


# In[352]:


for i, row in assembly.iterrows():
    assembly.loc[i,'assembly ul to add'] = assemblyuL[str(i)]
assembly['assembly ul to add'] = assembly['assembly ul to add'].apply(pd.to_numeric)
assembly


# In[353]:


#Combinations volume, to use when calculating amount of water to add
volume = {}
volume['0']= assembly.at[0,'assembly ul to add'] + assembly.at[1,'backbone ul to add']
volume['1']= assembly.at[2,'assembly ul to add'] + assembly.at[3,'backbone ul to add']   
volume['2']= assembly.at[4,'assembly ul to add'] + assembly.at[5,'backbone ul to add']
volume['3']= assembly.at[6,'assembly ul to add'] + assembly.at[7,'backbone ul to add']
volume['4']= assembly.at[8,'assembly ul to add'] + assembly.at[9,'backbone ul to add']
volume['5']= assembly.at[10,'assembly ul to add'] + assembly.at[11,'backbone ul to add']
volume['6']= assembly.at[12,'assembly ul to add'] + assembly.at[13,'backbone ul to add']
volume['7']= assembly.at[14,'assembly ul to add'] + assembly.at[15,'backbone ul to add']
volume['8']=assembly.at[17,'assembly ul to add'] + assembly.at[16,'backbone ul to add'] 



for i, row in combinations.iterrows():
    combinations.loc[i,'volume'] = volume[str(i)]
combinations


# Labware, Need to define a place for linearized vector backbone, master mix, each additional assembly piece, and the thermocycler

# In[354]:


IDNumb


# In[355]:


#volumes of linarized vector backbone and assembly pieces to add

volumeap=np.array([0])
volumebb=np.array([0])

if 0 in IDNumb:
    volumeap=np.append(volumeap,assembly.at[0,'assembly ul to add'])
    volumebb=np.append(volumebb,assembly.at[1,'backbone ul to add'])
else: 
    print(".")
if 1 in IDNumb:
    volumeap=np.append(volumeap,assembly.at[2,'assembly ul to add'])
    volumebb=np.append(volumebb,assembly.at[3,'backbone ul to add'])
else: 
    print(".")
if 2 in IDNumb:
    volumeap=np.append(volumeap,assembly.at[4,'assembly ul to add'])
    volumebb=np.append(volumebb,assembly.at[5,'backbone ul to add'])
else: 
    print(".")    
if 3 in IDNumb:
    volumeap=np.append(volumeap,assembly.at[6,'assembly ul to add'])
    volumebb=np.append(volumebb,assembly.at[7,'backbone ul to add'])
else: 
    print(".")    
if 4 in IDNumb:
    volumeap=np.append(volumeap,assembly.at[8,'assembly ul to add'])
    volumebb=np.append(volumebb,assembly.at[9,'backbone ul to add'])
else: 
    print(".")    
if 5 in IDNumb:
    volumeap=np.append(volumeap,assembly.at[10,'assembly ul to add'])
    volumebb=np.append(volumebb,assembly.at[11,'backbone ul to add'])
else: 
    print(".")    
if 6 in IDNumb:
    volumeap=np.append(volumeap,assembly.at[12,'assembly ul to add'])
    volumebb=np.append(volumebb,assembly.at[13,'backbone ul to add'])
else: 
    print(".")    
if 7 in IDNumb:
    volumeap=np.append(volumeap,assembly.at[14,'assembly ul to add'])
    volumebb=np.append(volumebb,assembly.at[15,'backbone ul to add'])
else: 
    print(".")    
if 8 in IDNumb:
    volumeap=np.append(volumeap,assembly.at[17,'assembly ul to add'])
    volumebb=np.append(volumebb,assembly.at[16,'backbone ul to add'])
else: 
    print(".")    

volumeap
volumebb


# In[356]:


x = len(IDNumb)
x


# In[357]:


a= ['A1','A2','A3','A4','A5','A6','B1','B2','B3','B4','B5','B6','C1','C2','C3','C4','C5','C6','D1','D2','D3','D4','D5','D6']
a


# In[358]:


from opentrons import protocol_api
from opentrons import simulate
protocol = simulate.get_protocol_api('2.2')
    #protocol run function. the part after the colon lets your editor know
    #where to look for autocomplete suggestions
  


    #labware loading
TempUnit = protocol.load_module('Temperature Module',7)#Confirm location
well = TempUnit.load_labware('opentrons_24_aluminumblock_nest_2ml_snapcap')
tiprack1 = protocol.load_labware('opentrons_96_tiprack_20ul',1)#Confirm location
mastermix_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap',2) #Confirm location
assembly_piece_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap',3) #Confirm location
backbone_piece_rack = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap',6) #Confirm location
DH2O_rack=protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap',5)#Water well location
    #pipette loading
left_pipette = protocol.load_instrument('p20_single_gen2','left')

#reaction_rack = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul',4) #should the reaction tube be a 2ml snapcap?
    #Reaction tube currently in well 4
r=0
while r < x:     
    #Master mix to reaction tube
    left_pipette.pick_up_tip(tiprack1[a[3*(r)]])
    left_pipette.aspirate(15, mastermix_rack['A1']) #need to pick up 15 ul of master mix
    left_pipette.dispense(15, well[a[0+r]]) # need to dispense 15 ul of master mix 
    left_pipette.blow_out()
#automatically drops in trash
    
    #DH20 water to reaction tube

    left_pipette.aspirate(5-volumeap[1+r]-volumebb[1+r],DH2O_rack['A1'])#how much linearized vector backbone should be asperated to reach 100ng
    left_pipette.dispense(5-volumeap[1+r]-volumebb[1+r],well[a[0+r]]) #transporting assembly piece to reaction tube
    left_pipette.blow_out()
    left_pipette.drop_tip()

    #assembly piece to reaction tube
    left_pipette.pick_up_tip(tiprack1[a[3*r+1]])
    left_pipette.aspirate(volumeap[1+r],assembly_piece_rack[a[0+r]])#how much linearized vector backbone should be asperated to reach 100ng
    left_pipette.dispense(volumeap[1+r],well[a[0+r]]) #transporting assembly piece to reaction tube
    left_pipette.drop_tip()

    #backbone piece to reaction tube
    left_pipette.pick_up_tip(tiprack1[a[3*r+2]])
    left_pipette.aspirate(volumebb[1+r],backbone_piece_rack[a[0+r]])#how much linearized vector backbone should be asperated to reach 100ng
    left_pipette.dispense(volumebb[1+r],well[a[0+r]]) #transporting assembly piece to reaction tube
    left_pipette.drop_tip()
    r += 1
    #Run the temp unit
TempUnit.set_temperature(50) #50 degrees Celsius
protocol.delay(minutes=60) #60 minutes
TempUnit.deactivate()
print("place reaction tube on ice")


# In[ ]:




