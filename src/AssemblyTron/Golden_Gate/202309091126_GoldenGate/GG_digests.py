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
    tc_mod.set_block_temperature(temperature=4) 
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
    right_pipette.aspirate(20, pcrplate['E11']) 
    right_pipette.dispense(20, secondarydils['E11']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(6.815452818239392, watertuberack['A1']) 
    right_pipette.dispense(6.815452818239392, secondarydils['A1']) 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(6, pcrplate['A1']) 
    left_pipette.dispense(6, secondarydils['A1']) 
    left_pipette.mix(3,3,secondarydils['A1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.mix(3,2.2718176060797974,secondarydils['A1']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(20, pcrplate['E11']) 
    right_pipette.dispense(20, secondarydils['E11']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(18.438616714697403, watertuberack['A1']) 
    right_pipette.dispense(18.438616714697403, secondarydils['F1']) 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, pcrplate['F1']) 
    left_pipette.dispense(1, secondarydils['F1']) 
    left_pipette.mix(3,3,secondarydils['F1']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,18.438616714697403,secondarydils['F1']) 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(20, pcrplate['F11']) 
    right_pipette.dispense(20, secondarydils['F11']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(15.561383285302592, watertuberack['A1']) 
    right_pipette.dispense(15.561383285302592, secondarydils['F1']) 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, pcrplate['F1']) 
    left_pipette.dispense(1, secondarydils['F1']) 
    left_pipette.mix(3,3,secondarydils['F1']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.561383285302592,secondarydils['F1']) 
    right_pipette.drop_tip() 
    protocol.pause('Clear off PCR plate and set up final Golden Gate assembly Tubes') 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.6666666666666667, secondarydils['E11']) 
    left_pipette.dispense(1.6666666666666667, pcrplate['B8']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2.0, secondarydils['A1']) 
    left_pipette.dispense(2.0, pcrplate['B8']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(6.68, watertuberack['A1']) 
    left_pipette.dispense(6.68, pcrplate['B8']) 
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
    left_pipette.aspirate(1.6666666666666667, secondarydils['E11']) 
    left_pipette.dispense(1.6666666666666667, pcrplate['B9']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2.0, secondarydils['F1']) 
    left_pipette.dispense(2.0, pcrplate['B9']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(6.68, watertuberack['A1']) 
    left_pipette.dispense(6.68, pcrplate['B9']) 
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
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.6666666666666667, secondarydils['F11']) 
    left_pipette.dispense(1.6666666666666667, pcrplate['B10']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2.0, secondarydils['F1']) 
    left_pipette.dispense(2.0, pcrplate['B10']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(6.68, watertuberack['A1']) 
    left_pipette.dispense(6.68, pcrplate['B10']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.65,cold_tuberack['C4']) 
    left_pipette.dispense(1.65,pcrplate['B10']) 
    left_pipette.mix(3,8,pcrplate['B10']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1,cold_tuberack['D5']) 
    left_pipette.dispense(1,pcrplate['B10']) 
    left_pipette.mix(3,9,pcrplate['B10']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1,cold_tuberack['D1']) 
    left_pipette.dispense(1,pcrplate['B10']) 
    left_pipette.mix(3,9,pcrplate['B10']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1,cold_tuberack['C5']) 
    left_pipette.dispense(1,pcrplate['B10']) 
    left_pipette.mix(3,9,pcrplate['B10']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15,pcrplate['B10']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
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
