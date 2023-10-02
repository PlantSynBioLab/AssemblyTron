from opentrons import protocol_api 
metadata = { 
    'protocolName': 'MoClo Assembly', 
    'author': 'John Bryant <jbryant2@vt.edu>', 
    'description': 'Protocol for putting together MoClo constructs', 
    'apiLevel': '2.10' 
    } 
def run(protocol: protocol_api.ProtocolContext): 
    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', '9') 
    tiprack3 = protocol.load_labware('opentrons_96_tiprack_10ul', '5') 
    watertuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical','3') 
    moclo_plate = protocol.load_labware('nest_96_wellplate_200ul_flat','4') 
    tc_mod = protocol.load_module('Thermocycler Module') 
    pcrplate = tc_mod.load_labware('nest_96_wellplate_100ul_pcr_full_skirt') 
    temp_module = protocol.load_module('temperature module', 1) 
    cold_tuberack = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', label='Temperature-Controlled Tubes') 
    temp_module.set_temperature(4) 
    tc_mod.open_lid() 
    right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1]) 
    left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3]) 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(8, watertuberack['A1']) 
    left_pipette.dispense(8, pcrplate['B2']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2,cold_tuberack['C4']) 
    left_pipette.dispense(2,pcrplate['B2']) 
    left_pipette.mix(3,8,pcrplate['B2']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['A1']) 
    left_pipette.dispense(1, pcrplate['B2']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['A9']) 
    left_pipette.dispense(1, pcrplate['B2']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['B2']) 
    left_pipette.dispense(1, pcrplate['B2']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['B3']) 
    left_pipette.dispense(1, pcrplate['B2']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['B6']) 
    left_pipette.dispense(1, pcrplate['B2']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['C2']) 
    left_pipette.dispense(1, pcrplate['B2']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['C3']) 
    left_pipette.dispense(1, pcrplate['B2']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['C4']) 
    left_pipette.dispense(1, pcrplate['B2']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1,cold_tuberack['D5']) 
    left_pipette.dispense(1,pcrplate['B2']) 
    left_pipette.mix(3,9,pcrplate['B2']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1,cold_tuberack['C5']) 
    left_pipette.dispense(1,pcrplate['B2']) 
    left_pipette.mix(3,9,pcrplate['B2']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15,pcrplate['B2']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(8, watertuberack['A1']) 
    left_pipette.dispense(8, pcrplate['B3']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2,cold_tuberack['C4']) 
    left_pipette.dispense(2,pcrplate['B3']) 
    left_pipette.mix(3,8,pcrplate['B3']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['A1']) 
    left_pipette.dispense(1, pcrplate['B3']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['A9']) 
    left_pipette.dispense(1, pcrplate['B3']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['B1']) 
    left_pipette.dispense(1, pcrplate['B3']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['B3']) 
    left_pipette.dispense(1, pcrplate['B3']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['B5']) 
    left_pipette.dispense(1, pcrplate['B3']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['C1']) 
    left_pipette.dispense(1, pcrplate['B3']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['C3']) 
    left_pipette.dispense(1, pcrplate['B3']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, moclo_plate['C4']) 
    left_pipette.dispense(1, pcrplate['B3']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1,cold_tuberack['D5']) 
    left_pipette.dispense(1,pcrplate['B3']) 
    left_pipette.mix(3,9,pcrplate['B3']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1,cold_tuberack['C5']) 
    left_pipette.dispense(1,pcrplate['B3']) 
    left_pipette.mix(3,9,pcrplate['B3']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15,pcrplate['B3']) 
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
