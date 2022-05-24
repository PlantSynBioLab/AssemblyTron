#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from opentrons import protocol_api, types

#Metadata is a dictionary of data that is read by the server and returned to the opentrons app. 
#give yourself credit. you are required to specify the 'apiLevel' herefrom opentrons import protocol_api
metadata = {
    'protocolName': 'Transformation Protocol',
    'author': 'Jimena Flor <jflorfig@vt.edu>',
    'description': 'Protocol for transforming E. coli cells and plating',
    'apiLevel': '2.10'
}
print(metadata)




def run(protocol: protocol_api.ProtocolContext):
    
    ##locations
    # Tiprack for 50 ul using right_pipette
    tiprack4 = protocol.load_labware('opentrons_96_tiprack_300ul', '4')
    # Temperature module
    temp_module = protocol.load_module('temperature module','1')
    cold_block = temp_module.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap')
    # Thermocycler
    tc_module = protocol.load_module('Thermocycler Module')
    PCR_plate = tc_module.load_labware('nest_96_wellplate_100ul_pcr_full_skirt')
    # Custom culture plate 
    custom_plate = protocol.load_labware('culture_2_wellplate_15659.96ul', '3')
    right_pipette = protocol.load_instrument('p300_single','right', tip_racks = [tiprack4])
    
    
    # ## Set temperature for Temp_module and Thermocycler
    # # Temperature module set to 4C
    # temp_module.set_temperature(4)
    # # Temperature thermocycler set to 4C
    # tc_module.set_block_temperature(4)
    # # Open lid 
    # tc_module.open_lid()
    
    #  ## Add 50 uL of cells to thermocycler 
    # right_pipette.pick_up_tip()
    # right_pipette.aspirate(50,cold_block['A1'])
    # right_pipette.dispense(50,PCR_plate['B3'])
    # right_pipette.drop_tip()
    
    # ## Place cell to plasmid in temperature module
    # # add 5 uL plasmid to thermocycler
    # right_pipette.pick_up_tip()
    # right_pipette.aspirate(5,cold_block['B1'])
    # right_pipette.dispense(5, PCR_plate['B3'])
    # right_pipette.mix(8, 10, PCR_plate['B3']) #mixing the sample mix.(rep, volume,location)
    # right_pipette.drop_tip()

    # ## Add 250 uL SOC-E-coli media- mixing with transfomation mix
    # right_pipette.pick_up_tip()
    # right_pipette.aspirate(250,cold_block['C1'])
    # right_pipette.dispense(250,cold_block['A2'])
    # right_pipette.mix(3, 250, cold_block['A2'])
    # right_pipette.drop_tip()

    # ## Heatshock for 60 seconds
    # tc_module.close_lid()
    # tc_module.set_lid_temperature(70)
    # tc_module.set_block_temperature(4, hold_time_minutes = 30, block_max_volume = 55)
    # tc_module.set_block_temperature(42, hold_time_minutes = 1, block_max_volume = 55)
    # tc_module.set_block_temperature(24)
    # tc_module.open_lid()
    
    #  ## moving transfomration mix back to cold block
    # right_pipette.pick_up_tip()
    # right_pipette.aspirate(55,PCR_plate['B3'])
    # right_pipette.dispense(55,cold_block['A2'])
    # right_pipette.drop_tip()
    
    
    # ## Pause for incubation
    # protocol.pause('Pause for an hour for recovery')
    
    
    # Dotting onto A1
    # #right_pipette.pick_up_tip()
    # right_pipette.pick_up_tip()
    # right_pipette.aspirate(10, cold_block['A2'])
    # right_pipette.dispense(10,custom_plate['A1'].from_center_cartesian(0, 0, 0))
    # right_pipette.blow_out()
    # right_pipette.drop_tip()
    
    # right_pipette.pick_up_tip()
    # right_pipette.aspirate(10, cold_block['A2'])
    # right_pipette.dispense(10,[types.Location(custom_plate['A1'].from_center_cartesian(0, 0.5, 0), custom_plate["A1"])])
    # right_pipette.blow_out()
    # right_pipette.drop_tip()
    
    # right_pipette.pick_up_tip()
    # right_pipette.aspirate(10, cold_block['A2'])
    # right_pipette.dispense(10,[types.Location(custom_plate['A1'].from_center_cartesian(0, -0.5, 0), custom_plate["A1"])])
    # right_pipette.blow_out()
    # right_pipette.drop_tip()

    # right_pipette.pick_up_tip()
    # right_pipette.aspirate(10, cold_block['A2'])
    # right_pipette.dispense(10,[types.Location(custom_plate['A1'].from_center_cartesian(0.5, 0, 0), custom_plate["A1"])])
    # right_pipette.blow_out()
    # right_pipette.drop_tip()

    # right_pipette.pick_up_tip()
    # right_pipette.aspirate(10, cold_block['A2'])
    # right_pipette.dispense(10,[types.Location(custom_plate['A1'].from_center_cartesian(-0.5, 0, 0), custom_plate["A1"])])
    # right_pipette.blow_out()
    # right_pipette.drop_tip()


    #right_pipette.distribute(10, cold_block['A2'], [custom_plate['A1'].center().move(custom_plate['A1'].from_center_cartesian(x=0, y=0.5, z=0))])

    #center_cart = types.Location(custom_plate['A1'].from_center_cartesian(0, 0.5, 0), custom_plate['A1'])
    right_pipette.pick_up_tip()
    right_pipette.aspirate(10, cold_block['A2'])
    right_pipette.dispense(10, types.Location(custom_plate['A1'].from_center_cartesian(0, 0, 0), custom_plate['A1']))
    right_pipette.blow_out()
    right_pipette.drop_tip()
    
    right_pipette.pick_up_tip()
    right_pipette.aspirate(10, cold_block['A2'])
    right_pipette.dispense(10, types.Location(custom_plate['A1'].from_center_cartesian(0, 0.5, 0), custom_plate['A1']))
    right_pipette.blow_out()
    right_pipette.drop_tip()

    right_pipette.pick_up_tip()
    right_pipette.aspirate(10, cold_block['A2'])
    right_pipette.dispense(10, types.Location(custom_plate['A1'].from_center_cartesian(0, -0.5, 0), custom_plate['A1']))
    right_pipette.blow_out()
    right_pipette.drop_tip()

    right_pipette.pick_up_tip()
    right_pipette.aspirate(10, cold_block['A2'])
    right_pipette.dispense(10, types.Location(custom_plate['A1'].from_center_cartesian(0.5, 0, 0), custom_plate['A1']))
    right_pipette.blow_out()
    right_pipette.drop_tip()

    right_pipette.pick_up_tip()
    right_pipette.aspirate(10, cold_block['A2'])
    right_pipette.dispense(10, types.Location(custom_plate['A1'].from_center_cartesian(-0.5, 0, 0), custom_plate['A1']))
    right_pipette.blow_out()
    right_pipette.drop_tip()

    # right_pipette.distribute(10, cold_block['A2'], [types.Location(custom_plate['A1'].from_center_cartesian(0, 0, 0), custom_plate["A1"])])
    # right_pipette.distribute(10, cold_block['A2'], [custom_plate.Location(custom_plate['A1'].from_center_cartesian(0, 0.5, 0), custom_plate["A1"])])
    # right_pipette.distribute(10, cold_block['A2'], [custom_plate.Location(custom_plate['A1'].from_center_cartesian(0, -0.5, 0), custom_plate["A1"])])
    # right_pipette.distribute(10, cold_block['A2'], [custom_plate.Location(custom_plate['A1'].from_center_cartesian(0.5, 0, 0), custom_plate["A1"])])
    # right_pipette.distribute(10, cold_block['A2'], [types.Location(custom_plate['A1'].from_center_cartesian(-0.5, 0, 0), custom_plate["A1"])])
    # #right_pipette.drop_tip()
    
    # # Dotting onto A2
    # #right_pipette.pick_up_tip()
    # right_pipette.distribute(10, cold_block['A2'], [types.Location(custom_plate['A2'].from_center_cartesian(0, 0, 0), custom_plate["A2"])])
    # right_pipette.distribute(10, cold_block['A2'], [types.Location(custom_plate['A2'].from_center_cartesian(0, 0.5, 0), custom_plate["A2"])])
    # right_pipette.distribute(10, cold_block['A2'], [types.Location(custom_plate['A2'].from_center_cartesian(0, -0.5, 0), custom_plate["A2"])])
    # right_pipette.distribute(10, cold_block['A2'], [types.Location(custom_plate['A2'].from_center_cartesian(0.5, 0, 0), custom_plate["A2"])])
    # right_pipette.distribute(10, cold_block['A2'], [types.Location(custom_plate['A2'].from_center_cartesian(-0.5, 0, 0), custom_plate["A2"])])
    # #right_pipette.drop_tip()
    
    
    
    
    
    
    
    
    
    
    
    
    

    
   
    
    
    
    

