from opentrons import protocol_api
import pandas as pd
import os

## Meta Data

metadata = {'protocolName': 'PME1 Digestion',
'author':'Mason Kellinger masonkellinger@vt.edu',
 'description':'First phase of yeast transformation',
 'apiLevel': '2.9'
}
print(metadata)

os.chdir("/data/user_storage/Restriction/")
os.getcwd()

plasmid = pd.read_csv("20220114_pme1/20220114_pme1.csv",engine = 'python', encoding='utf-8-sig')

plasmid = pd.DataFrame(plasmid)

plasmid['Buffer'] = float('4.4')
plasmid['PME1'] = float('1')
plasmid['Volume of Plasmid'] = ''
plasmid['Volume of Water'] = ''

plasmid['Volume of Plasmid'] = (1/(plasmid['Concentration'])) * 1000 * 1.5
plasmid['Volume of Water'] = 44 - plasmid['Volume of Plasmid'] - plasmid['Buffer'] - plasmid['PME1']

plasmid['total volume'] = float('44')


#plasmid templates arranged in an "L" formation
row2well= {}
row2well['0'] = 'A2'
row2well['1'] = 'B2'
row2well['2'] = 'C2'
row2well['3'] = 'D2'
row2well['4'] = 'D3'
row2well['5'] = 'D4'
row2well['6'] = 'D5'
row2well['7'] = 'D6'

plasmid['Plasmid Location'] = ''

for i, row in plasmid.iterrows():
    plasmid.loc[i,'Plasmid Location'] = row2well[str(i)]

#The pcr tube destination will change every time you use a new row of the 96 well pcr plate
row2tube= {}
#row2tube['0'] = 'B1'
#row2tube['1'] = 'B2'
#row2tube['2'] = 'B3'
#row2tube['3'] = 'B4'
#row2tube['4'] = 'B5'
#row2tube['5'] = 'B6'
#row2tube['6'] = 'B7'
#row2tube['7'] = 'B8'
#row2tube['0'] = 'C1'
row2tube['0'] = 'B2'
row2tube['1'] = 'B3'
row2tube['2'] = 'B4'
row2tube['3'] = 'B5'
row2tube['4'] = 'B6'
row2tube['5'] = 'B7'
# row2tube['7'] = 'C8'
# row2tube['0'] = 'F1'
# row2tube['1'] = 'F2'
# row2tube['2'] = 'F3'
# row2tube['3'] = 'F4'
# row2tube['4'] = 'F5'
# row2tube['5'] = 'F6'
# row2tube['6'] = 'F7'
# row2tube['7'] = 'F8'
# row2tube['8'] = 'F9'
# row2tube['0'] = 'D1'
# row2tube['1'] = 'D2'
# row2tube['2'] = 'D3'
# row2tube['3'] = 'D4'
# row2tube['4'] = 'D5'
# row2tube['5'] = 'D6'
# row2tube['6'] = 'D7'
# row2tube['7'] = 'D8'
# row2tube['8'] = 'D9'

plasmid['Digestion Tube'] = ''

for i, row in plasmid.iterrows():
    plasmid.loc[i,'Digestion Tube'] = row2tube[str(i)]

pcr2final= {}
pcr2final['0'] = 'A1'
pcr2final['1'] = 'A2'
pcr2final['2'] = 'A3'
pcr2final['3'] = 'A4'
pcr2final['4'] = 'A5'
pcr2final['5'] = 'A6'
pcr2final['6'] = 'B1'
pcr2final['7'] = 'B2'
pcr2final['8'] = 'B3'

plasmid['final tube'] = ''

for i, row in plasmid.iterrows():
    plasmid.loc[i,'final tube'] = pcr2final[str(i)]



from opentrons import protocol_api

#Metadata is a dictionary of data that is read by the server and returned to the opentrons app. 
#give yourself credit. you are required to specify the 'apiLevel' herefrom opentrons import protocol_api
metadata = {
    'protocolName': 'PME1 Digestion',
    'author': 'Mason Kellinger <masonkellinger@vt.edu> and John Bryant <jbryant2@vt.edu',
    'description': 'Protocol for digesting plasmids that have PME1 cut sites',
    'apiLevel': '2.10'
}
#print(metadata)

#################################################################################
#Commands
#############################################################################
def run(protocol: protocol_api.ProtocolContext):

     ## Loading labware
    thermo = protocol.load_module('Thermocycler Module')
    pcr = thermo.load_labware('nest_96_wellplate_100ul_pcr_full_skirt')
        
    tiprack1 = protocol.load_labware("opentrons_96_tiprack_10ul",5)
    tiprack2 = protocol.load_labware("opentrons_96_tiprack_300ul",2)
    finalprodtubes = protocol.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap",3)
    #tuberack = protocol.load_labware("opentrons_24_tuberack_nest_2ml_snapcap",4)
    temp_module = protocol.load_module('temperature module', 1)
    cold_tuberack = temp_module.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap', label='Temperature-Controlled Tubes')
    temp_module.set_temperature(4)
    print(temp_module.temperature)
    
 ## Loading tools
    pipette_right = protocol.load_instrument('p300_single_gen2','right',tip_racks = [tiprack2])
    pipette_left = protocol.load_instrument('p10_single','left',tip_racks = [tiprack1])
## Commands

    thermo.open_lid()

    protocol.pause('Prepare Tubes')

# pick up water -> dispense into pcr tube within thermocycler -> get rid of tip
    pipette_right.pick_up_tip()
    for i, row in plasmid.iterrows():
        pipette_right.aspirate(plasmid.loc[i].at['Volume of Water'],cold_tuberack['A1'],2)
        pipette_right.dispense(plasmid.loc[i].at['Volume of Water'],pcr[plasmid.loc[i].at['Digestion Tube']],2)
        pipette_right.blow_out()

    pipette_right.drop_tip()

# pick up plasmid  -> dispense into pcr tube -> get rid of tip  no blow out because aeresol

    for i, row in plasmid.iterrows():
        pipette_left.pick_up_tip()
        pipette_left.aspirate(plasmid.loc[i].at['Volume of Plasmid'],cold_tuberack[plasmid.loc[i].at['Plasmid Location']],2) #location of plasmid
        pipette_left.dispense(plasmid.loc[i].at['Volume of Plasmid'],pcr[plasmid.loc[i].at['Digestion Tube']],2)
        pipette_left.mix(3,plasmid.loc[i].at['Volume of Plasmid'],pcr[plasmid.loc[i].at['Digestion Tube']])
        pipette_left.blow_out()
        pipette_left.drop_tip()

# pick up buffer  -> dispense into pcr tube -> get rid of tip

    for i, row in plasmid.iterrows():
        pipette_left.pick_up_tip()
        pipette_left.aspirate(plasmid.loc[i].at['Buffer'],cold_tuberack['A3'],2)
        pipette_left.dispense(plasmid.loc[i].at['Buffer'],pcr[plasmid.loc[i].at['Digestion Tube']],2)
        pipette_left.mix(3,plasmid.loc[i].at['Buffer'],pcr[plasmid.loc[i].at['Digestion Tube']])
        pipette_left.blow_out()
        pipette_left.drop_tip()  


# pick up PME1 -> dispense into pcr tube -> get rid of tip

    for i, row in plasmid.iterrows():
        pipette_left.pick_up_tip()
        pipette_left.aspirate(plasmid.loc[i].at['PME1'],cold_tuberack['A4'],2)
        pipette_left.dispense(plasmid.loc[i].at['PME1'],pcr[plasmid.loc[i].at['Digestion Tube']],2)
        pipette_left.mix(3,plasmid.loc[i].at['PME1'],pcr[plasmid.loc[i].at['Digestion Tube']])
        pipette_left.blow_out()
        pipette_left.drop_tip()


    for i, row in plasmid.iterrows():

        if plasmid.loc[i].at['total volume'] > float('10'):
            pipette_right.pick_up_tip()
            pipette_right.mix(3,plasmid.loc[i].at['total volume'],pcr[plasmid.loc[i].at['Digestion Tube']])
            pipette_right.blow_out()
            pipette_right.drop_tip()
        else:
            pipette_left.pick_up_tip()
            pipette_left.mix(3,plasmid.loc[i].at['total volume'],pcr[plasmid.loc[i].at['Digestion Tube']])
            pipette_left.blow_out()
            pipette_left.drop_tip()

 #mixes contents around using the pipette tip  (reps,max volume,location)

    protocol.pause('put up enzymes and templates')
    temp_module.deactivate()
    thermo.close_lid()
    thermo.set_lid_temperature(105)
    thermo.set_block_temperature(37,0,30, block_max_volume = 44) #temp,seconds,minutes,ramprate(danger),max vol
    thermo.set_block_temperature(65,0,20, block_max_volume = 44)
    thermo.set_block_temperature(4, block_max_volume = 44)

    protocol.pause('wait until its time to dispense the product')

    thermo.open_lid()

    for i, row in plasmid.iterrows():

        if plasmid.loc[i].at['total volume'] > float('10'):
            pipette_right.pick_up_tip()
            pipette_right.aspirate(plasmid.loc[i].at['total volume'],pcr[plasmid.loc[i].at['Digestion Tube']],2)
            pipette_right.dispense(plasmid.loc[i].at['total volume'],finalprodtubes[plasmid.loc[i].at['final tube']],2)
            pipette_right.blow_out()
            pipette_right.drop_tip()
        
        else:
            pipette_left.pick_up_tip()
            pipette_left.aspirate(plasmid.loc[i].at['total volume'],pcr[plasmid.loc[i].at['Digestion Tube']],2)
            pipette_left.dispense(plasmid.loc[i].at['total volume'],finalprodtubes[plasmid.loc[i].at['final tube']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()

    thermo.close_lid()

    #could add a purple loading dye mix step here.


    




