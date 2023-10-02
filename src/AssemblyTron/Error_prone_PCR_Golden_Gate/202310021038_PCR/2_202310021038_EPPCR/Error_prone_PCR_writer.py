''' Golden Gate Assembly Protocol Script with separate PCRs

This script performs Golden Gate assembly where fragments for each assembly are amplified in separate tubes and uses a gradient thermocycler. This protocol is thoroughly validated and robust, so we recommend using it. 

This script runs on the OT-2 via the run app. It calls CSVs which must be transferred to the OT-2 processor prior to running. This script is not designed to run a personal computer on the command line.

'''

import pandas
import numpy as np
import os
from os.path import exists

# paths = pandas.read_csv('/data/user_storage/robotpaths.csv')
# paths

Input_values = pandas.read_csv('Input.csv') 
# Input_values
Date = str(int(Input_values.loc[0].at['Date']))
Date
Time = str(int(Input_values.loc[0].at['Time']))
Time

Q5 = Input_values.loc[0].at['Q5']
diltemp = (Input_values.loc[0].at['templatengs'])*(Input_values.loc[0].at['pcrvol'])/1
BSA = Input_values.loc[0].at['BSA']
Taq_buffer = Input_values.loc[0].at['Taq_buffer']
ErrorRate = pandas.read_csv('ErrorRate.csv')

if ErrorRate.loc[0].at['rate'] == "E% = 0.2": 
    dATP = 3.5
    dCTP = 4
    dGTP = 2
    dTTP = 1.35
    MnCl2 = 10
    MgCl2 = 10

if ErrorRate.loc[0].at['rate'] == "E% = 0.3": 
    dATP = 2
    dCTP = 2
    dGTP = 1.8
    dTTP = 1.26
    MnCl2 = 10
    MgCl2 = 8.16

if ErrorRate.loc[0].at['rate'] == "E% = 0.4": 
    dATP = 2.2
    dCTP = 2
    dGTP = 2.7
    dTTP = 1.86
    MnCl2 = 10
    MgCl2 = 11

if ErrorRate.loc[0].at['rate'] == "E% = 0.5": 
    dATP = 2.2
    dCTP = 2
    dGTP = 3.4
    dTTP = 2.36
    MnCl2 = 10
    MgCl2 = 13.28

if ErrorRate.loc[0].at['rate'] == "E% = 0.6": 
    dATP = 2.3
    dCTP = 2
    dGTP = 4.2
    dTTP = 2.9
    MnCl2 = 10
    MgCl2 = 15.8

if ErrorRate.loc[0].at['rate'] == "E% = 0.8": 
    dATP = 2.3
    dCTP = 2
    dGTP = 5.7
    dTTP = 4
    MnCl2 = 10
    MgCl2 = 20.8

if ErrorRate.loc[0].at['rate'] == "E% = 1.0": 
    dATP = 1.2
    dCTP = 1
    dGTP = 3.6
    dTTP = 2.5
    MnCl2 = 10
    MgCl2 = 13.12

if ErrorRate.loc[0].at['rate'] == "E% = 1.5":
    dATP = 1.2
    dCTP = 1
    dGTP = 5.5
    dTTP = 3.85
    MnCl2 = 10
    MgCl2 = 19.28

#os.chdir(Date+Time+'_GoldenGate')
oligos = pandas.read_csv('oligo.csv')

gradient = pandas.read_csv('gradient.csv')
pcr = pandas.read_csv('pcr.csv')
# assembly = pandas.read_csv('assembly.csv')
# combinations = pandas.read_csv('combinations.csv')
Length = pcr.nlargest(1,'Length')
# GG_dfs = pandas.read_csv('GG_dfs.csv')
# digests = pandas.read_csv('digests.csv')
# plasmid = pandas.read_csv('plasmid.csv')
section = pandas.read_csv('section.csv')

low_annealing_temp = pcr.nsmallest(1,'Mean Oligo Tm (3 Only)').reset_index()
high_annealing_temp = pcr.nlargest(1,'Mean Oligo Tm (3 Only)').reset_index()

delta = (float(high_annealing_temp.loc[0].at['Mean Oligo Tm (3 Only)']) - float(low_annealing_temp.loc[0].at['Mean Oligo Tm (3 Only)']))/30
print(pcr)
# if exists('gg1.csv'):
#     gg1 = pandas.read_csv('gg1.csv')
# if exists('gg2.csv'):
#     gg2 = pandas.read_csv('gg2.csv')
# if exists('gg3.csv'):
#     gg3 = pandas.read_csv('gg3.csv')
# if exists('gg4.csv'):
#     gg4 = pandas.read_csv('gg4.csv')
# if exists('gg5.csv'):
#     gg5 = pandas.read_csv('gg5.csv')
# if exists('gg6.csv'):
#     gg6 = pandas.read_csv('gg6.csv')

if '96well' in pcr.columns:
    pcr = pcr.rename(columns={"96well": "well", "96well2": "well2"})
    rackchanger = 'Y'
else:
    rackchanger = 'N'

def main():
    f = open('Error_prone_PCR.py','w+')
    f.write(
        "from opentrons import protocol_api \r\n"
        "metadata = { \r\n"
        "    'protocolName': 'Golden Gate', \r\n"
        "    'author': 'John Bryant <jbryant2@vt.edu>', \r\n"
        "    'description': 'Protocol for performing Golden Gate assembly', \r\n"
        "    'apiLevel': '2.10' \r\n"
        "    } \r\n"
        "def run(protocol: protocol_api.ProtocolContext): \r\n"

        "    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', '9') \r\n"
        "    tiprack3 = protocol.load_labware('opentrons_96_tiprack_10ul', '5') \r\n"

        "    watertuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical','3') \r\n"
    )
    if rackchanger == 'Y':
        f.write("    tuberack2 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul','2') \r\n")
    else:
        f.write("    tuberack2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','2') \r\n")
    f.write(
        "    secondarydils = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul','4') \r\n"
        "    tc_mod = protocol.load_module('Thermocycler Module') \r\n"
        "    pcrplate = tc_mod.load_labware('nest_96_wellplate_100ul_pcr_full_skirt') \r\n"
        "    temp_module = protocol.load_module('temperature module', 1) \r\n"
        "    cold_tuberack = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', label='Temperature-Controlled Tubes') \r\n"
        "    temp_module.set_temperature(4) \r\n"
        "    tc_mod.open_lid() \r\n"

        "    right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1]) \r\n"
        "    left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3]) \r\n"
    )
    x = 'PCR Mix'
    if x in section['parts'].values:
        #add water first
        for j, row in pcr.iterrows():
            f.write(
                "    right_pipette.pick_up_tip() \r\n"
                "    right_pipette.aspirate("+str(pcr.loc[j].at['total_water_toadd'])+", watertuberack['A1'], rate=2.0) \r\n"
                "    right_pipette.dispense("+str(pcr.loc[j].at['total_water_toadd'])+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                "    right_pipette.blow_out() \r\n"
                "    right_pipette.drop_tip() \r\n"
            )
        #add 1uL of BOTH (not each) primers
        for j, row in pcr.iterrows():
            f.write(
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(pcr.loc[j].at['primervol_x'])+", tuberack2['"+str(pcr.loc[j].at['well'])+"'], rate=2.0) \r\n"
                "    left_pipette.dispense("+str(pcr.loc[j].at['primervol_x'])+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                "    left_pipette.mix(3,2,pcrplate['"+str(pcr.loc[j].at['tube'])+"']) \r\n"
                "    left_pipette.drop_tip() \r\n"

                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(pcr.loc[j].at['primervol_y'])+", tuberack2['"+str(pcr.loc[j].at['well2'])+"'], rate=2.0) \r\n"
                "    left_pipette.dispense("+str(pcr.loc[j].at['primervol_y'])+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                "    left_pipette.mix(3,2,pcrplate['"+pcr.loc[j].at['tube']+"']) \r\n"
                "    left_pipette.drop_tip() \r\n"
            )

        #add 1uL of each template
        for j, row in pcr.iterrows():
            f.write(
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(pcr.loc[j].at['amount of template to add'])+", tuberack2['"+str(pcr.loc[j].at['template_well'])+"'], rate=2.0) \r\n"
                "    left_pipette.dispense("+str(pcr.loc[j].at['amount of template to add'])+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                "    left_pipette.mix(3,3,pcrplate['"+str(pcr.loc[j].at['tube'])+"']) \r\n"
                "    left_pipette.drop_tip() \r\n"
            )

        #Add BSA
        for j, row in pcr.iterrows():
            f.write(
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(BSA)+", cold_tuberack['C2'], rate=2.0) \r\n"
                "    left_pipette.dispense("+str(BSA)+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                "    left_pipette.blow_out() \r\n"
                "    left_pipette.drop_tip() \r\n"
            )

        #Add Taq buffer
        for j, row in pcr.iterrows():
            f.write(
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(Taq_buffer)+", cold_tuberack['C3'], rate=2.0) \r\n"
                "    left_pipette.dispense("+str(Taq_buffer)+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                "    left_pipette.blow_out() \r\n"
                "    left_pipette.drop_tip() \r\n"
            )

        #Add dATP
        for j, row in pcr.iterrows():
            f.write(
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(dATP)+", cold_tuberack['C4'], rate=2.0) \r\n"
                "    left_pipette.dispense("+str(dATP)+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                "    left_pipette.blow_out() \r\n"
                "    left_pipette.drop_tip() \r\n"
            )

        #Add dCTP
        for j, row in pcr.iterrows():
            f.write(
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(dCTP)+", cold_tuberack['C5'], rate=2.0) \r\n"
                "    left_pipette.dispense("+str(dCTP)+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                "    left_pipette.blow_out() \r\n"
                "    left_pipette.drop_tip() \r\n"
            )

        #Add dGTP
        for j, row in pcr.iterrows():
            f.write(
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(dGTP)+", cold_tuberack['C6'], rate=2.0) \r\n"
                "    left_pipette.dispense("+str(dGTP)+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                "    left_pipette.blow_out() \r\n"
                "    left_pipette.drop_tip() \r\n"
            )

        #Add dTTP
        for j, row in pcr.iterrows():
            f.write(
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(dTTP)+", cold_tuberack['D1'], rate=2.0) \r\n"
                "    left_pipette.dispense("+str(dTTP)+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                "    left_pipette.blow_out() \r\n"
                "    left_pipette.drop_tip() \r\n"
            )

        #Add MnCl2
        for j, row in pcr.iterrows():
            f.write(
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(MnCl2)+", cold_tuberack['D2'], rate=2.0) \r\n"
                "    left_pipette.dispense("+str(MnCl2)+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                "    left_pipette.blow_out() \r\n"
                "    left_pipette.drop_tip() \r\n"
            )

        #Add MgCl2
        for j, row in pcr.iterrows():
            f.write(
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(MgCl2)+", cold_tuberack['D3'], rate=2.0) \r\n"
                "    left_pipette.dispense("+str(MgCl2)+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                "    left_pipette.blow_out() \r\n"
                "    left_pipette.drop_tip() \r\n"
            )

        #add Taq polymerase to each reaction
        for j, row in pcr.iterrows():
            f.write(
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(Q5)+", cold_tuberack['C1'], rate=2.0) \r\n"
                "    left_pipette.aspirate("+str(Q5)+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                "    left_pipette.blow_out() \r\n"
                "    left_pipette.drop_tip() \r\n"
            )
        
        #mix up
        for j, row in pcr.iterrows():
            f.write(
                "    right_pipette.pick_up_tip() \r\n"
                "    right_pipette.mix(3,"+str(pcr.loc[j].at['total_water_toadd'])+",pcrplate['"+str(pcr.loc[j].at['tube'])+"']) \r\n"
                "    right_pipette.blow_out() \r\n"
                "    right_pipette.drop_tip() \r\n"
            )
        
        f.write(
            "    tc_mod.close_lid() \r\n"
            "    tc_mod.set_lid_temperature(temperature = 105) \r\n"
            "    tc_mod.set_block_temperature(95, hold_time_seconds=30, block_max_volume=100) \r\n"
        )
        
        cycle = 1
        x = 0 
        while cycle < 31:

            f.write(
                "    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) \r\n"
                "    tc_mod.set_block_temperature("+str(float(low_annealing_temp.loc[0].at['Mean Oligo Tm (3 Only)'])+x)+", hold_time_seconds=40, block_max_volume=100) \r\n"
                "    tc_mod.set_block_temperature(68, hold_time_seconds="+str(float(((Length['Length']/1000)*60)+10))+", block_max_volume=100) \r\n"
            )
            cycle = cycle + 1
            x = x + delta
            print(cycle)
            print(delta)

        f.write(
            "    tc_mod.set_block_temperature(68, hold_time_minutes=5, block_max_volume=100) \r\n"
            "    tc_mod.set_block_temperature(4) \r\n"
            "    tc_mod.set_lid_temperature(temperature = 45) \r\n"
            "    protocol.pause('wait until ready to dispense assemblies') \r\n"
            "    tc_mod.open_lid() \r\n"
            "    protocol.pause('just take them out manually...') \r\n"
        )

    f.close()   
        
if __name__== "__main__":
    main()
    
os.system("notepad.exe Error_prone_PCR.py")    