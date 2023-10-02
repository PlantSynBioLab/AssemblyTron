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
    right_pipette.dispense(8.75, pcrplate['E1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(8.75, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(8.75, pcrplate['D1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(8.75, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(8.75, pcrplate['E2'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(8.75, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(8.75, pcrplate['H1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(8.75, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(8.75, pcrplate['B1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A1'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['E1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['E1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A2'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['E1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['E1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A3'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['D1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['D1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A4'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['D1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['D1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A5'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['E2'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['E2']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A6'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['E2'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['E2']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B1'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['H1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['H1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B2'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['H1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['H1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B3'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['B1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['B1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B4'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['B1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['B1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B5'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['E1'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['E1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B5'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['D1'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['D1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B6'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['E2'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['E2']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['C1'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['H1'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['H1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['C2'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['B1'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['B1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(0.75, tuberack2['D6'], rate=2.0) 
    left_pipette.dispense(0.75, pcrplate['E1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(0.75, tuberack2['D6'], rate=2.0) 
    left_pipette.dispense(0.75, pcrplate['D1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(0.75, tuberack2['D6'], rate=2.0) 
    left_pipette.dispense(0.75, pcrplate['E2'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(0.75, tuberack2['D6'], rate=2.0) 
    left_pipette.dispense(0.75, pcrplate['H1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(0.75, tuberack2['D6'], rate=2.0) 
    left_pipette.dispense(0.75, pcrplate['B1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 
    right_pipette.aspirate(12.5, pcrplate['E1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 
    right_pipette.aspirate(12.5, pcrplate['D1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 
    right_pipette.aspirate(12.5, pcrplate['E2'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 
    right_pipette.aspirate(12.5, pcrplate['H1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 
    right_pipette.aspirate(12.5, pcrplate['B1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.5,pcrplate['E1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.5,pcrplate['D1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.5,pcrplate['E2']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.5,pcrplate['H1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.5,pcrplate['B1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    tc_mod.deactivate() 
    temp_module.deactivate() 
    protocol.pause('move to gradient thermocycler. set gradiet to be between 59.34023464340536 and 68.52046044542618. Extension time should be 31.740000000000002 seconds. Follow normal parameters for everything else. A1 is cool, A8 is hot.') 
    temp_module.set_temperature(4) 
    tc_mod.set_block_temperature(4) 
