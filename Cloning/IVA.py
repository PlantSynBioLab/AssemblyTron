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

#first import information from the j5 spreadsheet in order to perform appropriate steps
#import feather
#import pyarrow.feather as ft
import pandas
import numpy as np
import os
from datetime import date
 
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

paths = pandas.read_csv('/data/user_storage/robotpaths.csv')
paths



#Input_values = pandas.read_csv('Input.csv') 
Input_values = pandas.read_csv(paths.loc[0].at['opentrons_repo']+'/Cloning/Input.csv') 
Input_values
Date = str(int(Input_values.loc[0].at['Date']))
Date


Q5 = (0.5*Input_values.loc[0].at['pcrvol'])
diltemp = (Input_values.loc[0].at['templatengs'])*(Input_values.loc[0].at['pcrvol'])/1



os.chdir(paths.loc[0].at['opentrons_repo']+'/Cloning/'+Date+'_IVA')
os.getcwd()
oligos = pandas.read_csv('oligo.csv')
oligos


oligos['ID Number'] = oligos['ID Number'].astype(int)
oligos

if len(oligos.columns) < 9:
    oligos['well'] = ''
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
id2well['6'] = 'B1'
id2well['7'] = 'B2'
id2well['8'] = 'B3'
id2well['9'] = 'B4'
id2well['10'] = 'B5'
id2well['11'] = 'B6'
id2well['12'] = 'C1'
id2well['13'] = 'C2'
id2well['14'] = 'C3'
id2well['15'] = 'C4'
id2well['16'] = 'C5'
id2well['17'] = 'C6'
id2well['18'] = 'D1'
id2well['19'] = 'D2'
id2well['20'] = 'D3'
id2well['21'] = 'D4'
id2well['22'] = 'D5'
id2well['23'] = 'D6'

for i, row in oligos.iterrows():
    oligos.loc[i,'well'] = id2well[str(i)] #this only works because the index matces the id number. id number is a floating value
    oligos.loc[i,'stock primer concentration'] = Input_values.loc[0].at['stkprm']
    oligos.loc[i,'volume of stock primer to add'] = Input_values.loc[0].at['stkvol']
    oligos.loc[i,'concentration of diluted primer'] = Input_values.loc[0].at['dilprm']
oligos

for i, row in oligos.iterrows():
    oligos.loc[i,'volume of diluted primer'] = row['stock primer concentration']*row['volume of stock primer to add']/row['concentration of diluted primer']
    
oligos

oligos.to_csv('output_'+Date+'_oligo_IVA.csv')

##################################################################################################################################

#os.chdir("C:/Users/jonbr/Documents/GitHub/opentrons/Cloning/20210915_IVA")
os.getcwd()
pcr = pandas.read_csv('pcr.csv')
pcr.columns = pcr.columns.str.replace("'","")
pcr

pcr[['Reaction ID Number','Forward Oligo ID Number','Reverse Oligo ID Number']] = pcr[['Reaction ID Number','Forward Oligo ID Number','Reverse Oligo ID Number']].astype(int)
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

df



startnum = len(oligos['well'])

for i, row in df.iterrows():
    df.loc[i,'template_well'] = id2well[str(startnum+i)]
    


for i, row in df.iterrows():
    df.loc[i,'amount of template to add'] = 1


#template dilutions tells you what the temps need to be diluted to initially so that you can just add 1 uL of template to the pcr:
#need to fill in stock template values further down the script
diltemp = (Input_values.loc[0].at['templatengs'])*(Input_values.loc[0].at['pcrvol'])/1    
    
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

#df.to_csv('output_'+Date+'_templates_IVA.csv')

#df.dtypes

#this line of code integrates the template concentrations into the pcr df
pcr_plustemplates = pandas.merge(pcr,df,on='Primary Template')
pcr_plustemplates

if len(pcr_plustemplates.columns) == 17:

    for i, row in pcr_plustemplates.iterrows():
   
        pcr_plustemplates.loc[i,'concentration of template (ng/uL)'] = diltemp

pcr_plustemplates['volume of dilute template prepared'] = pcr_plustemplates['Template Concentration']*Input_values.loc[0].at['stkvol']/pcr_plustemplates['concentration of template (ng/uL)']

pcr_plustemplates

wellinfo = oligos[['ID Number','well']]
wellinfo

wellinfo = wellinfo.rename(columns={'ID Number':'Forward Oligo ID Number'})
pcr_plustemplates = pcr_plustemplates.merge(wellinfo, on= 'Forward Oligo ID Number')
wellinfo = wellinfo.rename(columns={'Forward Oligo ID Number':'Reverse Oligo ID Number','well':'well2'})
pcr_plustemplates = pcr_plustemplates.merge(wellinfo, on= 'Reverse Oligo ID Number')
pcr_plustemplates

pcr_plustemplates.to_csv('output_'+Date+'_pcr_IVA.csv')

#####################################################################################################################################3

#read in assembly pieces as dataframe .... might not need this info
#os.chdir("C:/Users/jonbr/Documents/GitHub/opentrons/Cloning/20210915_IVA")
os.getcwd()
assembly = pandas.read_csv('assembly.csv')
assembly

assembly.to_csv('output_'+Date+'_assembly_IVA.csv')

##############################################################################################################3

#os.chdir("C:/Users/jonbr/Documents/GitHub/opentrons/Cloning/20210915_IVA")
os.getcwd()
combinations = pandas.read_csv('combinations.csv')
combinations

combinations[['ID Number','Assembly Piece ID Number Bin 0','Assembly Piece ID Number Bin 1','Assembly Piece ID Number Bin 2','Assembly Piece ID Number Bin 3']] = combinations[['ID Number','Assembly Piece ID Number Bin 0','Assembly Piece ID Number Bin 1','Assembly Piece ID Number Bin 2','Assembly Piece ID Number Bin 3']].astype(int)
combinations

primerlocations = pcr_plustemplates[['Reaction ID Number','well','well2']]
primerlocations

if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 0']) == 'nan':
    primerlocations = primerlocations.rename(columns={'Reaction ID Number':'Assembly Piece ID Number Bin 0'})
    combinations = combinations.merge(primerlocations, on= 'Assembly Piece ID Number Bin 0')

if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 1']) == 'nan':
    primerlocations = primerlocations.rename(columns={'Assembly Piece ID Number Bin 0':'Assembly Piece ID Number Bin 1'})
    combinations = combinations.merge(primerlocations, on= 'Assembly Piece ID Number Bin 1')

if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 2']) == 'nan':
    primerlocations = primerlocations.rename(columns={'Assembly Piece ID Number Bin 1':'Assembly Piece ID Number Bin 2'})
    combinations = combinations.merge(primerlocations, on= 'Assembly Piece ID Number Bin 2')

#prevents well columns from having duplicate names
combinations.rename(columns={'well_x': 'well_a', 'well2_x': 'well_b', 'well_y': 'well_c', 'well2_y': 'well_d','well': 'well_e', 'well2': 'well_f'}, inplace=True)


if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 3']) == 'nan':
    primerlocations = primerlocations.rename(columns={'Assembly Piece ID Number Bin 2':'Assembly Piece ID Number Bin 3'})
    combinations = combinations.merge(primerlocations, on= 'Assembly Piece ID Number Bin 3')
    
if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 4']) == 'nan':
    primerlocations = primerlocations.rename(columns={'Assembly Piece ID Number Bin 3':'Assembly Piece ID Number Bin 4'})
    combinations = combinations.merge(primerlocations, on= 'Assembly Piece ID Number Bin 4')




combinations['primer concentrations'] = oligos['concentration of diluted primer']
combinations['amount primer to add to IVA'] = Input_values.loc[0].at['pcrvol']*Input_values.loc[0].at['primerconc']/combinations['primer concentrations']

templateinformation = pcr_plustemplates[['Reaction ID Number','template_well']]

if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 0']) == 'nan':
    templateinformation = templateinformation.rename(columns={'Reaction ID Number':'Assembly Piece ID Number Bin 0'})
    combinations = combinations.merge(templateinformation, on= 'Assembly Piece ID Number Bin 0')

if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 1']) == 'nan':
    templateinformation = templateinformation.rename(columns={'Assembly Piece ID Number Bin 0':'Assembly Piece ID Number Bin 1'})
    combinations = combinations.merge(templateinformation, on= 'Assembly Piece ID Number Bin 1')

if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 2']) == 'nan':
    templateinformation = templateinformation.rename(columns={'Assembly Piece ID Number Bin 1':'Assembly Piece ID Number Bin 2'})
    combinations = combinations.merge(templateinformation, on= 'Assembly Piece ID Number Bin 2')

#prevents template_well columns from having duplicate names
combinations.rename(columns={'template_well_x': 'template_well_a', 'template_well_y': 'template_well_b'}, inplace=True)
    
if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 3']) == 'nan':
    templateinformation = templateinformation.rename(columns={'Assembly Piece ID Number Bin 2':'Assembly Piece ID Number Bin 3'})
    combinations = combinations.merge(templateinformation, on= 'Assembly Piece ID Number Bin 3')
    
if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 4']) == 'nan':
    templateinformation = templateinformation.rename(columns={'Assembly Piece ID Number Bin 3':'Assembly Piece ID Number Bin 4'})
    combinations = combinations.merge(templateinformation, on= 'Assembly Piece ID Number Bin 4')

combinations['template concentrations'] = pcr_plustemplates['concentration of template (ng/uL)']
combinations['amount templates to add'] = Input_values.loc[0].at['pcrvol']*Input_values.loc[0].at['templatengs']/combinations['template concentrations']

combinations

filter_col = [col for col in combinations if col.startswith('well')] #here we calculate how much water to add
filter_col
primersadded = len(filter_col)

primersadded

temp_col = [col for col in combinations if col.startswith('template_')] #here we calculate how much water to add
temp_col
tempsadded = len(temp_col)


combinations['water to add'] = (Input_values.loc[0].at['pcrvol']-(primersadded*(Input_values.loc[0].at['pcrvol']*Input_values.loc[0].at['primerconc']/combinations['primer concentrations']))- tempsadded - Q5)


combinations

id2wellpcr = {}
id2wellpcr['0'] = 'A1'
id2wellpcr['1'] = 'A2'
id2wellpcr['2'] = 'A3'
id2wellpcr['3'] = 'A4'
id2wellpcr['4'] = 'A5'
id2wellpcr['5'] = 'A6'
id2wellpcr['6'] = 'A7'
id2wellpcr['7'] = 'A8'
id2wellpcr['8'] = 'A9'
id2wellpcr['9'] = 'A10'
id2wellpcr['10'] = 'A11'
id2wellpcr['11'] = 'A12'

combinations['pcrwell']=combinations['ID Number']
for i, row in combinations.iterrows():
    combinations.loc[i,'pcrwell'] = id2wellpcr[str(i)]
combinations


########################################################################################################################################
#determining which row of pcr rack to start on. 

# loc_i = pandas.read_csv('/data/user_storage/output_new_pcrwell_location.csv')

# if loc_i.loc[0].at['newlocation'].startswith('H'):

#     id2wellpcr = {}
#     id2wellpcr['0'] = 'A1'
#     id2wellpcr['1'] = 'A2'
#     id2wellpcr['2'] = 'A3'
#     id2wellpcr['3'] = 'A4'
#     id2wellpcr['4'] = 'A5'
#     id2wellpcr['5'] = 'A6'
#     id2wellpcr['6'] = 'A7'
#     id2wellpcr['7'] = 'A8'
#     id2wellpcr['8'] = 'A9'
#     id2wellpcr['9'] = 'A10'
#     id2wellpcr['10'] = 'A11'
#     id2wellpcr['11'] = 'A12'

# if loc_i.loc[0].at['newlocation'].startswith('A'):

#     id2wellpcr = {}
#     id2wellpcr['0'] = 'B1'
#     id2wellpcr['1'] = 'B2'
#     id2wellpcr['2'] = 'B3'
#     id2wellpcr['3'] = 'B4'
#     id2wellpcr['4'] = 'B5'
#     id2wellpcr['5'] = 'B6'
#     id2wellpcr['6'] = 'B7'
#     id2wellpcr['7'] = 'B8'
#     id2wellpcr['8'] = 'B9'
#     id2wellpcr['9'] = 'B10'
#     id2wellpcr['10'] = 'B11'
#     id2wellpcr['11'] = 'B12'

# if loc_i.loc[0].at['newlocation'].startswith('B'):

#     id2wellpcr = {}
#     id2wellpcr['0'] = 'C1'
#     id2wellpcr['1'] = 'C2'
#     id2wellpcr['2'] = 'C3'
#     id2wellpcr['3'] = 'C4'
#     id2wellpcr['4'] = 'C5'
#     id2wellpcr['5'] = 'C6'
#     id2wellpcr['6'] = 'C7'
#     id2wellpcr['7'] = 'C8'
#     id2wellpcr['8'] = 'C9'
#     id2wellpcr['9'] = 'C10'
#     id2wellpcr['10'] = 'C11'
#     id2wellpcr['11'] = 'C12'

# if loc_i.loc[0].at['newlocation'].startswith('C'):

#     id2wellpcr = {}
#     id2wellpcr['0'] = 'D1'
#     id2wellpcr['1'] = 'D2'
#     id2wellpcr['2'] = 'D3'
#     id2wellpcr['3'] = 'D4'
#     id2wellpcr['4'] = 'D5'
#     id2wellpcr['5'] = 'D6'
#     id2wellpcr['6'] = 'D7'
#     id2wellpcr['7'] = 'D8'
#     id2wellpcr['8'] = 'D9'
#     id2wellpcr['9'] = 'D10'
#     id2wellpcr['10'] = 'D11'
#     id2wellpcr['11'] = 'D12'

# if loc_i.loc[0].at['newlocation'].startswith('D'):

#     id2wellpcr = {}
#     id2wellpcr['0'] = 'E1'
#     id2wellpcr['1'] = 'E2'
#     id2wellpcr['2'] = 'E3'
#     id2wellpcr['3'] = 'E4'
#     id2wellpcr['4'] = 'E5'
#     id2wellpcr['5'] = 'E6'
#     id2wellpcr['6'] = 'E7'
#     id2wellpcr['7'] = 'E8'
#     id2wellpcr['8'] = 'E9'
#     id2wellpcr['9'] = 'E10'
#     id2wellpcr['10'] = 'E11'
#     id2wellpcr['11'] = 'E12'

# if loc_i.loc[0].at['newlocation'].startswith('E'):

#     id2wellpcr = {}
#     id2wellpcr['0'] = 'F1'
#     id2wellpcr['1'] = 'F2'
#     id2wellpcr['2'] = 'F3'
#     id2wellpcr['3'] = 'F4'
#     id2wellpcr['4'] = 'F5'
#     id2wellpcr['5'] = 'F6'
#     id2wellpcr['6'] = 'F7'
#     id2wellpcr['7'] = 'F8'
#     id2wellpcr['8'] = 'F9'
#     id2wellpcr['9'] = 'F10'
#     id2wellpcr['10'] = 'F11'
#     id2wellpcr['11'] = 'F12'

# if loc_i.loc[0].at['newlocation'].startswith('F'):

#     id2wellpcr = {}
#     id2wellpcr['0'] = 'G1'
#     id2wellpcr['1'] = 'G2'
#     id2wellpcr['2'] = 'G3'
#     id2wellpcr['3'] = 'G4'
#     id2wellpcr['4'] = 'G5'
#     id2wellpcr['5'] = 'G6'
#     id2wellpcr['6'] = 'G7'
#     id2wellpcr['7'] = 'G8'
#     id2wellpcr['8'] = 'G9'
#     id2wellpcr['9'] = 'G10'
#     id2wellpcr['10'] = 'G11'
#     id2wellpcr['11'] = 'G12'

# if loc_i.loc[0].at['newlocation'].startswith('G'):

#     id2wellpcr = {}
#     id2wellpcr['0'] = 'H1'
#     id2wellpcr['1'] = 'H2'
#     id2wellpcr['2'] = 'H3'
#     id2wellpcr['3'] = 'H4'
#     id2wellpcr['4'] = 'H5'
#     id2wellpcr['5'] = 'H6'
#     id2wellpcr['6'] = 'H7'
#     id2wellpcr['7'] = 'H8'
#     id2wellpcr['8'] = 'H9'
#     id2wellpcr['9'] = 'H10'
#     id2wellpcr['10'] = 'H11'
#     id2wellpcr['11'] = 'H12'

# ####################################################################################################################################

# combinations['pcrwell']=combinations['ID Number']
# for i, row in combinations.iterrows():
#     combinations.loc[i,'pcrwell'] = id2wellpcr[str(i)]
# combinations

# #combinations.to_csv('output_'+Date+'_combination_IVA.csv')

# last_pcrwell = len(combinations['pcrwell'])
# last_pcrwell
# last_pcrwell_id = last_pcrwell - 1
# last_pcrwell_id

# #lastlocation = plasmid['Digestion Tube'].iloc[-1]
# lastlocation = combinations.loc[last_pcrwell_id].at['pcrwell']
# lastlocation

# #lastlocation = 'H12'

# rowchar = lastlocation[0]
# r = ord(rowchar[0])

# if lastlocation == 'H12':
#     raise ValueError("you need new pcr wells")

# elif len(lastlocation) == 2:
#     newlocation = lastlocation[0] + str(int(lastlocation[1]) + 1)
    
# elif len(lastlocation) == 3:
#     if lastlocation[2] == '2':
#         newlocation = chr(r + 1) + '1'
#     elif lastlocation[2] == '1' or '0':
#         newlocation = lastlocation[0] + lastlocation[1] + str(int(lastlocation[2]) + 1)

# newlocation

   
# newlocation
# newlocationlist = [newlocation]

# columns = ['newlocation']

# # value: series of values
# newlocation_df = pandas.DataFrame(newlocationlist, columns=columns)
# newlocation_df

# newlocation_df.to_csv('/data/user_storage/output_new_pcrwell_location.csv')

###################################################################################################
#annealing calcs

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
    Lowest_high = locals()[x].nsmallest(1,'Upper_temp')
    Lowest_high
    Highest_low = locals()[x].nlargest(1,'Lower_temp')
    Highest_low
    LH = Lowest_high['Upper_temp']
    HL=Highest_low['Lower_temp']
    A = LH-HL
    if A.all() > 0:
        annealing_temp = Lowest_high['Upper_temp']
    if A.all() < 0:
        annealing_temp = (Lowest_high['Upper_temp']+Highest_low['Lower_temp'])/2
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

Annealing_and_extension.to_csv('output_'+Date+'_Annealing_extension.csv')
combinations.to_csv('output_'+Date+'_combinations.csv')
####################################################################################################################

##########################################################################################
from opentrons import protocol_api

#Metadata is a dictionary of data that is read by the server and returned to the opentrons app. 
#give yourself credit. you are required to specify the 'apiLevel' herefrom opentrons import protocol_api
metadata = {
    'protocolName': 'IVA Protocol',
    'author': 'John Bryant <jbryant2@vt.edu>',
    'description': 'Protocol for performing IVA assembly',
    'apiLevel': '2.10'
}
print(metadata)




def run(protocol: protocol_api.ProtocolContext): #for actually running the script in the robot
#will have to indent everything to be defined by the run function

#from opentrons import simulate
#protocol = simulate.get_protocol_api('2.2')
    
#labware:
    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', '9')
    tiprack2 = protocol.load_labware('opentrons_96_tiprack_300ul','6')
    tiprack3 = protocol.load_labware("opentrons_96_tiprack_10ul", '5')
#tuberack1 = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap','1') #holds stock primers and templates
    watertuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical','3') #holds molec bio grad H2O
    tuberack2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','2') # holds dilute primers and templates
    
    tc_mod = protocol.load_module('Thermocycler Module')
    pcrplate = tc_mod.load_labware('nest_96_wellplate_100ul_pcr_full_skirt')
    temp_module = protocol.load_module('temperature module', 1)
    cold_tuberack = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', label='Temperature-Controlled Tubes')
    temp_module.set_temperature(4)
    print(temp_module.temperature)
    tc_mod.open_lid()

#########Some notes:    
#specify the order of stock primers and template in tuberack1 here:
#good place to add the pop-up window
#A1-D3 = stock primers
#D4-D5 = stock templates
#stock tubes and dilution tubes need to be set up in the same order
#as of now Q5 is in 
    
#pipettes
    right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1, tiprack2])
    left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3])
    
##################################COMMANDS####################################
    
#add water to template dilution tubes. ***df is the template description dataframe
#Since we are just moving water I will use the same pipette tip to save plastic
    
    for i, row in df.iterrows():
        if df.loc[i].at['water to add'] > 12:
            right_pipette.pick_up_tip()
            right_pipette.aspirate(volume = df.loc[i].at['water to add'], location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
            right_pipette.dispense(df.loc[i].at['water to add'], tuberack2[df.loc[i].at['template_well']], rate=2.0)
            right_pipette.drop_tip()
        if 8 < df.loc[i].at['water to add'] < 12:
            right_pipette.pick_up_tip()
            right_pipette.aspirate(2*(df.loc[i].at['water to add']), watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
            right_pipette.dispense(2*(df.loc[i].at['water to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0)
            right_pipette.drop_tip()
        if df.loc[i].at['water to add'] < 8:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(4*(df.loc[i].at['water to add']), location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
            left_pipette.dispense(4*(df.loc[i].at['water to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0)
            left_pipette.drop_tip()
        #right_pipette.blow_out()

#add water to primer dilution tubes
    right_pipette.pick_up_tip()
    for i, row in oligos.iterrows():
        right_pipette.aspirate(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'], watertuberack['A1'], rate=2.0) #need to put 39uL of water into each dilution tube for primers,) #we need to find better way to loop through these commands
        right_pipette.dispense(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'], tuberack2[oligos.loc[i].at['well']], rate=2.0)
        #right_pipette.blow_out()
    right_pipette.drop_tip()    
    
#add stock templates to dilution tubes
    for i, row in df.iterrows():
        if df.loc[i].at['water to add'] > 12:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(df.loc[i].at['amount of template to add'], cold_tuberack[df.loc[i].at['template_well']], rate=2.0) #dilution well corresponds to stock well
            left_pipette.dispense(df.loc[i].at['amount of template to add'], tuberack2[df.loc[i].at['template_well']], rate=2.0) #makes a 12.5ng/uL template
            left_pipette.mix(3,5,tuberack2[df.loc[i].at['template_well']])
            #left_pipette.blow_out()
            left_pipette.drop_tip()
        if 8 < df.loc[i].at['water to add'] < 12:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(2*(df.loc[i].at['amount of template to add']), cold_tuberack[df.loc[i].at['template_well']], rate=2.0) #dilution well corresponds to stock well
            left_pipette.dispense(2*(df.loc[i].at['amount of template to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0) #makes a 12.5ng/uL template
            left_pipette.mix(3,5,tuberack2[df.loc[i].at['template_well']])
            #left_pipette.blow_out()
            left_pipette.drop_tip()
        if df.loc[i].at['water to add'] < 8:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(4*(df.loc[i].at['amount of template to add']), cold_tuberack[df.loc[i].at['template_well']], rate=2.0) #dilution well corresponds to stock well
            left_pipette.dispense(4*(df.loc[i].at['amount of template to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0) #makes a 12.5ng/uL template
            left_pipette.mix(3,5,tuberack2[df.loc[i].at['template_well']])
            #left_pipette.blow_out()
            left_pipette.drop_tip()
    
#add stock primers to dilution tube
    for i, row in oligos.iterrows():
        left_pipette.pick_up_tip() #add in an iterrows function
        left_pipette.aspirate(oligos.loc[i].at['volume of stock primer to add'], cold_tuberack[oligos.loc[i].at['well']], rate=2.0)
        left_pipette.dispense(oligos.loc[i].at['volume of stock primer to add'], tuberack2[oligos.loc[i].at['well']], rate=2.0)
        left_pipette.mix(3,5,tuberack2[oligos.loc[i].at['well']])
        #left_pipette.blow_out()
        left_pipette.drop_tip()
    
#mix contents with pipette tip (reps, max volume, location) for templates and primers
    # for i, row in df.iterrows():
    #     if df.loc[i].at['water to add'] > 8:
    #         right_pipette.pick_up_tip()
    #         right_pipette.mix(3,df.loc[i].at['water to add'],tuberack2[df.loc[i].at['template_well']])
    #         #right_pipette.blow_out()
    #         right_pipette.drop_tip()
    #     if df.loc[i].at['water to add'] < 8:
    #         right_pipette.pick_up_tip()
    #         right_pipette.mix(3,3*df.loc[i].at['water to add'],tuberack2[df.loc[i].at['template_well']])
    #         #right_pipette.blow_out()
    #         right_pipette.drop_tip()

    for i, row in oligos.iterrows():
        right_pipette.pick_up_tip()
        right_pipette.mix(3,oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'],tuberack2[oligos.loc[i].at['well']])
        #right_pipette.blow_out()
        right_pipette.drop_tip()

#robot pauses so user can take out stock primers and put in DNPNI
    protocol.pause('Take all stock primers and templates out. Add DPNI to A1, water to A2, and cutsmart to A3. Then proceed')
    
#now mix dilute primers, dilute templates, Q5, and water in pcr tube within thermocycler
    tc_mod.open_lid()
    
#add water first
    for i, row in combinations.iterrows():
        if combinations.loc[i].at['water to add'] > 8:
            right_pipette.pick_up_tip()
            right_pipette.aspirate(combinations.loc[i].at['water to add'], watertuberack['A1'], rate=2.0) #need to write a function to add up all volumes that are being added and figure out how much water to add in automated way
            right_pipette.dispense(combinations.loc[i].at['water to add'], pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
            right_pipette.blow_out()
            right_pipette.drop_tip()
        if combinations.loc[i].at['water to add'] < 8:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(combinations.loc[i].at['water to add'], watertuberack['A1'], rate=2.0) #need to write a function to add up all volumes that are being added and figure out how much water to add in automated way
            left_pipette.dispense(combinations.loc[i].at['water to add'], pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
            left_pipette.blow_out()
            left_pipette.drop_tip()
    
#add 1uL of each primer
    for i, row in combinations.iterrows():
        
        for j in filter_col:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(combinations.loc[i].at['amount primer to add to IVA'], tuberack2[combinations.loc[i].at[j]], rate=2.0)
            left_pipette.dispense(combinations.loc[i].at['amount primer to add to IVA'], pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
            #left_pipette.mix(3,2,pcrplate[combinations.loc[i].at['pcrwell']])
            left_pipette.blow_out()
            left_pipette.drop_tip()
    
#add 1uL of each template
    for i, row in combinations.iterrows():
        
        for j in temp_col:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(combinations.loc[i].at['amount templates to add'], tuberack2[combinations.loc[i].at[j]], rate=2.0)
            left_pipette.dispense(combinations.loc[i].at['amount templates to add'], pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
            #left_pipette.mix(3,3,pcrplate[combinations.loc[i].at['pcrwell']])
            left_pipette.blow_out()
            left_pipette.drop_tip()
    
#add Q5 to each reaction
#keep Q5 in tuberack1['D6']                                            
    for i, row in combinations.iterrows():
        right_pipette.pick_up_tip()
        right_pipette.aspirate(Q5, cold_tuberack['D6'], rate=2.0)
        right_pipette.dispense(Q5, pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
        right_pipette.mix(3,Q5+3,pcrplate[combinations.loc[i].at['pcrwell']])
        #right_pipette.blow_out()
        right_pipette.drop_tip()

#mix up
    # for i, row in combinations.iterrows():
    #     right_pipette.pick_up_tip()
    #     right_pipette.mix(3,combinations.loc[i].at['water to add'],pcrplate[combinations.loc[i].at['pcrwell']])
    #     right_pipette.blow_out()
    #     right_pipette.drop_tip()
    
#Now run thermocycler to amplify DNA
    
#these parameters can be altered for different pcr reactionsabs
#should automate calculation of the parameters from j5 spreadsheets.
#maybe use the median annealing temperature in the spreadsheet
    tc_mod.close_lid()
    tc_mod.set_lid_temperature(temperature = 105)
    tc_mod.set_block_temperature(98, hold_time_seconds=30, block_max_volume=25)
    profile = [
        {'temperature': 98, 'hold_time_seconds': 10},
        {'temperature': round(Annealing_and_extension.loc[0].at['Annealing temp'],1), 'hold_time_seconds': 30},
        {'temperature': 72, 'hold_time_seconds': round(Annealing_and_extension.loc[0].at['extension time (seconds)'],1)}] #should automate calculation of annealing temp based on spreadsheet
    tc_mod.execute_profile(steps=profile, repetitions=34, block_max_volume=25)
    tc_mod.set_block_temperature(72, hold_time_minutes=5, block_max_volume=25)
    tc_mod.set_block_temperature(4)
    tc_mod.open_lid()
    protocol.pause()

#Now add DPNI for digestion

    for i, row in combinations.iterrows():
        if Input_values.loc[0].at['DPwater'] > 10:
            right_pipette.pick_up_tip()
            right_pipette.aspirate(Input_values.loc[0].at['DPwater'], watertuberack['A1'], rate=2.0)
            right_pipette.dispense(Input_values.loc[0].at['DPwater'], pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
            right_pipette.mix(3,Input_values.loc[0].at['DPwater'],pcrplate[combinations.loc[i].at['pcrwell']])
            right_pipette.drop_tip()
        if Input_values.loc[0].at['DPwater'] < 10:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(Input_values.loc[0].at['DPwater'], watertuberack['A1'], rate=2.0)
            left_pipette.dispense(Input_values.loc[0].at['DPwater'], pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
            left_pipette.mix(3,Input_values.loc[0].at['DPwater'],pcrplate[combinations.loc[i].at['pcrwell']])
            left_pipette.drop_tip()

    for i, row in combinations.iterrows():
        left_pipette.pick_up_tip()
        left_pipette.aspirate(Input_values.loc[0].at['cutsmart'], cold_tuberack['D4'], rate=2.0)
        left_pipette.dispense(Input_values.loc[0].at['cutsmart'], pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
        left_pipette.mix(3,Input_values.loc[0].at['cutsmart'],pcrplate[combinations.loc[i].at['pcrwell']])
        left_pipette.drop_tip() 

    for i, row in combinations.iterrows():
        left_pipette.pick_up_tip()
        left_pipette.aspirate(Input_values.loc[0].at['DPNI'], cold_tuberack['D5'], rate=2.0)
        left_pipette.dispense(Input_values.loc[0].at['DPNI'], pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
        left_pipette.mix(3,Input_values.loc[0].at['cutsmart']+Input_values.loc[0].at['DPNI'],pcrplate[combinations.loc[i].at['pcrwell']])
        left_pipette.drop_tip()

    #mix up
    for i, row in combinations.iterrows():
        right_pipette.pick_up_tip()
        right_pipette.mix(3,Q5+Input_values.loc[0].at['DPwater']+Input_values.loc[0].at['cutsmart'],pcrplate[combinations.loc[i].at['pcrwell']])
        #right_pipette.blow_out()
        right_pipette.drop_tip()

    tc_mod.close_lid()

    tc_mod.set_lid_temperature(105)
    tc_mod.set_block_temperature(37, hold_time_minutes=30, block_max_volume=50)
    tc_mod.set_block_temperature(80, hold_time_minutes=20, block_max_volume=50)
    tc_mod.set_block_temperature(4, block_max_volume = 50)
    tc_mod.deactivate_lid()
    protocol.pause('hold until time to grab tubes')
    
    tc_mod.open_lid()

    print('all done')
