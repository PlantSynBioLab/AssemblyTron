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
    right_pipette.dispense(8.75, pcrplate['A1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(8.75, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(8.75, pcrplate['A4'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(8.75, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(8.75, pcrplate['A2'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(8.75, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(8.75, pcrplate['B1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A1'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['A1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['A1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A2'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['A1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['A1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A3'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['A4'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['A4']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A4'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['A4'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['A4']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A5'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['A2'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['A2']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A6'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['A2'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['A2']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B1'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['B1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['B1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B2'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['B1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['B1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B4'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['A1'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['A1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B4'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['A4'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['A4']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B5'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['A2'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['A2']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B5'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['B1'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['B1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(0.75, pcrplate['A1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(0.75, pcrplate['A4'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(0.75, pcrplate['A2'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(0.75, pcrplate['B1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 
    right_pipette.aspirate(12.5, pcrplate['A1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 
    right_pipette.aspirate(12.5, pcrplate['A4'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 
    right_pipette.aspirate(12.5, pcrplate['A2'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 
    right_pipette.aspirate(12.5, pcrplate['B1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.5,pcrplate['A1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.5,pcrplate['A4']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.5,pcrplate['A2']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.5,pcrplate['B1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    tc_mod.deactivate() 
    temp_module.deactivate() 
    protocol.pause('move to gradient thermocycler. set gradiet to be between 66.5494683956459 and 70.01340098628201. Extension time should be 94.62 seconds. Follow normal parameters for everything else. A1 is cool, A8 is hot.') 
    temp_module.set_temperature(4) 
    tc_mod.set_block_temperature(4) 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(18, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(18, pcrplate['A1'], rate=2.0) 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(18, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(18, pcrplate['A4'], rate=2.0) 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(18, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(18, pcrplate['A2'], rate=2.0) 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(18, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(18, pcrplate['B1'], rate=2.0) 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5, cold_tuberack['D4'], rate=2.0) 
    left_pipette.dispense(5, pcrplate['A1'], rate=2.0) 
    left_pipette.mix(3,10,pcrplate['A1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5, cold_tuberack['D4'], rate=2.0) 
    left_pipette.dispense(5, pcrplate['A4'], rate=2.0) 
    left_pipette.mix(3,10,pcrplate['A4']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5, cold_tuberack['D4'], rate=2.0) 
    left_pipette.dispense(5, pcrplate['A2'], rate=2.0) 
    left_pipette.mix(3,10,pcrplate['A2']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5, cold_tuberack['D4'], rate=2.0) 
    left_pipette.dispense(5, pcrplate['B1'], rate=2.0) 
    left_pipette.mix(3,10,pcrplate['B1']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,35.5,pcrplate['A1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,35.5,pcrplate['A4']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,35.5,pcrplate['A2']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,35.5,pcrplate['B1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(32.0,watertuberack['A1'],2) 
    right_pipette.dispense(32.0,pcrplate['E11'],2) 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.0,tuberack2['B3'],2) 
    right_pipette.dispense(12.0,pcrplate['E11'],2) 
    right_pipette.mix(3,12.0,pcrplate['E11']) 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5.0,cold_tuberack['D4'],2) 
    left_pipette.dispense(5.0,pcrplate['E11'],2) 
    left_pipette.mix(3,5.0,pcrplate['E11']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0,cold_tuberack['D5'],2) 
    left_pipette.dispense(1.0,pcrplate['E11'],2) 
    left_pipette.mix(3,1.0,pcrplate['E11']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,50.0,pcrplate['E11']) 
    right_pipette.drop_tip() 
    tc_mod.close_lid() 
    tc_mod.set_lid_temperature(105) 
    tc_mod.set_block_temperature(37,0,30, block_max_volume = 50) 
    tc_mod.set_block_temperature(80,0,20, block_max_volume = 50) 
    tc_mod.set_block_temperature(4, block_max_volume = 50) 
    tc_mod.open_lid() 
    temp_module.deactivate() 
    tiprack3.reset() 
    tiprack3 = protocol.load_labware('opentrons_96_tiprack_10ul', '6') 
    protocol.pause('REFILL TIP RACKS, and wait until its time to dispense the product') 
    temp_module.set_temperature(4) 
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
    right_pipette.aspirate(10.74, watertuberack['A1']) 
    right_pipette.dispense(10.74, secondarydils['A1']) 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(6, pcrplate['A1']) 
    left_pipette.dispense(6, secondarydils['A1']) 
    left_pipette.mix(3,3,secondarydils['A1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.mix(3,3.58,secondarydils['A1']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(23.759999999999998, watertuberack['A1']) 
    right_pipette.dispense(23.759999999999998, secondarydils['A4']) 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(6, pcrplate['A4']) 
    left_pipette.dispense(6, secondarydils['A4']) 
    left_pipette.mix(3,3,secondarydils['A4']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.mix(3,7.92,secondarydils['A4']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(7.565591397849462, watertuberack['A1']) 
    right_pipette.dispense(7.565591397849462, secondarydils['E11']) 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(6, pcrplate['E11']) 
    left_pipette.dispense(6, secondarydils['E11']) 
    left_pipette.mix(3,3,secondarydils['E11']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.mix(3,2.521863799283154,secondarydils['E11']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(20, pcrplate['A2']) 
    right_pipette.dispense(20, secondarydils['A2']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(31.621647058823534, watertuberack['A1']) 
    right_pipette.dispense(31.621647058823534, secondarydils['B1']) 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(4, pcrplate['B1']) 
    left_pipette.dispense(4, secondarydils['B1']) 
    left_pipette.mix(3,3,secondarydils['B1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.mix(3,7.9054117647058835,secondarydils['B1']) 
    left_pipette.drop_tip() 
    protocol.pause('Clear off PCR plate and set up final Golden Gate assembly Tubes') 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5.68, watertuberack['A1']) 
    left_pipette.dispense(5.68, pcrplate['B8']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.6666666666666667, secondarydils['E11']) 
    left_pipette.dispense(1.6666666666666667, pcrplate['B8']) 
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
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15,pcrplate['B8']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5.68, watertuberack['A1']) 
    left_pipette.dispense(5.68, pcrplate['B8']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2.0, secondarydils['A1']) 
    left_pipette.dispense(2.0, pcrplate['B8']) 
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
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15,pcrplate['B8']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5.68, watertuberack['A1']) 
    left_pipette.dispense(5.68, pcrplate['B8']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2.0, secondarydils['A4']) 
    left_pipette.dispense(2.0, pcrplate['B8']) 
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
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15,pcrplate['B8']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5.68, watertuberack['A1']) 
    left_pipette.dispense(5.68, pcrplate['B9']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2.0, secondarydils['E11']) 
    left_pipette.dispense(2.0, pcrplate['B9']) 
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
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15,pcrplate['B9']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5.68, watertuberack['A1']) 
    left_pipette.dispense(5.68, pcrplate['B9']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.6666666666666667, secondarydils['A2']) 
    left_pipette.dispense(1.6666666666666667, pcrplate['B9']) 
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
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15,pcrplate['B9']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5.68, watertuberack['A1']) 
    left_pipette.dispense(5.68, pcrplate['B9']) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2.0, secondarydils['B1']) 
    left_pipette.dispense(2.0, pcrplate['B9']) 
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
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15,pcrplate['B9']) 
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
