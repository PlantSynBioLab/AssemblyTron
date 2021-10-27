import pandas
import numpy as np
import os
from datetime import date
 
#for this to work you need to run the python script on the same day that you make the new directory
#today = date.today()
#starter_date = str(today.strftime('%Y%m%d'))
#if folder was created on diff date:
#starter_date = 'typedatehere'
pwd = str(os.getcwd())

def walk_up_folder(path, depth=1):
    _cur_depth = 1        
    while _cur_depth < depth:
        path = os.path.dirname(path)
        _cur_depth += 1
    return path   

paths = pandas.read_csv(walk_up_folder(os.getcwd(), 3)+'/robotpaths.csv',engine = 'python', encoding='utf-8-sig')
paths



#Input_values = pandas.read_csv('Input.csv') 
Input_values = pandas.read_csv('Input.csv') 
Input_values
Date = str(int(Input_values.loc[0].at['Date']))
Date