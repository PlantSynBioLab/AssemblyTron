metadata= {'protocolName': 'Pipette cleaning + plate cleaning',
'author':'Sriya Sridhar ',
'description':'Pipette cleaning for 1000ul tips',
'apiLevel':'2.2'
}
from opentrons import protocol_api
from opentrons import simulate
#protocol = simulate.get_protocol_api('2.2')

import pandas
import numpy as np
import os
#import tkinter as tk

#from tkinter import * 
#window = Tk()
#window.geometry("400x100")
# window.title("Tip well count")

# entry = Entry(window)
# entry.pack()

# def confirm():
#     label = Label(window,text = entry.get())
#     label.pack()
#     global Wellcount
#     Wellcount = entry.get()

#     window.destroy()
# button = Button(window,text="Enter number of pipette boxes to clean, from 1 to 4",command = confirm)
# button.pack()
# window.mainloop()

#example change

# Wellcount = int(Wellcount)
Wellcount=1
id2well = {}
id2well[0] = 'A1'
id2well[1] = 'A2'
id2well[2] = 'A3'
id2well[3] = 'A4'
id2well[4] = 'A5'
id2well[5] = 'A6'
id2well[6] = 'A7'
id2well[7] = 'A8'
id2well[8] = 'A9'
id2well[9] = 'A10'
id2well[10] = 'A11'
id2well[11] = 'A12'
id2well[12] = 'B1'
id2well[13] = 'B2'
id2well[14] = 'B3'
id2well[15] = 'B4'
id2well[16] = 'B5'
id2well[17] = 'B6'
id2well[18] = 'B7'
id2well[19] = 'B8'
id2well[20] = 'B9'
id2well[21] = 'B10'
id2well[22] = 'B11'
id2well[23] = 'B12'
id2well[24] = 'C1'
id2well[25] = 'C2'
id2well[26] = 'C3'
id2well[27] = 'C4'
id2well[28] = 'C5'
id2well[29] = 'C6'
id2well[30] = 'C7'
id2well[31] = 'C8'
id2well[32] = 'C9'
id2well[33] = 'C10'
id2well[34] = 'C11'
id2well[35] = 'C12'
id2well[36] = 'D1'
id2well[37] = 'D2'
id2well[38] = 'D3'
id2well[39] = 'D4'
id2well[40] = 'D5'
id2well[41] = 'D6'
id2well[42] = 'D7'
id2well[43] = 'D8'
id2well[44] = 'D9'
id2well[45] = 'D10'
id2well[46] = 'D11'
id2well[47] = 'D12'
id2well[48] = 'E1'
id2well[49] = 'E2'
id2well[50] = 'E3'
id2well[51] = 'E4'
id2well[52] = 'E5'
id2well[53] = 'E6'
id2well[54] = 'E7'
id2well[55] = 'E8'
id2well[56] = 'E9'
id2well[57] = 'E10'
id2well[58] = 'E11'
id2well[59] = 'E12'
id2well[60] = 'F1'
id2well[61] = 'F2'
id2well[62] = 'F3'
id2well[63] = 'F4'
id2well[64] = 'F5'
id2well[65] = 'F6'
id2well[66] = 'F7'
id2well[67] = 'F8'
id2well[68] = 'F9'
id2well[69] = 'F10'
id2well[70] = 'F11'
id2well[71] = 'F12'
id2well[72] = 'G1'
id2well[73] = 'G2'
id2well[74] = 'G3'
id2well[75] = 'G4'
id2well[76] = 'G5'
id2well[77] = 'G6'
id2well[78] = 'G7'
id2well[79] = 'G8'
id2well[80] = 'G9'
id2well[81] = 'G10'
id2well[82] = 'G11'
id2well[83] = 'G12'
id2well[84] = 'H1'
id2well[85] = 'H2'
id2well[86] = 'H3'
id2well[87] = 'H4'
id2well[88] = 'H5'
id2well[89] = 'H6'
id2well[90] = 'H7'
id2well[91] = 'H8'
id2well[92] = 'H9'
id2well[93] = 'H10'
id2well[94] = 'H11'
id2well[95] = 'H12'


def run(protocol: protocol_api.ProtocolContext):

    #from opentrons import simulate
    #protocol= simulate.get_protocol_api('2.0')
    right_pipette = protocol.load_instrument('p300_single','right')
    solutionrack = protocol.load_labware('opentrons_10_tuberack_nest_4x50ml_6x15ml_conical',3)#verify location
    plate = protocol.load_labware('nest_96_wellplate_200ul_flat',2)

    if Wellcount ==1:
        dirtytiprack = protocol.load_labware('opentrons_96_tiprack_300ul',1)
        cleantiprack = protocol.load_labware('opentrons_96_tiprack_300ul',5)
        r=0
        while r < 96:
        #cleaning the tip 
            right_pipette.pick_up_tip(dirtytiprack[id2well[r]])
            right_pipette.move_to(solutionrack['B4'].top())
            right_pipette.blow_out()
            right_pipette.mix(3,300,solutionrack['B4'])
            right_pipette.move_to(solutionrack['B4'].top())
            right_pipette.blow_out()
            right_pipette.mix(3,300,solutionrack['A4'])
            right_pipette.move_to(solutionrack['A4'].top()) #I think this lifts the tip out of the water
            right_pipette.blow_out()

        #cleaning the plate

            right_pipette.aspirate (280, solutionrack['B4']) #picking up bleach
            right_pipette.dispense(280, plate[id2well[r]])
            right_pipette.mix(3,270,plate[id2well[r]])
            right_pipette.aspirate(290, plate[id2well[r]])
            right_pipette.dispense(300, solutionrack['A1']) #get rid of used bleach in a waste tube
            
            right_pipette.aspirate (280, solutionrack['A4']) #picking up water to rinse
            right_pipette.dispense(280, plate[id2well[r]])
            right_pipette.mix(3,270,plate[id2well[r]])
            right_pipette.aspirate(280, plate[id2well[r]])
            right_pipette.dispense(300, solutionrack['A1']) #get rid of used water in a waste tube

        #cleaning the tip again

            right_pipette.move_to(solutionrack['B4'].top())
            right_pipette.blow_out()
            right_pipette.mix(3,300,solutionrack['B4'])
            right_pipette.move_to(solutionrack['B4'].top())
            right_pipette.blow_out()
            right_pipette.mix(3,300,solutionrack['A4'])
            right_pipette.move_to(solutionrack['A4'].top()) #I think this lifts the tip out of the water
            right_pipette.blow_out()

            right_pipette.drop_tip(cleantiprack[id2well[r]])

            r += 1

    # if Wellcount > 1:
    #     tiprack2 = protocol.load_labware('opentrons_96_tiprack_10ul',2)
    #     x=0
    #     while x < 96:
    #         right_pipette.pick_up_tip(tiprack6[id2well[x]])  
    #         right_pipette.mix(3,10,solutionrack['B4'])
    #         right_pipette.blow_out()
    #         right_pipette.return_tip()
    #         x += 1

    # if Wellcount > 2:
    #     tiprack3 = protocol.load_labware('opentrons_96_tiprack_10ul',4)  
    #     y=0
    #     while y < 96:
    #         right_pipette.pick_up_tip(tiprack3[id2well[y]])  
    #         right_pipette.mix(3,10,solutionrack['B4'])
    #         right_pipette.blow_out()
    #         right_pipette.return_tip()
    #         y += 1

    # if Wellcount > 3:
    #     tiprack4 = protocol.load_labware('opentrons_96_tiprack_10ul',6)  
    #     z=0
    #     while z < 96:
    #         right_pipette.pick_up_tip(tiprack4[id2well[z]])  
    #         right_pipette.mix(3,10,solutionrack['B4'])
    #         right_pipette.blow_out()
    #         right_pipette.return_tip()
    #         z += 1

    # if Wellcount > 4:
        
        