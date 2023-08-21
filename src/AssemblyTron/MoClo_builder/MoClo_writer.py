''' Golden Gate Assembly Protocol Script with separate PCRs

This script performs Golden Gate assembly where fragments for each assembly are amplified in separate tubes and uses a gradient thermocycler. This protocol is thoroughly validated and robust, so we recommend using it. 

This script runs on the OT-2 via the run app. It calls CSVs which must be transferred to the OT-2 processor prior to running. This script is not designed to run a personal computer on the command line.

'''

import pandas
import numpy as np
import os
from os.path import exists



Input_values = pandas.read_csv('Input.csv') 
# Input_values
Date = str(int(Input_values.loc[0].at['Date']))
Date
Time = str(int(Input_values.loc[0].at['Time']))
Time

#Q5 = (0.5*Input_values.loc[0].at['pcrvol'])
#diltemp = (Input_values.loc[0].at['templatengs'])*(Input_values.loc[0].at['pcrvol'])/1
#DMSO = (0.03*Input_values.loc[0].at['pcrvol'])

parts_df = pandas.read_csv('parts_df.csv')

#os.chdir(Date+Time+'_GoldenGate')

if exists('parts1.csv'):
    part1 = pandas.read_csv('parts1.csv')
if exists('parts2.csv'):
    part2 = pandas.read_csv('parts2.csv')
if exists('parts3.csv'):
    part3 = pandas.read_csv('parts3.csv')
if exists('parts4.csv'):
    part4 = pandas.read_csv('parts4.csv')
if exists('parts5.csv'):
    part5 = pandas.read_csv('parts5.csv')
if exists('parts6.csv'):
    part6 = pandas.read_csv('parts6.csv')






def main():
    f = open('MoClo_assembly.py','w+')
    f.write(
        "from opentrons import protocol_api \r\n"
        "metadata = { \r\n"
        "    'protocolName': 'MoClo Assembly', \r\n"
        "    'author': 'John Bryant <jbryant2@vt.edu>', \r\n"
        "    'description': 'Protocol for putting together MoClo constructs', \r\n"
        "    'apiLevel': '2.10' \r\n"
        "    } \r\n"

        "def run(protocol: protocol_api.ProtocolContext): \r\n"

        "    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', '9') \r\n"
        "    tiprack3 = protocol.load_labware('opentrons_96_tiprack_10ul', '5') \r\n"
        "    watertuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical','3') \r\n"
        #"    tuberack2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','2') \r\n"
        "    moclo_plate = protocol.load_labware('nest_96_wellplate_200ul_flat','4') \r\n"
        "    tc_mod = protocol.load_module('Thermocycler Module') \r\n"
        "    pcrplate = tc_mod.load_labware('nest_96_wellplate_100ul_pcr_full_skirt') \r\n"
        "    temp_module = protocol.load_module('temperature module', 1) \r\n"
        "    cold_tuberack = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', label='Temperature-Controlled Tubes') \r\n"
        "    temp_module.set_temperature(4) \r\n"
        "    tc_mod.open_lid() \r\n"

        "    right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1]) \r\n"
        "    left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3]) \r\n"
    )




###############################################################################################################################################################
#Golden Gate Setup


    for i, row in parts_df.iterrows():
        x = parts_df.loc[i].at['part#']
        f.write(
            #water
            "    left_pipette.pick_up_tip() \r\n"
            "    left_pipette.aspirate("+str(20 - len(globals()[x]['part']) - 2 - 1 - 1)+", watertuberack['A1']) \r\n"
            "    left_pipette.dispense("+str(20 - len(globals()[x]['part']) - 2 - 1 - 1)+", pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
            "    left_pipette.blow_out() \r\n"
            "    left_pipette.drop_tip() \r\n"

            #T4 buffer
            "    left_pipette.pick_up_tip() \r\n"
            "    left_pipette.aspirate(2,cold_tuberack['C4']) \r\n"
            "    left_pipette.dispense(2,pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
            "    left_pipette.mix(3,8,pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
            "    left_pipette.drop_tip() \r\n"

        )
        
        for i, row in globals()[x].iterrows():
            f.write(
                #temp
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate(1, moclo_plate['"+str(globals()[x].loc[i].at['well'])+"']) \r\n"
                "    left_pipette.dispense(1, pcrplate['"+str(globals()[x].loc[i].at['location_of_assembly'])+"']) \r\n"
                "    left_pipette.blow_out() \r\n"
                "    left_pipette.drop_tip() \r\n"
            )
        f.write(
            #BsaI
            "    left_pipette.pick_up_tip() \r\n"
            "    left_pipette.aspirate(1,cold_tuberack['D5']) \r\n"
            "    left_pipette.dispense(1,pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
            "    left_pipette.mix(3,9,pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
            "    left_pipette.drop_tip() \r\n"

            #T4 ligase
            "    left_pipette.pick_up_tip() \r\n"
            "    left_pipette.aspirate(1,cold_tuberack['C5']) \r\n"
            "    left_pipette.dispense(1,pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
            "    left_pipette.mix(3,9,pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
            "    left_pipette.drop_tip() \r\n"

            #one more mix
            "    right_pipette.pick_up_tip() \r\n"
            "    right_pipette.mix(3,15,pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
            "    right_pipette.blow_out() \r\n"
            "    right_pipette.drop_tip() \r\n"
        )


    f.write(
        "    tc_mod.close_lid() \r\n"
        "    tc_mod.set_lid_temperature(temperature = 105) \r\n"
        "    profile = [ \r\n"
        "        {'temperature': 37, 'hold_time_seconds': 180}, \r\n"
        "        {'temperature': 16, 'hold_time_seconds': 240}] \r\n"
        "    tc_mod.execute_profile(steps=profile, repetitions=25, block_max_volume=15) \r\n"
        "    tc_mod.set_block_temperature(50, hold_time_minutes=5, block_max_volume=15) \r\n"
        "    tc_mod.set_block_temperature(80, hold_time_minutes=5, block_max_volume=15) \r\n"
        "    tc_mod.set_block_temperature(4) \r\n"
        "    protocol.pause('wait until ready to dispense assemblies') \r\n"
        "    tc_mod.open_lid() \r\n"
        "    protocol.pause('just take them out manually...') \r\n"
    )

    f.close()   
        
if __name__== "__main__":
    main()
    
os.system("notepad.exe MoClo_assembly.py")