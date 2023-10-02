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
    right_pipette.aspirate(31.76, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(31.76, pcrplate['H1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(4.0, tuberack2['B1'], rate=2.0) 
    left_pipette.dispense(4.0, pcrplate['H1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['H1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(4.0, tuberack2['B2'], rate=2.0) 
    left_pipette.dispense(4.0, pcrplate['H1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['H1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B5'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['H1'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['H1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5, cold_tuberack['C2'], rate=2.0) 
    left_pipette.dispense(5, pcrplate['H1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(20, cold_tuberack['C3'], rate=2.0) 
    left_pipette.dispense(20, pcrplate['H1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2.2, cold_tuberack['C4'], rate=2.0) 
    left_pipette.dispense(2.2, pcrplate['H1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2, cold_tuberack['C5'], rate=2.0) 
    left_pipette.dispense(2, pcrplate['H1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(3.4, cold_tuberack['C6'], rate=2.0) 
    left_pipette.dispense(3.4, pcrplate['H1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2.36, cold_tuberack['D1'], rate=2.0) 
    left_pipette.dispense(2.36, pcrplate['H1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(10, cold_tuberack['D2'], rate=2.0) 
    left_pipette.dispense(10, pcrplate['H1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(13.28, cold_tuberack['D3'], rate=2.0) 
    left_pipette.dispense(13.28, pcrplate['H1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, cold_tuberack['C1'], rate=2.0) 
    left_pipette.aspirate(1, pcrplate['H1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,31.76,pcrplate['H1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    tc_mod.close_lid() 
    tc_mod.set_lid_temperature(temperature = 105) 
    tc_mod.set_block_temperature(95, hold_time_seconds=30, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(95, hold_time_seconds=20, block_max_volume=100) 
    tc_mod.set_block_temperature(68.423, hold_time_seconds=40, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_seconds=53.199999999999996, block_max_volume=100) 
    tc_mod.set_block_temperature(68, hold_time_minutes=5, block_max_volume=100) 
    tc_mod.set_block_temperature(4) 
    tc_mod.set_lid_temperature(temperature = 45) 
    protocol.pause('wait until ready to dispense assemblies') 
    tc_mod.open_lid() 
    protocol.pause('just take them out manually...') 
