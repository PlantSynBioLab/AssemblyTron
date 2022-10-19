'''Input.csv Updater 

This updater script is to ensure the robot calls the correct Input.csv file. Failure to complete this step could result in errors and failure. 

This script is run as a module on the command line with the command `AssemblyTron.Update_Input.py` or if it is being run from a subdirectory the command would be `AssemblyTron.{subdirectory folder}.{dated folder}.1_Update_Input.py`

'''
if __name__ == '__main__':
        
    import os
    import shutil
    import subprocess

    def walk_up_folder(path, depth=1):
        _cur_depth = 1        
        while _cur_depth < depth:
            path = os.path.dirname(path)
            _cur_depth += 1
        return path   

    shutil.copy2(os.getcwd()+'/Input.csv', walk_up_folder(os.getcwd(), 2))

    rc = subprocess.call([paths.loc[0].at['opentrons_repo']+'/Copy Cloning.bat'])
    rc
