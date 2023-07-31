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

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(8.75, watertuberack['A1'], rate=2.0) 

    # right_pipette.dispense(8.75, pcrplate['A2'], rate=2.0) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(8.75, watertuberack['A1'], rate=2.0) 

    # right_pipette.dispense(8.75, pcrplate['B2'], rate=2.0) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.0, tuberack2['A1'], rate=2.0) 

    # left_pipette.dispense(1.0, pcrplate['A2'], rate=2.0) 

    # left_pipette.mix(3,2,pcrplate['A2']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.0, tuberack2['A2'], rate=2.0) 

    # left_pipette.dispense(1.0, pcrplate['A2'], rate=2.0) 

    # left_pipette.mix(3,2,pcrplate['A2']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.0, tuberack2['A3'], rate=2.0) 

    # left_pipette.dispense(1.0, pcrplate['B2'], rate=2.0) 

    # left_pipette.mix(3,2,pcrplate['B2']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.0, tuberack2['A4'], rate=2.0) 

    # left_pipette.dispense(1.0, pcrplate['B2'], rate=2.0) 

    # left_pipette.mix(3,2,pcrplate['B2']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.0, tuberack2['B5'], rate=2.0) 

    # left_pipette.dispense(1.0, pcrplate['A2'], rate=2.0) 

    # left_pipette.mix(3,3,pcrplate['A2']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.0, tuberack2['B6'], rate=2.0) 

    # left_pipette.dispense(1.0, pcrplate['B2'], rate=2.0) 

    # left_pipette.mix(3,3,pcrplate['B2']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(0.75, tuberack2['D6'], rate=2.0) 

    # left_pipette.dispense(0.75, pcrplate['A2'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(0.75, tuberack2['D6'], rate=2.0) 

    # left_pipette.dispense(0.75, pcrplate['B2'], rate=2.0) 

    # left_pipette.blow_out() 

    # left_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 

    # right_pipette.aspirate(12.5, pcrplate['A2'], rate=2.0) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 

    # right_pipette.aspirate(12.5, pcrplate['B2'], rate=2.0) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,15.5,pcrplate['A2']) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,15.5,pcrplate['B2']) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    # tc_mod.deactivate() 

    # temp_module.deactivate() 

    # protocol.pause('move to gradient thermocycler. set gradiet to be between 61.886726818770136 and 85.00715812584316. Extension time should be 106.17 seconds. Follow normal parameters for everything else. A1 is cool, A8 is hot.') 

    # temp_module.set_temperature(4) 

    # tc_mod.set_block_temperature(4) 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(18, watertuberack['A1'], rate=2.0) 

    # right_pipette.dispense(18, pcrplate['A2'], rate=2.0) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(18, watertuberack['A1'], rate=2.0) 

    # right_pipette.dispense(18, pcrplate['B2'], rate=2.0) 

    # right_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(5, cold_tuberack['D4'], rate=2.0) 

    # left_pipette.dispense(5, pcrplate['A2'], rate=2.0) 

    # left_pipette.mix(3,10,pcrplate['A2']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(5, cold_tuberack['D4'], rate=2.0) 

    # left_pipette.dispense(5, pcrplate['B2'], rate=2.0) 

    # left_pipette.mix(3,10,pcrplate['B2']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(2, cold_tuberack['D3'], rate=2.0) 

    # left_pipette.dispense(2, pcrplate['A2'], rate=2.0) 

    # left_pipette.mix(3,10,pcrplate['A2']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(2, cold_tuberack['D3'], rate=2.0) 

    # left_pipette.dispense(2, pcrplate['B2'], rate=2.0) 

    # left_pipette.mix(3,10,pcrplate['B2']) 

    # left_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,35.5,pcrplate['A2']) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,35.5,pcrplate['B2']) 

    # right_pipette.blow_out() 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(39.37037037037037,watertuberack['A1'],2) 

    # right_pipette.dispense(39.37037037037037,pcrplate['E11'],2) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(39.833333333333336,watertuberack['A1'],2) 

    # right_pipette.dispense(39.833333333333336,pcrplate['F11'],2) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(39.6268221574344,watertuberack['A1'],2) 

    # right_pipette.dispense(39.6268221574344,pcrplate['G11'],2) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(39.6268221574344,watertuberack['A1'],2) 

    # right_pipette.dispense(39.6268221574344,pcrplate['A11'],2) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(39.22292993630573,watertuberack['A1'],2) 

    # right_pipette.dispense(39.22292993630573,pcrplate['C11'],2) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.aspirate(39.23809523809524,watertuberack['A1'],2) 

    # right_pipette.dispense(39.23809523809524,pcrplate['D11'],2) 

    # right_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(4.62962962962963,tuberack2['A5'],2) 

    # left_pipette.dispense(4.62962962962963,pcrplate['E11'],2) 

    # left_pipette.mix(3,4.62962962962963,pcrplate['E11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(4.166666666666667,tuberack2['A6'],2) 

    # left_pipette.dispense(4.166666666666667,pcrplate['F11'],2) 

    # left_pipette.mix(3,4.166666666666667,pcrplate['F11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(4.373177842565598,tuberack2['B1'],2) 

    # left_pipette.dispense(4.373177842565598,pcrplate['G11'],2) 

    # left_pipette.mix(3,4.373177842565598,pcrplate['G11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(4.373177842565598,tuberack2['B2'],2) 

    # left_pipette.dispense(4.373177842565598,pcrplate['A11'],2) 

    # left_pipette.mix(3,4.373177842565598,pcrplate['A11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(4.777070063694268,tuberack2['B3'],2) 

    # left_pipette.dispense(4.777070063694268,pcrplate['C11'],2) 

    # left_pipette.mix(3,4.777070063694268,pcrplate['C11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(4.761904761904762,tuberack2['B4'],2) 

    # left_pipette.dispense(4.761904761904762,pcrplate['D11'],2) 

    # left_pipette.mix(3,4.761904761904762,pcrplate['D11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(5.0,cold_tuberack['D4'],2) 

    # left_pipette.dispense(5.0,pcrplate['E11'],2) 

    # left_pipette.mix(3,5.0,pcrplate['E11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(5.0,cold_tuberack['D4'],2) 

    # left_pipette.dispense(5.0,pcrplate['F11'],2) 

    # left_pipette.mix(3,5.0,pcrplate['F11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(5.0,cold_tuberack['D4'],2) 

    # left_pipette.dispense(5.0,pcrplate['G11'],2) 

    # left_pipette.mix(3,5.0,pcrplate['G11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(5.0,cold_tuberack['D4'],2) 

    # left_pipette.dispense(5.0,pcrplate['A11'],2) 

    # left_pipette.mix(3,5.0,pcrplate['A11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(5.0,cold_tuberack['D4'],2) 

    # left_pipette.dispense(5.0,pcrplate['C11'],2) 

    # left_pipette.mix(3,5.0,pcrplate['C11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(5.0,cold_tuberack['D4'],2) 

    # left_pipette.dispense(5.0,pcrplate['D11'],2) 

    # left_pipette.mix(3,5.0,pcrplate['D11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.0,cold_tuberack['D5'],2) 

    # left_pipette.dispense(1.0,pcrplate['E11'],2) 

    # left_pipette.mix(3,1.0,pcrplate['E11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.0,cold_tuberack['D5'],2) 

    # left_pipette.dispense(1.0,pcrplate['F11'],2) 

    # left_pipette.mix(3,1.0,pcrplate['F11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.0,cold_tuberack['D5'],2) 

    # left_pipette.dispense(1.0,pcrplate['G11'],2) 

    # left_pipette.mix(3,1.0,pcrplate['G11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.0,cold_tuberack['D5'],2) 

    # left_pipette.dispense(1.0,pcrplate['A11'],2) 

    # left_pipette.mix(3,1.0,pcrplate['A11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.0,cold_tuberack['D5'],2) 

    # left_pipette.dispense(1.0,pcrplate['C11'],2) 

    # left_pipette.mix(3,1.0,pcrplate['C11']) 

    # left_pipette.drop_tip() 

    # left_pipette.pick_up_tip() 

    # left_pipette.aspirate(1.0,cold_tuberack['D5'],2) 

    # left_pipette.dispense(1.0,pcrplate['D11'],2) 

    # left_pipette.mix(3,1.0,pcrplate['D11']) 

    # left_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,50.0,pcrplate['E11']) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,50.0,pcrplate['F11']) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,50.0,pcrplate['G11']) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,50.0,pcrplate['A11']) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,50.0,pcrplate['C11']) 

    # right_pipette.drop_tip() 

    # right_pipette.pick_up_tip() 

    # right_pipette.mix(3,50.0,pcrplate['D11']) 

    # right_pipette.drop_tip() 

    # tc_mod.close_lid() 

    # tc_mod.set_lid_temperature(105) 

    # tc_mod.set_block_temperature(37,0,30, block_max_volume = 50) 

    # tc_mod.set_block_temperature(80,0,20, block_max_volume = 50) 

    tc_mod.set_block_temperature(4, block_max_volume = 50) 

    tc_mod.open_lid() 

    # temp_module.deactivate() 

    # tiprack3.reset() 

    # tiprack3 = protocol.load_labware('opentrons_96_tiprack_10ul', '6') 

    # protocol.pause('REFILL TIP RACKS, and wait until its time to dispense the product') 

    # temp_module.set_temperature(4) 

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

    right_pipette.aspirate(20, pcrplate['A2']) 

    right_pipette.dispense(20, secondarydils['A2']) 

    right_pipette.blow_out() 

    right_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.aspirate(20, pcrplate['F11']) 

    right_pipette.dispense(20, secondarydils['F11']) 

    right_pipette.blow_out() 

    right_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.aspirate(20, pcrplate['A2']) 

    right_pipette.dispense(20, secondarydils['A2']) 

    right_pipette.blow_out() 

    right_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.aspirate(20, pcrplate['G11']) 

    right_pipette.dispense(20, secondarydils['G11']) 

    right_pipette.blow_out() 

    right_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.aspirate(20, pcrplate['A2']) 

    right_pipette.dispense(20, secondarydils['A2']) 

    right_pipette.blow_out() 

    right_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.aspirate(20, pcrplate['A11']) 

    right_pipette.dispense(20, secondarydils['A11']) 

    right_pipette.blow_out() 

    right_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.aspirate(25.779539170506908, watertuberack['A1']) 

    right_pipette.dispense(25.779539170506908, secondarydils['B2']) 

    right_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(6, pcrplate['B2']) 

    left_pipette.dispense(6, secondarydils['B2']) 

    left_pipette.mix(3,3,secondarydils['B2']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.mix(3,8.593179723502303,secondarydils['B2']) 

    left_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.aspirate(20, pcrplate['C11']) 

    right_pipette.dispense(20, secondarydils['C11']) 

    right_pipette.blow_out() 

    right_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.aspirate(25.779539170506908, watertuberack['A1']) 

    right_pipette.dispense(25.779539170506908, secondarydils['B2']) 

    right_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(6, pcrplate['B2']) 

    left_pipette.dispense(6, secondarydils['B2']) 

    left_pipette.mix(3,3,secondarydils['B2']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.mix(3,8.593179723502303,secondarydils['B2']) 

    left_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.aspirate(20, pcrplate['D11']) 

    right_pipette.dispense(20, secondarydils['D11']) 

    right_pipette.blow_out() 

    right_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.aspirate(25.6468202764977, watertuberack['A1']) 

    right_pipette.dispense(25.6468202764977, secondarydils['B2']) 

    right_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(6, pcrplate['B2']) 

    left_pipette.dispense(6, secondarydils['B2']) 

    left_pipette.mix(3,3,secondarydils['B2']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.mix(3,8.5489400921659,secondarydils['B2']) 

    left_pipette.drop_tip() 

    protocol.pause('Clear off PCR plate and set up final Golden Gate assembly Tubes') 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(7.629999999999999, watertuberack['A1']) 

    left_pipette.dispense(7.629999999999999, pcrplate['B8']) 

    left_pipette.blow_out() 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1.6666666666666667, secondarydils['E11']) 

    left_pipette.dispense(1.6666666666666667, pcrplate['B8']) 

    left_pipette.blow_out() 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1.0493387890648165, secondarydils['A2']) 

    left_pipette.dispense(1.0493387890648165, pcrplate['B8']) 

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

    left_pipette.aspirate(1,cold_tuberack['C5']) 

    left_pipette.dispense(1,pcrplate['B8']) 

    left_pipette.mix(3,9,pcrplate['B8']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1,cold_tuberack['C1']) 

    left_pipette.dispense(1,pcrplate['B8']) 

    left_pipette.mix(3,9,pcrplate['B8']) 

    left_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.mix(3,15,pcrplate['B8']) 

    right_pipette.blow_out() 

    right_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(7.629999999999999, watertuberack['A1']) 

    left_pipette.dispense(7.629999999999999, pcrplate['B9']) 

    left_pipette.blow_out() 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1.6666666666666667, secondarydils['F11']) 

    left_pipette.dispense(1.6666666666666667, pcrplate['B9']) 

    left_pipette.blow_out() 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1.0493387890648165, secondarydils['A2']) 

    left_pipette.dispense(1.0493387890648165, pcrplate['B9']) 

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

    left_pipette.aspirate(1,cold_tuberack['C5']) 

    left_pipette.dispense(1,pcrplate['B9']) 

    left_pipette.mix(3,9,pcrplate['B9']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1,cold_tuberack['C1']) 

    left_pipette.dispense(1,pcrplate['B9']) 

    left_pipette.mix(3,9,pcrplate['B9']) 

    left_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.mix(3,15,pcrplate['B9']) 

    right_pipette.blow_out() 

    right_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(7.629999999999999, watertuberack['A1']) 

    left_pipette.dispense(7.629999999999999, pcrplate['B10']) 

    left_pipette.blow_out() 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1.6666666666666667, secondarydils['G11']) 

    left_pipette.dispense(1.6666666666666667, pcrplate['B10']) 

    left_pipette.blow_out() 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1.0493387890648165, secondarydils['A2']) 

    left_pipette.dispense(1.0493387890648165, pcrplate['B10']) 

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

    left_pipette.aspirate(1,cold_tuberack['C5']) 

    left_pipette.dispense(1,pcrplate['B10']) 

    left_pipette.mix(3,9,pcrplate['B10']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1,cold_tuberack['C1']) 

    left_pipette.dispense(1,pcrplate['B10']) 

    left_pipette.mix(3,9,pcrplate['B10']) 

    left_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.mix(3,15,pcrplate['B10']) 

    right_pipette.blow_out() 

    right_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(6.68, watertuberack['A1']) 

    left_pipette.dispense(6.68, pcrplate['B11']) 

    left_pipette.blow_out() 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1.6666666666666667, secondarydils['A11']) 

    left_pipette.dispense(1.6666666666666667, pcrplate['B11']) 

    left_pipette.blow_out() 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(2.0, secondarydils['B2']) 

    left_pipette.dispense(2.0, pcrplate['B11']) 

    left_pipette.blow_out() 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1.65,cold_tuberack['C4']) 

    left_pipette.dispense(1.65,pcrplate['B11']) 

    left_pipette.mix(3,8,pcrplate['B11']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1,cold_tuberack['D5']) 

    left_pipette.dispense(1,pcrplate['B11']) 

    left_pipette.mix(3,9,pcrplate['B11']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1,cold_tuberack['C5']) 

    left_pipette.dispense(1,pcrplate['B11']) 

    left_pipette.mix(3,9,pcrplate['B11']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1,cold_tuberack['C1']) 

    left_pipette.dispense(1,pcrplate['B11']) 

    left_pipette.mix(3,9,pcrplate['B11']) 

    left_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.mix(3,15,pcrplate['B11']) 

    right_pipette.blow_out() 

    right_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(6.68, watertuberack['A1']) 

    left_pipette.dispense(6.68, pcrplate['C2']) 

    left_pipette.blow_out() 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1.6666666666666667, secondarydils['C11']) 

    left_pipette.dispense(1.6666666666666667, pcrplate['C2']) 

    left_pipette.blow_out() 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(2.0, secondarydils['B2']) 

    left_pipette.dispense(2.0, pcrplate['C2']) 

    left_pipette.blow_out() 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1.65,cold_tuberack['C4']) 

    left_pipette.dispense(1.65,pcrplate['C2']) 

    left_pipette.mix(3,8,pcrplate['C2']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1,cold_tuberack['D5']) 

    left_pipette.dispense(1,pcrplate['C2']) 

    left_pipette.mix(3,9,pcrplate['C2']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1,cold_tuberack['C5']) 

    left_pipette.dispense(1,pcrplate['C2']) 

    left_pipette.mix(3,9,pcrplate['C2']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1,cold_tuberack['C1']) 

    left_pipette.dispense(1,pcrplate['C2']) 

    left_pipette.mix(3,9,pcrplate['C2']) 

    left_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.mix(3,15,pcrplate['C2']) 

    right_pipette.blow_out() 

    right_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(6.68, watertuberack['A1']) 

    left_pipette.dispense(6.68, pcrplate['C3']) 

    left_pipette.blow_out() 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1.6666666666666667, secondarydils['D11']) 

    left_pipette.dispense(1.6666666666666667, pcrplate['C3']) 

    left_pipette.blow_out() 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(2.0, secondarydils['B2']) 

    left_pipette.dispense(2.0, pcrplate['C3']) 

    left_pipette.blow_out() 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1.65,cold_tuberack['C4']) 

    left_pipette.dispense(1.65,pcrplate['C3']) 

    left_pipette.mix(3,8,pcrplate['C3']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1,cold_tuberack['D5']) 

    left_pipette.dispense(1,pcrplate['C3']) 

    left_pipette.mix(3,9,pcrplate['C3']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1,cold_tuberack['C5']) 

    left_pipette.dispense(1,pcrplate['C3']) 

    left_pipette.mix(3,9,pcrplate['C3']) 

    left_pipette.drop_tip() 

    left_pipette.pick_up_tip() 

    left_pipette.aspirate(1,cold_tuberack['C1']) 

    left_pipette.dispense(1,pcrplate['C3']) 

    left_pipette.mix(3,9,pcrplate['C3']) 

    left_pipette.drop_tip() 

    right_pipette.pick_up_tip() 

    right_pipette.mix(3,15,pcrplate['C3']) 

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

