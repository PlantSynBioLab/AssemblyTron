'''OT-2 Demo Script

This is a demo script designed to be executed on the OT-2 run app. It shows the OT-2 in action.

This script does not require any input files.

'''


#from opentrons import protocol_api

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

#labware:
    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', '9')
    #tiprack2 = protocol.load_labware('opentrons_96_tiprack_300ul','6')
    #tiprack3 = protocol.load_labware("opentrons_96_tiprack_10ul", '5')
    #tuberack1 = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap','1') #holds stock primers and templates
    #watertuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical','3') #holds molec bio grad H2O
    tuberack2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','2') # holds dilute primers and templates
    
    tc_mod = protocol.load_module('Thermocycler Module')
    pcrplate = tc_mod.load_labware('nest_96_wellplate_100ul_pcr_full_skirt')
    temp_module = protocol.load_module('temperature module', 1)
    cold_tuberack = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', label='Temperature-Controlled Tubes')
    temp_module.set_temperature(23)
    print(temp_module.temperature)
    tc_mod.open_lid()

    
#pipettes
    right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1])
    #left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3])
    
##################################COMMANDS####################################
    
#add water to template dilution tubes. ***df is the template description dataframe
#Since we are just moving water I will use the same pipette tip to save plastic
    right_pipette.pick_up_tip()
    right_pipette.aspirate(volume = 50, location = cold_tuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
    right_pipette.dispense(50, tuberack2['A1'], rate=2.0)
    right_pipette.drop_tip()

    protocol.pause('explain dilution')

#add water to primer dilution tubes
    right_pipette.pick_up_tip()
    right_pipette.aspirate(50, tuberack2['D6'], rate=2.0) #need to put 39uL of water into each dilution tube for primers,) #we need to find better way to loop through these commands
    right_pipette.dispense(50, pcrplate['H12'], rate=2.0)
    right_pipette.drop_tip()    
    
    tc_mod.close_lid()
    