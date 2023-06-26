''' Golden Gate Assembly Protocol Script with separate PCRs

This script performs Golden Gate assembly where fragments for each assembly are amplified in separate tubes and uses a gradient thermocycler. This protocol is thoroughly validated and robust, so we recommend using it. 

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
    'protocolName': 'Golden Gate',
    'author': 'John Bryant <jbryant2@vt.edu>',
    'description': 'Protocol for performing Golden Gate assembly',
    'apiLevel': '2.10'
}
print(metadata)




def run(protocol: protocol_api.ProtocolContext): #for actually running the script in the robot

#from opentrons import simulate
#protocol = simulate.get_protocol_api('2.2')
    paths = pandas.read_csv('/data/user_storage/robotpaths.csv')
    paths

    Input_values = pandas.read_csv(paths.loc[0].at['opentrons_repo']+'/Golden_Gate/Input.csv') 
    # Input_values
    Date = str(int(Input_values.loc[0].at['Date']))
    Date
    Time = str(int(Input_values.loc[0].at['Time']))
    Time

    Q5 = (0.5*Input_values.loc[0].at['pcrvol'])
    diltemp = (Input_values.loc[0].at['templatengs'])*(Input_values.loc[0].at['pcrvol'])/1
    DMSO = (0.03*Input_values.loc[0].at['pcrvol'])

    os.chdir(paths.loc[0].at['opentrons_repo']+'Golden_Gate/'+Date+Time+'_GoldenGate')
    oligos = pandas.read_csv('oligo.csv')

    gradient = pandas.read_csv('gradient.csv')
    pcr = pandas.read_csv('pcr.csv')
    assembly = pandas.read_csv('assembly.csv')
    combinations = pandas.read_csv('combinations.csv')
    Length = pcr.nlargest(1,'Length')
    GG_dfs = pandas.read_csv('GG_dfs.csv')
    digests = pandas.read_csv('digests.csv')
    plasmid = pandas.read_csv('plasmid.csv')
        

    if exists('gg1.csv'):
        gg1 = pandas.read_csv('gg1.csv')
    if exists('gg2.csv'):
        gg2 = pandas.read_csv('gg2.csv')
    if exists('gg3.csv'):
        gg3 = pandas.read_csv('gg3.csv')
    if exists('gg4.csv'):
        gg4 = pandas.read_csv('gg4.csv')

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
#     right_pipette.pick_up_tip()
#     for i, row in df.iterrows():
#         if df.loc[i].at['water to add'] > 8:
#             right_pipette.aspirate(volume = df.loc[i].at['water to add'], location = watertuberack['A1'], rate=1.0) #total vol dilute template - vol stock template to add
#             right_pipette.dispense(df.loc[i].at['water to add'], plate96[df.loc[i].at['template_well']], rate=1.0)
#         if df.loc[i].at['water to add'] < 8:
#             right_pipette.aspirate(volume = 3*(df.loc[i].at['water to add']), location = watertuberack['A1'], rate=1.0) #total vol dilute template - vol stock template to add
#             right_pipette.dispense(3*(df.loc[i].at['water to add']), plate96[df.loc[i].at['template_well']], rate=1.0)
#        #right_pipette.blow_out()
# #digestions water
#     # for i, row in digests.iterrows():
#     #     right_pipette.aspirate(volume = digests.loc[i].at['water to add'], location = watertuberack['A1'], rate=1.0) #total vol dilute template - vol stock template to add
#     #     right_pipette.dispense(digests.loc[i].at['water to add'], tuberack2[digests.loc[i].at['well']], rate=1.0)
#         #right_pipette.blow_out()

# #add water to primer dilution tubes
#     for i, row in oligos.iterrows():
#         right_pipette.aspirate(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'], watertuberack['A1'], rate=1.0) #need to put 39uL of water into each dilution tube for primers,) #we need to find better way to loop through these commands
#         right_pipette.dispense(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'], plate96[oligos.loc[i].at['96well']], rate=1.0)
#         #right_pipette.blow_out()
#     right_pipette.drop_tip()    
    
# #add stock templates to dilution tubes
#     for i, row in df.iterrows():
#         if df.loc[i].at['water to add'] > 8:
#             left_pipette.pick_up_tip()
#             left_pipette.aspirate(df.loc[i].at['amount of template to add'], locals()df.loc[i].at['rack'][df.loc[i].at['template_origin']], rate=1.0) #dilution well corresponds to stock well
#             left_pipette.dispense(df.loc[i].at['amount of template to add'], plate96[df.loc[i].at['template_well']], rate=1.0) #makes a 12.5ng/uL template
#             left_pipette.mix(3,5,plate96[df.loc[i].at['template_well']])
#         #left_pipette.blow_out()
#             left_pipette.drop_tip()
#         if df.loc[i].at['water to add'] < 8:
#             left_pipette.pick_up_tip()
#             left_pipette.aspirate(3*(df.loc[i].at['amount of template to add']), locals()df.loc[i].at['rack'][df.loc[i].at['template_origin']], rate=1.0) #dilution well corresponds to stock well
#             left_pipette.dispense(3*(df.loc[i].at['amount of template to add']), plate96[df.loc[i].at['template_well']], rate=1.0) #makes a 12.5ng/uL template
#             left_pipette.mix(3,5,plate96[df.loc[i].at['template_well']])
#             #left_pipette.blow_out()
#             left_pipette.drop_tip()

# #add stock templates for digests:
#     # for i, row in digests.iterrows():
#     #     left_pipette.pick_up_tip()
#     #     left_pipette.aspirate(digests.loc[i].at['amount of template to add'], cold_tuberack[digests.loc[i].at['well']], rate=1.0) #dilution well corresponds to stock well
#     #     left_pipette.dispense(digests.loc[i].at['amount of template to add'], tuberack2[digests.loc[i].at['well']], rate=1.0) #makes a 12.5ng/uL template
#     #     #left_pipette.blow_out()
#     #     left_pipette.drop_tip()
    
# #add stock primers to dilution tube
#     for i, row in oligos.iterrows():
#         left_pipette.pick_up_tip() #add in an iterrows function
#         left_pipette.aspirate(oligos.loc[i].at['volume of stock primer to add'], locals()df.loc[i].at['rack'][oligos.loc[i].at['24well']], rate=1.0)
#         left_pipette.dispense(oligos.loc[i].at['volume of stock primer to add'], plate96[oligos.loc[i].at['96well']], rate=1.0)
#         left_pipette.mix(3,5,plate96[oligos.loc[i].at['well']])
#         #left_pipette.blow_out()
#         left_pipette.drop_tip()
    
# #mix contents with pipette tip (reps, max volume, location) for templates and primers
#     for i, row in df.iterrows():
#         if df.loc[i].at['water to add'] > 8:
#             right_pipette.pick_up_tip()
#             right_pipette.mix(3,df.loc[i].at['water to add'],plate96[df.loc[i].at['template_well']])
#             #right_pipette.blow_out()
#             right_pipette.drop_tip()
#         if df.loc[i].at['water to add'] < 8:
#             right_pipette.pick_up_tip()
#             right_pipette.mix(3,3*(df.loc[i].at['water to add']),plate96[df.loc[i].at['template_well']])
#             #right_pipette.blow_out()
#             right_pipette.drop_tip()

#     # for i, row in digests.iterrows():
#     #     right_pipette.pick_up_tip()
#     #     right_pipette.mix(3,digests.loc[i].at['water to add'],tuberack2[digests.loc[i].at['well']])
#     #     #right_pipette.blow_out()
#     #     right_pipette.drop_tip()
        
#     for i, row in oligos.iterrows():
#         right_pipette.pick_up_tip()
#         right_pipette.mix(3,oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'],plate96[oligos.loc[i].at['96well']])
#         #right_pipette.blow_out()
#         right_pipette.drop_tip()

# #robot pauses so user can take out stock primers and put in DNPNI
#     protocol.pause('Take all stock primers and templates out. Add Q5 to D6, BsaI to D5, and cutsmart to D4. Then proceed')
    
# #now mix dilute primers, dilute templates, Q5, and water in pcr tube within thermocycler
#     tc_mod.open_lid()
#     tc_mod.set_block_temperature(4)


##########################################################################################################################
#pcr rxn
##########################################################################################################################

#    for i in range(0,pcr['run'].sum()+1):

    x = 'PCR Mix'
    if x in Input_values['section'].values:

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
                left_pipette.aspirate(DMSO, tuberack2['D6'], rate=2.0)
                left_pipette.dispense(DMSO, pcrplate[pcr.loc[j].at['tube']], rate=2.0)    
                left_pipette.blow_out()
                left_pipette.drop_tip() 

    #add Q5 to each reaction
    #keep Q5 in tuberack1['D6']                                            
        for j, row in pcr.iterrows():
                right_pipette.pick_up_tip()
                right_pipette.aspirate(Q5, cold_tuberack['D6'], rate=2.0)
                right_pipette.aspirate(Q5, pcrplate[pcr.loc[j].at['tube']], rate=2.0)
                #right_pipette.mix(3,Q5+3,pcrplate[pcr.loc[i].at['frag_pcr_tube']])
                right_pipette.blow_out()
                right_pipette.drop_tip()

    #mix up
        for j, row in pcr.iterrows():
                right_pipette.pick_up_tip()
                right_pipette.mix(3,Q5+3,pcrplate[pcr.loc[j].at['tube']])
                right_pipette.blow_out()
                right_pipette.drop_tip()
        
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


    x = 'DPNI Digest'
    if x in Input_values['section'].values:
#Now add DPNI for digestion

        for i, row in pcr.iterrows():
            right_pipette.pick_up_tip()
            right_pipette.aspirate(Input_values.loc[0].at['DPwater'], watertuberack['A1'], rate=2.0)
            right_pipette.dispense(Input_values.loc[0].at['DPwater'], pcrplate[pcr.loc[i].at['tube']], rate=2.0)
            #right_pipette.blow_out()
            right_pipette.drop_tip()

        for i, row in pcr.iterrows():
            left_pipette.pick_up_tip()
            left_pipette.aspirate(Input_values.loc[0].at['cutsmart'], cold_tuberack['D4'], rate=2.0)
            left_pipette.dispense(Input_values.loc[0].at['cutsmart'], pcrplate[pcr.loc[i].at['tube']], rate=2.0)
            #left_pipette.mix(3,10,pcrplate[pcr.loc[i].at['tube']])
            #left_pipette.blow_out()
            left_pipette.drop_tip() 

        for i, row in pcr.iterrows():
            left_pipette.pick_up_tip()
            left_pipette.aspirate(Input_values.loc[0].at['DPNI'], cold_tuberack['D3'], rate=2.0)
            left_pipette.dispense(Input_values.loc[0].at['DPNI'], pcrplate[pcr.loc[i].at['tube']], rate=2.0)
            left_pipette.mix(3,10,pcrplate[pcr.loc[i].at['tube']])
            #left_pipette.blow_out()
            left_pipette.drop_tip()

    #mix up
        for i, row in pcr.iterrows():
            right_pipette.pick_up_tip()
            right_pipette.mix(3,Q5+Input_values.loc[0].at['DPwater']+Input_values.loc[0].at['cutsmart'],pcrplate[pcr.loc[i].at['tube']])
            right_pipette.blow_out()
            right_pipette.drop_tip()

#Do the bsa1 Digestion
##########################################################################################################################
##########################################################################################################################

# pick up water -> dispense into pcr tube within thermocycler -> get rid of tip
    for i, row in plasmid.iterrows():
        if plasmid.loc[i].at['Concentration'] > 1:
            right_pipette.pick_up_tip()
            right_pipette.aspirate(plasmid.loc[i].at['Volume of Water'],watertuberack['A1'],2)
            right_pipette.dispense(plasmid.loc[i].at['Volume of Water'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
            #right_pipette.blow_out()
            right_pipette.drop_tip()

# pick up plasmid  -> dispense into pcr tube -> get rid of tip  no blow out because aeresol
    
    for i, row in plasmid.iterrows():
        if plasmid.loc[i].at['Volume of Plasmid'] < 10:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(plasmid.loc[i].at['Volume of Plasmid'],tuberack2[plasmid.loc[i].at['Plasmid Location']],2) #location of plasmid
            left_pipette.dispense(plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
            left_pipette.mix(3,plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
            #left_pipette.blow_out()
            left_pipette.drop_tip()

        if plasmid.loc[i].at['Volume of Plasmid'] in range(10, 100):
            right_pipette.pick_up_tip()
            right_pipette.aspirate(plasmid.loc[i].at['Volume of Plasmid'],tuberack2[plasmid.loc[i].at['Plasmid Location']],2) #location of plasmid
            right_pipette.dispense(plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
            right_pipette.mix(3,plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
            #right_pipette.blow_out()
            right_pipette.drop_tip()

# pick up buffer  -> dispense into pcr tube -> get rid of tip

    for i, row in plasmid.iterrows():
        if plasmid.loc[i].at['Concentration'] > 1:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(plasmid.loc[i].at['Buffer'],cold_tuberack['D4'],2)
            left_pipette.dispense(plasmid.loc[i].at['Buffer'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
            left_pipette.mix(3,plasmid.loc[i].at['Buffer'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
            #left_pipette.blow_out()
            left_pipette.drop_tip()  


# pick up BsaI -> dispense into pcr tube -> get rid of tip

    for i, row in plasmid.iterrows():
        if plasmid.loc[i].at['Concentration'] > 1:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(plasmid.loc[i].at['BSA1'],cold_tuberack['D5'],2)
            left_pipette.dispense(plasmid.loc[i].at['BSA1'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
            left_pipette.mix(3,plasmid.loc[i].at['BSA1'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
            #left_pipette.blow_out()
            left_pipette.drop_tip()


    for i, row in plasmid.iterrows():
        if plasmid.loc[i].at['Concentration'] > 1:
            if plasmid.loc[i].at['total volume'] > float('10'):
                right_pipette.pick_up_tip()
                right_pipette.mix(3,plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
                right_pipette.drop_tip()
            else:
                left_pipette.pick_up_tip()
                left_pipette.mix(3,plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
                left_pipette.drop_tip()

 #mixes contents around using the pipette tip  (reps,max volume,location)


        tc_mod.close_lid()
        tc_mod.set_lid_temperature(105)
        tc_mod.set_block_temperature(37,0,30, block_max_volume = 50) #temp,seconds,minutes,ramprate(danger),max vol
        tc_mod.set_block_temperature(80,0,20, block_max_volume = 50)
        tc_mod.set_block_temperature(4, block_max_volume = 50)
        tc_mod.open_lid()

        temp_module.deactivate()
        #tiprack3.reset_tipracks(self)
        #left_pipette.reset()
        tiprack3.reset()

        tiprack3 = protocol.load_labware("opentrons_96_tiprack_10ul", '6')
        #left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3])

        
        protocol.pause('REFILL TIP RACKS, and wait until its time to dispense the product')

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

    x = 'Golden Gate Setup'
    if x in Input_values['section'].values:
    #set up goldengate
    #here i'm trying to slow dow aspirate rate for the viscous 100X BSA
        left_pipette.flow_rate.aspirate = 50
        right_pipette.flow_rate.aspirate = 50
        #mix the T4 BSA combo
        right_pipette.pick_up_tip()
        right_pipette.aspirate(30,cold_tuberack['D2'])
        right_pipette.dispense(30,cold_tuberack['C4'])
        right_pipette.blow_out()
        right_pipette.drop_tip()

        left_pipette.flow_rate.aspirate = 10
        left_pipette.pick_up_tip()
        left_pipette.aspirate(3,cold_tuberack['C6'])
        left_pipette.dispense(3,cold_tuberack['C4'])
        #left_pipette.blow_out()
        left_pipette.mix(3,10,cold_tuberack['C4'])
        #left_pipette.blow_out()
        left_pipette.flow_rate.aspirate = 50
        left_pipette.drop_tip()

    #for i in range(0,e):
        
        for i, row in GG_dfs.iterrows():
            x = GG_dfs.loc[i].at['gg#']
            #wawa = 15 - round(locals()[x].loc[:,'final amount to add'].sum(),2) - 1 - 1 - 1.65

            for i, row in locals()[x].iterrows():
                
                if locals()[x].loc[i].at['initial required amount'] <1:
    #########################################################################################################
    ############adding h20
                    if locals()[x].loc[i].at['H20 to add to 1uL of fragment'] > 10:
                        right_pipette.pick_up_tip()
                        right_pipette.aspirate(locals()[x].loc[i].at['H20 to add to 1uL of fragment'], watertuberack['A1'])
                        right_pipette.dispense(locals()[x].loc[i].at['H20 to add to 1uL of fragment'], secondarydils[locals()[x].loc[i].at['frag_loc']])
                        #right_pipette.blow_out()
                        right_pipette.drop_tip()

                    if 8 < locals()[x].loc[i].at['H20 to add to 1uL of fragment'] < 10:
                        left_pipette.pick_up_tip()
                        left_pipette.aspirate(locals()[x].loc[i].at['H20 to add to 1uL of fragment'], watertuberack['A1'])
                        left_pipette.dispense(locals()[x].loc[i].at['H20 to add to 1uL of fragment'], secondarydils[locals()[x].loc[i].at['frag_loc']])
                        #left_pipette.blow_out()
                        left_pipette.drop_tip()

                    if 5< locals()[x].loc[i].at['H20 to add to 1uL of fragment'] < 8:
                        right_pipette.pick_up_tip()
                        right_pipette.aspirate(4*(locals()[x].loc[i].at['H20 to add to 1uL of fragment']), watertuberack['A1'])
                        right_pipette.dispense(4*(locals()[x].loc[i].at['H20 to add to 1uL of fragment']), secondarydils[locals()[x].loc[i].at['frag_loc']])
                        #right_pipette.blow_out()
                        right_pipette.drop_tip()

                    if locals()[x].loc[i].at['H20 to add to 1uL of fragment'] < 5:
                        right_pipette.pick_up_tip()
                        right_pipette.aspirate(6*(locals()[x].loc[i].at['H20 to add to 1uL of fragment']), watertuberack['A1'])
                        right_pipette.dispense(6*(locals()[x].loc[i].at['H20 to add to 1uL of fragment']), secondarydils[locals()[x].loc[i].at['frag_loc']])
                        #right_pipette.blow_out()
                        right_pipette.drop_tip()
    #####################################################################################################
    ############adding temp
                    if locals()[x].loc[i].at['H20 to add to 1uL of fragment'] > 8:
                        left_pipette.pick_up_tip()
                        left_pipette.aspirate(1, pcrplate[locals()[x].loc[i].at['frag_loc']])
                        left_pipette.dispense(1, secondarydils[locals()[x].loc[i].at['frag_loc']])
                        left_pipette.mix(3,3,secondarydils[locals()[x].loc[i].at['frag_loc']])
                        #left_pipette.blow_out()
                        left_pipette.drop_tip()

                    if 5< locals()[x].loc[i].at['H20 to add to 1uL of fragment'] < 8:
                        left_pipette.pick_up_tip()
                        left_pipette.aspirate(4, pcrplate[locals()[x].loc[i].at['frag_loc']])
                        left_pipette.dispense(4, secondarydils[locals()[x].loc[i].at['frag_loc']])
                        left_pipette.mix(3,3,secondarydils[locals()[x].loc[i].at['frag_loc']])
                        #left_pipette.blow_out()
                        left_pipette.drop_tip()

                    if locals()[x].loc[i].at['H20 to add to 1uL of fragment'] < 5:
                        left_pipette.pick_up_tip()
                        left_pipette.aspirate(6, pcrplate[locals()[x].loc[i].at['frag_loc']])
                        left_pipette.dispense(6, secondarydils[locals()[x].loc[i].at['frag_loc']])
                        left_pipette.mix(3,3,secondarydils[locals()[x].loc[i].at['frag_loc']])
                        #left_pipette.blow_out()
                        left_pipette.drop_tip()
                    
                    if locals()[x].loc[i].at['H20 to add to 1uL of fragment'] > 10:
                        right_pipette.pick_up_tip()
                        right_pipette.mix(3,locals()[x].loc[i].at['H20 to add to 1uL of fragment'],secondarydils[locals()[x].loc[i].at['frag_loc']])
                        right_pipette.drop_tip()

                    if locals()[x].loc[i].at['H20 to add to 1uL of fragment'] < 10:
                        if locals()[x].loc[i].at['H20 to add to 1uL of fragment'] >5:
                            left_pipette.pick_up_tip()
                            left_pipette.mix(3,locals()[x].loc[i].at['H20 to add to 1uL of fragment'],secondarydils[locals()[x].loc[i].at['frag_loc']])
                            left_pipette.drop_tip()
                        if locals()[x].loc[i].at['H20 to add to 1uL of fragment'] < 5:
                            left_pipette.pick_up_tip()
                            left_pipette.mix(3,2*(locals()[x].loc[i].at['H20 to add to 1uL of fragment']),secondarydils[locals()[x].loc[i].at['frag_loc']])
                            left_pipette.drop_tip()
                    #if locals()[x].loc[i].at['H20 to add to 1uL of fragment'] < 8:
                        #print('skip') #do nothing

                    
                else:
                    left_pipette.pick_up_tip()
                    left_pipette.aspirate(20, pcrplate[locals()[x].loc[i].at['frag_loc']])
                    left_pipette.dispense(20, secondarydils[locals()[x].loc[i].at['frag_loc']])
                    left_pipette.blow_out()
                    left_pipette.drop_tip()


        protocol.pause('Clear off PCR plate and set up final Golden Gate assembly Tubes')

        for i, row in GG_dfs.iterrows():
            x = GG_dfs.loc[i].at['gg#']
            #wawa = 15 - round(locals()[x].loc[:,'final amount to add'].sum(),2) - 1 - 1 - 1.65
            for i, row in locals()[x].iterrows():
            
                #how much water you need to add
                left_pipette.pick_up_tip()
                left_pipette.aspirate(15 - round(locals()[x]['final amount to add'].sum(),2) - 1 - 1 - 1.65, watertuberack['A1'])
                left_pipette.dispense(15 - round(locals()[x]['final amount to add'].sum(),2) - 1 - 1 - 1.65, pcrplate[locals()[x].loc[0].at['location_of_assembly']])
                left_pipette.blow_out()
                left_pipette.drop_tip()
                    
                left_pipette.pick_up_tip()
                left_pipette.aspirate(locals()[x].loc[i].at['final amount to add'], secondarydils[locals()[x].loc[i].at['frag_loc']])
                left_pipette.dispense(locals()[x].loc[i].at['final amount to add'], pcrplate[locals()[x].loc[i].at['location_of_assembly']])
                left_pipette.blow_out()
                left_pipette.drop_tip()
            
            #pipette the T4 BSA combo into GG assemblies
                left_pipette.pick_up_tip()
                left_pipette.aspirate(1.65,cold_tuberack['C4'])
                left_pipette.dispense(1.65,pcrplate[locals()[x].loc[0].at['location_of_assembly']])
                left_pipette.mix(3,8,pcrplate[locals()[x].loc[0].at['location_of_assembly']])
                #left_pipette.blow_out()
                left_pipette.drop_tip()
            
            #pipette the BsaI in
                left_pipette.pick_up_tip()
                left_pipette.aspirate(1,cold_tuberack['D5'])
                left_pipette.dispense(1,pcrplate[locals()[x].loc[0].at['location_of_assembly']])
                left_pipette.mix(3,9,pcrplate[locals()[x].loc[0].at['location_of_assembly']])
                #left_pipette.blow_out()
                left_pipette.drop_tip()
            
            #pipette the T4 ligase in
                left_pipette.pick_up_tip()
                left_pipette.aspirate(1,cold_tuberack['C5'])
                left_pipette.dispense(1,pcrplate[locals()[x].loc[0].at['location_of_assembly']])
                left_pipette.mix(3,9,pcrplate[locals()[x].loc[0].at['location_of_assembly']])
                #left_pipette.blow_out()
                left_pipette.drop_tip()
            
            # one more mix
                right_pipette.pick_up_tip()
                right_pipette.mix(3,15,pcrplate[locals()[x].loc[0].at['location_of_assembly']])
                right_pipette.blow_out()
                right_pipette.drop_tip()
        
    x = 'Golden Gate Run'
    if x in Input_values['section'].values:
    
        tc_mod.close_lid()
        tc_mod.set_lid_temperature(temperature = 105)
        profile = [
            {'temperature': 37, 'hold_time_seconds': 180},
            {'temperature': 16, 'hold_time_seconds': 240}]
        tc_mod.execute_profile(steps=profile, repetitions=25, block_max_volume=15)
        tc_mod.set_block_temperature(50, hold_time_minutes=5, block_max_volume=15)
        tc_mod.set_block_temperature(80, hold_time_minutes=5, block_max_volume=15)
        tc_mod.set_block_temperature(4)
        protocol.pause('wait until ready to dispense assemblies')
        
        tc_mod.open_lid()

        protocol.pause('just take them out manually...')
        
    #for i in range(0,e):
        
        # for i, row in GG_dfs.iterrows():
        #     x = GG_dfs.loc[i].at['gg#']
        
        #     right_pipette.pick_up_tip()
        #     right_pipette.aspirate(15,pcrplate[locals()[x].loc[0].at['location_of_assembly']])
        #     right_pipette.dispense(15,tuberack2[dis_tube.loc[i].at['dispense_tube']])
        #     right_pipette.blow_out()
        #     right_pipette.drop_tip()
        

    print('all done')