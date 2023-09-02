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
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(8.75, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(8.75, pcrplate['C1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(8.75, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(8.75, pcrplate['B1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(8.75, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(8.75, pcrplate['B2'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(8.75, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(8.75, pcrplate['D1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A1'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['C1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['C1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A2'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['C1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['C1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A3'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['B1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['B1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A4'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['B1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['B1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A5'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['B2'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['B2']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A6'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['B2'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['B2']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B1'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['D1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['D1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B2'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['D1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['D1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B5'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['C1'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['C1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B5'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['B1'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['B1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B6'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['B2'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['B2']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B6'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['D1'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['D1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(0.75, tuberack2['D6'], rate=2.0) 
    left_pipette.dispense(0.75, pcrplate['C1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(0.75, tuberack2['D6'], rate=2.0) 
    left_pipette.dispense(0.75, pcrplate['B1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(0.75, tuberack2['D6'], rate=2.0) 
    left_pipette.dispense(0.75, pcrplate['B2'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(0.75, tuberack2['D6'], rate=2.0) 
    left_pipette.dispense(0.75, pcrplate['D1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 
    right_pipette.aspirate(12.5, pcrplate['C1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 
    right_pipette.aspirate(12.5, pcrplate['B1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 
    right_pipette.aspirate(12.5, pcrplate['B2'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 
    right_pipette.aspirate(12.5, pcrplate['D1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.5,pcrplate['C1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.5,pcrplate['B1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.5,pcrplate['B2']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.5,pcrplate['D1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    tc_mod.close_lid() 
    tc_mod.set_lid_temperature(temperature = 105) 
    tc_mod.set_block_temperature(98, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(63.017, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(63.14475, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(63.2725, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(63.40025, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(63.528000000000006, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(63.655750000000005, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(63.783500000000004, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(63.91125, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(64.039, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(64.16675000000001, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(64.2945, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(64.42225, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(64.55, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(64.67775, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(64.80550000000001, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(64.93325, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.061, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.18875, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.3165, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.44425, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.572, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.69975000000001, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.8275, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.95525, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.083, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.21075, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.3385, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.46625, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.594, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.72175, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.8495, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.97725, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(67.105, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(67.23275, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.53, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_minutes=5, block_max_volume=25) 
    tc_mod.set_block_temperature(4) 
    tc_mod.set_lid_temperature(temperature = 45) 
    protocol.pause('wait until ready to dispense assemblies') 
    tc_mod.open_lid() 
    protocol.pause('just take them out manually...') 
