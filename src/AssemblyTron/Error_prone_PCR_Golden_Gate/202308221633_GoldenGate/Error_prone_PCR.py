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

    #temp_module.set_temperature(4) 

    tc_mod.open_lid() 

    right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1]) 

    left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3]) 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(45.580000000000005, watertuberack['A1'], rate=2.0) 

    # right_pipette.dispense(45.580000000000005, pcrplate['A3'], rate=2.0) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(45.580000000000005, watertuberack['A1'], rate=2.0) 

    # right_pipette.dispense(45.580000000000005, pcrplate['A5'], rate=2.0) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(4.0, tuberack2['A3'], rate=2.0) 

    # left_pipette.dispense(4.0, pcrplate['A3'], rate=2.0) 

    # left_pipette.mix(3,2,pcrplate['A3']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(4.0, tuberack2['A4'], rate=2.0) 

    # left_pipette.dispense(4.0, pcrplate['A3'], rate=2.0) 

    # left_pipette.mix(3,2,pcrplate['A3']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(4.0, tuberack2['B1'], rate=2.0) 

    # left_pipette.dispense(4.0, pcrplate['A5'], rate=2.0) 

    # left_pipette.mix(3,2,pcrplate['A5']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(4.0, tuberack2['B2'], rate=2.0) 

    # left_pipette.dispense(4.0, pcrplate['A5'], rate=2.0) 

    # left_pipette.mix(3,2,pcrplate['A5']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.0, tuberack2['B3'], rate=2.0) 

    # left_pipette.dispense(1.0, pcrplate['A3'], rate=2.0) 

    # left_pipette.mix(3,3,pcrplate['A3']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.0, tuberack2['B4'], rate=2.0) 

    # left_pipette.dispense(1.0, pcrplate['A5'], rate=2.0) 

    # left_pipette.mix(3,3,pcrplate['A5']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(5, tuberack2['C2'], rate=2.0) 

    # left_pipette.dispense(5, pcrplate['A3'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(5, tuberack2['C2'], rate=2.0) 

    # left_pipette.dispense(5, pcrplate['A5'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(20, tuberack2['C3'], rate=2.0) 

    # right_pipette.dispense(20, pcrplate['A3'], rate=2.0) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(20, tuberack2['C3'], rate=2.0) 

    # right_pipette.dispense(20, pcrplate['A5'], rate=2.0) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.2, tuberack2['C4'], rate=2.0) 

    # left_pipette.dispense(1.2, pcrplate['A3'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.2, tuberack2['C4'], rate=2.0) 

    # left_pipette.dispense(1.2, pcrplate['A5'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1, tuberack2['C5'], rate=2.0) 

    # left_pipette.dispense(1, pcrplate['A3'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1, tuberack2['C5'], rate=2.0) 

    # left_pipette.dispense(1, pcrplate['A5'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(3.6, tuberack2['C6'], rate=2.0) 

    # left_pipette.dispense(3.6, pcrplate['A3'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(3.6, tuberack2['C6'], rate=2.0) 

    # left_pipette.dispense(3.6, pcrplate['A5'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(2.5, tuberack2['D1'], rate=2.0) 

    # left_pipette.dispense(2.5, pcrplate['A3'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(2.5, tuberack2['D1'], rate=2.0) 

    # left_pipette.dispense(2.5, pcrplate['A5'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(10, tuberack2['D2'], rate=2.0) 

    # left_pipette.dispense(10, pcrplate['A3'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(10, tuberack2['D2'], rate=2.0) 

    # left_pipette.dispense(10, pcrplate['A5'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(8.16, tuberack2['D3'], rate=2.0) 

    # left_pipette.dispense(8.16, pcrplate['A3'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(8.16, tuberack2['D3'], rate=2.0) 

    # left_pipette.dispense(8.16, pcrplate['A5'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(1, cold_tuberack['C1'], rate=2.0) 

    # right_pipette.aspirate(1, pcrplate['A3'], rate=2.0) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(1, cold_tuberack['C1'], rate=2.0) 

    # right_pipette.aspirate(1, pcrplate['A5'], rate=2.0) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,4,pcrplate['A3']) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,4,pcrplate['A5']) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    tc_mod.close_lid() 

    tc_mod.set_lid_temperature(temperature = 105) 

    tc_mod.set_block_temperature(95, hold_time_seconds=30, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(63.017, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(63.16178333333334, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(63.30656666666667, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(63.451350000000005, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(63.596133333333334, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(63.74091666666667, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(63.8857, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(64.03048333333334, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(64.17526666666667, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(64.32005000000001, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(64.46483333333333, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(64.60961666666667, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(64.7544, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(64.89918333333334, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(65.04396666666666, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(65.18875, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(65.33353333333334, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(65.47831666666667, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(65.62310000000001, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(65.76788333333333, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(65.91266666666667, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(66.05745, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(66.20223333333334, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(66.34701666666666, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(66.4918, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(66.63658333333333, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(66.78136666666667, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(66.92615, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(67.07093333333333, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 

    tc_mod.set_block_temperature(67.21571666666667, hold_time_seconds=40, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_seconds=25.5, block_max_volume=100) 

    tc_mod.set_block_temperature(68, hold_time_minutes=5, block_max_volume=100) 

    tc_mod.set_block_temperature(4) 

    tc_mod.set_lid_temperature(temperature = 45) 

    protocol.pause('wait until ready to dispense assemblies') 

    tc_mod.open_lid() 

    protocol.pause('just take them out manually...') 

