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
    right_pipette.aspirate(45.580000000000005, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(45.580000000000005, pcrplate['A4'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(45.580000000000005, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(45.580000000000005, pcrplate['B4'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(4.0, tuberack2['A1'], rate=2.0) 
    left_pipette.dispense(4.0, pcrplate['A4'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['A4']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(4.0, tuberack2['A2'], rate=2.0) 
    left_pipette.dispense(4.0, pcrplate['A4'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['A4']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(4.0, tuberack2['A3'], rate=2.0) 
    left_pipette.dispense(4.0, pcrplate['B4'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['B4']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(4.0, tuberack2['A4'], rate=2.0) 
    left_pipette.dispense(4.0, pcrplate['B4'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['B4']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A5'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['A4'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['A4']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A6'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['B4'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['B4']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5, tuberack2['C2'], rate=2.0) 
    left_pipette.dispense(5, pcrplate['A4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5, tuberack2['C2'], rate=2.0) 
    left_pipette.dispense(5, pcrplate['B4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(20, tuberack2['C3'], rate=2.0) 
    left_pipette.dispense(20, pcrplate['A4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(20, tuberack2['C3'], rate=2.0) 
    left_pipette.dispense(20, pcrplate['B4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.2, tuberack2['C4'], rate=2.0) 
    left_pipette.dispense(1.2, pcrplate['A4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.2, tuberack2['C4'], rate=2.0) 
    left_pipette.dispense(1.2, pcrplate['B4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, tuberack2['C5'], rate=2.0) 
    left_pipette.dispense(1, pcrplate['A4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, tuberack2['C5'], rate=2.0) 
    left_pipette.dispense(1, pcrplate['B4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(3.6, tuberack2['C6'], rate=2.0) 
    left_pipette.dispense(3.6, pcrplate['A4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(3.6, tuberack2['C6'], rate=2.0) 
    left_pipette.dispense(3.6, pcrplate['B4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2.5, tuberack2['D1'], rate=2.0) 
    left_pipette.dispense(2.5, pcrplate['A4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2.5, tuberack2['D1'], rate=2.0) 
    left_pipette.dispense(2.5, pcrplate['B4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(10, tuberack2['D2'], rate=2.0) 
    left_pipette.dispense(10, pcrplate['A4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(10, tuberack2['D2'], rate=2.0) 
    left_pipette.dispense(10, pcrplate['B4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(7.12, tuberack2['D3'], rate=2.0) 
    left_pipette.dispense(7.12, pcrplate['A4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(7.12, tuberack2['D3'], rate=2.0) 
    left_pipette.dispense(7.12, pcrplate['B4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(1, cold_tuberack['C1'], rate=2.0) 
    right_pipette.aspirate(1, pcrplate['A4'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(1, cold_tuberack['C1'], rate=2.0) 
    right_pipette.aspirate(1, pcrplate['B4'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,4,pcrplate['A4']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,4,pcrplate['B4']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    tc_mod.deactivate() 
    temp_module.deactivate() 
    protocol.pause('move to gradient thermocycler. set gradiet to be between 50.29877762915102 and 84.88044246145425. Extension time should be 106.17 seconds. Follow normal parameters for everything else. A1 is cool, A8 is hot.') 
    temp_module.set_temperature(4) 
    tc_mod.set_block_temperature(4) 
