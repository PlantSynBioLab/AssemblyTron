#Modified version 2/28/20

################################################################################
# Up to 88 rxns per single run and 24 rxns for triplicate of each combination of DNA assembly

#This protocol is optimized for maximum walkaway time and percision
################################################################################

import time
import math

from opentrons import robot, instruments, labware, modules

num_rxns = len(combinations_to_make)

################################################################################
# For this protocol, the biorad_96_wellplate_200ul_pcr, is placed on the top of the TempDeck alone without the Opentrons 96 well aluminum block.
################################################################################

# Load in Bio-Rad 96 Well Plate on temp deck for moclos, transformation, and outgrowth.
temp_deck = modules.load('tempdeck', '10')
reaction_plate = labware.load('biorad_96_wellplate_200ul_pcr', '10', share=True)
temp_deck.set_temperature(10)

# Load in 1 10ul tiprack and 2 300ul tipracks
tr_10 = [labware.load('opentrons_96_tiprack_10ul', '3')]
tr_300 = [labware.load('opentrons_96_tiprack_300ul', '6'), labware.load('opentrons_96_tiprack_300ul', '9')]

# Load in pipettes
p10_single = instruments.P10_Single(mount='right', tip_racks=tr_10)
p300_multi = instruments.P300_Multi(mount='left', tip_racks=tr_300)

################################################################################
# This deck slot location is dedicated for the reaction plate after MoClo protocol is completed, so at the beginning of the protocol there isn't an actual plate existing in this slot location.

post_moclo_reaction_plate = labware.load('biorad_96_wellplate_200ul_pcr', '7', 'Post-MoClo Reaction Plate')
################################################################################

# Load in water, SOC, and wash trough (USA Scientific 12 Well Reservoir 22ml)
trough = labware.load('usascientific_12_reservoir_22ml', '5', 'Reagents trough')
water = trough.wells(0) #Well 1
wash_0 = trough.wells(1) #Well 2
wash_1 = trough.wells(2) #Well 3
soc = trough.wells(3) #Well 4
liquid_waste = trough.wells(4) #Well 5

# Load in 1 agar plate, same antibiotic for all plasmids is assumed (e-gelgol)
# Be careful labware e-gelgol is an old container type, and could eventually be removed by Opentrons!
agar_plate = labware.load('e-gelgol', '2', 'Agar Plate')

#available_deck_slots = ['1', '4', '8', '11']

#####################Start the Transformation protocol##########################
################################################################################
# The robotic liquid handler would automatically pause when the modular cloning protocol is completed, indicated by the blue light (cooling down) of the Temperature Module.

#Remove the reaction_plate from the top of the Temperature Module and place it on Slot 7 which is assigned to the post_moclo_reaction_plate at the beginning of the protocol, and remove the adhesive film.

#Before beginning the Cell Transformation protocol, load 10 μL/well of chemically competent cells into a new Bio-Rad 96 Well Plate and place it on the top of the Temperature Module.

#Be sure to un-pause the robot after completing all the steps listed above!
################################################################################

'''Use 10uL of competent cells with 2uL of each DNA rections from the MoClo protocol'''

# At the beginning of this for loop, the Bio-Rad 96 Well Plate (reaction_plate) now contains 10 uL of competent cells per wells (well 1 through 88)
p10_single.pick_up_tip()
# Add 2 ul of rxns to comp cells
for i in range(0, num_rxns):
	p10_single.transfer(2, post_moclo_reaction_plate.wells(i).bottom(0.5), reaction_plate.wells(i).bottom(0.5), new_tip='never')
	p10_single.mix(4, 10, reaction_plate.wells(i).bottom(0.5))
	p10_single.blow_out()
	p10_single.mix(2, 10, wash_0.bottom(0.5))
	p10_single.blow_out()
	p10_single.mix(2, 10, wash_1.bottom(0.5))
	p10_single.blow_out()
# Two washing steps are added to allow recycling of the tips
p10_single.drop_tip()

# Incubate at 4C, then heat shock.
'''Be sure to un-pause the robot in between the heat shock'''
temp_deck.set_temperature(4)
p10_single.delay(minutes=30)
temp_deck.set_temperature(42)
p10_single.delay(minutes=1)
temp_deck.set_temperature(4)
p10_single.delay(minutes=5)

# Add soc.
p300_multi.pick_up_tip()
for i in range(0, num_cols):
	p300_multi.transfer(150, soc.bottom(), reaction_plate.cols(i).bottom(1), new_tip='never')
	p300_multi.mix(2, 150, reaction_plate.cols(i).bottom(1))
	p300_multi.blow_out()
	p300_multi.mix(2, 300, wash_0.bottom())
	p300_multi.blow_out()
	p300_multi.mix(2, 300, wash_1.bottom())
	p300_multi.blow_out()
# Two washing steps are added to allow recycling of the tips
p300_multi.drop_tip()

# Grow for 1 hr, seal the plate with adhesive film to avoid evaporation
temp_deck.set_temperature(37)
p10_single.delay(minutes=60)
robot.pause()
temp_deck.deactivate()
################################################################################
# Remove the adhesive film from the Reaction Plate before perceeding to Cell Plating.
# Be sure to un-pause the robot after removing the adhesive film!
################################################################################

# Dilute the recovered transformation reactions and start plating
################################################################################
# All recovered transformation reactions are diluted to 10% of its original concentration before plating
################################################################################

#Dilution
p300_multi.pick_up_tip()
for i in range(0, num_cols):
	p300_multi.transfer(157, reaction_plate.cols(i).bottom(0.5), liquid_waste.bottom(), new_tip='never')
	p300_multi.blow_out()
	p300_multi.mix(2, 300, wash_0.bottom())
	p300_multi.blow_out()
	p300_multi.mix(2, 300, wash_1.bottom())
	p300_multi.blow_out()
	# Two washing steps are added to allow recycling of the tips
	p300_multi.transfer(45, soc.bottom(), reaction_plate.cols(i).bottom(0.5), new_tip='never')
	p300_multi.mix(2, 50, reaction_plate.cols(i).bottom(0.5))
	p300_multi.blow_out()
	p300_multi.mix(2, 300, wash_0.bottom())
	p300_multi.blow_out()
	p300_multi.mix(2, 300, wash_1.bottom())
	p300_multi.blow_out()
# Two washing steps are added to allow recycling of the tips
p300_multi.drop_tip()

#Plating
################################################################################
# Un-comment line 141, and line 145 through line 152 if you're plating for triplicate of each reactions.
################################################################################
#count2 = 0
for i in range(0, num_cols):
	p300_multi.pick_up_tip()
	p300_multi.transfer(10, reaction_plate.cols(i).bottom(0.5), agar_plate.cols(i).bottom(0.3), new_tip='never')
	#p300_multi.transfer(1, reaction_plate.cols(i).bottom(0.5), agar_plate.cols(i).bottom(-1), new_tip='never')
	#p300_multi.transfer(9, reaction_plate.cols(i).bottom(0.5), agar_plate.cols(i+count2).bottom(0.8), new_tip='never')
	#p300_multi.transfer(1, reaction_plate.cols(i).bottom(0.5), agar_plate.cols(i+count2).bottom(-1), new_tip='never')
	#p300_multi.transfer(9, reaction_plate.cols(i).bottom(0.5), agar_plate.cols(i+count2+1).bottom(0.8), new_tip='never')
	#p300_multi.transfer(1, reaction_plate.cols(i).bottom(0.5), agar_plate.cols(i+count2+1).bottom(-1), new_tip='never')
	#p300_multi.transfer(9, reaction_plate.cols(i).bottom(0.5), agar_plate.cols(i+count2+2).bottom(0.8), new_tip='never')
	#p300_multi.transfer(1, reaction_plate.cols(i).bottom(0.5), agar_plate.cols(i+count2+2).bottom(-1), new_tip='never')
	#count2 += 2
	p300_multi.drop_tip()
