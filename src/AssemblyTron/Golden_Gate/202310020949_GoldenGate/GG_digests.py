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
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(8.75, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(8.75, pcrplate['A1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(8.75, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(8.75, pcrplate['H1'], rate=2.0) 
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
    left_pipette.dispense(1.0, pcrplate['H1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['H1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['A4'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['H1'], rate=2.0) 
    left_pipette.mix(3,2,pcrplate['H1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B1'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['A1'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['A1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1.0, tuberack2['B2'], rate=2.0) 
    left_pipette.dispense(1.0, pcrplate['H1'], rate=2.0) 
    left_pipette.mix(3,3,pcrplate['H1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(0.75, tuberack2['D6'], rate=2.0) 
    left_pipette.dispense(0.75, pcrplate['A1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(0.75, tuberack2['D6'], rate=2.0) 
    left_pipette.dispense(0.75, pcrplate['H1'], rate=2.0) 
    left_pipette.blow_out() 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 
    right_pipette.aspirate(12.5, pcrplate['A1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.5, cold_tuberack['D6'], rate=2.0) 
    right_pipette.aspirate(12.5, pcrplate['H1'], rate=2.0) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.5,pcrplate['A1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.5,pcrplate['H1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    tc_mod.close_lid() 
    tc_mod.set_lid_temperature(temperature = 105) 
    tc_mod.set_block_temperature(98, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.562, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.62004411764705, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.67808823529411, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.73613235294117, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.79417647058823, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.8522205882353, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.91026470588235, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(65.96830882352941, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.02635294117647, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.08439705882353, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.14244117647058, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.20048529411764, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.2585294117647, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.31657352941177, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.37461764705883, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.43266176470588, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.49070588235294, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.54875, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.60679411764706, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.66483823529411, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.72288235294117, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.78092647058824, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.8389705882353, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.89701470588236, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(66.95505882352941, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(67.01310294117647, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(67.07114705882353, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(67.12919117647058, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(67.18723529411764, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(67.2452794117647, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(67.30332352941177, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(67.36136764705883, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(67.41941176470588, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) 
    tc_mod.set_block_temperature(67.47745588235294, hold_time_seconds=30, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_seconds=94.74, block_max_volume=25) 
    tc_mod.set_block_temperature(72, hold_time_minutes=5, block_max_volume=25) 
    tc_mod.set_block_temperature(4) 
    tc_mod.set_lid_temperature(temperature = 45) 
    protocol.pause('wait until ready to dispense assemblies') 
    tc_mod.open_lid() 
    protocol.pause('just take them out manually...') 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(18, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(18, pcrplate['A1'], rate=2.0) 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(18, watertuberack['A1'], rate=2.0) 
    right_pipette.dispense(18, pcrplate['H1'], rate=2.0) 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5, cold_tuberack['D4'], rate=2.0) 
    left_pipette.dispense(5, pcrplate['A1'], rate=2.0) 
    left_pipette.mix(3,10,pcrplate['A1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(5, cold_tuberack['D4'], rate=2.0) 
    left_pipette.dispense(5, pcrplate['H1'], rate=2.0) 
    left_pipette.mix(3,10,pcrplate['H1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2, cold_tuberack['D3'], rate=2.0) 
    left_pipette.dispense(2, pcrplate['A1'], rate=2.0) 
    left_pipette.mix(3,10,pcrplate['A1']) 
    left_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(2, cold_tuberack['D3'], rate=2.0) 
    left_pipette.dispense(2, pcrplate['H1'], rate=2.0) 
    left_pipette.mix(3,10,pcrplate['H1']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,35.5,pcrplate['A1']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,35.5,pcrplate['H1']) 
    right_pipette.blow_out() 
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
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(38.0,watertuberack['A1'],2) 
    right_pipette.dispense(38.0,pcrplate['E11'],2) 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(36.66666666666666,watertuberack['A1'],2) 
    right_pipette.dispense(36.66666666666666,pcrplate['F11'],2) 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(12.0,tuberack2['A5'],2) 
    right_pipette.dispense(12.0,pcrplate['E11'],2) 
    right_pipette.mix(3,12.0,pcrplate['E11']) 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,50.0,pcrplate['E11']) 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,50.0,pcrplate['F11']) 
    right_pipette.drop_tip() 
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
    right_pipette.dispense(18.438616714697403, secondarydils['H1']) 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, pcrplate['H1']) 
    left_pipette.dispense(1, secondarydils['H1']) 
    left_pipette.mix(3,3,secondarydils['H1']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,18.438616714697403,secondarydils['H1']) 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(20, pcrplate['F11']) 
    right_pipette.dispense(20, secondarydils['F11']) 
    right_pipette.blow_out() 
    right_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.aspirate(15.561383285302592, watertuberack['A1']) 
    right_pipette.dispense(15.561383285302592, secondarydils['H1']) 
    right_pipette.drop_tip() 
    left_pipette.pick_up_tip() 
    left_pipette.aspirate(1, pcrplate['H1']) 
    left_pipette.dispense(1, secondarydils['H1']) 
    left_pipette.mix(3,3,secondarydils['H1']) 
    left_pipette.drop_tip() 
    right_pipette.pick_up_tip() 
    right_pipette.mix(3,15.561383285302592,secondarydils['H1']) 
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
    left_pipette.aspirate(2.0, secondarydils['H1']) 
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
    left_pipette.aspirate(2.0, secondarydils['H1']) 
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
