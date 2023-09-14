'''Dilution Script for up to 24 primers and templates

This script contains a protocol for diluting up to 96 primers and templates to concentrations specified in the AssemblyTron.Golden_Gate.Setup_nodigests_seppcr_gradient_24 module. 

This script runs on the OT-2 via the run app. It calls CSVs which must be transferred to the OT-2 processor prior to running. This script is not designed to run a personal computer on the command line.

'''


import pandas
import numpy as np
import os


# paths = pandas.read_csv('/data/user_storage/robotpaths.csv')
# paths

Input_values = pandas.read_csv('Input.csv') 
Date = str(int(Input_values.loc[0].at['Date']))
Date
Time = str(int(Input_values.loc[0].at['Time']))
Time
#os.chdir('/Golden_Gate/'+Date+Time+'_GoldenGate')
oligos = pandas.read_csv('oligo.csv')
assembly = pandas.read_csv('assembly.csv')
pcr = pandas.read_csv('pcr.csv')
combinations = pandas.read_csv('combinations.csv')
df = pandas.read_csv('templates.csv')
digests = pandas.read_csv('digests.csv')
section = pandas.read_csv('section.csv')

def main():
    f = open('GG_dilutions.py','w+')
    f.write(
        "from opentrons import protocol_api \r\n"
        "metadata = { \r\n"
        "    'protocolName': 'Golden Gate Primer and Template Dilutions', \r\n"
        "    'author': 'John Bryant <jbryant2@vt.edu>', \r\n"
        "    'description': 'Protocol for performing PCR reactions and Plasmid assembly for TIR1 and AFB mutants', \r\n"
        "    'apiLevel': '2.10' \r\n"
        "    } \r\n"

        "def run(protocol: protocol_api.ProtocolContext): \r\n"

        "    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', '9') \r\n"
        "    tiprack3 = protocol.load_labware('opentrons_96_tiprack_10ul', '5') \r\n"
        "    watertuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical','3') \r\n"
        "    tuberack2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','2') \r\n"
        "    tc_mod = protocol.load_module('Thermocycler Module') \r\n"
        "    pcrplate = tc_mod.load_labware('nest_96_wellplate_100ul_pcr_full_skirt') \r\n"
        "    temp_module = protocol.load_module('temperature module', 1) \r\n"
        "    cold_tuberack = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', label='Temperature-Controlled Tubes') \r\n"
        "    temp_module.set_temperature(4) \r\n"
        "    tc_mod.open_lid() \r\n"

        "    right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1]) \r\n"
        "    left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3]) \r\n"       
    )

    x = 'Dilution'
    if x in section['parts'].values:
        f.write(
            "    right_pipette.pick_up_tip() \r\n"
        )
        for i, row in df.iterrows():
            if df.loc[i].at['water to add'] > 8:
                f.write(
                    "    right_pipette.aspirate(volume = "+str(df.loc[i].at['water to add'])+", location = watertuberack['A1'], rate=1.0) \r\n"
                    "    right_pipette.dispense("+str(df.loc[i].at['water to add'])+", tuberack2['"+str(df.loc[i].at['template_well'])+"'], rate=1.0) \r\n"
                )
            if df.loc[i].at['water to add'] < 8:
                f.write(
                    "    right_pipette.aspirate(volume = "+str(3*(df.loc[i].at['water to add']))+", location = watertuberack['A1'], rate=1.0) \r\n"
                    "    right_pipette.dispense("+str(3*(df.loc[i].at['water to add']))+", tuberack2['"+str(df.loc[i].at['template_well'])+"'], rate=1.0) \r\n"
                )

        # Unnecessary to dilute digest templates    
        # for i, row in digests.iterrows():
        #     f.write(
        #         "    right_pipette.aspirate(volume = "+str(digests.loc[i].at['water to add'])+", location = watertuberack['A1'], rate=1.0) \r\n"
        #         "    right_pipette.dispense("+str(digests.loc[i].at['water to add'])+", tuberack2['"+str(digests.loc[i].at['well'])+"'], rate=1.0) \r\n"
        #     )

        for i, row in oligos.iterrows():
            f.write(
                "    right_pipette.aspirate("+str(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'])+", watertuberack['A1'], rate=1.0) \r\n"
                "    right_pipette.dispense("+str(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'])+", tuberack2['"+str(oligos.loc[i].at['well'])+"'], rate=1.0) \r\n"
            )
        f.write(
            "    right_pipette.drop_tip() \r\n"
        )

        #add stock templates to dilution tubes
        for i, row in df.iterrows():
            if df.loc[i].at['water to add'] > 8:
                f.write(
                    "    left_pipette.pick_up_tip() \r\n"
                    "    left_pipette.aspirate("+str(df.loc[i].at['amount of template to add'])+", cold_tuberack['"+str(df.loc[i].at['template_well'])+"'], rate=1.0) \r\n"
                    "    left_pipette.dispense("+str(df.loc[i].at['amount of template to add'])+", tuberack2['"+str(df.loc[i].at['template_well'])+"'], rate=1.0) \r\n"
                    "    left_pipette.mix(3,5,tuberack2['"+str(df.loc[i].at['template_well'])+"']) \r\n"
                    "    left_pipette.drop_tip() \r\n"
                )
            if df.loc[i].at['water to add'] < 8:
                f.write(
                    "    left_pipette.pick_up_tip() \r\n"
                    "    left_pipette.aspirate("+str(3*(df.loc[i].at['amount of template to add']))+", cold_tuberack['"+str(df.loc[i].at['template_well'])+"'], rate=1.0) \r\n"
                    "    left_pipette.dispense("+str(3*(df.loc[i].at['amount of template to add']))+", tuberack2['"+str(df.loc[i].at['template_well'])+"'], rate=1.0) \r\n"
                    "    left_pipette.mix(3,5,tuberack2['"+str(df.loc[i].at['template_well'])+"']) \r\n"
                    "    left_pipette.drop_tip() \r\n"
                )
        #add stock templates for digests:
        # for i, row in digests.iterrows():
        #     f.write(
        #         "    left_pipette.pick_up_tip() \r\n"
        #         "    left_pipette.aspirate("+str(digests.loc[i].at['amount of template to add'])+", cold_tuberack['"+str(digests.loc[i].at['well'])+"'], rate=1.0) \r\n"
        #         "    left_pipette.dispense("+str(digests.loc[i].at['amount of template to add'])+", tuberack2['"+str(digests.loc[i].at['well'])+"'], rate=1.0) \r\n"
        #         "    left_pipette.drop_tip() \r\n"
        #     )

        #add stock primers to dilution tube
        for i, row in oligos.iterrows():
            f.write(
                "    left_pipette.pick_up_tip() \r\n"
                "    left_pipette.aspirate("+str(oligos.loc[i].at['volume of stock primer to add'])+", cold_tuberack['"+str(oligos.loc[i].at['well'])+"'], rate=1.0) \r\n"
                "    left_pipette.dispense("+str(oligos.loc[i].at['volume of stock primer to add'])+", tuberack2['"+str(oligos.loc[i].at['well'])+"'], rate=1.0) \r\n"
                "    left_pipette.mix(3,5,tuberack2['"+str(oligos.loc[i].at['well'])+"']) \r\n"
                "    left_pipette.drop_tip() \r\n"
            )

        #mix contents with pipette tip (reps, max volume, location) for templates and primers
        for i, row in df.iterrows():
            if df.loc[i].at['water to add'] > 8:
                f.write(
                    "    right_pipette.pick_up_tip() \r\n"
                    "    right_pipette.mix(3,"+str(df.loc[i].at['water to add'])+",tuberack2['"+str(df.loc[i].at['template_well'])+"']) \r\n"
                    "    right_pipette.drop_tip() \r\n"
                )
            if df.loc[i].at['water to add'] < 8:
                f.write(
                    "    right_pipette.pick_up_tip() \r\n"
                    "    right_pipette.mix(3,"+str(3*(df.loc[i].at['water to add']))+",tuberack2['"+str(df.loc[i].at['template_well'])+"']) \r\n"
                    "    right_pipette.drop_tip() \r\n"
                )
            
        # for i, row in digests.iterrows():
        #     f.write(
        #         "    right_pipette.pick_up_tip() \r\n"
        #         "    right_pipette.mix(3,"+str(digests.loc[i].at['water to add'])+",tuberack2['"+str(digests.loc[i].at['well'])+"']) \r\n"
        #         "    right_pipette.drop_tip() \r\n"
        #     )

        for i, row in oligos.iterrows():
            f.write(
                "    right_pipette.pick_up_tip() \r\n"
                "    right_pipette.mix(3,"+str(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'])+",tuberack2['"+str(oligos.loc[i].at['well'])+"']) \r\n"
                "    right_pipette.drop_tip() \r\n"
            )
        f.write(
            "    protocol.pause('Take all stock primers and templates out. Add Q5 to D6, BsaI to D5, and cutsmart to D4. Then proceed') \r\n"
        )

    f.close()
if __name__== "__main__":
    main()
    
os.system("notepad.exe GG_dilutions.py")