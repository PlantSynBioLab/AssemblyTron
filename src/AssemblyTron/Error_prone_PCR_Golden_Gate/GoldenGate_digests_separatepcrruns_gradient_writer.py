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

Q5 = (0.5*Input_values.loc[0].at['pcrvol'])
diltemp = (Input_values.loc[0].at['templatengs'])*(Input_values.loc[0].at['pcrvol'])/1
DMSO = (0.03*Input_values.loc[0].at['pcrvol'])

#os.chdir(Date+Time+'_GoldenGate')
if exists('oligos.csv'):
    oligos = pandas.read_csv('oligo.csv')

gradient = pandas.read_csv('gradient.csv')
if exists('pcr.csv'):
    pcr = pandas.read_csv('pcr.csv')
if exists('assembly.csv'):
    assembly = pandas.read_csv('assembly.csv')
if exists('combinations.csv'):
    combinations = pandas.read_csv('combinations.csv')
if exists('pcr.csv'):
    Length = pcr.nlargest(1,'Length')
if exists('GG_dfs.csv'):
    GG_dfs = pandas.read_csv('GG_dfs.csv')
if exists('digests.csv'):
    digests = pandas.read_csv('digests.csv')
if exists('plasmid.csv'):
    plasmid = pandas.read_csv('plasmid.csv')
if exists('section.csv'):
    section = pandas.read_csv('section.csv')
if exists('pcr.csv'):
    low_annealing_temp = pcr.nsmallest(1,'Mean Oligo Tm (3 Only)').reset_index()
    high_annealing_temp = pcr.nlargest(1,'Mean Oligo Tm (3 Only)').reset_index()

    delta = (float(high_annealing_temp.loc[0].at['Mean Oligo Tm (3 Only)']) - float(low_annealing_temp.loc[0].at['Mean Oligo Tm (3 Only)']))/34

    
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

if '96well' in pcr.columns:
    pcr = pcr.rename(columns={"96well": "well", "96well2": "well2"})
    rackchanger = 'Y'
else:
    rackchanger = 'N'

def main():
    f = open('GG_digests.py','w+')
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

        #Add DMSO
        for j, row in pcr.iterrows():
            f.write(
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(DMSO)+", tuberack2['D6'], rate=2.0) \r\n"
                "    left_pipette.dispense("+str(DMSO)+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                "    left_pipette.blow_out() \r\n"
                "    left_pipette.drop_tip() \r\n"
            )

        #add High-Fi polymerase to each reaction
        for j, row in pcr.iterrows():
            f.write(
                "    right_pipette.pick_up_tip() \r\n"
                "    right_pipette.aspirate("+str(Q5)+", cold_tuberack['D6'], rate=2.0) \r\n"
                "    right_pipette.aspirate("+str(Q5)+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                "    right_pipette.blow_out() \r\n"
                "    right_pipette.drop_tip() \r\n"
            )
        
        #mix up
        for j, row in pcr.iterrows():
            f.write(
                "    right_pipette.pick_up_tip() \r\n"
                "    right_pipette.mix(3,"+str(Q5+3)+",pcrplate['"+str(pcr.loc[j].at['tube'])+"']) \r\n"
                "    right_pipette.blow_out() \r\n"
                "    right_pipette.drop_tip() \r\n"
            )
        
        if Input_values.loc[0].at['Combinatorial_pcr_params'] == 2:
            f.write(
                "    tc_mod.deactivate() \r\n"
                "    temp_module.deactivate() \r\n"
                "    protocol.pause('move to gradient thermocycler. set gradiet to be between "+str(gradient.loc[0].at['temp'])+" and "+str(gradient.loc[7].at['temp'])+". Extension time should be "+str(float((Length['Length']/1000)*30))+" seconds. Follow normal parameters for everything else. A1 is cool, A8 is hot.') \r\n"
                "    temp_module.set_temperature(4) \r\n"
                "    tc_mod.set_block_temperature(4) \r\n"
            )
        
        if Input_values.loc[0].at['Combinatorial_pcr_params'] == 1:
            f.write(
                "    tc_mod.close_lid() \r\n"
                "    tc_mod.set_lid_temperature(temperature = 105) \r\n"
                "    tc_mod.set_block_temperature(98, hold_time_seconds=30, block_max_volume=25) \r\n"
            )
            
            cycle = 1
            x = 0 
            while cycle < 35:

                f.write(
                    "    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) \r\n"
                    "    tc_mod.set_block_temperature("+str(float(low_annealing_temp.loc[0].at['Mean Oligo Tm (3 Only)'])+x)+", hold_time_seconds=30, block_max_volume=25) \r\n"
                    "    tc_mod.set_block_temperature(72, hold_time_seconds="+str(float((Length['Length']/1000)*30))+", block_max_volume=25) \r\n"
                )
                cycle = cycle + 1
                x = x + delta
                print(cycle)
                print(delta)

            f.write(
                "    tc_mod.set_block_temperature(72, hold_time_minutes=5, block_max_volume=25) \r\n"
                "    tc_mod.set_block_temperature(4) \r\n"
                "    tc_mod.set_lid_temperature(temperature = 45) \r\n"
                "    protocol.pause('wait until ready to dispense assemblies') \r\n"
                "    tc_mod.open_lid() \r\n"
                "    protocol.pause('just take them out manually...') \r\n"
            )            
        
#######################################################################################################################################################
    x = 'DPNI Digest'
    if x in section['parts'].values:
        
        #water for digestion
        for i, row in pcr.iterrows():
            f.write(
                "    right_pipette.pick_up_tip() \r\n"
                "    right_pipette.aspirate("+str(Input_values.loc[0].at['DPwater'])+", watertuberack['A1'], rate=2.0) \r\n"
                "    right_pipette.dispense("+str(Input_values.loc[0].at['DPwater'])+", pcrplate['"+str(pcr.loc[i].at['tube'])+"'], rate=2.0) \r\n"
                "    right_pipette.drop_tip() \r\n"
            )

        #cutsmart for digestion
        for i, row in pcr.iterrows():
            f.write(
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(Input_values.loc[0].at['cutsmart'])+", cold_tuberack['D4'], rate=2.0) \r\n"
                "    left_pipette.dispense("+str(Input_values.loc[0].at['cutsmart'])+", pcrplate['"+str(pcr.loc[i].at['tube'])+"'], rate=2.0) \r\n"
                "    left_pipette.mix(3,10,pcrplate['"+str(pcr.loc[i].at['tube'])+"']) \r\n"
                "    left_pipette.drop_tip() \r\n"
            )

        #Add DpnI
        for i, row in pcr.iterrows():
            f.write(
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(Input_values.loc[0].at['DPNI'])+", cold_tuberack['D3'], rate=2.0) \r\n"
                "    left_pipette.dispense("+str(Input_values.loc[0].at['DPNI'])+", pcrplate['"+str(pcr.loc[i].at['tube'])+"'], rate=2.0) \r\n"
                "    left_pipette.mix(3,10,pcrplate['"+str(pcr.loc[i].at['tube'])+"']) \r\n"
                "    left_pipette.drop_tip() \r\n"
            )

        #mix up
        for i, row in pcr.iterrows():
            f.write(
                "    right_pipette.pick_up_tip() \r\n"
                "    right_pipette.mix(3,"+str(Q5+Input_values.loc[0].at['DPwater']+Input_values.loc[0].at['cutsmart'])+",pcrplate['"+str(pcr.loc[i].at['tube'])+"']) \r\n"
                "    right_pipette.blow_out() \r\n"
                "    right_pipette.drop_tip() \r\n"
            )

        f.write(
            "    tc_mod.close_lid() \r\n"
            "    tc_mod.set_lid_temperature(105) \r\n"
            "    tc_mod.set_block_temperature(37,0,30, block_max_volume = 50) \r\n"
            "    tc_mod.set_block_temperature(80,0,20, block_max_volume = 50) \r\n"
            "    tc_mod.set_block_temperature(4, block_max_volume = 50) \r\n"
            "    tc_mod.open_lid() \r\n"
            "    temp_module.deactivate() \r\n"
            "    tiprack3.reset() \r\n"
            "    tiprack3 = protocol.load_labware('opentrons_96_tiprack_10ul', '6') \r\n"
            "    protocol.pause('REFILL TIP RACKS, and wait until its time to dispense the product') \r\n"
            "    temp_module.set_temperature(4) \r\n"
        )

##############################################################################################################################################################################
#Dilutions for entry vectors

        #water
        for i, row in plasmid.iterrows():
            if plasmid.loc[i].at['Concentration'] > 1:
                f.write(
                    "    right_pipette.pick_up_tip() \r\n"
                    "    right_pipette.aspirate("+str(plasmid.loc[i].at['Volume of Water'])+",watertuberack['A1'],2) \r\n"
                    "    right_pipette.dispense("+str(plasmid.loc[i].at['Volume of Water'])+",pcrplate['"+str(digests.loc[i].at['frag_pcr_tube'])+"'],2) \r\n"
                    "    right_pipette.drop_tip() \r\n"
                )

        #plasmid
        for i, row in plasmid.iterrows():
            if plasmid.loc[i].at['Volume of Plasmid'] < 10:
                f.write(
                    "    left_pipette.pick_up_tip() \r\n"
                    "    left_pipette.aspirate("+str(plasmid.loc[i].at['Volume of Plasmid'])+",tuberack2['"+str(plasmid.loc[i].at['Plasmid Location'])+"'],2) \r\n"
                    "    left_pipette.dispense("+str(plasmid.loc[i].at['Volume of Plasmid'])+",pcrplate['"+str(digests.loc[i].at['frag_pcr_tube'])+"'],2) \r\n"
                    "    left_pipette.mix(3,"+str(plasmid.loc[i].at['Volume of Plasmid'])+",pcrplate['"+str(digests.loc[i].at['frag_pcr_tube'])+"']) \r\n"
                    "    left_pipette.drop_tip() \r\n"
                )

            if plasmid.loc[i].at['Volume of Plasmid'] in range(10, 100):
                f.write(
                    "    right_pipette.pick_up_tip() \r\n"
                    "    right_pipette.aspirate("+str(plasmid.loc[i].at['Volume of Plasmid'])+",tuberack2['"+str(plasmid.loc[i].at['Plasmid Location'])+"'],2) \r\n"
                    "    right_pipette.dispense("+str(plasmid.loc[i].at['Volume of Plasmid'])+",pcrplate['"+str(digests.loc[i].at['frag_pcr_tube'])+"'],2) \r\n"
                    "    right_pipette.mix(3,"+str(plasmid.loc[i].at['Volume of Plasmid'])+",pcrplate['"+str(digests.loc[i].at['frag_pcr_tube'])+"']) \r\n"
                    "    right_pipette.drop_tip() \r\n"
                )

        # #Cutsmart Buffer
        # for i, row in plasmid.iterrows():
        #     if plasmid.loc[i].at['Concentration'] > 1:
        #         f.write(
        #             "    left_pipette.pick_up_tip() \r\n"
        #             "    left_pipette.aspirate("+str(plasmid.loc[i].at['Buffer'])+",cold_tuberack['D4'],2) \r\n"
        #             "    left_pipette.dispense("+str(plasmid.loc[i].at['Buffer'])+",pcrplate['"+str(digests.loc[i].at['frag_pcr_tube'])+"'],2) \r\n"
        #             "    left_pipette.mix(3,"+str(plasmid.loc[i].at['Buffer'])+",pcrplate['"+str(digests.loc[i].at['frag_pcr_tube'])+"']) \r\n"
        #             "    left_pipette.drop_tip() \r\n"
        #         )

        # #Add BsaI
        # for i, row in plasmid.iterrows():
        #     if plasmid.loc[i].at['Concentration'] > 1:
        #         f.write(
        #             "    left_pipette.pick_up_tip() \r\n"
        #             "    left_pipette.aspirate("+str(plasmid.loc[i].at['BSA1'])+",cold_tuberack['D5'],2) \r\n"
        #             "    left_pipette.dispense("+str(plasmid.loc[i].at['BSA1'])+",pcrplate['"+str(digests.loc[i].at['frag_pcr_tube'])+"'],2) \r\n"
        #             "    left_pipette.mix(3,"+str(plasmid.loc[i].at['BSA1'])+",pcrplate['"+str(digests.loc[i].at['frag_pcr_tube'])+"']) \r\n"
        #             "    left_pipette.drop_tip() \r\n"
        #         )

        #mix
        for i, row in plasmid.iterrows():
            if plasmid.loc[i].at['Concentration'] > 1:
                if plasmid.loc[i].at['total volume'] > float('10'):
                    f.write(
                        "    right_pipette.pick_up_tip() \r\n"
                        "    right_pipette.mix(3,"+str(plasmid.loc[i].at['total volume'])+",pcrplate['"+str(digests.loc[i].at['frag_pcr_tube'])+"']) \r\n"
                        "    right_pipette.drop_tip() \r\n"
                    )
                else:
                    f.write(
                        "    left_pipette.pick_up_tip() \r\n"
                        "    left_pipette.mix(3,"+str(plasmid.loc[i].at['total volume'])+",pcrplate['"+str(digests.loc[i].at['frag_pcr_tube'])+"']) \r\n"
                        "    left_pipette.drop_tip() \r\n"
                    )



###############################################################################################################################################################
#Golden Gate Setup
    x = 'Golden Gate Setup'
    if x in section['parts'].values:

        f.write(
            "    left_pipette.flow_rate.aspirate = 50 \r\n"
            "    right_pipette.flow_rate.aspirate = 50 \r\n"
            "    right_pipette.pick_up_tip() \r\n"
            "    right_pipette.aspirate(30,cold_tuberack['D2']) \r\n"
            "    right_pipette.dispense(30,cold_tuberack['C4']) \r\n"
            "    right_pipette.blow_out() \r\n"
            "    right_pipette.drop_tip() \r\n"
            "    left_pipette.flow_rate.aspirate = 10 \r\n"
            "    left_pipette.pick_up_tip() \r\n"
            "    left_pipette.aspirate(3,cold_tuberack['C6']) \r\n"
            "    left_pipette.dispense(3,cold_tuberack['C4']) \r\n"
            "    left_pipette.mix(3,10,cold_tuberack['C4']) \r\n"
            "    left_pipette.flow_rate.aspirate = 50 \r\n"
            "    left_pipette.drop_tip() \r\n"
        )

        for i, row in GG_dfs.iterrows():
            x = GG_dfs.loc[i].at['gg#']
            for i, row in globals()[x].iterrows():  
                if globals()[x].loc[i].at['initial required amount'] <1:
                    #adding h20
                    if globals()[x].loc[i].at['H20 to add to 1uL of fragment'] > 10:
                        f.write(
                            "    right_pipette.pick_up_tip() \r\n"
                            "    right_pipette.aspirate("+str(globals()[x].loc[i].at['H20 to add to 1uL of fragment'])+", watertuberack['A1']) \r\n"
                            "    right_pipette.dispense("+str(globals()[x].loc[i].at['H20 to add to 1uL of fragment'])+", secondarydils['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    right_pipette.drop_tip() \r\n"
                        )
                    if 8 < globals()[x].loc[i].at['H20 to add to 1uL of fragment'] < 10:
                        f.write(
                            "    left_pipette.pick_up_tip() \r\n"
                            "    left_pipette.aspirate("+str(globals()[x].loc[i].at['H20 to add to 1uL of fragment'])+", watertuberack['A1']) \r\n"
                            "    left_pipette.dispense("+str(globals()[x].loc[i].at['H20 to add to 1uL of fragment'])+", secondarydils['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    left_pipette.drop_tip() \r\n"
                        )
                    if 5< globals()[x].loc[i].at['H20 to add to 1uL of fragment'] < 8:
                        f.write(
                            "    right_pipette.pick_up_tip() \r\n"
                            "    right_pipette.aspirate("+str(4*(globals()[x].loc[i].at['H20 to add to 1uL of fragment']))+", watertuberack['A1']) \r\n"
                            "    right_pipette.dispense("+str(4*(globals()[x].loc[i].at['H20 to add to 1uL of fragment']))+", secondarydils['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    right_pipette.drop_tip() \r\n"
                        )
                    if globals()[x].loc[i].at['H20 to add to 1uL of fragment'] < 5:
                        f.write(
                            "    right_pipette.pick_up_tip() \r\n"
                            "    right_pipette.aspirate("+str(6*(globals()[x].loc[i].at['H20 to add to 1uL of fragment']))+", watertuberack['A1']) \r\n"
                            "    right_pipette.dispense("+str(6*(globals()[x].loc[i].at['H20 to add to 1uL of fragment']))+", secondarydils['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    right_pipette.drop_tip() \r\n"
                        )
                    
                    #add template
                    if globals()[x].loc[i].at['H20 to add to 1uL of fragment'] > 8:
                        f.write(
                            "    left_pipette.pick_up_tip() \r\n"
                            "    left_pipette.aspirate(1, pcrplate['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    left_pipette.dispense(1, secondarydils['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    left_pipette.mix(3,3,secondarydils['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    left_pipette.drop_tip() \r\n"
                        )
                    if 5< globals()[x].loc[i].at['H20 to add to 1uL of fragment'] < 8:
                        f.write(
                            "    left_pipette.pick_up_tip() \r\n"
                            "    left_pipette.aspirate(4, pcrplate['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    left_pipette.dispense(4, secondarydils['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    left_pipette.mix(3,3,secondarydils['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    left_pipette.drop_tip() \r\n"
                        )
                    if globals()[x].loc[i].at['H20 to add to 1uL of fragment'] < 5:
                        f.write(
                            "    left_pipette.pick_up_tip() \r\n"
                            "    left_pipette.aspirate(6, pcrplate['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    left_pipette.dispense(6, secondarydils['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    left_pipette.mix(3,3,secondarydils['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    left_pipette.drop_tip() \r\n"
                        )
                    
                    if globals()[x].loc[i].at['H20 to add to 1uL of fragment'] > 10:
                        f.write(
                            "    right_pipette.pick_up_tip() \r\n"
                            "    right_pipette.mix(3,"+str(globals()[x].loc[i].at['H20 to add to 1uL of fragment'])+",secondarydils['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    right_pipette.drop_tip() \r\n"
                        )
                    if globals()[x].loc[i].at['H20 to add to 1uL of fragment'] < 10:
                        if globals()[x].loc[i].at['H20 to add to 1uL of fragment'] >5:
                            f.write(
                                "    left_pipette.pick_up_tip() \r\n"
                                "    left_pipette.mix(3,"+str(globals()[x].loc[i].at['H20 to add to 1uL of fragment'])+",secondarydils['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                                "    left_pipette.drop_tip() \r\n"
                            )
                        if globals()[x].loc[i].at['H20 to add to 1uL of fragment'] < 5:
                            f.write(
                                "    left_pipette.pick_up_tip() \r\n"
                                "    left_pipette.mix(3,"+str(2*globals()[x].loc[i].at['H20 to add to 1uL of fragment'])+",secondarydils['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                                "    left_pipette.drop_tip() \r\n"
                            )

                else:
                    f.write(
                        "    right_pipette.pick_up_tip() \r\n"
                        "    right_pipette.aspirate(20, pcrplate['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                        "    right_pipette.dispense(20, secondarydils['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                        "    right_pipette.blow_out() \r\n"
                        "    right_pipette.drop_tip() \r\n"
                    )

        f.write(
            "    protocol.pause('Clear off PCR plate and set up final Golden Gate assembly Tubes') \r\n"
        )

        copies = Input_values.loc[0].at['copies']
        current = 1
        while current <= copies:
        
            for i, row in GG_dfs.iterrows():
                x = GG_dfs.loc[i].at['gg#']
                for i, row in globals()[x].iterrows():
                    f.write(

                        #templates

                        "    left_pipette.pick_up_tip() \r\n"
                        "    left_pipette.aspirate("+str(globals()[x].loc[i].at['final amount to add'])+", secondarydils['"+str(globals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                        "    left_pipette.dispense("+str(globals()[x].loc[i].at['final amount to add'])+", pcrplate['"+str(globals()[x].loc[i].at['location_of_assembly'])+"']) \r\n"
                        "    left_pipette.blow_out() \r\n"
                        "    left_pipette.drop_tip() \r\n"

                    )

                if Input_values.loc[0].at['paqCI'] == 1:
                    f.write(
                        #water
                        "    left_pipette.pick_up_tip() \r\n"
                        "    left_pipette.aspirate("+str(15 - round(globals()[x]['final amount to add'].sum(),2) - 1 - 1 - 1.65)+", watertuberack['A1']) \r\n" #accounts for activator
                        "    left_pipette.dispense("+str(15 - round(globals()[x]['final amount to add'].sum(),2) - 1 - 1 - 1.65)+", pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
                        "    left_pipette.blow_out() \r\n"
                        "    left_pipette.drop_tip() \r\n"
                    )
                
                
                if Input_values.loc[0].at['paqCI'] == 2:
                    f.write(
                    #water
                        "    left_pipette.pick_up_tip() \r\n"
                        "    left_pipette.aspirate("+str(15 - round(globals()[x]['final amount to add'].sum(),2) - 1 -1  - 1 - 1.65)+", watertuberack['A1']) \r\n" #accounts for activator
                        "    left_pipette.dispense("+str(15 - round(globals()[x]['final amount to add'].sum(),2) - 1 -1- 1 - 1.65)+", pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
                        "    left_pipette.blow_out() \r\n"
                        "    left_pipette.drop_tip() \r\n"
                    )
                    
                f.write(

                    #T4+BSA buffer combo
                    "    left_pipette.pick_up_tip() \r\n"
                    "    left_pipette.aspirate(1.65,cold_tuberack['C4']) \r\n"
                    "    left_pipette.dispense(1.65,pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
                    "    left_pipette.mix(3,8,pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
                    "    left_pipette.drop_tip() \r\n"

                    #restriction enzyme

                    "    left_pipette.pick_up_tip() \r\n"
                    "    left_pipette.aspirate(1,cold_tuberack['D5']) \r\n"
                    "    left_pipette.dispense(1,pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
                    "    left_pipette.mix(3,9,pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
                    "    left_pipette.drop_tip() \r\n"
                )
                
                if Input_values.loc[0].at['paqCI'] == 2:
                    f.write(
                        "    left_pipette.pick_up_tip() \r\n"
                        "    left_pipette.aspirate(1,cold_tuberack['D1']) \r\n"
                        "    left_pipette.dispense(1,pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
                        "    left_pipette.mix(3,9,pcrplate['"+str(globals()[x].loc[0].at['location_of_assembly'])+"']) \r\n"
                        "    left_pipette.drop_tip() \r\n"
                    )

                f.write(
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
            current = current + 1

            f.write(
                "    protocol.pause('move final assembly tubes aside and put in new tubes for the next copy of your assembly.') \r\n"
            )
    
    x = 'Golden Gate Run'
    if x in section['parts'].values:
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
    
os.system("notepad.exe GG_digests.py")    