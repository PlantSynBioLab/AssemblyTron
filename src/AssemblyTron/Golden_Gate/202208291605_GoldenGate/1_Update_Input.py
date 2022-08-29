import os
import shutil
import subprocess
import pandas

def walk_up_folder(path, depth=1):
    _cur_depth = 1        
    while _cur_depth < depth:
        path = os.path.dirname(path)
        _cur_depth += 1
    return path   

shutil.copy2(os.getcwd()+'/Input.csv', walk_up_folder(os.getcwd(), 2))

paths = pandas.read_csv(walk_up_folder(os.getcwd(), 3)+'/paths.csv')
paths

rc = subprocess.call([paths.loc[0].at['opentrons_repo']+'/Copy Cloning.bat'])
rc
