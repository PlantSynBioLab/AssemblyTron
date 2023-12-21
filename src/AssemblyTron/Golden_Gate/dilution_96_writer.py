'''A writer script that creates a Dilution Script in OpenTrons API for up to 96 primers and templates when there are no digested entry plasmids included in the design. 

This script contains a protocol for diluting up to 96 primers and templates to concentrations specified in the AssemblyTron.Golden_Gate.Setup_nodigests_seppcr_gradient_96 module. 

This script generates a text file that runs on the OT-2 via the run app. It calls CSVs to make a customized protocol script. This script is designed to run on a personal computer on the command line.

'''
if __name__ == '__main__':
    import pandas
    import numpy as np
    import os

    def write_dilution():



        def main():

            Input_values = pandas.read_csv('Input.csv') 
            Date = str(int(Input_values.loc[0].at['Date']))
            Date
            Time = str(int(Input_values.loc[0].at['Time']))
            Time
            os.chdir(Date+Time+'_GoldenGate')
            oligos = pandas.read_csv('oligo.csv')
            assembly = pandas.read_csv('assembly.csv')
            pcr = pandas.read_csv('pcr.csv')
            combinations = pandas.read_csv('combinations.csv')
            df = pandas.read_csv('templates.csv')
            section =pandas.read_csv('section.csv')

            f = open('GG_dilutions.py','w+')
            f.write(
                "from opentrons import protocol_api \r\n"
                "metadata = { \r\n"
                "    'protocolName': '96 well dilution script for Golden Gate assembly', \r\n"
                "    'author': 'John Bryant <jbryant2@vt.edu>', \r\n"
                "    'description': 'Dilute primers and templates (up to 96 combined)', \r\n"
                "    'apiLevel': '2.10' \r\n"
                "    } \r\n"

                "def run(protocol: protocol_api.ProtocolContext): \r\n"

                "#DECK DEFINITIONS############################################################################################### \r\n"
                "    tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', '9') \r\n"
                "    tiprack3 = protocol.load_labware('opentrons_96_tiprack_10ul', '6') \r\n"
                "    deckslot4 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','4') \r\n"
                "    deckslot5 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','5') \r\n"
                "    deckslot1 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','1') \r\n"
                "    deckslot2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','2') \r\n"
                "    plate96 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', '3') \r\n"
                "    watertuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', '8') \r\n"

                "    right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1]) \r\n"
                "    left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3]) \r\n"
            )

            x = 'Dilution'
            if x in section['parts'].values:

                #add water for templates
                f.write(
                    "    right_pipette.pick_up_tip() \r\n"
                )
                for i, row in df.iterrows():
                    if df.loc[i].at['water to add'] > 8:
                        f.write(
                            "    right_pipette.aspirate("+str(df.loc[i].at['water to add'])+", watertuberack['A1'], rate=1.0) \r\n"
                            "    right_pipette.dispense("+str(df.loc[i].at['water to add'])+", plate96['"+str(df.loc[i].at['template_well'])+"'], rate=1.0) \r\n"
                        )
                    if df.loc[i].at['water to add'] < 8:
                        f.write(
                            "    right_pipette.aspirate("+str(3*df.loc[i].at['water to add'])+", watertuberack['A1'], rate=1.0) \r\n"
                            "    right_pipette.dispense("+str(3*df.loc[i].at['water to add'])+", plate96['"+str(df.loc[i].at['template_well'])+"'], rate=1.0) \r\n"
                        )
                
                #add water to primer dilution tubes
                for i, row in oligos.iterrows():
                    f.write(
                        "    right_pipette.aspirate("+str(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'])+", watertuberack['A1'], rate=1.0) \r\n"
                        "    right_pipette.dispense("+str(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'])+", plate96['"+str(oligos.loc[i].at['96well'])+"'], rate=1.0) \r\n"
                    )
                f.write(
                    "    right_pipette.drop_tip() \r\n"
                )

                #add stock templates to dilution tubes
                for i, row in df.iterrows():
                    if df.loc[i].at['water to add'] > 8:
                        f.write(
                            "    left_pipette.pick_up_tip() \r\n"
                            "    left_pipette.aspirate("+str(df.loc[i].at['amount of template to add'])+", "+str(df.loc[i].at['rack'])+"['"+str(df.loc[i].at['template_origin'])+"'], rate=1.0) \r\n"
                            "    left_pipette.dispense("+str(df.loc[i].at['amount of template to add'])+", plate96['"+str(df.loc[i].at['template_well'])+"'], rate=1.0) \r\n"
                            "    left_pipette.mix(3,5,plate96['"+str(df.loc[i].at['template_well'])+"']) \r\n"
                            "    left_pipette.drop_tip() \r\n"
                        )
                    if df.loc[i].at['water to add'] < 8:
                        f.write(
                            "    left_pipette.pick_up_tip() \r\n"
                            "    left_pipette.aspirate("+str(3*(df.loc[i].at['amount of template to add']))+", "+str(df.loc[i].at['rack'])+"['"+str(df.loc[i].at['template_origin'])+"'], rate=1.0) \r\n"
                            "    left_pipette.dispense("+str(3*(df.loc[i].at['amount of template to add']))+", plate96['"+str(df.loc[i].at['template_well'])+"'], rate=1.0) \r\n"
                            "    left_pipette.mix(3,5,plate96['"+str(df.loc[i].at['template_well'])+"']) \r\n"
                            "    left_pipette.drop_tip() \r\n"
                        )

                #add stock primers to dilution tube
                for i, row in oligos.iterrows():
                    f.write(
                        "    left_pipette.pick_up_tip() \r\n"
                        "    left_pipette.aspirate("+str(oligos.loc[i].at['volume of stock primer to add'])+", "+str(oligos.loc[i].at['rack'])+"['"+str(oligos.loc[i].at['24well'])+"'], rate=1.0) \r\n"
                        "    left_pipette.dispense("+str(oligos.loc[i].at['volume of stock primer to add'])+", plate96['"+str(oligos.loc[i].at['96well'])+"'], rate=1.0) \r\n"
                        "    left_pipette.mix(3,5,plate96['"+str(oligos.loc[i].at['96well'])+"']) \r\n"
                        "    left_pipette.drop_tip() \r\n"
                    )

                #mix contents with pipette tip (reps, max volume, location) for templates and primers
                for i, row in df.iterrows():
                    if df.loc[i].at['water to add'] > 8:
                        f.write(
                            "    right_pipette.pick_up_tip() \r\n"
                            "    right_pipette.mix(3,"+str(df.loc[i].at['water to add'])+",plate96['"+str(df.loc[i].at['template_well'])+"']) \r\n"
                            "    right_pipette.drop_tip() \r\n"
                        )
                    if df.loc[i].at['water to add'] < 8:
                        f.write(
                            "    right_pipette.pick_up_tip() \r\n"
                            "    right_pipette.mix(3,"+str(3*(df.loc[i].at['water to add']))+",plate96['"+str(df.loc[i].at['template_well'])+"']) \r\n"
                            "    right_pipette.drop_tip() \r\n"
                        )

                for i, row in oligos.iterrows():
                    f.write(
                        "    right_pipette.pick_up_tip() \r\n"
                        "    right_pipette.mix(3,"+str(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'])+",plate96['"+str(oligos.loc[i].at['96well'])+"']) \r\n"
                        "    right_pipette.drop_tip() \r\n"
                    )

                f.write(
                    "    protocol.pause('Take all stock primers and templates out. Add Q5 to D6, BsaI to D5, and cutsmart to D4. Then proceed') \r\n"
                )

            f.close()

        main()

        os.system("notepad.exe GG_dilutions.py")