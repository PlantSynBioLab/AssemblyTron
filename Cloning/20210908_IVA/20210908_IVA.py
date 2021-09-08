#variables:
#primer dilutions:
stkprm = 100 #concentration of the stock primer you are adding
stkvol = 1 #the volume of stock primer you are adding
dilprm = 2.5 #this is the concentration in uM that you want your working dilution to be

#pcr reaction
# need to get this from the df##Numprimers = 4 #this is how many primers go in each pcr reaction.
primerconcentration = 0.1 #this is the concentration you want each primer to be in the pcr reaction
pcrvol = 25 #this is the total volume of your pcr reaction 
templatengs = .5 #this is the concentration of template you want in your pcr rxn in ng/uL

#template dilutions tells you what the temps need to be diluted to initially so that you can just add 1 uL of template to the pcr:
#need to fill in stock template values further down the script
diltemp = (templatengs)*(pcrvol)/1

Q5 = 12.5 #How much Q5 to add
DPNI = 1 #How much DPNI to add
DPwater = 19
cutsmart = 5

#first import information from the j5 spreadsheet in order to perform appropriate steps
#import feather
#import pyarrow.feather as ft
import pandas
import numpy as np
import os

########################################################################################################

os.chdir("/data/user_storage/cloning/20210908_IVA")
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
    oligos.loc[i,'stock primer concentration'] = stkprm
    oligos.loc[i,'volume of stock primer to add'] = stkvol
    oligos.loc[i,'concentration of diluted primer'] = dilprm
    
for i, row in oligos.iterrows():
    oligos.loc[i,'volume of diluted primer'] = row['stock primer concentration']*row['volume of stock primer to add']/row['concentration of diluted primer']
    
oligos

################################################################################################################

os.chdir("/data/user_storage/cloning/20210908_IVA")
os.getcwd()
pcr = pandas.read_csv('pcr.csv')
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
df['Template Concentration'] = [455] #all you have to do is input the template concentrations in the right order

df

startnum = len(oligos['well'])

for i, row in df.iterrows():
    df.loc[i,'template_well'] = id2well[str(startnum+i)]
    


for i, row in df.iterrows():
    df.loc[i,'amount of template to add'] = 1


for i, row in df.iterrows():
   
        df.loc[i,'concentration of template (ng/uL)'] = diltemp

df['volume of dilute template prepared'] = df['Template Concentration']*stkvol/df['concentration of template (ng/uL)']

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

df.dtypes

#this line of code integrates the template concentrations into the pcr df
pcr_plustemplates = pandas.merge(pcr,df,on='Primary Template')
pcr_plustemplates

if len(pcr_plustemplates.columns) == 17:

    for i, row in pcr_plustemplates.iterrows():
   
        pcr_plustemplates.loc[i,'concentration of template (ng/uL)'] = diltemp

pcr_plustemplates['volume of dilute template prepared'] = pcr_plustemplates['Template Concentration']*stkvol/pcr_plustemplates['concentration of template (ng/uL)']

pcr_plustemplates

wellinfo = oligos[['ID Number','well']]
wellinfo

wellinfo = wellinfo.rename(columns={'ID Number':'Forward Oligo ID Number'})
pcr_plustemplates = pcr_plustemplates.merge(wellinfo, on= 'Forward Oligo ID Number')
wellinfo = wellinfo.rename(columns={'Forward Oligo ID Number':'Reverse Oligo ID Number','well':'well2'})
pcr_plustemplates = pcr_plustemplates.merge(wellinfo, on= 'Reverse Oligo ID Number')
pcr_plustemplates

################################################################################################################################

#read in assembly pieces as dataframe .... might not need this info
os.chdir("/data/user_storage/cloning/20210908_IVA")
os.getcwd()
assembly = pandas.read_csv('assembly.csv')
assembly

#############################################################################################################################

os.chdir("/data/user_storage/cloning/20210908_IVA")
os.getcwd()
combinations = pandas.read_csv('combinations.csv')
combinations

combinations[['ID Number','Assembly Piece ID Number Bin 0','Assembly Piece ID Number Bin 1','Assembly Piece ID Number Bin 2']] = combinations[['ID Number','Assembly Piece ID Number Bin 0','Assembly Piece ID Number Bin 1','Assembly Piece ID Number Bin 2']].astype(int)
combinations

primerlocations = pcr_plustemplates[['Reaction ID Number','well','well2']]
primerlocations

primerlocations = primerlocations.rename(columns={'Reaction ID Number':'Assembly Piece ID Number Bin 0'})
combinations = combinations.merge(primerlocations, on= 'Assembly Piece ID Number Bin 0')

primerlocations = primerlocations.rename(columns={'Assembly Piece ID Number Bin 0':'Assembly Piece ID Number Bin 1'})
combinations = combinations.merge(primerlocations, on= 'Assembly Piece ID Number Bin 1')

primerlocations = primerlocations.rename(columns={'Assembly Piece ID Number Bin 1':'Assembly Piece ID Number Bin 2'})
combinations = combinations.merge(primerlocations, on= 'Assembly Piece ID Number Bin 2')



combinations['primer concentrations'] = oligos['concentration of diluted primer']
combinations['amount primer to add to IVA'] = pcrvol*primerconcentration/combinations['primer concentrations']

templateinformation = pcr_plustemplates[['Reaction ID Number','template_well']]

templateinformation = templateinformation.rename(columns={'Reaction ID Number':'Assembly Piece ID Number Bin 0'})
combinations = combinations.merge(templateinformation, on= 'Assembly Piece ID Number Bin 0')

templateinformation = templateinformation.rename(columns={'Assembly Piece ID Number Bin 0':'Assembly Piece ID Number Bin 1'})
combinations = combinations.merge(templateinformation, on= 'Assembly Piece ID Number Bin 1')

templateinformation = templateinformation.rename(columns={'Assembly Piece ID Number Bin 1':'Assembly Piece ID Number Bin 2'})
combinations = combinations.merge(templateinformation, on= 'Assembly Piece ID Number Bin 2')

combinations['template concentrations'] = pcr_plustemplates['concentration of template (ng/uL)']
combinations['amount templates to add'] = pcrvol*templatengs/combinations['template concentrations']


filter_col = [col for col in combinations if col.startswith('well')] #here we calculate how much water to add
filter_col
primersadded = len(filter_col)

temp_col = [col for col in combinations if col.startswith('template_')] #here we calculate how much water to add
temp_col
tempsadded = len(temp_col)


combinations['water to add'] = (pcrvol-primersadded- tempsadded - Q5)


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

#############################################################################################################################

from opentrons import protocol_api

#Metadata is a dictionary of data that is read by the server and returned to the opentrons app. 
#give yourself credit. you are required to specify the 'apiLevel' herefrom opentrons import protocol_api
metadata = {
    'protocolName': 'ARF7 Deletions Protocol',
    'author': 'John Bryant <jbryant2@vt.edu>',
    'description': 'Protocol for performing PCR reactions and Plasmid assembly for TIR1 and AFB mutants',
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
    right_pipette.pick_up_tip()
    for i, row in df.iterrows():
        right_pipette.aspirate(volume = df.loc[i].at['water to add'], location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
        right_pipette.dispense(df.loc[i].at['water to add'], tuberack2[df.loc[i].at['template_well']], rate=2.0)
    
#add water to primer dilution tubes
    for i, row in oligos.iterrows():
        right_pipette.aspirate(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'], watertuberack['A1'], rate=2.0) #need to put 39uL of water into each dilution tube for primers,) #we need to find better way to loop through these commands
        right_pipette.dispense(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'], tuberack2[oligos.loc[i].at['well']], rate=2.0)
    right_pipette.drop_tip()    
    
#add stock templates to dilution tubes
    for i, row in df.iterrows():
        right_pipette.pick_up_tip()
        right_pipette.aspirate(df.loc[i].at['amount of template to add'], cold_tuberack[df.loc[i].at['template_well']], rate=2.0) #dilution well corresponds to stock well
        right_pipette.dispense(df.loc[i].at['amount of template to add'], tuberack2[df.loc[i].at['template_well']], rate=2.0) #makes a 12.5ng/uL template
        right_pipette.drop_tip()
    
#add stock primers to dilution tube
    for i, row in oligos.iterrows():
        left_pipette.pick_up_tip() #add in an iterrows function
        left_pipette.aspirate(oligos.loc[i].at['volume of stock primer to add'], cold_tuberack[oligos.loc[i].at['well']], rate=2.0)
        left_pipette.dispense(oligos.loc[i].at['volume of stock primer to add'], tuberack2[oligos.loc[i].at['well']], rate=2.0)
        left_pipette.drop_tip()
    
#robot pauses so user can take out stock primers and put in DNPNI
    protocol.pause('Take all stock primers and templates out. Add DPNI to A1, water to A2, and cutsmart to A3. Then proceed')
    
#now mix dilute primers, dilute templates, Q5, and water in pcr tube within thermocycler
    tc_mod.open_lid()
    
#add water first
    for i, row in combinations.iterrows():
        
        right_pipette.pick_up_tip()
        right_pipette.aspirate(combinations.loc[i].at['water to add'], watertuberack['A1'], rate=2.0) #need to write a function to add up all volumes that are being added and figure out how much water to add in automated way
        right_pipette.dispense(combinations.loc[i].at['water to add'], pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
        right_pipette.drop_tip()
    
#add 1uL of each primer
    for i, row in combinations.iterrows():
        
        for j in filter_col:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(combinations.loc[i].at['amount primer to add to IVA'], tuberack2[combinations.loc[i].at[j]], rate=2.0)
            left_pipette.dispense(combinations.loc[i].at['amount primer to add to IVA'], pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
            left_pipette.drop_tip()
    
#add 1uL of each template
    for i, row in combinations.iterrows():
        
        for j in temp_col:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(combinations.loc[i].at['amount templates to add'], tuberack2[combinations.loc[i].at[j]], rate=2.0)
            left_pipette.dispense(combinations.loc[i].at['amount primer to add to IVA'], pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
            left_pipette.drop_tip()
    
#add Q5 to each reaction
#keep Q5 in tuberack1['D6']                                            
    for i, row in combinations.iterrows():
        right_pipette.pick_up_tip()
        right_pipette.aspirate(Q5, cold_tuberack['D6'], rate=2.0)
        right_pipette.aspirate(Q5, pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
        right_pipette.drop_tip()
    
#Now run thermocycler to amplify DNA
    
#these parameters can be altered for different pcr reactionsabs
#should automate calculation of the parameters from j5 spreadsheets.
#maybe use the median annealing temperature in the spreadsheet
    
    tc_mod.set_lid_temperature(temperature = 105)
    tc_mod.close_lid()
    tc_mod.set_block_temperature(98, hold_time_seconds=30, block_max_volume=25)
    profile = [
        {'temperature': 98, 'hold_time_seconds': 10},
        {'temperature': 68, 'hold_time_seconds': 30},
        {'temperature': 72, 'hold_time_seconds': 60}] #should automate calculation of annealing temp based on spreadsheet
    tc_mod.execute_profile(steps=profile, repetitions=34, block_max_volume=25)
    tc_mod.set_block_temperature(72, hold_time_minutes=5, block_max_volume=25)
    tc_mod.set_block_temperature(4)
    tc_mod.open_lid()

#Now add DPNI for digestion

    for i, row in combinations.iterrows():
        right_pipette.pick_up_tip()
        right_pipette.aspirate(DPwater, cold_tuberack['A2'], rate=2.0)
        right_pipette.aspirate(DPwater, pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
        right_pipette.drop_tip()

    for i, row in combinations.iterrows():
        left_pipette.pick_up_tip()
        left_pipette.aspirate(cutsmart, cold_tuberack['A3'], rate=2.0)
        left_pipette.aspirate(cutsmart, pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
        left_pipette.drop_tip() 

    for i, row in combinations.iterrows():
        left_pipette.pick_up_tip()
        left_pipette.aspirate(DPNI, cold_tuberack['A1'], rate=2.0)
        left_pipette.aspirate(DPNI, pcrplate[combinations.loc[i].at['pcrwell']], rate=2.0)
        left_pipette.drop_tip()

    tc_mod.close_lid()
    tc_mod.set_block_temperature(37, hold_time_minutes=15, block_max_volume=50)
    tc_mod.set_block_temperature(80, hold_time_minutes=20, block_max_volume=50)
    tc_mod.set_block_temperature(4)
    tc_mod.deactivate_lid()
    protocol.pause('hold until time to grab tubes')
    
    tc_mod.open_lid()

    print('all done')