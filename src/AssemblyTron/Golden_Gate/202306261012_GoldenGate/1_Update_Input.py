'''Input.csv Updater 

This updater script is to ensure the robot calls the correct Input.csv file. Failure to complete this step could result in errors and failure. 

This script requires `pandas` to be installed in the python environment where running.

This script is run as a module on the command line with the command `AssemblyTron.Update_Input.py` or if it is being run from a subdirectory the command would be `AssemblyTron.{subdirectory folder}.{dated folder}.1_Update_Input.py`

'''
if __name__ == '__main__':
        
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

    paths = pandas.read_csv(walk_up_folder(os.getcwd(), 3)+'\paths.csv') 

    shutil.copy2(os.getcwd()+'/Input.csv', walk_up_folder(os.getcwd(), 2))

    rc = subprocess.call([paths.loc[0].at['opentrons_repo']+'/Copy Cloning.bat'])
    rc
