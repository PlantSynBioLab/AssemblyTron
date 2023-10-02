''' Homology Dependent Assembly Protocol Script with separate PCRs

This script performs Homology dependent assembly where fragments for each assembly are amplified in separate tubes and uses a gradient thermocycler. This protocol is thoroughly validated and robust, so we recommend using it. 

This script runs on the OT-2 via the run app. It calls CSVs which must be transferred to the OT-2 processor prior to running. This script is not designed to run a personal computer on the command line.

'''


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
from os.path import exists
#from datetime import date

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




#########################################################################################################################################
#########actual commands#############3

from opentrons import protocol_api

#Metadata is a dictionary of data that is read by the server and returned to the opentrons app. 
#give yourself credit. you are required to specify the 'apiLevel' herefrom opentrons import protocol_api
metadata = {
    'protocolName': 'IVA Separate PCRs',
    'author': 'John Bryant <jbryant2@vt.edu>',
    'description': 'Protocol for performing PCR reactions and Plasmid assembly for TIR1 and AFB mutants',
    'apiLevel': '2.10'
}
print(metadata)




def run(protocol: protocol_api.ProtocolContext): #for actually running the script in the robot
#will have to indent everything to be defined by the run function

#from opentrons import simulate
#protocol = simulate.get_protocol_api('2.2')
    paths = pandas.read_csv('/data/user_storage/robotpaths.csv')
    paths

    Input_values = pandas.read_csv(paths.loc[0].at['opentrons_repo']+'/Cloning/Input.csv') 
    Date = str(int(Input_values.loc[0].at['Date']))
    Time = str(int(Input_values.loc[0].at['Time']))

    Q5 = (0.5*Input_values.loc[0].at['pcrvol'])
    diltemp = (Input_values.loc[0].at['templatengs'])*(Input_values.loc[0].at['pcrvol'])/1
    DMSO = (0.03*Input_values.loc[0].at['pcrvol'])

    os.chdir(paths.loc[0].at['opentrons_repo']+'/Cloning/'+Date+Time+'_IVA')
    # os.getcwd()
    oligos = pandas.read_csv('oligo.csv')
    gradient = pandas.read_csv('gradient.csv')
    pcr = pandas.read_csv('pcr.csv')
    assembly = pandas.read_csv('assembly.csv')
    combinations = pandas.read_csv('combinations.csv')
    Length = pcr.nlargest(1,'Length')
    GG_dfs = pandas.read_csv('GG_dfs.csv')
    section = pandas.read_csv('section.csv')
        
    if exists('gg1.csv'):
        gg1 = pandas.read_csv('gg1.csv')
    if exists('gg2.csv'):
        gg2 = pandas.read_csv('gg2.csv')
    if exists('gg3.csv'):
        gg3 = pandas.read_csv('gg3.csv')
    if exists('gg4.csv'):
        gg4 = pandas.read_csv('gg4.csv')
    if exists('gg5.csv'):
        gg5 = pandas.read_csv('gg5.csv')
    if exists('gg6.csv'):
        gg6 = pandas.read_csv('gg6.csv')
    if exists('gg7.csv'):
        gg7 = pandas.read_csv('gg7.csv')
    if exists('gg8.csv'):
        gg8 = pandas.read_csv('gg8.csv')
    if exists('gg9.csv'):
        gg9 = pandas.read_csv('gg9.csv')
    if exists('gg10.csv'):
        gg10 = pandas.read_csv('gg10.csv')
    if exists('gg11.csv'):
        gg11 = pandas.read_csv('gg11.csv')
    if exists('gg12.csv'):
        gg12 = pandas.read_csv('gg12.csv')

    if '96well' in pcr.columns:
        pcr = pcr.rename(columns={"96well": "well", "96well2": "well2"})
        rackchanger = 'Y'
    else:
        rackchanger = 'N'
#labware:
    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', '9')
    #tiprack2 = protocol.load_labware("opentrons_96_tiprack_10ul",'6')
    tiprack3 = protocol.load_labware("opentrons_96_tiprack_10ul", '5')
#tuberack1 = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap','1') #holds stock primers and templates
    watertuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical','3') #holds molec bio grad H2O
    if rackchanger == 'Y':
        tuberack2 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul','2')
    else:
        tuberack2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','2') # holds dilute primers and templates
    
    secondarydils = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul','4')
    tc_mod = protocol.load_module('Thermocycler Module')
    pcrplate = tc_mod.load_labware('nest_96_wellplate_100ul_pcr_full_skirt')
    temp_module = protocol.load_module('temperature module', 1)
    cold_tuberack = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', label='Temperature-Controlled Tubes')
    temp_module.set_temperature(4)
    print(temp_module.temperature)
    tc_mod.open_lid()

# #########Some notes:    
# #specify the order of stock primers and template in tuberack1 here:
# #good place to add the pop-up window
# #A1-D3 = stock primers
# #D4-D5 = stock templates
# #stock tubes and dilution tubes need to be set up in the same order
# #as of now Q5 is in 
    
#pipettes
    right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1])
    left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3])


    
##################################COMMANDS####################################
    
#add water to template dilution tubes. ***df is the template description dataframe
#Since we are just moving water I will use the same pipette tip to save plastic

#     x = 'Dilution'
#     if x in Input_values['section'].values:

# #add water for templates
#         for i, row in df.iterrows():
#             if df.loc[i].at['water to add'] > 10:
#                 right_pipette.pick_up_tip()
#                 right_pipette.aspirate(volume = df.loc[i].at['water to add'], location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
#                 right_pipette.dispense(df.loc[i].at['water to add'], tuberack2[df.loc[i].at['template_well']], rate=2.0)
#                 right_pipette.drop_tip()
#             if 3.333 < df.loc[i].at['water to add'] < 10:
#                 if 3*(df.loc[i].at['water to add']) < 10:
#                     left_pipette.pick_up_tip()
#                     left_pipette.aspirate(3*(df.loc[i].at['water to add']), location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
#                     left_pipette.dispense(3*(df.loc[i].at['water to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0)
#                     left_pipette.drop_tip()
#                 else:
#                     right_pipette.pick_up_tip()
#                     right_pipette.aspirate(3*(df.loc[i].at['water to add']), location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
#                     right_pipette.dispense(3*(df.loc[i].at['water to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0)
#                     right_pipette.drop_tip()
#             if 1 < df.loc[i].at['water to add'] < 3.333:
#                 if 4*(df.loc[i].at['water to add']) < 10:
#                     left_pipette.pick_up_tip()
#                     left_pipette.aspirate(4*(df.loc[i].at['water to add']), location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
#                     left_pipette.dispense(4*(df.loc[i].at['water to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0)
#                     left_pipette.drop_tip()
#                 else:
#                     right_pipette.pick_up_tip()
#                     right_pipette.aspirate(4*(df.loc[i].at['water to add']), location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
#                     right_pipette.dispense(4*(df.loc[i].at['water to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0)
#                     right_pipette.drop_tip()
#             if df.loc[i].at['water to add'] < 1:
#                 left_pipette.pick_up_tip()
#                 left_pipette.aspirate(6*(df.loc[i].at['water to add']), location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
#                 left_pipette.dispense(6*(df.loc[i].at['water to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0)
#                 left_pipette.drop_tip()

#             #right_pipette.blow_out()
    

#     #add water to primer dilution tubes
#         right_pipette.pick_up_tip()
#         for i, row in oligos.iterrows():
#             right_pipette.aspirate(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'], watertuberack['A1'], rate=2.0) #need to put 39uL of water into each dilution tube for primers,) #we need to find better way to loop through these commands
#             right_pipette.dispense(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'], tuberack2[oligos.loc[i].at['well']], rate=2.0)
#             #right_pipette.blow_out()
#         right_pipette.drop_tip()    
        
#     #add stock templates to dilution tubes
#         for i, row in df.iterrows():
#             if df.loc[i].at['water to add'] > 10:
#                 left_pipette.pick_up_tip()
#                 left_pipette.aspirate(df.loc[i].at['amount of template to add'], cold_tuberack[df.loc[i].at['template_well']], rate=2.0) #dilution well corresponds to stock well
#                 left_pipette.dispense(df.loc[i].at['amount of template to add'], tuberack2[df.loc[i].at['template_well']], rate=2.0) #makes a 12.5ng/uL template
#                 left_pipette.mix(3,5,tuberack2[df.loc[i].at['template_well']])
#                 #left_pipette.blow_out()
#                 left_pipette.drop_tip()
#             if 3.333 < df.loc[i].at['water to add'] < 10:
#                 left_pipette.pick_up_tip()
#                 left_pipette.aspirate(3*(df.loc[i].at['amount of template to add']), cold_tuberack[df.loc[i].at['template_well']], rate=2.0) #dilution well corresponds to stock well
#                 left_pipette.dispense(3*(df.loc[i].at['amount of template to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0) #makes a 12.5ng/uL template
#                 left_pipette.mix(3,5,tuberack2[df.loc[i].at['template_well']])
#                 #left_pipette.blow_out()
#                 left_pipette.drop_tip()
#             if 1 < df.loc[i].at['water to add'] < 3.333:
#                 left_pipette.pick_up_tip()
#                 left_pipette.aspirate(4*(df.loc[i].at['amount of template to add']), cold_tuberack[df.loc[i].at['template_well']], rate=2.0) #dilution well corresponds to stock well
#                 left_pipette.dispense(4*(df.loc[i].at['amount of template to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0) #makes a 12.5ng/uL template
#                 left_pipette.mix(3,5,tuberack2[df.loc[i].at['template_well']])
#                 #left_pipette.blow_out()
#                 left_pipette.drop_tip()
#             if df.loc[i].at['water to add'] < 1:
#                 left_pipette.pick_up_tip()
#                 left_pipette.aspirate(6*(df.loc[i].at['amount of template to add']), cold_tuberack[df.loc[i].at['template_well']], rate=2.0) #dilution well corresponds to stock well
#                 left_pipette.dispense(6*(df.loc[i].at['amount of template to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0) #makes a 12.5ng/uL template
#                 left_pipette.mix(3,5,tuberack2[df.loc[i].at['template_well']])
#                 #left_pipette.blow_out()
#                 left_pipette.drop_tip()

#     #add stock templates for digests:
#         # for i, row in digests.iterrows():
#         #     left_pipette.pick_up_tip()
#         #     left_pipette.aspirate(digests.loc[i].at['amount of template to add'], cold_tuberack[digests.loc[i].at['well']], rate=1.0) #dilution well corresponds to stock well
#         #     left_pipette.dispense(digests.loc[i].at['amount of template to add'], tuberack2[digests.loc[i].at['well']], rate=1.0) #makes a 12.5ng/uL template
#         #     #left_pipette.blow_out()
#         #     left_pipette.drop_tip()
        
#     #add stock primers to dilution tube
#         for i, row in oligos.iterrows():
#             left_pipette.pick_up_tip() #add in an iterrows function
#             left_pipette.aspirate(oligos.loc[i].at['volume of stock primer to add'], cold_tuberack[oligos.loc[i].at['well']], rate=1.0)
#             left_pipette.dispense(oligos.loc[i].at['volume of stock primer to add'], tuberack2[oligos.loc[i].at['well']], rate=1.0)
#             left_pipette.mix(3,5,tuberack2[oligos.loc[i].at['well']])
#             #left_pipette.blow_out()
#             left_pipette.drop_tip()
        
#     #mix contents with pipette tip (reps, max volume, location) for templates and primers
#         # for i, row in df.iterrows():
#         #     if df.loc[i].at['water to add'] > 8:
#         #         right_pipette.pick_up_tip()
#         #         right_pipette.mix(3,df.loc[i].at['water to add'],tuberack2[df.loc[i].at['template_well']])
#         #         #right_pipette.blow_out()
#         #         right_pipette.drop_tip()
#         #     if df.loc[i].at['water to add'] < 8:
#         #         right_pipette.pick_up_tip()
#         #         right_pipette.mix(3,3*(df.loc[i].at['water to add']),tuberack2[df.loc[i].at['template_well']])
#         #         #right_pipette.blow_out()
#         #         right_pipette.drop_tip()

#         # for i, row in digests.iterrows():
#         #     right_pipette.pick_up_tip()
#         #     right_pipette.mix(3,digests.loc[i].at['water to add'],tuberack2[digests.loc[i].at['well']])
#         #     #right_pipette.blow_out()
#         #     right_pipette.drop_tip()
            
#         for i, row in oligos.iterrows():
#             right_pipette.pick_up_tip()
#             right_pipette.mix(3,oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'],tuberack2[oligos.loc[i].at['well']])
#             #right_pipette.blow_out()
#             right_pipette.drop_tip()

#     #robot pauses so user can take out stock primers and put in DNPNI
#         protocol.pause('Take all stock primers and templates out. Add Q5 to D6, BsaI to D5, and cutsmart to D4. Then proceed')
        
#     #now mix dilute primers, dilute templates, Q5, and water in pcr tube within thermocycler
#         tc_mod.open_lid()
        


##########################################################################################################################
#pcr rxn
##########################################################################################################################

    x = 'PCR Mix'
    if x in section['parts'].values:

#add water first
        for j, row in pcr.iterrows():
            right_pipette.pick_up_tip()
            right_pipette.aspirate(pcr.loc[j].at['total_water_toadd'], watertuberack['A1'], rate=2.0) #need to write a function to add up all volumes that are being added and figure out how much water to add in automated way
            right_pipette.dispense(pcr.loc[j].at['total_water_toadd'], pcrplate[pcr.loc[j].at['tube']], rate=2.0)
            right_pipette.blow_out()
            right_pipette.drop_tip()
        
    #add 1uL of BOTH (not each) primers
        for j, row in pcr.iterrows():
            left_pipette.pick_up_tip()
            left_pipette.aspirate(pcr.loc[j].at['primervol_x'], tuberack2[pcr.loc[j].at['well']], rate=2.0)
            left_pipette.dispense(pcr.loc[j].at['primervol_x'], pcrplate[pcr.loc[j].at['tube']], rate=2.0)
            left_pipette.mix(3,2,pcrplate[pcr.loc[j].at['tube']])
            #left_pipette.blow_out()            
            left_pipette.drop_tip()
            
            left_pipette.pick_up_tip()
            left_pipette.aspirate(pcr.loc[j].at['primervol_y'], tuberack2[pcr.loc[j].at['well2']], rate=2.0)            
            left_pipette.dispense(pcr.loc[j].at['primervol_y'], pcrplate[pcr.loc[j].at['tube']], rate=2.0)
            left_pipette.mix(3,2,pcrplate[pcr.loc[j].at['tube']])
            #left_pipette.blow_out()
            left_pipette.drop_tip()
        
    #add 1uL of each template
        for j, row in pcr.iterrows():
            left_pipette.pick_up_tip()
            left_pipette.aspirate(pcr.loc[j].at['amount of template to add'], tuberack2[pcr.loc[j].at['template_well']], rate=2.0)
            left_pipette.dispense(pcr.loc[j].at['amount of template to add'], pcrplate[pcr.loc[j].at['tube']], rate=2.0)
            left_pipette.mix(3,3,pcrplate[pcr.loc[j].at['tube']])
            #left_pipette.blow_out()
            left_pipette.drop_tip()

    #Add DMSO
        for j, row in pcr.iterrows():
            left_pipette.pick_up_tip()
            if rackchanger == 'Y':
                left_pipette.aspirate(DMSO, tuberack2['H12'], rate=2.0)
            else:
                left_pipette.aspirate(DMSO, tuberack2['D6'], rate=2.0)
            left_pipette.dispense(DMSO, pcrplate[pcr.loc[j].at['tube']], rate=2.0)    
            left_pipette.blow_out()
            left_pipette.drop_tip() 

    #add Q5 to each reaction
    #keep Q5 in tuberack1['D6']                                            
        for j, row in pcr.iterrows():
            right_pipette.pick_up_tip()
            right_pipette.aspirate(Q5, cold_tuberack['D6'], rate=2.0)
            right_pipette.dispense(Q5, pcrplate[pcr.loc[j].at['tube']], rate=2.0)
            right_pipette.mix(3,Q5+3,pcrplate[pcr.loc[j].at['tube']])
            #right_pipette.mix(3,Q5+3,pcrplate[pcr.loc[i].at['frag_pcr_tube']])
            right_pipette.blow_out()
            right_pipette.drop_tip()

    #mix up
        # for j, row in pcr.iterrows():
        #     right_pipette.pick_up_tip()
        #     right_pipette.mix(3,Q5+3,pcrplate[pcr.loc[j].at['tube']])
        #     right_pipette.blow_out()
        #     right_pipette.drop_tip()
        
        protocol.pause('take out enzymes before cold stuff shuts off. Also restock tip racks')


        tc_mod.deactivate()
        temp_module.deactivate()
        
        protocol.pause('move to gradient thermocycler. set gradiet to be between '+str(gradient.loc[0].at['temp'])+' and '+str(gradient.loc[7].at['temp'])+'. Extension time should be '+str((Length['Length']/1000)*30)+' seconds. Follow normal parameters for everything else. A1 is cool, A8 is hot.')

        temp_module.set_temperature(4)
        tc_mod.set_block_temperature(4)



#Now run thermocycler to amplify DNA
    
#these parameters can be altered for different pcr reactionsabs
#should automate calculation of the parameters from j5 spreadsheets.
#maybe use the median annealing temperature in the spreadsheet
    
        #for j, row in annealing_extension.iterrows():
    # tc_mod.close_lid()
    # tc_mod.set_lid_temperature(temperature = 105)
    # tc_mod.set_block_temperature(98, hold_time_seconds=30, block_max_volume=25)
    # profile = [
    #     {'temperature': 98, 'hold_time_seconds': 10},
    #     {'temperature': round(annealing_extension.loc[i].at['annealing_temp'],1), 'hold_time_seconds': 30},
    #     {'temperature': 72, 'hold_time_seconds': round(annealing_extension.loc[i].at['extension time'],1)}] #should automate calculation of annealing temp based on spreadsheet
    # tc_mod.execute_profile(steps=profile, repetitions=34, block_max_volume=25)
    # tc_mod.set_block_temperature(72, hold_time_minutes=5, block_max_volume=25)
    # tc_mod.set_block_temperature(4)
    # protocol.pause('wait until ready to continue')
    # tc_mod.open_lid()
        
    # for j, row in pcr.iterrows():
    #     if pcr.loc[j,'run'] == i:
    #         right_pipette.pick_up_tip()
    #         right_pipette.aspirate(Input_values.loc[0].at['pcrvol'],pcrplate[pcr.loc[j].at['frag_pcr_tube']],2)
    #         right_pipette.dispense(Input_values.loc[0].at['pcrvol'],cold_tuberack[pcr.loc[j].at['holding_tube']],2)
    #         #right_pipette.blow_out()
    #         right_pipette.drop_tip()

    # for i, row in pcr.iterrows():
    #     right_pipette.pick_up_tip()
    #     right_pipette.aspirate(Input_values.loc[0].at['pcrvol'],cold_tuberack[pcr.loc[i].at['holding_tube']],2)
    #     right_pipette.dispense(Input_values.loc[0].at['pcrvol'],pcrplate[pcr.loc[i].at['frag_pcr_tube']],2)
    #     right_pipette.blow_out()
    #     right_pipette.drop_tip()
    t300=0
    t10 =0
    x = 'DPNI Digest'
    if x in section['parts'].values:
        tiprackposition = {}
        tiprackposition[0] = 'A1'
        tiprackposition[1] = 'A2'
        tiprackposition[2] = 'A3'
        tiprackposition[3] = 'A4'
        tiprackposition[4] = 'A5'
        tiprackposition[5] = 'A6'
        tiprackposition[6] = 'A7'
        tiprackposition[7] = 'A8'
        tiprackposition[8] = 'A9'
        tiprackposition[9] = 'A10'
        tiprackposition[10] = 'A11'
        tiprackposition[11] = 'A12'
        tiprackposition[12] = 'B1'
        tiprackposition[13] = 'B2'
        tiprackposition[14] = 'B3'
        tiprackposition[15] = 'B4'
        tiprackposition[16] = 'B5'
        tiprackposition[17] = 'B6'
        tiprackposition[18] = 'B7'
        tiprackposition[19] = 'B8'
        tiprackposition[20] = 'B9'
        tiprackposition[21] = 'B10'
        tiprackposition[22] = 'B11'
        tiprackposition[23] = 'B12'
        tiprackposition[24] = 'C1'
        tiprackposition[25] = 'C2'
        tiprackposition[26] = 'C3'
        tiprackposition[27] = 'C4'
        tiprackposition[28] = 'C5'
        tiprackposition[29] = 'C6'
        tiprackposition[30] = 'C7'
        tiprackposition[31] = 'C8'
        tiprackposition[32] = 'C9'
        tiprackposition[33] = 'C10'
        tiprackposition[34] = 'C11'
        tiprackposition[35] = 'C12'
        tiprackposition[36] = 'D1'
        tiprackposition[37] = 'D2'
        tiprackposition[38] = 'D3'
        tiprackposition[39] = 'D4'
        tiprackposition[40] = 'D5'
        tiprackposition[41] = 'D6'
        tiprackposition[42] = 'D7'
        tiprackposition[43] = 'D8'
        tiprackposition[44] = 'D9'
        tiprackposition[45] = 'D10'
        tiprackposition[46] = 'D11'
        tiprackposition[47] = 'D12'
        tiprackposition[48] = 'E1'
        tiprackposition[49] = 'E2'
        tiprackposition[50] = 'E3'
        tiprackposition[51] = 'E4'
        tiprackposition[52] = 'E5'
        tiprackposition[53] = 'E6'
        tiprackposition[54] = 'E7'
        tiprackposition[55] = 'E8'
        tiprackposition[56] = 'E9'
        tiprackposition[57] = 'E10'
        tiprackposition[58] = 'E11'
        tiprackposition[59] = 'E12'
        tiprackposition[60] = 'F1'
        tiprackposition[61] = 'F2'
        tiprackposition[62] = 'F3'
        tiprackposition[63] = 'F4'
        tiprackposition[64] = 'F5'
        tiprackposition[65] = 'F6'
        tiprackposition[66] = 'F7'
        tiprackposition[67] = 'F8'
        tiprackposition[68] = 'F9'
        tiprackposition[69] = 'F10'
        tiprackposition[70] = 'F11'
        tiprackposition[71] = 'F12'
        tiprackposition[72] = 'G1'
        tiprackposition[73] = 'G2'
        tiprackposition[74] = 'G3'
        tiprackposition[75] = 'G4'
        tiprackposition[76] = 'G5'
        tiprackposition[77] = 'G6'
        tiprackposition[78] = 'G7'
        tiprackposition[79] = 'G8'
        tiprackposition[80] = 'G9'
        tiprackposition[81] = 'G10'
        tiprackposition[82] = 'G11'
        tiprackposition[83] = 'G12'
        tiprackposition[84] = 'H1'
        tiprackposition[85] = 'H2'
        tiprackposition[86] = 'H3'
        tiprackposition[87] = 'H4'
        tiprackposition[88] = 'H5'
        tiprackposition[89] = 'H6'
        tiprackposition[90] = 'H7'
        tiprackposition[91] = 'H8'
        tiprackposition[92] = 'H9'
        tiprackposition[93] = 'H10'
        tiprackposition[94] = 'H11'
        tiprackposition[95] = 'H12' 
        #right_pipette.reset()
        #rack= protocol.load_labware('tiprack',7) 
        #del protocol.deck['9']
        #tiprack = protocol.load_labware('biorad_96_wellplate_200ul_pcr',9) 
        
        #del protocol.deck[9]
        #tiprack1.reset()
        #m300_tip_count = 0

        #tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', 9)
        
        
        #del protocol.tiprack1
        #tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', '9')
        #tiprack1.reset()

        
        #left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3])

        
        protocol.pause('REFILL TIP RACKS, and wait until its time to dispense the product')

#Now add DPNI for digestion

        for i, row in pcr.iterrows():
            right_pipette.pick_up_tip(tiprack1[tiprackposition[t300]])
            right_pipette.aspirate(Input_values.loc[0].at['DPwater'], watertuberack['A1'], rate=2.0)
            right_pipette.dispense(Input_values.loc[0].at['DPwater'], pcrplate[pcr.loc[i].at['tube']], rate=2.0)
            #right_pipette.blow_out()
            right_pipette.drop_tip()
            t300+=1

        for i, row in pcr.iterrows():
            left_pipette.pick_up_tip(tiprack3[tiprackposition[t10]])
            left_pipette.aspirate(Input_values.loc[0].at['cutsmart'], cold_tuberack['D4'], rate=2.0)
            left_pipette.dispense(Input_values.loc[0].at['cutsmart'], pcrplate[pcr.loc[i].at['tube']], rate=2.0)
            #left_pipette.mix(3,10,pcrplate[pcr.loc[i].at['tube']])
            #left_pipette.blow_out()
            left_pipette.drop_tip() 
            t10+=1

        for i, row in pcr.iterrows():
            left_pipette.pick_up_tip(tiprack3[tiprackposition[t10]])
            left_pipette.aspirate(Input_values.loc[0].at['DPNI'], cold_tuberack['D3'], rate=2.0)
            left_pipette.dispense(Input_values.loc[0].at['DPNI'], pcrplate[pcr.loc[i].at['tube']], rate=2.0)
            left_pipette.mix(3,10,pcrplate[pcr.loc[i].at['tube']])
            #left_pipette.blow_out()
            left_pipette.drop_tip()
            t10+=1

    #mix up
        # for i, row in pcr.iterrows():
        #     right_pipette.pick_up_tip(tiprack1[tiprackposition[t]])
        #     right_pipette.mix(3,Q5+Input_values.loc[0].at['DPwater']+Input_values.loc[0].at['cutsmart'],pcrplate[pcr.loc[i].at['tube']])
        #     right_pipette.blow_out()
        #     right_pipette.drop_tip()
        #     t+=1

#Do the bsa1 Digestion
##########################################################################################################################
##########################################################################################################################

# # pick up water -> dispense into pcr tube within thermocycler -> get rid of tip
#     for i, row in plasmid.iterrows():
#         if plasmid.loc[i].at['Concentration'] > 1:
#             right_pipette.pick_up_tip()
#             right_pipette.aspirate(plasmid.loc[i].at['Volume of Water'],watertuberack['A1'],2)
#             right_pipette.dispense(plasmid.loc[i].at['Volume of Water'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
#             right_pipette.blow_out()
#             right_pipette.drop_tip()

# # pick up plasmid  -> dispense into pcr tube -> get rid of tip  no blow out because aeresol
    
#     for i, row in plasmid.iterrows():
#         if plasmid.loc[i].at['Volume of Plasmid'] < 10:
#             left_pipette.pick_up_tip()
#             left_pipette.aspirate(plasmid.loc[i].at['Volume of Plasmid'],tuberack2[plasmid.loc[i].at['Plasmid Location']],2) #location of plasmid
#             left_pipette.dispense(plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
#             left_pipette.mix(3,plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
#             left_pipette.blow_out()
#             left_pipette.drop_tip()

#         if plasmid.loc[i].at['Volume of Plasmid'] in range(10, 100):
#             right_pipette.pick_up_tip()
#             right_pipette.aspirate(plasmid.loc[i].at['Volume of Plasmid'],tuberack2[plasmid.loc[i].at['Plasmid Location']],2) #location of plasmid
#             right_pipette.dispense(plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
#             right_pipette.mix(3,plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
#             right_pipette.blow_out()
#             right_pipette.drop_tip()

# # pick up buffer  -> dispense into pcr tube -> get rid of tip

#     for i, row in plasmid.iterrows():
#         if plasmid.loc[i].at['Concentration'] > 1:
#             left_pipette.pick_up_tip()
#             left_pipette.aspirate(plasmid.loc[i].at['Buffer'],cold_tuberack['D4'],2)
#             left_pipette.dispense(plasmid.loc[i].at['Buffer'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
#             left_pipette.mix(3,plasmid.loc[i].at['Buffer'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
#             left_pipette.blow_out()
#             left_pipette.drop_tip()  


# # pick up BsaI -> dispense into pcr tube -> get rid of tip

#     for i, row in plasmid.iterrows():
#         if plasmid.loc[i].at['Concentration'] > 1:
#             left_pipette.pick_up_tip()
#             left_pipette.aspirate(plasmid.loc[i].at['BSA1'],cold_tuberack['D5'],2)
#             left_pipette.dispense(plasmid.loc[i].at['BSA1'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
#             left_pipette.mix(3,plasmid.loc[i].at['BSA1'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
#             left_pipette.blow_out()
#             left_pipette.drop_tip()


#     for i, row in plasmid.iterrows():
#         if plasmid.loc[i].at['Concentration'] > 1:
#             if plasmid.loc[i].at['total volume'] > float('10'):
#                 right_pipette.pick_up_tip()
#                 right_pipette.mix(3,plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
#                 right_pipette.drop_tip()
#             else:
#                 left_pipette.pick_up_tip()
#                 left_pipette.mix(3,plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
#                 left_pipette.drop_tip()

#  #mixes contents around using the pipette tip  (reps,max volume,location)

        temp_module.deactivate()
        tc_mod.close_lid()
        tc_mod.set_lid_temperature(105)
        tc_mod.set_block_temperature(37,0,60, block_max_volume = 50) #temp,seconds,minutes,ramprate(danger),max vol
        tc_mod.set_block_temperature(80,0,20, block_max_volume = 50)
        tc_mod.set_block_temperature(4, block_max_volume = 50)
        tc_mod.open_lid()

    t300=0
    t10=0
    x = 'Combine Fragments'
    if x in section['parts'].values:
    
    #tiprack3.reset_tipracks(self)
    #left_pipette.reset()
        # tiprack3.reset()

        # tiprack3 = protocol.load_labware("opentrons_96_tiprack_10ul", '6')
        #left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3])

        
        protocol.pause('REFILL BOTH TIP RACKS, move 96 well block to deckslot 4, setting tube configuration the same as the Gradient arrangement')

        temp_module.set_temperature(4)

        #tc_mod.open_lid()

    #don't need to move out the digestion this way
        # for i, row in plasmid.iterrows():
        #     if plasmid.loc[i].at['Concentration'] > 1:
        #         if plasmid.loc[i].at['total volume'] > float('10'):
        #             right_pipette.pick_up_tip()
        #             right_pipette.aspirate(plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
        #             right_pipette.dispense(plasmid.loc[i].at['total volume'],tuberack2[plasmid.loc[i].at['final tube']],2)
        #             right_pipette.blow_out()
        #             right_pipette.drop_tip()
            
        #         else:
        #             left_pipette.pick_up_tip()
        #             left_pipette.aspirate(plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
        #             left_pipette.dispense(plasmid.loc[i].at['total volume'],tuberack2[plasmid.loc[i].at['final tube']],2)
        #             left_pipette.blow_out()
        #             left_pipette.drop_tip()


        # tc_mod.close_lid()
        # tc_mod.set_block_temperature(37, hold_time_minutes=15, block_max_volume=50)
        # tc_mod.set_block_temperature(80, hold_time_minutes=20, block_max_volume=50)
        # tc_mod.set_block_temperature(4)
        # tc_mod.deactivate_lid()
        # protocol.pause('hold until time to grab tubes')
        
        # tc_mod.open_lid()

    #Don't need to move out the digestion this way
    #Now replace first digested part
        
    #     for i, row in plasmid.iterrows():
    #         if plasmid.loc[i].at['Concentration'] > 1:
    #             if plasmid.loc[i].at['total volume'] > float('10'):
    #                 right_pipette.pick_up_tip()
    #                 right_pipette.aspirate(plasmid.loc[i].at['total volume'],tuberack2[plasmid.loc[i].at['final tube']],2)
    #                 right_pipette.dispense(plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
    #                 right_pipette.blow_out()
    #                 right_pipette.drop_tip()
            
    #             else:
    #                 left_pipette.pick_up_tip()
    #                 left_pipette.aspirate(plasmid.loc[i].at['total volume'],tuberack2[plasmid.loc[i].at['final tube']],2)
    #                 left_pipette.dispense(plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
    #                 left_pipette.blow_out()
    #                 left_pipette.drop_tip()


    ##########################################################################################################################
    # mix up IVA reactions 


        for i, row in GG_dfs.iterrows():
            x = GG_dfs.loc[i].at['gg#']
        
        #add all fragments to the GG tube
            for i, row in locals()[x].iterrows():
                right_pipette.pick_up_tip(tiprack1[tiprackposition[t300]])
                right_pipette.aspirate(50, pcrplate[locals()[x].loc[i].at['frag_loc']])
                right_pipette.dispense(50, secondarydils[locals()[x].loc[i].at['frag_loc']])
                right_pipette.blow_out()
                right_pipette.drop_tip()
                t300+=1
    
        
        protocol.pause('clear thermocycler tubes and arrange the final assembly tubes according to the reaction_setup file')


        for i, row in GG_dfs.iterrows():
            x = GG_dfs.loc[i].at['gg#']

            for i, row in locals()[x].iterrows():
                if locals()[x].loc[i].at['final amount to add'] < 10:
                    left_pipette.pick_up_tip(tiprack3[tiprackposition[t10]])
                    left_pipette.aspirate(locals()[x].loc[i].at['final amount to add'], secondarydils[locals()[x].loc[i].at['frag_loc']])
                    left_pipette.dispense(locals()[x].loc[i].at['final amount to add'], pcrplate[locals()[x].loc[i].at['location_of_assembly']])
                    left_pipette.blow_out()
                    left_pipette.drop_tip()
                    t10+=1
                else:
                    right_pipette.pick_up_tip(tiprack1[tiprackposition[t300]])
                    right_pipette.aspirate(locals()[x].loc[i].at['final amount to add'], secondarydils[locals()[x].loc[i].at['frag_loc']])
                    right_pipette.dispense(locals()[x].loc[i].at['final amount to add'], pcrplate[locals()[x].loc[i].at['location_of_assembly']])
                    right_pipette.blow_out()
                    right_pipette.drop_tip()
                    t300+=1
    
        # one more mix
            # right_pipette.pick_up_tip()
            # right_pipette.mix(3,15,pcrplate[locals()[x].loc[0].at['location_of_assembly']])
            # right_pipette.blow_out()
            # right_pipette.drop_tip()
    
        print('all done')