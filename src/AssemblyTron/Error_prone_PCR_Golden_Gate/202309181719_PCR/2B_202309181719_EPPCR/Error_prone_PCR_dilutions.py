from opentrons import protocol_api 

metadata = { 

    'protocolName': 'Error prone PCR', 

    'author': 'John Bryant <jbryant2@vt.edu>', 

    'description': 'Protocol for performing PCR reactions and Plasmid assembly for TIR1 and AFB mutants', 

    'apiLevel': '2.10' 

    } 

def run(protocol: protocol_api.ProtocolContext): 

    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', '9') 

    tiprack3 = protocol.load_labware('opentrons_96_tiprack_10ul', '5') 

    watertuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical','3') 

    tuberack2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','2') 

    tc_mod = protocol.load_module('Thermocycler Module') 

    pcrplate = tc_mod.load_labware('nest_96_wellplate_100ul_pcr_full_skirt') 

    temp_module = protocol.load_module('temperature module', 1) 

    cold_tuberack = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', label='Temperature-Controlled Tubes') 

    temp_module.set_temperature(4) 

    tc_mod.open_lid() 

    right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1]) 

    left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3]) 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(volume = 7.726102941176471, location = watertuberack['A1'], rate=1.0) 

    left_pipette.dispense(7.726102941176471, tuberack2['B5'], rate=1.0)

    left_pipette.drop_tip()

    right_pipette.pick_up_tip() 

    # right_pipette.aspirate(19.0, watertuberack['A1'], rate=1.0) 

    # right_pipette.dispense(19.0, tuberack2['A1'], rate=1.0) 

    # right_pipette.aspirate(19.0, watertuberack['A1'], rate=1.0) 

    # right_pipette.dispense(19.0, tuberack2['A2'], rate=1.0) 

    # right_pipette.aspirate(19.0, watertuberack['A1'], rate=1.0) 

    # right_pipette.dispense(19.0, tuberack2['A3'], rate=1.0) 

    # right_pipette.aspirate(19.0, watertuberack['A1'], rate=1.0) 

    # right_pipette.dispense(19.0, tuberack2['A4'], rate=1.0) 

    # right_pipette.aspirate(19.0, watertuberack['A1'], rate=1.0) 

    # right_pipette.dispense(19.0, tuberack2['A5'], rate=1.0) 

    # right_pipette.aspirate(19.0, watertuberack['A1'], rate=1.0) 

    # right_pipette.dispense(19.0, tuberack2['A6'], rate=1.0) 

    right_pipette.aspirate(19.0, watertuberack['A1'], rate=1.0) 

    right_pipette.dispense(19.0, tuberack2['B1'], rate=1.0) 

    right_pipette.aspirate(19.0, watertuberack['A1'], rate=1.0) 

    right_pipette.dispense(19.0, tuberack2['B2'], rate=1.0) 

    # right_pipette.aspirate(19.0, watertuberack['A1'], rate=1.0) 

    # right_pipette.dispense(19.0, tuberack2['B3'], rate=1.0) 

    # right_pipette.aspirate(19.0, watertuberack['A1'], rate=1.0) 

    # right_pipette.dispense(19.0, tuberack2['B4'], rate=1.0) 

    right_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(3.0, cold_tuberack['B5'], rate=1.0) 

    left_pipette.dispense(3.0, tuberack2['B5'], rate=1.0) 

    left_pipette.mix(3,5,tuberack2['B5']) 

    left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1, cold_tuberack['A1'], rate=1.0) 

    # left_pipette.dispense(1, tuberack2['A1'], rate=1.0) 

    # left_pipette.mix(3,5,tuberack2['A1']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1, cold_tuberack['A2'], rate=1.0) 

    # left_pipette.dispense(1, tuberack2['A2'], rate=1.0) 

    # left_pipette.mix(3,5,tuberack2['A2']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1, cold_tuberack['A3'], rate=1.0) 

    # left_pipette.dispense(1, tuberack2['A3'], rate=1.0) 

    # left_pipette.mix(3,5,tuberack2['A3']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1, cold_tuberack['A4'], rate=1.0) 

    # left_pipette.dispense(1, tuberack2['A4'], rate=1.0) 

    # left_pipette.mix(3,5,tuberack2['A4']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1, cold_tuberack['A5'], rate=1.0) 

    # left_pipette.dispense(1, tuberack2['A5'], rate=1.0) 

    # left_pipette.mix(3,5,tuberack2['A5']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1, cold_tuberack['A6'], rate=1.0) 

    # left_pipette.dispense(1, tuberack2['A6'], rate=1.0) 

    # left_pipette.mix(3,5,tuberack2['A6']) 

    # left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1, cold_tuberack['B1'], rate=1.0) 

    left_pipette.dispense(1, tuberack2['B1'], rate=1.0) 

    left_pipette.mix(3,5,tuberack2['B1']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1, cold_tuberack['B2'], rate=1.0) 

    left_pipette.dispense(1, tuberack2['B2'], rate=1.0) 

    left_pipette.mix(3,5,tuberack2['B2']) 

    left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1, cold_tuberack['B3'], rate=1.0) 

    # left_pipette.dispense(1, tuberack2['B3'], rate=1.0) 

    # left_pipette.mix(3,5,tuberack2['B3']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1, cold_tuberack['B4'], rate=1.0) 

    # left_pipette.dispense(1, tuberack2['B4'], rate=1.0) 

    # left_pipette.mix(3,5,tuberack2['B4']) 

    # left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.mix(3,7.726102941176471,tuberack2['B5']) 

    left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # right_pipette.mix(3,19.0,tuberack2['A1']) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,19.0,tuberack2['A2']) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,19.0,tuberack2['A3']) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,19.0,tuberack2['A4']) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,19.0,tuberack2['A5']) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,19.0,tuberack2['A6']) 

    # right_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.mix(3,19.0,tuberack2['B1']) 

    right_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.mix(3,19.0,tuberack2['B2']) 

    right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,19.0,tuberack2['B3']) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,19.0,tuberack2['B4']) 

    # right_pipette.drop_tip() 

    protocol.pause('Take all stock primers and templates out. Add Q5 to D6, BsaI to D5, and cutsmart to D4. Then proceed') 

