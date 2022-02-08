import pandas as pd
import os
from opentrons import protocol_api
import numpy as np

plasmids_df = pd.read_csv('WL_plasmids.csv')
plasmids_df = plasmids_df[['pWL','plate','row','col','bacterial res']]
plasmids_df = plasmids_df[(plasmids_df['plate'] == 1) | (plasmids_df['plate'] == 2)]

for i, row in plasmids_df.iterrows():
    if (plasmids_df.loc[i,'bacterial res']) == 'Ampicillin':
        plasmids_df.loc[i,'bacterial res'] = 'Amp'
        
for i, row in plasmids_df.iterrows():
    if (plasmids_df.loc[i,'bacterial res']) == 'AMP/Chlor':
        plasmids_df.loc[i,'bacterial res'] = 'Amp/Chl'
        
for i, row in plasmids_df.iterrows():
    if (plasmids_df.loc[i,'bacterial res']) == 'AMP':
        plasmids_df.loc[i,'bacterial res'] = 'Amp'
        
for i, row in plasmids_df.iterrows():
    if (plasmids_df.loc[i,'bacterial res']) == 'Chloramphenicol':
        plasmids_df.loc[i,'bacterial res'] = 'Chl'
        
for i, row in plasmids_df.iterrows():
    if (plasmids_df.loc[i,'bacterial res']) == 'zeocin':
        plasmids_df.loc[i,'bacterial res'] = 'Zeo'
        
for i, row in plasmids_df.iterrows():
    if (plasmids_df.loc[i,'bacterial res']) == '':
        plasmids_df.loc[i,'bacterial res'] = 'NaN'
        
for i, row in plasmids_df.iterrows():
    if '/' in str(plasmids_df.loc[i,'bacterial res']):
        x = plasmids_df.loc[i,'bacterial res'].find('/')
        first = plasmids_df.loc[i,'bacterial res'][:x]
        second = plasmids_df.loc[i,'bacterial res'][x+1:]
        
        plasmids_df.loc[i,'bacterial res'] = first
        plasmids_df.loc[i,'bacterial res2'] = second
        
for i, row in plasmids_df.iterrows():
    if ' ' in str(plasmids_df.loc[i,'bacterial res']):
        x = plasmids_df.loc[i,'bacterial res'].find(' ')
        first = plasmids_df.loc[i,'bacterial res'][:x]
        second = plasmids_df.loc[i,'bacterial res'][x+1:]
        
        plasmids_df.loc[i,'bacterial res'] = first
        plasmids_df.loc[i,'bacterial res2'] = second
        

plasmids_df['col'] = plasmids_df['col'].astype(int)

plasmids_df['loc'] = plasmids_df['row'] + plasmids_df['col'].astype(str)


#location of resistance in tube rack

for i, row in plasmids_df.iterrows():
    if plasmids_df.loc[i,'bacterial res'] == 'Amp':
        plasmids_df.loc[i,'anti loc'] = 'A1'

        
for i, row in plasmids_df.iterrows():
    if plasmids_df.loc[i,'bacterial res'] == 'Kan':
        plasmids_df.loc[i,'anti loc'] = 'A2'

        
for i, row in plasmids_df.iterrows():
    if plasmids_df.loc[i,'bacterial res'] == 'Chl':
        plasmids_df.loc[i,'anti loc'] = 'A3'

        
for i, row in plasmids_df.iterrows():
    if plasmids_df.loc[i,'bacterial res'] == 'Tet':
        plasmids_df.loc[i,'anti loc'] = 'A4'
 
        
for i, row in plasmids_df.iterrows():
    if plasmids_df.loc[i,'bacterial res'] == 'Spec':
        plasmids_df.loc[i,'anti loc'] = 'A5'

        
for i, row in plasmids_df.iterrows():
    if plasmids_df.loc[i,'bacterial res'] == 'Gent':
        plasmids_df.loc[i,'anti loc'] = 'B1'

        
for i, row in plasmids_df.iterrows():
    if plasmids_df.loc[i,'bacterial res'] == 'Zeo':
        plasmids_df.loc[i,'anti loc'] = 'B2'
        
for i, row in plasmids_df.iterrows():
    if plasmids_df.loc[i,'bacterial res'] == 'Carb':
        plasmids_df.loc[i,'anti loc'] = 'B3'
           

for i, row in plasmids_df.iterrows():
    if plasmids_df.loc[i,'bacterial res2'] == 'Chl':
        plasmids_df.loc[i,'anti loc2'] = 'A3'


for i, row in plasmids_df.iterrows():
    if plasmids_df.loc[i,'bacterial res2'] == 'Kan':
        plasmids_df.loc[i,'anti loc2'] = 'A2'

for i, row in plasmids_df.iterrows():
    if plasmids_df.loc[i,'bacterial res2'] == 'Gent':
        plasmids_df.loc[i,'anti loc2'] = 'B1'



plasmids_df['num of res'] = ''

for i, rows in plasmids_df.iterrows():
    if (pd.isna(plasmids_df.loc[i,'bacterial res']) == True) & (pd.isna(plasmids_df.loc[i,'bacterial res2']) == True):
        plasmids_df.loc[i,'num of res'] = 0
    elif (pd.isna(plasmids_df.loc[i,'bacterial res']) == False) & (pd.isna(plasmids_df.loc[i,'bacterial res2']) == True):
        plasmids_df.loc[i,'num of res'] = 1
    else:
        plasmids_df.loc[i,'num of res'] = 2

value = [[50,1000]]
overnight_df = pd.DataFrame(data=value,columns = ['inoc(uL)','totalvol(uL)'])

dilution_df = pd.read_csv("resistance gene reccomendations.csv")
dilution_df['dispense vol(uL)'] = 20
dilution_df['total overnight vol(uL)'] = int(overnight_df['totalvol(uL)'])
dilution_df['Rec amount(ug)'] = dilution_df['Rec Conc(ug/uL)'] * dilution_df['total overnight vol(uL)']
dilution_df['dispense conc(ug/uL)'] = dilution_df['Rec amount(ug)'] / dilution_df['dispense vol(uL)']
dilution_df['volume of stock(mL)'] = 5
dilution_df['amount of anti powder(mg)'] = dilution_df['dispense conc(ug/uL)'] * dilution_df['volume of stock(mL)']

overnight_df['anti(uL)'] = dilution_df['dispense vol(uL)']
overnight_df['media-to-add(uL)'] = overnight_df['totalvol(uL)'] - overnight_df['anti(uL)']- overnight_df['inoc(uL)']


for i, row in dilution_df.iterrows():
    if (dilution_df.loc[i,'amount of anti powder(mg)']) < 5:
        dilution_df.loc[i,'volume of stock(mL)'] = 100
        dilution_df.loc[i,'amount of anti powder(mg)'] = dilution_df.loc[i,'dispense conc(ug/uL)'] * dilution_df.loc[i,'volume of stock(mL)']


## Meta Data

metadata = {'protocolName': 'Plate Replication',
'author':'Mason Kellinger masonkellinger@vt.edu',
 'description':'Plate Replication',
 'apiLevel': '2.9'
}



tiprack1 = protocol.load_labware("opentrons_96_tiprack_300ul",1)
tiprack3 = protocol.load_labware("opentrons_96_tiprack_300ul",3)
tiprack4 = protocol.load_labware("opentrons_96_tiprack_300ul",6)
tiprack5 = protocol.load_labware("opentrons_96_tiprack_300ul",11)
tiprack2 = protocol.load_labware("opentrons_96_tiprack_1000ul",2)

pipette_left = protocol.load_instrument('p300_single','left',tip_racks = [tiprack1,tiprack3,tiprack4,tiprack5])
pipette_right = protocol.load_instrument('p1000_single_gen2','right',tip_racks = [tiprack2])

deepwell1 = protocol.load_labware('nest_96_wellplate_2ml_deep',4)
deepwell2 = protocol.load_labware('nest_96_wellplate_2ml_deep',7)
deepwell3 = protocol.load_labware('nest_96_wellplate_2ml_deep',5)  # 1->3 2->4
deepwell4 = protocol.load_labware('nest_96_wellplate_2ml_deep',8)
media_res = protocol.load_labware('agilent_1_reservoir_290ml',9)

anti_tubes = protocol.load_labware('opentrons_15_tuberack_falcon_15ml_conical',10)


pipette_right.pick_up_tip()
for i, rows in plasmids_df.iterrows():
    if plasmids_df.loc[i,'plate'] == 1:
        
          #for each cell in deepwell aspirate and dispense correct amount of media
        pipette_right.aspirate(volume = int(overnight_df['media-to-add(uL)']),location = media_res['A1'],rate = 2)
        pipette_right.dispense(int(overnight_df['media-to-add(uL)']),deepwell3[plasmids_df.loc[i].at['loc']],2)
        pipette_right.blow_out()
        
pipette_right.drop_tip()
        
for i, rows in plasmids_df.iterrows():
    if plasmids_df.loc[i,'plate'] == 1:
        
        if plasmids_df.loc[i,'bacterial res'] == 'Amp':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['A1'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell3[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
        
        if plasmids_df.loc[i,'bacterial res'] == 'Kan':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['A2'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell3[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res'] == 'Chl':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['A3'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell3[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res'] == 'Tet':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['A4'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell3[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res'] == 'Spec':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['A5'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell3[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res'] == 'Gent':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['B1'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell3[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res'] == 'Zeo':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['B2'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell3[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res'] == 'Carb':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['B3'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell3[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if pd.isna(plasmids_df.loc[i,'bacterial res']) == True:
            pass      
                
                
        if plasmids_df.loc[i,'bacterial res2'] == 'Chl':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['A3'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell3[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res2'] == 'Kan':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['A2'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell3[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res2'] == 'Gent':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['B1'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell3[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
for i, rows in plasmids_df.iterrows():
    if plasmids_df.loc[i,'plate'] == 1:
                
        pipette_left.pick_up_tip()
        pipette_left.aspirate(int(overnight_df['inoc(uL)']),deepwell1[plasmids_df.loc[i].at['loc']],2)
        pipette_left.dispense(int(overnight_df['inoc(uL)']),deepwell3[plasmids_df.loc[i].at['loc']],2)
        pipette_left.blow_out()
        pipette_left.drop_tip()


pipette_right.pick_up_tip()
for i, rows in plasmids_df.iterrows():
    if plasmids_df.loc[i,'plate'] == 2:
        
        pipette_right.aspirate(volume = int(overnight_df['media-to-add(uL)']),location = media_res['A1'],rate = 2)
        pipette_right.dispense(int(overnight_df['media-to-add(uL)']),deepwell3[plasmids_df.loc[i].at['loc']],2)
        pipette_right.blow_out()
        
pipette_right.drop_tip()
        
for i, rows in plasmids_df.iterrows():
    if plasmids_df.loc[i,'plate'] == 2:
        
        if plasmids_df.loc[i,'bacterial res'] == 'Amp':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['A1'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell4[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
        
        if plasmids_df.loc[i,'bacterial res'] == 'Kan':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['A2'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell4[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res'] == 'Chl':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['A3'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell4[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res'] == 'Tet':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['A4'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell4[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res'] == 'Spec':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['A5'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell4[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res'] == 'Gent':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['B1'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell4[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res'] == 'Zeo':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['B2'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell4[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res'] == 'Carb':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['B3'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell4[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if pd.isna(plasmids_df.loc[i,'bacterial res']) == True:
            pass      
                
                
        if plasmids_df.loc[i,'bacterial res2'] == 'Chl':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['A3'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell4[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res2'] == 'Kan':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['A2'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell4[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                
        if plasmids_df.loc[i,'bacterial res2'] == 'Gent':
            pipette_left.pick_up_tip()
            pipette_left.aspirate(int(overnight_df['anti(uL)']),anti_tubes['B1'])
            pipette_left.dispense(int(overnight_df['anti(uL)']),deepwell4[plasmids_df.loc[i].at['loc']],2)
            pipette_left.blow_out()
            pipette_left.drop_tip()
                         
pipette_left.reset_tipracks()
protocol.pause("replace tiprack in position 1")

for i, rows in plasmids_df.iterrows():
    if plasmids_df.loc[i,'plate'] == 2:
                
        pipette_left.pick_up_tip()
        pipette_left.aspirate(int(overnight_df['inoc(uL)']),deepwell2[plasmids_df.loc[i].at['loc']],2)
        pipette_left.dispense(int(overnight_df['inoc(uL)']),deepwell4[plasmids_df.loc[i].at['loc']],2)
        pipette_left.blow_out()
        pipette_left.drop_tip()
              


