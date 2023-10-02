from opentrons import protocol_api 
metadata = { 
    'protocolName': 'Golden Gate', 
    'author': 'John Bryant <jbryant2@vt.edu>', 
    'description': 'Protocol for performing Golden Gate assembly', 
    'apiLevel': '2.10' 
    } 
def run(protocol: protocol_api.ProtocolContext): 
    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', '9') 
    tiprack3 = protocol.load_labware('opentrons_96_tiprack_10ul', '5') 
    watertuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical','3') 
    tuberack2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','2') 
    secondarydils = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul','4') 
    tc_mod = protocol.load_module('Thermocycler Module') 
    pcrplate = tc_mod.load_labware('nest_96_wellplate_100ul_pcr_full_skirt') 
    temp_module = protocol.load_module('temperature module', 1) 
    cold_tuberack = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', label='Temperature-Controlled Tubes') 
    temp_module.set_temperature(4) 
    tc_mod.open_lid() 
    right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1]) 
    left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3]) 
    left_pipette.flow_rate.aspirate = 50 
    right_pipette.flow_rate.aspirate = 50 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(30,cold_tuberack['D2']) 
    right_pipette.dispense(30,cold_tuberack['C4']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    left_pipette.flow_rate.aspirate = 10 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(3,cold_tuberack['C6']) 
    left_pipette.dispense(3,cold_tuberack['C4']) 
    left_pipette.mix(3,10,cold_tuberack['C4']) 
    left_pipette.flow_rate.aspirate = 50 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(20, pcrplate['E1']) 
    right_pipette.dispense(20, secondarydils['E1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(20, pcrplate['D1']) 
    right_pipette.dispense(20, secondarydils['D1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(20, pcrplate['H1']) 
    right_pipette.dispense(20, secondarydils['H1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(20, pcrplate['E2']) 
    right_pipette.dispense(20, secondarydils['E2']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(20, pcrplate['E1']) 
    right_pipette.dispense(20, secondarydils['E1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(20, pcrplate['D1']) 
    right_pipette.dispense(20, secondarydils['D1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(20, pcrplate['B1']) 
    right_pipette.dispense(20, secondarydils['B1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(20, pcrplate['E2']) 
    right_pipette.dispense(20, secondarydils['E2']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    protocol.pause('Clear off PCR plate and set up final Golden Gate assembly Tubes') 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.311221859426018, secondarydils['E1']) 
    left_pipette.dispense(1.311221859426018, pcrplate['B8']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.818181818181818, secondarydils['D1']) 
    left_pipette.dispense(1.818181818181818, pcrplate['B8']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.237326001031105, secondarydils['H1']) 
    left_pipette.dispense(1.237326001031105, pcrplate['B8']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.7185083347654235, secondarydils['E2']) 
    left_pipette.dispense(1.7185083347654235, pcrplate['B8']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(4.26, watertuberack['A1']) 
    left_pipette.dispense(4.26, pcrplate['B8']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.65,cold_tuberack['C4']) 
    left_pipette.dispense(1.65,pcrplate['B8']) 
    left_pipette.mix(3,8,pcrplate['B8']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1,cold_tuberack['D5']) 
    left_pipette.dispense(1,pcrplate['B8']) 
    left_pipette.mix(3,9,pcrplate['B8']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1,cold_tuberack['D1']) 
    left_pipette.dispense(1,pcrplate['B8']) 
    left_pipette.mix(3,9,pcrplate['B8']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1,cold_tuberack['C5']) 
    left_pipette.dispense(1,pcrplate['B8']) 
    left_pipette.mix(3,9,pcrplate['B8']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15,pcrplate['B8']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.311221859426018, secondarydils['E1']) 
    left_pipette.dispense(1.311221859426018, pcrplate['B9']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.818181818181818, secondarydils['D1']) 
    left_pipette.dispense(1.818181818181818, pcrplate['B9']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.237326001031105, secondarydils['B1']) 
    left_pipette.dispense(1.237326001031105, pcrplate['B9']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.7185083347654235, secondarydils['E2']) 
    left_pipette.dispense(1.7185083347654235, pcrplate['B9']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(4.26, watertuberack['A1']) 
    left_pipette.dispense(4.26, pcrplate['B9']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.65,cold_tuberack['C4']) 
    left_pipette.dispense(1.65,pcrplate['B9']) 
    left_pipette.mix(3,8,pcrplate['B9']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1,cold_tuberack['D5']) 
    left_pipette.dispense(1,pcrplate['B9']) 
    left_pipette.mix(3,9,pcrplate['B9']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1,cold_tuberack['D1']) 
    left_pipette.dispense(1,pcrplate['B9']) 
    left_pipette.mix(3,9,pcrplate['B9']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1,cold_tuberack['C5']) 
    left_pipette.dispense(1,pcrplate['B9']) 
    left_pipette.mix(3,9,pcrplate['B9']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15,pcrplate['B9']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    protocol.pause('move final assembly tubes aside and put in new tubes for the next copy of your assembly.') 
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
