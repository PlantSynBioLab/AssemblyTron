''' A writer script for generating a Homology Dependent Assembly Protocol Script with separate PCRs in OpenTrons API.

This script allows users to perform Homology dependent assembly where fragments for each assembly are amplified in separate tubes and uses a gradient thermocycler. This protocol is thoroughly validated and robust, so we recommend using it. 

This script generates a text file that runs on the OT-2 via the run app. It calls CSVs to make a customized protocol script. This script is designed to run on a personal computer on the command line.

'''
if __name__ == '__main__':
    import pandas
    import numpy as np
    import os
    from os.path import exists

    # paths = pandas.read_csv('/data/user_storage/robotpaths.csv')
    # paths
    def write_pcr():

        def main():

            Input_values = pandas.read_csv('Input.csv') 
            Date = str(int(Input_values.loc[0].at['Date']))
            Time = str(int(Input_values.loc[0].at['Time']))

            Q5 = (0.5*Input_values.loc[0].at['pcrvol'])
            diltemp = (Input_values.loc[0].at['templatengs'])*(Input_values.loc[0].at['pcrvol'])/1
            DMSO = (0.03*Input_values.loc[0].at['pcrvol'])

            #os.chdir(paths.loc[0].at['opentrons_repo']+'/Cloning/'+Date+Time+'_IVA')
            # os.getcwd()
            oligos = pandas.read_csv('oligo.csv')
            gradient = pandas.read_csv('gradient.csv')
            pcr = pandas.read_csv('pcr.csv')
            assembly = pandas.read_csv('assembly.csv')
            combinations = pandas.read_csv('combinations.csv')
            Length = pcr.nlargest(1,'Length')
            GG_dfs = pandas.read_csv('GG_dfs.csv')
            section = pandas.read_csv('section.csv')

            low_annealing_temp = pcr.nsmallest(1,'Mean Oligo Tm (3 only)').reset_index()
            high_annealing_temp = pcr.nlargest(1,'Mean Oligo Tm (3 only)').reset_index()

            delta = (float(high_annealing_temp.loc[0].at['Mean Oligo Tm (3 only)']) - float(low_annealing_temp.loc[0].at['Mean Oligo Tm (3 only)']))/34

                
            if exists('gg1.csv'):
                gg1 = pandas.read_csv('gg1.csv')
            if exists('gg2.csv'):
                gg2 = pandas.read_csv('gg2.csv')
            if exists('gg3.csv'):
                gg3 = pandas.read_csv('gg3.csv')
            if exists('gg4.csv'):
                gg4 = pandas.read_csv('gg4.csv')
            if exists('gg5.csv'):
                gg5 = pandas.read_csv('gg5.csv')
            if exists('gg6.csv'):
                gg6 = pandas.read_csv('gg6.csv')
            if exists('gg7.csv'):
                gg7 = pandas.read_csv('gg7.csv')
            if exists('gg8.csv'):
                gg8 = pandas.read_csv('gg8.csv')
            if exists('gg9.csv'):
                gg9 = pandas.read_csv('gg9.csv')
            if exists('gg10.csv'):
                gg10 = pandas.read_csv('gg10.csv')
            if exists('gg11.csv'):
                gg11 = pandas.read_csv('gg11.csv')
            if exists('gg12.csv'):
                gg12 = pandas.read_csv('gg12.csv')

            if '96well' in pcr.columns:
                pcr = pcr.rename(columns={"96well": "well", "96well2": "well2"})
                rackchanger = 'Y'
            else:
                rackchanger = 'N'

            f = open('IVA.py','w+')
            f.write(
                "from opentrons import protocol_api \r\n"
                "metadata = { \r\n"
                "    'protocolName': 'Golden Gate', \r\n"
                "    'author': 'John Bryant <jbryant2@vt.edu>', \r\n"
                "    'description': 'Protocol for performing PCR reactions and Plasmid assembly', \r\n"
                "    'apiLevel': '2.10' \r\n"
                "    } \r\n"
                "def run(protocol: protocol_api.ProtocolContext): \r\n"

                "    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', '9') \r\n"
                "    tiprack3 = protocol.load_labware('opentrons_96_tiprack_10ul', '5') \r\n"
                "    watertuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical','3') \r\n"
            )
            if rackchanger == 'Y':
                f.write(
                    "    tuberack2 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul','2') \r\n"
                )
            else:
                f.write(
                    "    tuberack2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','2') \r\n"
                )
            f.write(
                "    secondarydils = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul','4') \r\n"
                "    tc_mod = protocol.load_module('Thermocycler Module') \r\n"
                "    pcrplate = tc_mod.load_labware('nest_96_wellplate_100ul_pcr_full_skirt') \r\n"
                "    temp_module = protocol.load_module('temperature module', 1) \r\n"
                "    cold_tuberack = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', label='Temperature-Controlled Tubes') \r\n"
                "    temp_module.set_temperature(4) \r\n"
                "    tc_mod.open_lid() \r\n"

                "    right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1]) \r\n"
                "    left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3]) \r\n"
            )

            x = 'PCR Mix'
            if x in section['parts'].values:

                #add water first
                for j, row in pcr.iterrows():
                    f.write(
                        "    right_pipette.pick_up_tip() \r\n"
                        "    right_pipette.aspirate("+str(pcr.loc[j].at['total_water_toadd'])+", watertuberack['A1'], rate=2.0) \r\n"
                        "    right_pipette.dispense("+str(pcr.loc[j].at['total_water_toadd'])+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                        "    right_pipette.blow_out() \r\n"
                        "    right_pipette.drop_tip() \r\n"
                    )

                for j, row in pcr.iterrows():
                    f.write(
                        "    left_pipette.pick_up_tip() \r\n"
                        "    left_pipette.aspirate("+str(pcr.loc[j].at['primervol_x'])+", tuberack2['"+str(pcr.loc[j].at['well'])+"'], rate=2.0) \r\n"
                        "    left_pipette.dispense("+str(pcr.loc[j].at['primervol_x'])+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                        "    left_pipette.mix(3,2,pcrplate['"+str(pcr.loc[j].at['tube'])+"']) \r\n"
                        "    left_pipette.drop_tip() \r\n"

                        "    left_pipette.pick_up_tip() \r\n"
                        "    left_pipette.aspirate("+str(pcr.loc[j].at['primervol_y'])+", tuberack2['"+str(pcr.loc[j].at['well2'])+"'], rate=2.0) \r\n"
                        "    left_pipette.dispense("+str(pcr.loc[j].at['primervol_y'])+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                        "    left_pipette.mix(3,2,pcrplate['"+str(pcr.loc[j].at['tube'])+"']) \r\n"
                        "    left_pipette.drop_tip() \r\n"
                    )

                #add 1uL of each template
                for j, row in pcr.iterrows():
                    f.write(
                        "    left_pipette.pick_up_tip() \r\n"
                    )
                    if rackchanger == 'Y':
                        f.write(
                            "    left_pipette.aspirate("+str(DMSO)+", tuberack2['H12'], rate=2.0) \r\n"
                        )
                    else:
                        f.write(
                            "    left_pipette.aspirate("+str(DMSO)+", tuberack2['D6'], rate=2.0) \r\n"
                        )
                    f.write(
                        "    left_pipette.dispense("+str(DMSO)+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                        "    left_pipette.blow_out() \r\n"
                        "    left_pipette.drop_tip() \r\n"
                    )

                #add Q5 to each reaction
                #keep Q5 in tuberack1['D6']                                            
                for j, row in pcr.iterrows():
                    f.write(
                        "    right_pipette.pick_up_tip() \r\n"
                        "    right_pipette.aspirate("+str(Q5)+", cold_tuberack['D6'], rate=2.0) \r\n"
                        "    right_pipette.dispense("+str(Q5)+", pcrplate['"+str(pcr.loc[j].at['tube'])+"'], rate=2.0) \r\n"
                        "    right_pipette.mix(3,"+str(Q5+3)+",pcrplate['"+str(pcr.loc[j].at['tube'])+"']) \r\n"
                        "    right_pipette.blow_out() \r\n"
                        "    right_pipette.drop_tip() \r\n"
                    )

                
                if Input_values.loc[0].at['Combinatorial_pcr_params'] == 2:
                    f.write(
                        "    tc_mod.deactivate() \r\n"
                        "    temp_module.deactivate() \r\n"
                        "    protocol.pause('move to gradient thermocycler. set gradiet to be between "+str(gradient.loc[0].at['temp'])+" and "+str(gradient.loc[7].at['temp'])+". Extension time should be "+str(float((Length['Length']/1000)*30))+" seconds. Follow normal parameters for everything else. A1 is cool, A8 is hot.') \r\n"
                        "    temp_module.set_temperature(4) \r\n"
                        "    tc_mod.set_block_temperature(4) \r\n"
                    )
                
                if Input_values.loc[0].at['Combinatorial_pcr_params'] == 1:
                    f.write(
                        "    tc_mod.close_lid() \r\n"
                        "    tc_mod.set_lid_temperature(temperature = 105) \r\n"
                        "    tc_mod.set_block_temperature(98, hold_time_seconds=30, block_max_volume=25) \r\n"
                    )
                    
                    cycle = 1
                    x = 0 
                    while cycle < 35:

                        f.write(
                            "    tc_mod.set_block_temperature(98, hold_time_seconds=10, block_max_volume=25) \r\n"
                            "    tc_mod.set_block_temperature("+str(float(low_annealing_temp.loc[0].at['Mean Oligo Tm (3 only)'])+x)+", hold_time_seconds=30, block_max_volume=25) \r\n"
                            "    tc_mod.set_block_temperature(72, hold_time_seconds="+str(float((Length['Length']/1000)*30))+", block_max_volume=25) \r\n"
                        )
                        cycle = cycle + 1
                        x = x + delta
                        print(cycle)
                        print(delta)

                    f.write(
                        "    tc_mod.set_block_temperature(72, hold_time_minutes=5, block_max_volume=25) \r\n"
                        "    tc_mod.set_block_temperature(4) \r\n"
                        "    tc_mod.set_lid_temperature(temperature = 45) \r\n"
                        "    protocol.pause('wait until ready to dispense assemblies') \r\n"
                        "    tc_mod.open_lid() \r\n"
                        "    protocol.pause('just take them out manually...') \r\n"
                    )
                
                
                
                # f.write(
                #     "    protocol.pause('take out enzymes before cold stuff shuts off. Also restock tip racks') \r\n"
                #     "    tc_mod.deactivate() \r\n"
                #     "    temp_module.deactivate() \r\n"
                #     "    protocol.pause('move to gradient thermocycler. set gradiet to be between "+str(gradient.loc[0].at['temp'])+" and "+str(gradient.loc[7].at['temp'])+". Extension time should be "+str(float((Length['Length']/1000)*30))+" seconds. Follow normal parameters for everything else. A1 is cool, A8 is hot.') \r\n"
                #     "    temp_module.set_temperature(4) \r\n"
                #     "    tc_mod.set_block_temperature(4) \r\n"
                # )

            t300=0
            t10 =0
            x = 'DPNI Digest'
            if x in section['parts'].values:
                tiprackposition = {}
                tiprackposition[0] = 'A1'
                tiprackposition[1] = 'A2'
                tiprackposition[2] = 'A3'
                tiprackposition[3] = 'A4'
                tiprackposition[4] = 'A5'
                tiprackposition[5] = 'A6'
                tiprackposition[6] = 'A7'
                tiprackposition[7] = 'A8'
                tiprackposition[8] = 'A9'
                tiprackposition[9] = 'A10'
                tiprackposition[10] = 'A11'
                tiprackposition[11] = 'A12'
                tiprackposition[12] = 'B1'
                tiprackposition[13] = 'B2'
                tiprackposition[14] = 'B3'
                tiprackposition[15] = 'B4'
                tiprackposition[16] = 'B5'
                tiprackposition[17] = 'B6'
                tiprackposition[18] = 'B7'
                tiprackposition[19] = 'B8'
                tiprackposition[20] = 'B9'
                tiprackposition[21] = 'B10'
                tiprackposition[22] = 'B11'
                tiprackposition[23] = 'B12'
                tiprackposition[24] = 'C1'
                tiprackposition[25] = 'C2'
                tiprackposition[26] = 'C3'
                tiprackposition[27] = 'C4'
                tiprackposition[28] = 'C5'
                tiprackposition[29] = 'C6'
                tiprackposition[30] = 'C7'
                tiprackposition[31] = 'C8'
                tiprackposition[32] = 'C9'
                tiprackposition[33] = 'C10'
                tiprackposition[34] = 'C11'
                tiprackposition[35] = 'C12'
                tiprackposition[36] = 'D1'
                tiprackposition[37] = 'D2'
                tiprackposition[38] = 'D3'
                tiprackposition[39] = 'D4'
                tiprackposition[40] = 'D5'
                tiprackposition[41] = 'D6'
                tiprackposition[42] = 'D7'
                tiprackposition[43] = 'D8'
                tiprackposition[44] = 'D9'
                tiprackposition[45] = 'D10'
                tiprackposition[46] = 'D11'
                tiprackposition[47] = 'D12'
                tiprackposition[48] = 'E1'
                tiprackposition[49] = 'E2'
                tiprackposition[50] = 'E3'
                tiprackposition[51] = 'E4'
                tiprackposition[52] = 'E5'
                tiprackposition[53] = 'E6'
                tiprackposition[54] = 'E7'
                tiprackposition[55] = 'E8'
                tiprackposition[56] = 'E9'
                tiprackposition[57] = 'E10'
                tiprackposition[58] = 'E11'
                tiprackposition[59] = 'E12'
                tiprackposition[60] = 'F1'
                tiprackposition[61] = 'F2'
                tiprackposition[62] = 'F3'
                tiprackposition[63] = 'F4'
                tiprackposition[64] = 'F5'
                tiprackposition[65] = 'F6'
                tiprackposition[66] = 'F7'
                tiprackposition[67] = 'F8'
                tiprackposition[68] = 'F9'
                tiprackposition[69] = 'F10'
                tiprackposition[70] = 'F11'
                tiprackposition[71] = 'F12'
                tiprackposition[72] = 'G1'
                tiprackposition[73] = 'G2'
                tiprackposition[74] = 'G3'
                tiprackposition[75] = 'G4'
                tiprackposition[76] = 'G5'
                tiprackposition[77] = 'G6'
                tiprackposition[78] = 'G7'
                tiprackposition[79] = 'G8'
                tiprackposition[80] = 'G9'
                tiprackposition[81] = 'G10'
                tiprackposition[82] = 'G11'
                tiprackposition[83] = 'G12'
                tiprackposition[84] = 'H1'
                tiprackposition[85] = 'H2'
                tiprackposition[86] = 'H3'
                tiprackposition[87] = 'H4'
                tiprackposition[88] = 'H5'
                tiprackposition[89] = 'H6'
                tiprackposition[90] = 'H7'
                tiprackposition[91] = 'H8'
                tiprackposition[92] = 'H9'
                tiprackposition[93] = 'H10'
                tiprackposition[94] = 'H11'
                tiprackposition[95] = 'H12'

                for i, row in pcr.iterrows():
                    f.write(
                        "    right_pipette.pick_up_tip(tiprack1['"+str(tiprackposition[t300])+"']) \r\n"
                        "    right_pipette.aspirate("+str(Input_values.loc[0].at['DPwater'])+", watertuberack['A1'], rate=2.0) \r\n"
                        "    right_pipette.dispense("+str(Input_values.loc[0].at['DPwater'])+", pcrplate['"+str(pcr.loc[i].at['tube'])+"'], rate=2.0) \r\n"
                        "    right_pipette.drop_tip() \r\n"
                    )
                    t300+=1

                for i, row in pcr.iterrows():
                    f.write(
                        "    left_pipette.pick_up_tip(tiprack3['"+str(tiprackposition[t10])+"']) \r\n"
                        "    left_pipette.aspirate("+str(Input_values.loc[0].at['cutsmart'])+", cold_tuberack['D4'], rate=2.0) \r\n"
                        "    left_pipette.dispense("+str(Input_values.loc[0].at['cutsmart'])+", pcrplate['"+str(pcr.loc[i].at['tube'])+"'], rate=2.0) \r\n"
                        "    left_pipette.drop_tip() \r\n"
                    )
                    t10+=1

                for i, row in pcr.iterrows():
                    f.write(
                        "    left_pipette.pick_up_tip(tiprack3['"+str(tiprackposition[t10])+"']) \r\n"
                        "    left_pipette.aspirate("+str(Input_values.loc[0].at['DPNI'])+", cold_tuberack['D3'], rate=2.0) \r\n"
                        "    left_pipette.dispense("+str(Input_values.loc[0].at['DPNI'])+", pcrplate['"+str(pcr.loc[i].at['tube'])+"'], rate=2.0) \r\n"
                        "    left_pipette.mix(3,10,pcrplate['"+str(pcr.loc[i].at['tube'])+"']) \r\n"
                        "    left_pipette.drop_tip() \r\n"
                    )
                    t10+=1

                f.write(
                    "    temp_module.deactivate() \r\n"
                    "    tc_mod.close_lid() \r\n"
                    "    tc_mod.set_lid_temperature(105) \r\n"
                    "    tc_mod.set_block_temperature(37,0,60, block_max_volume = 50) \r\n"
                    "    tc_mod.set_block_temperature(80,0,20, block_max_volume = 50) \r\n"
                    "    tc_mod.set_block_temperature(4, block_max_volume = 50) \r\n"
                    "    tc_mod.open_lid() \r\n"
                    "    protocol.pause('REFILL BOTH TIP RACKS, move 96 well block to deckslot 4, setting tube configuration the same as the Gradient arrangement') \r\n"
                    "    temp_module.set_temperature(4) \r\n"
                )

            t300=0
            t10=0
            x = 'Combine Fragments'
            if x in section['parts'].values:
                
                for i, row in GG_dfs.iterrows():
                    x = GG_dfs.loc[i].at['gg#']
                
                    #add all fragments to the assembly tube
                    for i, row in locals()[x].iterrows():
                        f.write(
                            "    right_pipette.pick_up_tip(tiprack1['"+str(tiprackposition[t300])+"']) \r\n"
                            "    right_pipette.aspirate(50, pcrplate['"+str(locals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    right_pipette.dispense(50, secondarydils['"+str(locals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                            "    right_pipette.blow_out() \r\n"
                            "    right_pipette.drop_tip() \r\n"
                        )
                        t300+=1

                f.write(
                    "    protocol.pause('clear thermocycler tubes and arrange the final assembly tubes according to the reaction_setup file') \r\n"
                )

                for i, row in GG_dfs.iterrows():
                    x = GG_dfs.loc[i].at['gg#']

                    for i, row in locals()[x].iterrows():
                        if locals()[x].loc[i].at['final amount to add'] < 10:
                            f.write(
                                "    left_pipette.pick_up_tip(tiprack3['"+str(tiprackposition[t10])+"']) \r\n"
                                "    left_pipette.aspirate("+str(locals()[x].loc[i].at['final amount to add'])+", secondarydils['"+str(locals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                                "    left_pipette.dispense("+str(locals()[x].loc[i].at['final amount to add'])+", pcrplate['"+str(locals()[x].loc[i].at['location_of_assembly'])+"']) \r\n"
                                "    left_pipette.blow_out() \r\n"
                                "    left_pipette.drop_tip() \r\n"
                            )
                            t10+=1
                        else:
                            f.write(
                                "    right_pipette.pick_up_tip(tiprack1['"+str(tiprackposition[t300])+"']) \r\n"
                                "    right_pipette.aspirate("+str(locals()[x].loc[i].at['final amount to add'])+", secondarydils['"+str(locals()[x].loc[i].at['frag_loc'])+"']) \r\n"
                                "    right_pipette.dispense("+str(locals()[x].loc[i].at['final amount to add'])+", pcrplate['"+str(locals()[x].loc[i].at['location_of_assembly'])+"']) \r\n"
                                "    right_pipette.blow_out() \r\n"
                                "    right_pipette.drop_tip() \r\n"
                            )
                            t300+=1

            f.close()   
                
        # if __name__== "__main__":
        main()

        os.system("notepad.exe IVA.py") 
