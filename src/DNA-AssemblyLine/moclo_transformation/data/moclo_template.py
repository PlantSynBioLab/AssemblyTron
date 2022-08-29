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

p10_single = instruments.P10_Single(mount='right', tip_racks=tr_10)

# Need to provide the instructions for loading reagent
reagents_plate = labware.load(COLD_BLOCK, '4', 'Reagents Plate')
ligase = reagents_plate.wells('H12') #MoClo
restriction_enzyme = reagents_plate.wells('G12') #MoClo
buffer = reagents_plate.wells('F12') # MoClo
water = reagents_plate.wells('E12')

# Load in water, SOC, and wash trough (USA Scientific 12 Well Reservoir 22ml)
trough = labware.load('usascientific_12_reservoir_22ml', '5', 'Reagents trough')
water = trough.wells(0) #Well 1
wash_0 = trough.wells(1) #Well 2
wash_1 = trough.wells(2) #Well 3

dna_plate_dict = {}
for plate_name in dna_plate_map_dict.keys():
	dna_plate_dict[plate_name] = labware.load('biorad_96_wellplate_200ul_pcr', '1', 'Input DNA Plate')

#available_deck_slots = ['2', '6', '8', '9', '11']

############################Start the MoClo protocol############################

################################################################################
# For this protocol, the biorad_96_wellplate_200ul_pcr, is placed on the top of the TempDeck alone without the metal part.
################################################################################

# Add water, buffer, restriction enzyme, ligase, and buffer to 2x master mix (2xMM).
#Prepare 2xMM for 2-part assembly at 20uL total volume
for i in range(2):
	p10_single.pick_up_tip()
	p10_single.transfer((150), water.bottom(), reaction_plate.wells(95-i).bottom(0.5), new_tip='never') #Water
	p10_single.blow_out()
	p10_single.drop_tip()
	p10_single.pick_up_tip()
	p10_single.transfer(24, buffer.bottom(), reaction_plate.wells(95-i).bottom(0.5), new_tip='never') #Buffer (1uL/rxn)
	p10_single.mix(2, 10, reaction_plate.wells(95-i).bottom(0.5))
	p10_single.blow_out()
	p10_single.drop_tip()
	p10_single.pick_up_tip()
	p10_single.transfer(6, ligase.bottom(), reaction_plate.wells(95-i).bottom(0.5), new_tip='never') #Ligase (0.25uL/rxn)
	p10_single.mix(2, 10, reaction_plate.wells(95-i).bottom(0.5))
	p10_single.blow_out()
	p10_single.drop_tip()
	p10_single.pick_up_tip()
	p10_single.transfer(12, restriction_enzyme.bottom(), reaction_plate.wells(95-i).bottom(0.5), new_tip='never') #Restriction Enzyme  (0.5uL/rxn)
	p10_single.mix(2, 10, reaction_plate.wells(95-i).bottom(0.5))
	p10_single.blow_out()
	p10_single.drop_tip()

#Prepare 2xMM for 5-part assembly at 20uL total volume
for i in range(2):
	p10_single.pick_up_tip()
	p10_single.transfer((78), water.bottom(), reaction_plate.wells(93-i).bottom(0.5), new_tip='never') #Water
	p10_single.blow_out()
	p10_single.drop_tip()
	p10_single.pick_up_tip()
	p10_single.transfer(24, buffer.bottom(), reaction_plate.wells(93-i).bottom(0.5), new_tip='never') #Buffer (1uL/rxn)
	p10_single.mix(2, 10, reaction_plate.wells(93-i).bottom(0.5))
	p10_single.blow_out()
	p10_single.drop_tip()
	p10_single.pick_up_tip()
	p10_single.transfer(6, ligase.bottom(), reaction_plate.wells(93-i).bottom(0.5), new_tip='never') #Ligase (0.25uL/rxn)
	p10_single.mix(2, 10, reaction_plate.wells(93-i).bottom(0.5))
	p10_single.blow_out()
	p10_single.drop_tip()
	p10_single.pick_up_tip()
	p10_single.transfer(12, restriction_enzyme.bottom(), reaction_plate.wells(93-i).bottom(0.5), new_tip='never') #Restriction Enzyme  (0.5uL/rxn)
	p10_single.mix(2, 10, reaction_plate.wells(93-i).bottom(0.5))
	p10_single.blow_out()
	p10_single.drop_tip()

#Prepare 2xMM for 8-part assembly at 20uL total volume
for i in range(2):
	p10_single.pick_up_tip()
	p10_single.transfer((6), water.bottom(), reaction_plate.wells(91-i).bottom(0.5), new_tip='never') #Water
	p10_single.blow_out()
	p10_single.drop_tip()
	p10_single.pick_up_tip()
	p10_single.transfer(24, buffer.bottom(), reaction_plate.wells(91-i).bottom(0.5), new_tip='never') #Buffer (1uL/rxn)
	p10_single.mix(2, 10, reaction_plate.wells(91-i).bottom(0.5))
	p10_single.blow_out()
	p10_single.drop_tip()
	p10_single.pick_up_tip()
	p10_single.transfer(6, ligase.bottom(), reaction_plate.wells(91-i).bottom(0.5), new_tip='never') #Ligase (0.25uL/rxn)
	p10_single.mix(2, 10, reaction_plate.wells(91-i).bottom(0.5))
	p10_single.blow_out()
	p10_single.drop_tip()
	p10_single.pick_up_tip()
	p10_single.transfer(12, restriction_enzyme.bottom(), reaction_plate.wells(91-i).bottom(0.5), new_tip='never') #Restriction Enzyme  (0.5uL/rxn)
	p10_single.mix(2, 10, reaction_plate.wells(91-i).bottom(0.5))
	p10_single.blow_out()
	p10_single.drop_tip()

# Add master mix to each wells that would contain rxn
# Add 2xMM to 2-part assembly
p10_single.pick_up_tip()
for i in range(12):
	p10_single.transfer(16, reaction_plate.wells(95).bottom(), reaction_plate.wells(i).bottom(0.3), new_tip='never')
	p10_single.blow_out()
p10_single.drop_tip()

p10_single.pick_up_tip()
for i in range(12):
	p10_single.transfer(16, reaction_plate.wells(94).bottom(), reaction_plate.wells(12+i).bottom(0.3), new_tip='never')
	p10_single.blow_out()
p10_single.drop_tip()

# Add 2xMM to 5-part assembly
p10_single.pick_up_tip()
for i in range(12):
	p10_single.transfer(10, reaction_plate.wells(93).bottom(), reaction_plate.wells(24+i).bottom(0.3), new_tip='never')
	p10_single.blow_out()
p10_single.drop_tip()

p10_single.pick_up_tip()
for i in range(12):
	p10_single.transfer(10, reaction_plate.wells(92).bottom(), reaction_plate.wells(36+i).bottom(0.3), new_tip='never')
	p10_single.blow_out()
p10_single.drop_tip()

# Add 2xMM to 8-part assembly
p10_single.pick_up_tip()
for i in range(12):
	p10_single.transfer(4, reaction_plate.wells(91).bottom(), reaction_plate.wells(48+i).bottom(0.3), new_tip='never')
	p10_single.blow_out()
p10_single.drop_tip()

p10_single.pick_up_tip()
for i in range(12):
	p10_single.transfer(4, reaction_plate.wells(90).bottom(), reaction_plate.wells(60+i).bottom(0.3), new_tip='never')
	p10_single.blow_out()
p10_single.drop_tip()

#This function checks the existance of DNA parts and returns for well location of the parts
def find_dna(name, dna_plate_map_dict, dna_plate_dict):
	"""Return a well containing the named DNA."""
	for plate_name, plate_map in dna_plate_map_dict.items():
		for i, row in enumerate(plate_map):
			for j, dna_name in enumerate(row):
				if dna_name == name:
					well_num = 8 * j + i
					return(dna_plate_dict[plate_name].wells(well_num))
	raise ValueError("Could not find dna piece named \"{0}\"".format(name))

#This function checks if the DNA parts exist in the DNA plates and returns for well locaion of output DNA combinations
def find_combination(name, combinations_to_make):
	"""Return a well containing the named combination."""
	for i, combination in enumerate(combinations_to_make):
		if combination["name"] == name:
			return reaction_plate.wells(i)
	raise ValueError("Could not find combination \"{0}\".".format(name))

combinations_by_part = {}
for i in combinations_to_make:
	name = i["name"]
	for j in i["parts"]:
		if j in combinations_by_part.keys():
			combinations_by_part[j].append(name)
		else:
			combinations_by_part[j] = [name]

# This section of the code combines and mix the DNA parts according to the combination list
for part, combinations in combinations_by_part.items():
	part_well = find_dna(part, dna_plate_map_dict, dna_plate_dict)
	combination_wells = [find_combination(x, combinations_to_make) for x in combinations]
	p10_single.pick_up_tip()
	while combination_wells:
		if len(combination_wells) > 5:
			current_wells = combination_wells[0:5]
			combination_wells = combination_wells[5:]
		else:
			current_wells = combination_wells
			combination_wells = []
		p10_single.aspirate(2 * len(current_wells), part_well.bottom(0.5))
		for i in current_wells:
			p10_single.dispense(2, i.bottom(0.5))
		if combination_wells:
			p10_single.mix(2, 10, wash_0.bottom(0.5))
			p10_single.blow_out()
			p10_single.mix(2, 10, wash_1.bottom(0.5))
			p10_single.blow_out()
	# Two washing steps are added to allow recycling of the tips
	p10_single.drop_tip()

# Seal the Reaction Plate with adhesive film, and incubate plate for 35 cycles of 37C for 1.5 minutes and 16C for 3 minutes, followed by 1 cycle at 50C for 5 minutes, and 80C for 10 minutes.

################################################################################
# Seal the Reaction Plate to avoid liquid evaporation.
# Discard the empty PCR tubes previously containing buffer, ligase, and restriction enzyme.
# Remove the Input_DNA_Plate from the Deck Space. Remaining DNA may be saved by sealing the Input_DNA_Plate with adhesive film and storing at -20°C
################################################################################

temp_deck.deactivate()
