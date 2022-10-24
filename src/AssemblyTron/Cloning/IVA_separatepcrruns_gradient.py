''' Homology Dependent Assembly Protocol Script with separate PCRs

This script performs Homology dependent assembly where fragments for each assembly are amplified in separate tubes and uses a gradient thermocycler. This protocol is thoroughly validated and robust, so we recommend using it. 

This script runs on the OT-2 via the run app. It calls CSVs which must be transferred to the OT-2 processor prior to running. This script is not designed to run a personal computer on the command line.

'''
if __name__ == '__main__':

    #variables:
    #primer dilutions:
    #stkprm = 100 #concentration of the stock primer you are adding
    #stkvol = 1 #the volume of stock primer you are adding
    #dilprm = 2.5 #this is the concentration in uM that you want your working dilution to be

    #pcr reaction
    # need to get this from the df##Numprimers = 4 #this is how many primers go in each pcr reaction.
    #primerconcentration = 0.1 #this is the concentration you want each primer to be in the pcr reaction
    #pcrvol = 25 #this is the total volume of your pcr reaction 
    #templatengs = .5 #this is the concentration of template you want in your pcr rxn in ng/uL

    #template dilutions tells you what the temps need to be diluted to initially so that you can just add 1 uL of template to the pcr:
    #need to fill in stock template values further down the script
    #diltemp = (templatengs)*(pcrvol)/1

    #total_volume = 25
    #Q5 = total_volume - (0.5*(total_volume)) #How much Q5 to add
    #DPNI = 1 #How much DPNI to add
    #DPwater = 19
    #cutsmart = 5

    #goldengate param inputs
    #ngdesired=100



    #first import information from the j5 spreadsheet in order to perform appropriate steps
    #import feather
    #import pyarrow.feather as ft
    import pandas
    import numpy as np
    import os
    #from datetime import date
    
    #for this to work you need to run the python script on the same day that you make the new directory
    #today = date.today()
    #starter_date = str(today.strftime('%Y%m%d'))
    #if folder was created on diff date:
    #starter_date = 'typedatehere'
    # pwd = str(os.getcwd())

    # def walk_up_folder(path, depth=1):
    #     _cur_depth = 1        
    #     while _cur_depth < depth:
    #         path = os.path.dirname(path)
    #         _cur_depth += 1
    #     return path   

    paths = pandas.read_csv('/data/user_storage/robotpaths.csv')
    paths



    #Input_values = pandas.read_csv('Input.csv') 
    Input_values = pandas.read_csv(paths.loc[0].at['opentrons_repo']+'/Cloning/Input.csv') 
    # Input_values
    Date = str(int(Input_values.loc[0].at['Date']))
    Time = str(int(Input_values.loc[0].at['Time']))

    # Date

    Q5 = (0.5*Input_values.loc[0].at['pcrvol'])
    diltemp = (Input_values.loc[0].at['templatengs'])*(Input_values.loc[0].at['pcrvol'])/1
    DMSO = (0.03*Input_values.loc[0].at['pcrvol'])

    os.chdir(paths.loc[0].at['opentrons_repo']+'/Cloning/'+Date+Time+'_IVA')
    # os.getcwd()
    oligos = pandas.read_csv('oligo.csv')
    # oligos

    gradient = pandas.read_csv('gradient.csv')
    # oligos['ID Number'] = oligos['ID Number'].astype(int)
    # oligos

    # if len(oligos.columns) < 9:
    #     oligos['well'] = ''
    #     oligos['stock primer concentration'] = ''
    #     oligos['volume of stock primer to add'] = ''
    #     oligos['concentration of diluted primer'] = ''
    #     oligos['volume of diluted primer'] = '' #this is a calculated value
    #     oligos['how much of the diluted primer is left'] = '' #also a calculated value
    # oligos

    # #custom 4x6 well plate dictionary. hardcoded specifically for the labware used. 
    # #this could easily be replace with another well specification dictionary

    # id2well = {}
    # id2well['0'] = 'A1'
    # id2well['1'] = 'A2'
    # id2well['2'] = 'A3'
    # id2well['3'] = 'A4'
    # id2well['4'] = 'A5'
    # id2well['5'] = 'A6'
    # id2well['6'] = 'B1'
    # id2well['7'] = 'B2'
    # id2well['8'] = 'B3'
    # id2well['9'] = 'B4'
    # id2well['10'] = 'B5'
    # id2well['11'] = 'B6'
    # id2well['12'] = 'C1'
    # id2well['13'] = 'C2'
    # id2well['14'] = 'C3'
    # id2well['15'] = 'C4'
    # id2well['16'] = 'C5'
    # id2well['17'] = 'C6'
    # id2well['18'] = 'D1'
    # id2well['19'] = 'D2'
    # id2well['20'] = 'D3'
    # id2well['21'] = 'D4'
    # id2well['22'] = 'D5'
    # id2well['23'] = 'D6'

    pcr = pandas.read_csv('pcr.csv')
    # id2pcrrr = pcr.set_index('Reaction ID Number').to_dict()['tube']

    # #id2pcrrr = {}
    # #id2pcrrr['0'] = 'B2'
    # #id2pcrrr['1'] = 'B3'
    # #id2pcrrr['2'] = 'B4'
    # #id2pcrrr['3'] = 'B5'
    # #id2pcrrr['4'] = 'B6'
    # #id2pcrrr['5'] = 'B7'
    # #id2pcrrr['6'] = 'B8'
    # #id2pcrrr['7'] = 'B9'
    # # id2pcrrr['8'] = 'B10'
    # # id2pcrrr['9'] = 'B11'
    # # id2pcrrr['10'] = 'C2'
    # # id2pcrrr['11'] = 'C3'
    # # id2pcrrr['12'] = 'C4'
    # # id2pcrrr['13'] = 'C5'
    # # id2pcrrr['14'] = 'C6'
    # # id2pcrrr['15'] = 'C7'
    # # id2pcrrr['16'] = 'C8'
    # # id2pcrrr['17'] = 'C9'
    # # id2pcrrr['18'] = 'C10'
    # # id2pcrrr['19'] = 'C11'
    # # id2pcrrr['20'] = 'D2'
    # # id2pcrrr['21'] = 'D3'
    # # id2pcrrr['22'] = 'D4'
    # # id2pcrrr['23'] = 'D5'


    # for i, row in oligos.iterrows():
    #     oligos.loc[i,'well'] = id2well[str(i)] #this only works because the index matces the id number. id number is a floating value
    #     oligos.loc[i,'stock primer concentration'] = Input_values.loc[0].at['stkprm']
    #     oligos.loc[i,'volume of stock primer to add'] = Input_values.loc[0].at['stkvol']
    #     oligos.loc[i,'concentration of diluted primer'] = Input_values.loc[0].at['dilprm']

        
    # for i, row in oligos.iterrows():
    #     oligos.loc[i,'volume of diluted primer'] = row['stock primer concentration']*row['volume of stock primer to add']/row['concentration of diluted primer']
        

    # oligos['amount primer to add to frag amplification'] = Input_values.loc[0].at['pcrvol']*Input_values.loc[0].at['primerconc']/oligos['concentration of diluted primer']
    # oligos

    # oligos.to_csv('output_'+Date+'_oligo_IVA.csv')

    ###################################################################################################################################################################################
    #assembly

    #read in assembly pieces as dataframe .... might not need this info
    #os.chdir("C:/Users/jonbr/Documents/GitHub/opentrons/Golden_Gate/Part1_PCR_Mason/")
    assembly = pandas.read_csv('assembly.csv')
    # assembly

    # # for i, row in assembly.iterrows():
    # #     assembly.loc[i,'pcr_frag_tube'] = id2pcrrr[i]
    # # assembly

    # sub = 0
    # for i, row in assembly.iterrows():
    #     if assembly.loc[i,'Reaction Type'] == 'PCR':
    #         assembly.loc[i,'pcr_frag_tube'] = id2pcrrr[i-sub]
    #     else:
    #         assembly.loc[i,'pcr_frag_tube'] = np.nan
    #         sub = sub + 1
    # assembly

    # assembly.to_csv('output_'+Date+'_assembly_IVA.csv')

    ##############################################################################################################################################################################################
    #digests

    # #os.chdir("C:/Users/jonbr/Documents/GitHub/opentrons/Golden_Gate/Part1_PCR_Mason/")
    # os.getcwd()
    # digests = pandas.read_csv('digests.csv')
    # digests
    # #digest_conc=138 #automate digest concentration entry with inputs.py
    # digest_conc = Input_values.loc[0].at['concdigesttemp']
    # digests['digest_conc']=digest_conc
    # digests
    # startnum = len(oligos['well'])
    # for i, row in digests.iterrows():
    #     digests.loc[i,'well'] = id2well[str(startnum+ i)]
    # digests

    # next_startnum = startnum+len(digests['well'])
    # digests

    # for i, row in digests.iterrows():
    #     digests.loc[i,'amount of template to add'] = 1


    # for i, row in digests.iterrows():
    
    #         digests.loc[i,'concentration of template (ng/uL)'] = diltemp

    # digests['volume of dilute template prepared'] = digests['digest_conc']*Input_values.loc[0].at['stkvol']/digests['concentration of template (ng/uL)']

    # digests['water to add']= digests['volume of dilute template prepared']-digests['amount of template to add']
    # digests

    # for i, row in digests.iterrows():
    #     digests.loc[i,'frag_pcr_tube'] = id2well[str(i)]
    # digests

    # digests.to_csv('output_'+Date+'_digests_GoldenGate.csv')

    ##################################################################################################################################
    #pcr

    #os.chdir("C:/Users/jonbr/Documents/GitHub/opentrons/Golden_Gate/Part1_PCR_Mason/")
    # pcr = pandas.read_csv('pcr.csv')
    # pcr.columns = pcr.columns.str.replace("'","")
    # pcr

    # pcr[['Reaction ID Number','Forward Oligo ID Number','Reverse Oligo ID Number']] = pcr[['Reaction ID Number','Forward Oligo ID Number','Reverse Oligo ID Number']].astype(int)
    # pcr


    # #if bumpback > 0:
    # #    pcr.index = np.arange(1, len(pcr) + 1)
    # pcr

    # #here we create an object with each unique template from the
    # templates = pcr["Primary Template"]
    # unique_templates = templates.drop_duplicates(keep = 'first', inplace = False)
    # unique_templates

    # df = pandas.DataFrame(unique_templates)

    # df = df.reset_index()
    # df = df.drop('index', 1)

    # df['Template Concentration'] = ''
    # df

    # #enter template concentrations here
    # df['Template Concentration'] = Input_values['template concentrations'] #all you have to do is input the template concentrations in the right order

    # #df = df[df.line_race != 0]


    # startnum = len(oligos['well'])

    # for i, row in df.iterrows():
    #     df.loc[i,'template_well'] = id2well[str(startnum+i)]
        


    # for i, row in df.iterrows():
    #     df.loc[i,'amount of template to add'] = 1


    # for i, row in df.iterrows():
    
    #         df.loc[i,'concentration of template (ng/uL)'] = diltemp

    # df['volume of dilute template prepared'] = df['Template Concentration']*Input_values.loc[0].at['stkvol']/df['concentration of template (ng/uL)']

    # df['water to add']= df['volume of dilute template prepared']-df['amount of template to add']


    # #df['volume of dilute template prepared'] = df['volume of dilute template prepared'].astype(float)
    # #df['concentration of template (ng/uL)'] = df['concentration of template (ng/uL)'].astype(float)
    # #df['amount of template to add'] = df['amount of template to add'].astype(float)

    # #df['water to add'] = df['water to add'].astype(int)
    # #df['concentration of template (ng/uL)'] = df['concentration of template (ng/uL)'].astype(int)
    # #df['volume of dilute template prepared'] = df['volume of dilute template prepared'].astype(int)
    # #df['amount of template to add'] = df['amount of template to add'].astype(int)

    # df['water to add'].astype(np.float32)
    # df['amount of template to add'].astype(np.float32)
    # df['concentration of template (ng/uL)'].astype(np.float32)
    # df['volume of dilute template prepared'].astype(np.float32)

    # #df['amount of template to add'] = pd.Series.astype(df['amount of template to add'], dtype=float)
    # #df['concentration of template (ng/uL)'] = pd.Series.astype(df['concentration of template (ng/uL)'], dtype=float)
    # #df['volume of dilute template prepared'] = pd.Series.astype(df['volume of dilute template prepared'], dtype=float,)
    # df

    # #if bumpback > 0:
    # #    df.index = np.arange(0+bumpback, len(df) + bumpback)
        
    # df
    # #df.to_csv('output_'+Date+'_templates_IVA.csv')

    # #df.dtypes

    # #this line of code integrates the template concentrations into the pcr df
    # pcr = pandas.merge(pcr,df,on='Primary Template')
    # pcr

    # if len(pcr.columns) == 17:

    #     for i, row in pcr.iterrows():
    
    #         pcr.loc[i,'concentration of template (ng/uL)'] = diltemp

    # pcr['volume of dilute template prepared'] = pcr['Template Concentration']*Input_values.loc[0].at['stkvol']/pcr['concentration of template (ng/uL)']

    # pcr

    # wellinfo = oligos[['ID Number','well']]
    # wellinfo

    # wellinfo = wellinfo.rename(columns={'ID Number':'Forward Oligo ID Number'})
    # pcr = pcr.merge(wellinfo, on= 'Forward Oligo ID Number')
    # wellinfo = wellinfo.rename(columns={'Forward Oligo ID Number':'Reverse Oligo ID Number','well':'well2'})
    # pcr = pcr.merge(wellinfo, on= 'Reverse Oligo ID Number')
    # pcr

    # pcr['total_water_toadd'] = Input_values.loc[0].at['pcrvol']-Q5-DMSO-1-1-1
    # pcr

    # #pcrstart  = len(digests['well'])
    # for i, row in pcr.iterrows():
    #     pcr.loc[i,'frag_pcr_tube'] = id2pcrrr[i]
    # pcr

    # prvol = pandas.DataFrame()
    # prvol['well'] = oligos['well']
    # prvol['primervol'] = '' 
    # prvol['primervol'] = oligos['amount primer to add to frag amplification']
    # pcr = pcr.merge(prvol, on='well')
    # prvol = prvol.rename(columns={'well':'well2'})
    # pcr = pcr.merge(prvol, on='well2')
    # pcr

    # pcr.to_csv('output_'+Date+'_pcr_GoldenGate.csv')

    #######################################################################################################################################################################################################################
    #combinations

    #os.chdir("C:/Users/jonbr/Documents/GitHub/opentrons/Golden_Gate/Part1_PCR_Mason/")

    combinations = pandas.read_csv('combinations.csv')
    # combinations

    # if Input_values.loc[0].at['Combinatorial_pcr_params'] == 1:
    #     pieces = [columns for columns in combinations if columns.startswith('Assembly Piece ID Number Bin ')]
    #     frame = combinations[pieces]
    #     #frame2 = frame.transpose()
    #     frame

    #     if str(frame.loc[0].at['Assembly Piece ID Number Bin 0']) == 'nan':
    #         del frame['Assembly Piece ID Number Bin 0']
    #     if str(frame.loc[0].at['Assembly Piece ID Number Bin 1']) == 'nan':
    #         del frame['Assembly Piece ID Number Bin 1']
    #     if str(frame.loc[0].at['Assembly Piece ID Number Bin 2']) == 'nan':
    #         del frame['Assembly Piece ID Number Bin 2']
    #     if str(frame.loc[0].at['Assembly Piece ID Number Bin 3']) == 'nan':
    #         del frame['Assembly Piece ID Number Bin 3']
    #     if str(frame.loc[0].at['Assembly Piece ID Number Bin 4']) == 'nan':
    #         del frame['Assembly Piece ID Number Bin 4']
    #     frame2 = frame.transpose()
    #     frame

    #     frame += startnum
    #     frame
    #     frame= frame.values.astype(str)
    #     frame = pandas.DataFrame(frame)
    #     frame
    #     result_1 = frame.replace(id2well)
    #     result_1

    #     combinations_plustemplocs = pandas.concat([combinations, result_1], axis=1)
    #     combinations_plustemplocs

    #     pieces = [columns for columns in combinations if columns.startswith('Assembly Piece ID Number Bin ')]
    #     frame = combinations[pieces]

    #     if str(frame.loc[0].at['Assembly Piece ID Number Bin 0']) == 'nan':
    #         del frame['Assembly Piece ID Number Bin 0']
    #     if str(frame.loc[0].at['Assembly Piece ID Number Bin 1']) == 'nan':
    #         del frame['Assembly Piece ID Number Bin 1']
    #     if str(frame.loc[0].at['Assembly Piece ID Number Bin 2']) == 'nan':
    #         del frame['Assembly Piece ID Number Bin 2']
    #     if str(frame.loc[0].at['Assembly Piece ID Number Bin 3']) == 'nan':
    #         del frame['Assembly Piece ID Number Bin 3']
    #     if str(frame.loc[0].at['Assembly Piece ID Number Bin 4']) == 'nan':
    #         del frame['Assembly Piece ID Number Bin 4']
    #     frame2 = frame.transpose()
    #     frame2

    # #need to remove the row of linearized fragments from the digest when calculating pcr parameters
    #     if assembly.loc[0].at['Reaction Type'] == 'Digest Linearized':
    #         frame2 = frame2.drop(frame2.index[0])
    #         frame2 -= 1
    #     frame2

    #     pcr_info = [columns for columns in pcr if columns.startswith('Mean Oligo Tm (3')]
    #     morepcr_info = [columns for columns in pcr if columns.startswith('Delta Oligo Tm (3')]
    #     anotherpcr_info = [columns for columns in pcr if columns.startswith('Length')]
    #     pcr_info = pcr_info + morepcr_info + anotherpcr_info
    #     pcr_info

    #     for column in frame2:
    #         listoffrags = frame2[column].to_list()
    #         listoffrags
        
    #         tablee = pcr[pcr_info]
    #         tablee = tablee.iloc[listoffrags, :]
        
    #         if column == 0:
    #             params0 = tablee.copy()
    #         if column == 1:
    #             params1 = tablee.copy()
    #         if column == 2:
    #             params2 = tablee.copy()
    #         if column == 3:
    #             params3 = tablee.copy()
    #         if column == 4:
    #             params4 = tablee.copy()
    #         if column == 5:
    #             params5 = tablee.copy()
    #         if column == 6:
    #             params6 = tablee.copy()
    #         if column == 7:
    #             params7 = tablee.copy()
    #         if column == 8:
    #             params8 = tablee.copy()
    #         if column == 9:
    #             params9 = tablee.copy()
    #         if column == 10:
    #             params10 = tablee.copy()
    #         if column == 11:
    #             params11 = tablee.copy()

            
    #     params0

    # #so looks like this script will be limited for finding pcr conditions for just 2 construct. have to update for more


    #     if len(combinations['ID Number']) == 1:
    #         Lengthparams0 = params0.nlargest(1,'Length')
    #         Lengthparams0['Length'] = (Lengthparams0['Length']/1000)*30
    #         lengthlist = Lengthparams0['Length'].to_list()
    #         finallengthlist = lengthlist

    #         params_tables = {'parmx': ['params0']}
    #         params_tables = pandas.DataFrame(data=params_tables)
    #         params_tables

    #         GG_dfs = {'gg#': ['gg1']}
    #         GG_dfs = pandas.DataFrame(data=GG_dfs)

    #     if len(combinations['ID Number']) == 2:
    #         Lengthparams0 = params0.nlargest(1,'Length')
    #         Lengthparams0['Length'] = (Lengthparams0['Length']/1000)*30
    #         lengthlist = Lengthparams0['Length'].to_list()

    #         Lengthparams1 = params1.nlargest(1,'Length')
    #         Lengthparams1['Length'] = (Lengthparams1['Length']/1000)*30
    #         lengthlist1 = Lengthparams1['Length'].to_list()
    #         finallengthlist = lengthlist + lengthlist1 

    #         params_tables = {'parmx': ['params0','params1']}
    #         params_tables = pandas.DataFrame(data=params_tables)
    #         params_tables

    #         GG_dfs = {'gg#': ['gg1','gg2']}
    #         GG_dfs = pandas.DataFrame(data=GG_dfs)

    #     if len(combinations['ID Number']) == 3:
    #         Lengthparams0 = params0.nlargest(1,'Length')
    #         Lengthparams0['Length'] = (Lengthparams0['Length']/1000)*30
    #         lengthlist = Lengthparams0['Length'].to_list()

    #         Lengthparams1 = params1.nlargest(1,'Length')
    #         Lengthparams1['Length'] = (Lengthparams1['Length']/1000)*30
    #         lengthlist1 = Lengthparams1['Length'].to_list()

    #         Lengthparams2 = params2.nlargest(1,'Length')
    #         Lengthparams2['Length'] = (Lengthparams2['Length']/1000)*30
    #         lengthlist2 = Lengthparams2['Length'].to_list()
    #         finallengthlist = lengthlist + lengthlist1 +lengthlist2

    #         params_tables = {'parmx': ['params0','params1','params2']}
    #         params_tables = pandas.DataFrame(data=params_tables)
    #         params_tables

    #         GG_dfs = {'gg#': ['gg1','gg2','gg3']}
    #         GG_dfs = pandas.DataFrame(data=GG_dfs)

    #     if len(combinations['ID Number']) == 4:
    #         Lengthparams0 = params0.nlargest(1,'Length')
    #         Lengthparams0['Length'] = (Lengthparams0['Length']/1000)*30
    #         lengthlist = Lengthparams0['Length'].to_list()

    #         Lengthparams1 = params1.nlargest(1,'Length')
    #         Lengthparams1['Length'] = (Lengthparams1['Length']/1000)*30
    #         lengthlist1 = Lengthparams1['Length'].to_list()

    #         Lengthparams2 = params2.nlargest(1,'Length')
    #         Lengthparams2['Length'] = (Lengthparams2['Length']/1000)*30
    #         lengthlist2 = Lengthparams2['Length'].to_list()

    #         Lengthparams3 = params3.nlargest(1,'Length')
    #         Lengthparams3['Length'] = (Lengthparams3['Length']/1000)*30
    #         lengthlist3 = Lengthparams3['Length'].to_list()
    #         finallengthlist = lengthlist + lengthlist1 +lengthlist2 + lengthlist3

    #         params_tables = {'parmx': ['params0','params1','params2','params3']}
    #         params_tables = pandas.DataFrame(data=params_tables)
    #         params_tables

    #         GG_dfs = {'gg#': ['gg1','gg2','gg3','gg4']}
    #         GG_dfs = pandas.DataFrame(data=GG_dfs)

    # #Lengthparams2 = params2.nlargest(1,'Length')
    # #   Lengthparams2['Length'] = (Lengthparams2['Length']/1000)*60
    #  #   lengthlist = Lengthparams2['Length'].to_list()
    #   #  print(lengthlist)

    # #Lengthparams3 = params0.nlargest(1,'Length')
    # #Lengthparams0['Length'] = (Lengthparams0['Length']/1000)*60
    # #lengthlist = Lengthparams0['Length'].to_list()
    # #print(lengthlist)

    # #Lengthparams0 = params0.nlargest(1,'Length')
    # #Lengthparams0['Length'] = (Lengthparams0['Length']/1000)*60
    # #lengthlist = Lengthparams0['Length'].to_list()
    # #print(lengthlist)



    #     combinations['Extension_time_sec'] = finallengthlist
    #     combinations

    #     extens = combinations.nlargest(1,'Extension_time_sec')
    #     extension_final = extens['Extension_time_sec']
    #     extension_final

    # #solved the problem of not being able to loop through multiple dataframes

    #     annealing=[]
    #     for i, row in params_tables.iterrows():
    #         x = params_tables.loc[i].at['parmx']
    # #locals()[x]
    #         locals()[x]['Upper_temp'] = locals()[x]['Mean Oligo Tm (3 Only)'] + locals()[x]['Delta Oligo Tm (3Only)']
    #         locals()[x]['Lower_temp'] = locals()[x]['Mean Oligo Tm (3 Only)'] - locals()[x]['Delta Oligo Tm (3Only)']
    #         HL = locals()[x].nsmallest(1,'Upper_temp').reset_index()#.values.tolist()
    #         HL = HL['Upper_temp'].values.tolist()
    #         LH = locals()[x].nlargest(1,'Lower_temp').reset_index()#.values.tolist()
    #         LH = LH['Lower_temp'].values.tolist()    
    #         if LH[0] > HL[0]:
    #             annealing_temp = (LH[0]+HL[0])/2 + ((LH[0]-HL[0])/3)
    #         if LH[0] < HL[0]:
    #             annealing_temp = HL[0]
    #         annealing.append(annealing_temp)

    # #dfff = np.array(annealing)
    #     dfff = pandas.DataFrame(annealing)
    #     dfff = dfff.sum(axis=1)
    #     avg_annealing = dfff.mean() 
    #     avg_annealing

    #     Annealing_and_extension = pandas.DataFrame({'Annealing temp': avg_annealing,
    #                    'extension time (seconds)': extension_final})
    #     Annealing_and_extension = Annealing_and_extension.reset_index()
    #     Annealing_and_extension = Annealing_and_extension.drop(columns = ['index'])
    #     Annealing_and_extension

    #     Annealing_and_extension.to_csv('output_'+Date+'_Annealing_extension.csv')

    # ######################separate pcrrxns####################################
    # ########################################################################
    # if Input_values.loc[0].at['Combinatorial_pcr_params'] == 2:
    #     gradient = pandas.read_csv('gradient.csv')
        
    #     # runnumber = 0

    #     # pcr
    #     # pcr['Upper_temp'] = pcr['Mean Oligo Tm (3 Only)'] + pcr['Delta Oligo Tm (3Only)']
    #     # pcr['Lower_temp'] = pcr['Mean Oligo Tm (3 Only)'] - pcr['Delta Oligo Tm (3Only)']
    #     # pcr

    #     # temps = pcr['Mean Oligo Tm (3 Only)'].values.tolist()
        
    #     # deltaa =  pcr.nsmallest(1,'Delta Oligo Tm (3Only)').reset_index()
    #     # delta_val = deltaa.loc[0].at['Delta Oligo Tm (3Only)'].tolist()
    #     # delta_temp = deltaa.loc[0].at['Mean Oligo Tm (3 Only)'].tolist()
        
    #     # U = delta_temp + delta_val
    #     # L = delta_temp - delta_val

    #     # redo = 1
        
    #     # while redo == 1:

    #     #     current = 0
    #     #     CV = 0

    #     #     num = 100000
    #     #     for x in range(num):    
        
    #     #         #temps = [59.499,65.4245,67.8095,62.142,62.7575]
    #     #         #temps

    #     #         one = np.random.uniform(50,70)
    #     #         #one = round(numpy.random.uniform(50, 70), 1)
    #     #         eight = np.random.uniform(70,90)
    #     #         #eight = round(numpy.random.uniform(70, 90), 1)

    #     #         two = one +((2-1)/(8-1)) * (eight-one)
    #     #         three = one +((3-1)/(8-1)) * (eight-one)
    #     #         four = one +((4-1)/(8-1)) * (eight-one)
    #     #         five = one +((5-1)/(8-1)) * (eight-one)
    #     #         six = one +((6-1)/(8-1)) * (eight-one)
    #     #         seven = one +((7-1)/(8-1)) * (eight-one)

    #     #         vector = [one,two,three,four,five,six,seven,eight]

    #     #         f = []
    #     #         i = 0
    #     #         while i < len(vector):
    #     #             j = 0
    #     #             while j < len(temps):
    #     #                 Diff = abs(vector[i]-temps[j])
    #     #                 if Diff > 0.4:
    #     #                     f.append(100.0)
    #     #                 if Diff < 0.4:
    #     #                     f.append(Diff)
    #     #                 j = j + 1
    #     #             i = i + 1
    #     #         sum(f)
        
    #     #         #if sum(f) < 3505.0 & :
            
    #     #         if current == 0:
            
    #     #             current = sum(f)
    #     #             CV = vector
        
    #     #         else:
    #     #             if sum(f) < current:
    #     #                 current = sum(f)
    #     #                 CV = vector
                
    #     #     #find upper and lower for lowest range rxn
    #     #     #lowest delta -> upper and lower -> check temps
    #     #     #U = 65.6955
    #     #     #L = 65.1535

    #     #     i = 0
    #     #     while i < len(CV):
    #     #         if L<CV[i]<U:
    #     #             print('good')
    #     #             redo = 2
    #     #             break
    #     #         else:
    #     #             redo = 1
    #     #             print(redo)
    #     #         i = i + 1
        


    #     # gradient = pandas.DataFrame(CV, columns=['temp'])
    #     # wells = ['A1','A2','A3','A4','A5','A6','A7','A8']
    #     # gradient['tube'] = wells
        
    #     # for i, row in pcr.iterrows():
    #     #     diffss = []
    #     #     for j, row in gradient.iterrows():
    #     #         aaa = pcr.loc[i].at['Mean Oligo Tm (3 Only)']
    #     #         bbb = gradient.loc[j].at['temp']
    #     #         A = abs(aaa - bbb )
    #     #         diffss.append(A)
    #     #     min_val = min(diffss)
    #     #     min_index = diffss.index(min_val)
    #     #     pcr.loc[i,'tube'] = gradient.loc[min_index].at['tube']
    #     # pcr

    #     # dupin = {}
    #     # dupin['A1'] = 'B1'
    #     # dupin['A2'] = 'B2'
    #     # dupin['A3'] = 'B3'
    #     # dupin['A4'] = 'B4'
    #     # dupin['A5'] = 'B5'
    #     # dupin['A6'] = 'B6'
    #     # dupin['A7'] = 'B7'
    #     # dupin['A8'] = 'B8'

    #     # duplicate_in_tube = pcr.duplicated(subset=['tube'])
    #     # if duplicate_in_tube.any():
    #     #     tes = pcr.loc[duplicate_in_tube]
    #     #     index = tes.index
    #     # index
    #     # i = 0
    #     # while i < len(index):
    #     #     letter = pcr.loc[index[i]].at['tube']
    #     #     pcr.loc[index[i],'tube'] = dupin[letter]
    #     #     i = i + 1
    #     # pcr

    #     # gradient.to_csv('gradient.csv')




    # # multiple pcr run variation.
    #     # runnumber = 0
    #     # annealing = []
    #     # pcr['run'] = ''
    #     # for i, row in pcr.iterrows():
        
    #     #     comparison1 = pandas.DataFrame()
    #     #     comparison2 = pandas.DataFrame()
    #     #     comparison3 = pandas.DataFrame()
    #     #     comparison4 = pandas.DataFrame()
    #     #     comparison5 = pandas.DataFrame()
    #     #     comparison6 = pandas.DataFrame()   
                
    #     #     if i == 0:
    #     #         pcr.loc[i,'run'] = runnumber
    #     #         annealing_temp = pcr.loc[i].at['Upper_temp']
    #     #         annealing.append(annealing_temp)
                
    #     #     if i == 1:
    #     #         comparison1 = pcr.iloc[i-1,:]
    #     #         comparison2 = pcr.iloc[i,:] #last one is the row we're on and evaluatinh
                
    #     #         HL = comparison1['Upper_temp']
    #     #         LH = comparison1['Lower_temp']   
                
    #     #         HL2 = comparison2['Upper_temp']
    #     #         LH2 = comparison2['Lower_temp'] 
                    
    #     #         if LH2 < HL:
    #     #             annealing_temp = LH2
    #     #             pcr.loc[i,'run'] = pcr.loc[0,'run']
                    
    #     #         elif LH2 > HL:
    #     #             runnumber = runnumber + 1
    #     #             annealing_temp = LH2 #pcr.loc[i].at['Upper_temp']#(LH[0]+HL[0])/2 + ((LH[0]-HL[0])/3)
    #     #             pcr.loc[i,'run'] = runnumber
                
    #     #         annealing.append(annealing_temp)
                        
    #     #     if i == 2:
    #     #         comparison1 = pcr.iloc[i-2,:]
    #     #         comparison2 = pcr.iloc[i-1,:]
    #     #         comparison3 = pcr.iloc[i,:]
                        
    #     #         HL = comparison1['Upper_temp']
    #     #         LH = comparison1['Lower_temp']    
                
    #     #         HL2 = comparison2['Upper_temp']
    #     #         LH2 = comparison2['Lower_temp'] 
                        
    #     #         HL3 = comparison3['Upper_temp']
    #     #         LH3 = comparison3['Lower_temp'] 
                        
    #     #         if LH3 < HL:
    #     #             annealing_temp = LH3
    #     #             pcr.loc[i,'run'] = pcr.loc[0,'run']
                    
    #     #         elif LH3 < HL2:
    #     #             annealing_temp = LH3
    #     #             pcr.loc[i,'run'] = pcr.loc[1,'run'] 

    #     #         elif LH3 > HL and LH3 > HL2:
    #     #             runnumber = runnumber + 1
    #     #             annealing_temp = LH3 #(LH[0]+HL[0])/2 + ((LH[0]-HL[0])/3)
    #     #             pcr.loc[i,'run'] = runnumber
                
    #     #         annealing.append(annealing_temp)
                        
    #     #     if i == 3:
    #     #         comparison1 = pcr.iloc[i-3,:]
    #     #         comparison2 = pcr.iloc[i-2,:]
    #     #         comparison3 = pcr.iloc[i-1,:]
    #     #         comparison4 = pcr.iloc[i,:]
                    
    #     #         HL = comparison1['Upper_temp']
    #     #         LH = comparison1['Lower_temp']    
                
    #     #         HL2 = comparison2['Upper_temp']
    #     #         LH2 = comparison2['Lower_temp'] 
                
    #     #         HL3 = comparison3['Upper_temp']
    #     #         LH3 = comparison3['Lower_temp'] 
                
    #     #         HL4 = comparison4['Upper_temp']
    #     #         LH4 = comparison4['Lower_temp']
                        
    #     #         if LH4 < HL:
    #     #             annealing_temp = LH4
    #     #             pcr.loc[i,'run'] = pcr.loc[0,'run']
                    
    #     #         elif LH4 < HL2:
    #     #             annealing_temp = LH4
    #     #             pcr.loc[i,'run'] = pcr.loc[1,'run'] 
                    
    #     #         elif LH4 < HL3:
    #     #             annealing_temp = LH4
    #     #             pcr.loc[i,'run'] = pcr.loc[2,'run'] 

    #     #         elif LH4 > HL and LH4 > HL2 and LH4 > HL3:
    #     #             runnumber = runnumber + 1
    #     #             annealing_temp = LH4 #(LH[0]+HL[0])/2 + ((LH[0]-HL[0])/3)
    #     #             pcr.loc[i,'run'] = runnumber
            
    #     #         annealing.append(annealing_temp)
                        
    #     #     if i == 4:
    #     #         comparison1 = pcr.iloc[i-4,:]
    #     #         comparison2 = pcr.iloc[i-3,:]
    #     #         comparison3 = pcr.iloc[i-2,:]
    #     #         comparison4 = pcr.iloc[i-1,:]
    #     #         comparison5 = pcr.iloc[i,:]
                
    #     #         HL = comparison1['Upper_temp']
    #     #         LH = comparison1['Lower_temp']    
                
    #     #         HL2 = comparison2['Upper_temp']
    #     #         LH2 = comparison2['Lower_temp'] 
                    
    #     #         HL3 = comparison3['Upper_temp']
    #     #         LH3 = comparison3['Lower_temp'] 
                    
    #     #         HL4 = comparison4['Upper_temp']
    #     #         LH4 = comparison4['Lower_temp'] 
                    
    #     #         HL5 = comparison5['Upper_temp']
    #     #         LH5 = comparison5['Lower_temp'] 
                
    #     #         if LH5 < HL:
    #     #             annealing_temp = LH5
    #     #             pcr.loc[i,'run'] = pcr.loc[0,'run']
                
    #     #         elif LH5 < HL2:
    #     #             annealing_temp = LH5
    #     #             pcr.loc[i,'run'] = pcr.loc[1,'run']
                    
    #     #         elif LH5 < HL3:
    #     #             annealing_temp = LH5
    #     #             pcr.loc[i,'run'] = pcr.loc[2,'run'] 
                        
    #     #         elif LH5 < HL4:
    #     #             annealing_temp = LH5
    #     #             pcr.loc[i,'run'] = pcr.loc[3,'run'] 

    #     #         elif LH5 > HL and LH5 > HL2 and LH5 > HL3 and LH5 > HL4:
    #     #             runnumber = runnumber + 1
    #     #             annealing_temp = LH5 #(LH[0]+HL[0])/2 + ((LH[0]-HL[0])/3)
    #     #             pcr.loc[i,'run'] = runnumber
                
    #     #         annealing.append(annealing_temp)
                        
                        
    #     #     if i == 5:
    #     #         comparison1 = pcr.iloc[i-5,:]
    #     #         comparison1 = pcr.iloc[i-4,:]
    #     #         comparison2 = pcr.iloc[i-3,:]
    #     #         comparison3 = pcr.iloc[i-2,:]
    #     #         comparison4 = pcr.iloc[i-1,:]
    #     #         comparison5 = pcr.iloc[i,:]
                
    #     #         HL = comparison1['Upper_temp']
    #     #         LH = comparison1['Lower_temp']    
                
    #     #         HL2 = comparison2['Upper_temp']
    #     #         LH2 = comparison2['Lower_temp']    
                
    #     #         HL3 = comparison3['Upper_temp']
    #     #         LH3 = comparison3['Lower_temp'] 
                    
    #     #         HL4 = comparison4['Upper_temp']
    #     #         LH4 = comparison4['Lower_temp'] 
                
    #     #         HL5 = comparison5['Upper_temp']
    #     #         LH5 = comparison5['Lower_temp'] 
                    
    #     #         HL6 = comparison6['Upper_temp']
    #     #         LH6 = comparison6['Lower_temp'] 
                    
    #     #         if LH6 < HL:
    #     #             annealing_temp = LH6
    #     #             pcr.loc[i,'run'] = pcr.loc[0,'run']
                    
    #     #         elif LH6 < HL2:
    #     #             annealing_temp = LH6
    #     #             pcr.loc[i,'run'] = pcr.loc[1,'run']
                    
    #     #         elif LH6 < HL3:
    #     #             annealing_temp = LH6
    #     #             pcr.loc[i,'run'] = pcr.loc[2,'run']
                    
    #     #         elif LH6 < HL4:
    #     #             annealing_temp = LH6
    #     #             pcr.loc[i,'run'] = pcr.loc[3,'run'] 
                        
    #     #         elif LH6 < HL5:
    #     #             annealing_temp = LH6
    #     #             pcr.loc[i,'run'] = pcr.loc[4,'run'] 

    #     #         elif LH6 > HL and LH6 > HL2 and LH6 > HL3 and LH6 > HL4 and LH6 > HL5:
    #     #             runnumber = runnumber + 1
    #     #             annealing_temp = LH6 #(LH[0]+HL[0])/2 + ((LH[0]-HL[0])/3)
    #     #             pcr.loc[i,'run'] = runnumber
                
    #     #         annealing.append(annealing_temp)
                    
    #     # pcr['annealing_temp'] = annealing  

    #     # rxn1 = pcr.copy()
    #     # rxn2 = pcr.copy()
    #     # rxn3 = pcr.copy()
    #     # rxn4 = pcr.copy()

    #     # for i, row in pcr.iterrows():
        
    #     #     if not pcr.loc[i].at['run'] == 0:
    #     #         rxn1.drop(i,axis=0,inplace=True)

    #     #     if not pcr.loc[i].at['run'] == 1:
    #     #         rxn2.drop(i,axis=0,inplace=True)

    #     #     if not pcr.loc[i,'run'] == 2:
    #     #         rxn3.drop(i,axis=0,inplace=True)
        
    #     #     if not pcr.loc[i,'run'] == 3:
    #     #         rxn4.drop(i,axis=0,inplace=True)
                
    #     # rxns_tables = {'rxn': ['rxn1']}
    #     # rxns_tables = pandas.DataFrame(data=rxns_tables)
    #     # v=0
        
    #     # if len(rxn2.index) >= 1:
    #     #     rxns_tables = {'rxn': ['rxn1','rxn2']}
    #     #     rxns_tables = pandas.DataFrame(data=rxns_tables)
    #     #     v=1
    #     # if len(rxn2.index) < 1:
    #     #     del rxn2    
    
    #     # if len(rxn3.index) >= 1:
    #     #     rxns_tables = {'rxn': ['rxn1','rxn2','rxn3']}
    #     #     rxns_tables = pandas.DataFrame(data=rxns_tables)
    #     #     v=2
    #     # if len(rxn3.index) < 1:
    #     #     del rxn3

    #     # if len(rxn4.index) >= 1:
    #     #     rxns_tables = {'rxn': ['rxn1','rxn2','rxn3','rxn4']}
    #     #     rxns_tables = pandas.DataFrame(data=rxns_tables) 
    #     #     v=3
    #     # if len(rxn4.index) < 1:
    #         # del rxn4
        
        
        
    #     #rxns_tables = {'rxn': ['rxn1','rxn2']}
    #     #rxns_tables = pandas.DataFrame(data=rxns_tables)
    #     # for i, row in rxns_tables.iterrows():
    #     #     x = rxns_tables.loc[i].at['rxn']
    Length = pcr.nlargest(1,'Length')
        
    #     #L = l.values.tolist()
    #     #L[0] 
    #     # if v==0:
    #     #     allrxns = rxn1
    #     # if v==1:
    #     #     allrxns = pandas.concat([rxn1, rxn2], axis=0)
    #     # if v==2:
    #     #     allrxns = pandas.concat([rxn1, rxn2,rxn3], axis=0)
    #     # if v==3:
    #     #     allrxns = pandas.concat([rxn1, rxn2,rxn3,rxn4], axis=0)
        
    #     # allrxnsimppart = allrxns.iloc[:,[28,30]]
        
        
    #     # pcr = pcr.merge(allrxnsimppart, on= 'run', how='right')
    #     # pcr = pcr.drop_duplicates(subset=['Reaction ID Number'])
    #     # pcr = pcr.reset_index()
    #     # pcr
    # #allrxnsimppart
    #     # id2hold = {}
    #     # id2hold['0'] = 'C1'
    #     # id2hold['1'] = 'C2'
    #     # id2hold['2'] = 'C3'
    #     # id2hold['3'] = 'C4'
    #     # id2hold['4'] = 'C5'
    #     # id2hold['5'] = 'C6'


    #     # for i, row in pcr.iterrows():
    #     #     pcr.loc[i,'holding_tube'] = id2hold[str(i)]
    #     # pcr
    #     # annealing_extension = pcr.iloc[:,[29,30,31]]
    #     # annealing_extension = annealing_extension.drop_duplicates()
    #     # annealing_extension = annealing_extension.reset_index()
    #     # annealing_extension
        
    #     combinations = pandas.read_csv('combinations.csv')
    #     combinations

    # #if Input_values.loc[0].at['Combinatorial_pcr_params'] == 'Y':
    #     pieces = [columns for columns in combinations if columns.startswith('Assembly Piece ID Number Bin ')]
    #     frame = combinations[pieces]
    # #frame2 = frame.transpose()
    #     frame
    #     if str(frame.loc[0].at['Assembly Piece ID Number Bin 0']) == 'nan':
    #         del frame['Assembly Piece ID Number Bin 0']
    #     if str(frame.loc[0].at['Assembly Piece ID Number Bin 1']) == 'nan':
    #         del frame['Assembly Piece ID Number Bin 1']
    #     if str(frame.loc[0].at['Assembly Piece ID Number Bin 2']) == 'nan':
    #         del frame['Assembly Piece ID Number Bin 2']
    #     if str(frame.loc[0].at['Assembly Piece ID Number Bin 3']) == 'nan':
    #         del frame['Assembly Piece ID Number Bin 3']
    #     if str(frame.loc[0].at['Assembly Piece ID Number Bin 4']) == 'nan':
    #         del frame['Assembly Piece ID Number Bin 4']
    #     partss = frame

    # #frame += startnum
    # #frame
    #     frame= frame.values.astype(str)
    #     frame = pandas.DataFrame(frame)
    #     frame
    #     result_1 = frame.replace(id2well)
    #     result_1

    #     combinations_plustemplocs = pandas.concat([combinations, result_1], axis=1)
    #     combinations_plustemplocs
    #     fragnumber = 0.5*(len(combinations.iloc[0,:])-3)
    # goldengs = len(combinations['ID Number'])
    # goldengs
    # if goldengs == 1:
    #     GG_dfs = {'gg#': ['gg1']}
    #     GG_dfs = pandas.DataFrame(data=GG_dfs)
    # if goldengs == 2:
    #     GG_dfs = {'gg#': ['gg1','gg2']}
    #     GG_dfs = pandas.DataFrame(data=GG_dfs)
    # if goldengs == 3:
    #     GG_dfs = {'gg#': ['gg1','gg2','gg3']}
    #     GG_dfs = pandas.DataFrame(data=GG_dfs)
    # if goldengs == 4:
    #     GG_dfs = {'gg#': ['gg1','gg2','gg3','gg4']}
    #     GG_dfs = pandas.DataFrame(data=GG_dfs)
        

    # ################################################################################################################################################
    # #continued combination processing to set up actual Golden Gate assembly dataframes

    # #os.chdir("C:/Users/jonbr/Documents/Github/opentrons/Golden_Gate/Part2_Assembly_Cam")
    # #os.getcwd()
    # #fragments = pandas.read_csv('fragments.csv')
    # #fragments

    # #put final goldengate assembly products on row C for good measure

    # id2wellpcr = {}
    # id2wellpcr['0'] = 'B2'
    # id2wellpcr['1'] = 'B3'
    # id2wellpcr['2'] = 'B4'
    # id2wellpcr['3'] = 'B5'
    # id2wellpcr['4'] = 'B6'
    # id2wellpcr['5'] = 'B7'
    # id2wellpcr['6'] = 'B8'
    # id2wellpcr['7'] = 'B9'
    # id2wellpcr['8'] = 'B10'
    # id2wellpcr['9'] = 'B11'
    # id2wellpcr['10'] = 'C2'
    # id2wellpcr['11'] = 'C3'
    # id2wellpcr['12'] = 'C4'
    # id2wellpcr['13'] = 'C5'


    # combinations
    # #add in the looping like in IVA here so that the GG loop will work

    # ID_tube = assembly[['Reaction ID Number','pcr_frag_tube']]

    # if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 0']) == 'nan':
    #     ID_tube = ID_tube.rename(columns={'Reaction ID Number':'Assembly Piece ID Number Bin 0'})
    #     combinations = combinations.merge(ID_tube, on= 'Assembly Piece ID Number Bin 0')
    #     combs_shor = [columns for columns in combinations if columns.startswith('pcr_frag_tube')]
    #     combs_short = combinations[combs_shor]
    #     #combs_short = combinations[['pcr_frag_tube']] #,'pcr_frag_tube_y','pcr_frag_tube'

    # if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 1']) == 'nan':
    #     ID_tube = ID_tube.rename(columns={'Assembly Piece ID Number Bin 0':'Assembly Piece ID Number Bin 1'})
    #     combinations = combinations.merge(ID_tube, on= 'Assembly Piece ID Number Bin 1')
    #     combs_shor = [columns for columns in combinations if columns.startswith('pcr_frag_tube')]
    #     combs_short = combinations[combs_shor]
    #     #combs_short = combinations[['pcr_frag_tube_x','pcr_frag_tube_y']] #,'pcr_frag_tube_y','pcr_frag_tube'

    # if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 2']) == 'nan':
    #     ID_tube = ID_tube.rename(columns={'Assembly Piece ID Number Bin 1':'Assembly Piece ID Number Bin 2'})
    #     combinations = combinations.merge(ID_tube, on= 'Assembly Piece ID Number Bin 2')
    #     combs_shor = [columns for columns in combinations if columns.startswith('pcr_frag_tube')]
    #     combs_short = combinations[combs_shor]
    #     #combs_short = combinations[['pcr_frag_tube_x','pcr_frag_tube_y','pcr_frag_tube']] #,'pcr_frag_tube_y','pcr_frag_tube'

    # if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 3']) == 'nan':
    #     ID_tube = ID_tube.rename(columns={'Assembly Piece ID Number Bin 2':'Assembly Piece ID Number Bin 3'})
    #     combinations = combinations.merge(ID_tube, on= 'Assembly Piece ID Number Bin 3')
    #     combs_shor = [columns for columns in combinations if columns.startswith('pcr_frag_tube')]
    #     combs_short = combinations[combs_shor]
    #     #combs_short = combinations[['pcr_frag_tube_x','pcr_frag_tube_y','pcr_frag_tube']] #,'pcr_frag_tube_y','pcr_frag_tube'
    # combs_short = combs_short.T.drop_duplicates().T

    # if not str(combinations.loc[0].at['Assembly Piece ID Number Bin 4']) == 'nan':
    #     ID_tube = ID_tube.rename(columns={'Assembly Piece ID Number Bin 3':'Assembly Piece ID Number Bin 4'})
    #     combinations = combinations.merge(ID_tube, on= 'Assembly Piece ID Number Bin 4')
    #     combs_shor = [columns for columns in combinations if columns.startswith('pcr_frag_tube')]
    #     combs_short = combinations[combs_shor]
    #     #combs_short = combinations[['pcr_frag_tube_x','pcr_frag_tube_y','pcr_frag_tube']] #,'pcr_frag_tube_y','pcr_frag_tube'
    # combs_short = combs_short.T.drop_duplicates().T



    # combs_short = combs_short.transpose()
    # combs_short

    # gg1 = pandas.DataFrame()
    # gg2 = pandas.DataFrame()
    # gg3 = pandas.DataFrame()
    # gg4 = pandas.DataFrame()

    # dil_tu = {}
    # dil_tu['A1'] = 'F1'
    # dil_tu['A2'] = 'F2'
    # dil_tu['A3'] = 'F3'
    # dil_tu['A4'] = 'F4'
    # dil_tu['A5'] = 'F5'
    # dil_tu['A6'] = 'F6'
    # dil_tu['A7'] = 'F7'
    # dil_tu['A8'] = 'F8'
    # dil_tu['B1'] = 'G1'
    # dil_tu['B2'] = 'G2'
    # dil_tu['B3'] = 'G3'
    # dil_tu['B4'] = 'G4'
    # dil_tu['B5'] = 'G5'
    # dil_tu['B6'] = 'G6'
    # dil_tu['B7'] = 'G7'
    # dil_tu['B8'] = 'G8'
    # dil_tu['C1'] = 'H1'
    # dil_tu['C2'] = 'H2'
    # dil_tu['C3'] = 'H3'
    # dil_tu['C4'] = 'H4'
    # dil_tu['C5'] = 'H5'
    # dil_tu['C6'] = 'H6'
    # dil_tu['C7'] = 'H7'
    # dil_tu['C8'] = 'H8'
    # dil_tu['D1'] = 'H2'
    # dil_tu['D2'] = 'H3'
    # dil_tu['D3'] = 'H4'
    # dil_tu['D4'] = 'H5'
    # dil_tu['D5'] = 'H6'
    # dil_tu['D6'] = 'H7'
    # dil_tu['D7'] = 'H8'
    # dil_tu['D8'] = 'H9'
    # dil_tu['E1'] = 'H3'
    # dil_tu['E2'] = 'H4'
    # dil_tu['E3'] = 'H5'
    # dil_tu['E4'] = 'H6'
    # dil_tu['E5'] = 'H7'
    # dil_tu['E6'] = 'H8'
    # dil_tu['E7'] = 'H9'
    # dil_tu['E8'] = 'H10'

    # #dil_tu['B7'] = 'C7'
    # #dil_tu['B8'] = 'C8'
    # #dil_tu['B9'] = 'C9'

    # e = len(combs_short.columns)

    # #next_tc_tube = len(assembly.index)
    # #changing next_tc_tube to 6 just to make room for a solid six fragment gradient every time
    # next_tc_tube = 6


        
    # for i, row in GG_dfs.iterrows():
    #     x = GG_dfs.loc[i].at['gg#']
    #     locals()[x] = combs_short[[i]]
    #     locals()[x].loc[:,'conc_assumed']= 60

    #     bps = assembly[['Sequence Length','pcr_frag_tube']]

    #     bps = bps.rename(columns={'pcr_frag_tube':i})
    #     locals()[x] = locals()[x].merge(bps, on= i)
        
    #     backbone_length=locals()[x]["Sequence Length"].max()
    #     backbone_length
            
    #     locals()[x] = locals()[x].rename(columns={0:'frag_loc',1:'frag_loc',2:'frag_loc',3:'frag_loc',4:'frag_loc',5:'frag_loc'})
        
    #        #for i, row in plasmid.iterrows():
    #        #     plasmid.loc[i,'final tube'] = pcr2final[str(i)]
            
            
    #     for i, row in locals()[x].iterrows():
    #         locals()[x].loc[i,'dil_tube'] = dil_tu[locals()[x].loc[i,'frag_loc']]

    #     for i, row in locals()[x].iterrows():
    #         locals()[x].loc[i, "final amount to add"] = 50/len(partss.columns)

    #         locals()[x].loc[i,'location_of_assembly'] = id2wellpcr[str(next_tc_tube)]
        
    #     next_tc_tube = next_tc_tube + 1

    # combinations.to_csv('output_'+Date+'_combinations.csv')

    # dt = {'dispense_tube': ['C3','C4','C5','C6']}
    # dis_tube = pandas.DataFrame(data=dt)

    #########################################################################################################################
    # #plasmid dataframe object for the digestion
    # plasmid = pandas.DataFrame()
    # plasmid['Plasmid'] = Input_values['pwldigesttemp']
    # plasmid['Concentration'] = Input_values['concdigesttemp']
    # #plasmid = pandas.DataFrame(plasmid)
    # plasmid

    # plasmid['Buffer'] = float('5')
    # plasmid['BSA1'] = float('1')
    # plasmid['Volume of Plasmid'] = ''
    # plasmid['Volume of Water'] = ''

    # plasmid['Volume of Plasmid'] = (1/(plasmid['Concentration'])) * 1000 * 1
    # plasmid['Volume of Water'] = 50- plasmid['Volume of Plasmid'] - plasmid['Buffer'] - plasmid['BSA1']

    # plasmid['total volume'] = float(50)


    # #plasmid templates arranged in an "L" formation
    # row2well= {}
    # row2well['0'] = 'A2'
    # row2well['1'] = 'B2'
    # row2well['2'] = 'C2'
    # row2well['3'] = 'D2'
    # row2well['4'] = 'D3'
    # row2well['5'] = 'D4'
    # row2well['6'] = 'D5'
    # row2well['7'] = 'D6'

    # plasmid['Plasmid Location'] = ''
    # plasmid

    # for i, row in plasmid.iterrows():
    #     plasmid.loc[i,'Plasmid Location'] = id2well[str(i+startnum)]
    # plasmid

    # pcr2final= {}
    # pcr2final['0'] = 'D6'
    # pcr2final['1'] = 'D5'
    # pcr2final['2'] = 'D4'
    # pcr2final['3'] = 'D3'
    # pcr2final['4'] = 'D2'
    # pcr2final['5'] = 'D1'
    # pcr2final['6'] = 'C6'
    # pcr2final['7'] = 'C5'
    # pcr2final['8'] = 'C4'

    # plasmid['final tube'] = ''

    # for i, row in plasmid.iterrows():
    #     plasmid.loc[i,'final tube'] = pcr2final[str(i)]
    # plasmid



    GG_dfs = pandas.read_csv('GG_dfs.csv')
        

    from os.path import exists
    if exists('gg1.csv'):
        gg1 = pandas.read_csv('gg1.csv')
    if exists('gg2.csv'):
        gg2 = pandas.read_csv('gg2.csv')
    if exists('gg3.csv'):
        gg3 = pandas.read_csv('gg3.csv')
    if exists('gg4.csv'):
        gg4 = pandas.read_csv('gg4.csv')



    if '96well' in pcr.columns:
        pcr = pcr.rename(columns={"96well": "well", "96well2": "well2"})
        rackchanger = 'Y'
    else:
        rackchanger = 'N'


    #########################################################################################################################################
    #########actual commands#############3

    from opentrons import protocol_api

    #Metadata is a dictionary of data that is read by the server and returned to the opentrons app. 
    #give yourself credit. you are required to specify the 'apiLevel' herefrom opentrons import protocol_api
    metadata = {
        'protocolName': 'IVA Separate PCRs',
        'author': 'John Bryant <jbryant2@vt.edu>',
        'description': 'Protocol for performing PCR reactions and Plasmid assembly for TIR1 and AFB mutants',
        'apiLevel': '2.10'
    }
    print(metadata)




    def run(protocol: protocol_api.ProtocolContext): #for actually running the script in the robot
    #will have to indent everything to be defined by the run function

    #from opentrons import simulate
    #protocol = simulate.get_protocol_api('2.2')
        
    #labware:
        tiprack1 = protocol.load_labware('opentrons_96_tiprack_300ul', '9')
        #tiprack2 = protocol.load_labware("opentrons_96_tiprack_10ul",'6')
        tiprack3 = protocol.load_labware("opentrons_96_tiprack_10ul", '5')
    #tuberack1 = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap','1') #holds stock primers and templates
        watertuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical','3') #holds molec bio grad H2O
        if rackchanger == 'Y':
            tuberack2 = protocol.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul','2')
        else:
            tuberack2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','2') # holds dilute primers and templates
        
        tc_mod = protocol.load_module('Thermocycler Module')
        pcrplate = tc_mod.load_labware('nest_96_wellplate_100ul_pcr_full_skirt')
        temp_module = protocol.load_module('temperature module', 1)
        cold_tuberack = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', label='Temperature-Controlled Tubes')
        temp_module.set_temperature(4)
        print(temp_module.temperature)
        tc_mod.open_lid()

    # #########Some notes:    
    # #specify the order of stock primers and template in tuberack1 here:
    # #good place to add the pop-up window
    # #A1-D3 = stock primers
    # #D4-D5 = stock templates
    # #stock tubes and dilution tubes need to be set up in the same order
    # #as of now Q5 is in 
        
    #pipettes
        right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1])
        left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3])


        
    ##################################COMMANDS####################################
        
    #add water to template dilution tubes. ***df is the template description dataframe
    #Since we are just moving water I will use the same pipette tip to save plastic

    #     x = 'Dilution'
    #     if x in Input_values['section'].values:

    # #add water for templates
    #         for i, row in df.iterrows():
    #             if df.loc[i].at['water to add'] > 10:
    #                 right_pipette.pick_up_tip()
    #                 right_pipette.aspirate(volume = df.loc[i].at['water to add'], location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
    #                 right_pipette.dispense(df.loc[i].at['water to add'], tuberack2[df.loc[i].at['template_well']], rate=2.0)
    #                 right_pipette.drop_tip()
    #             if 3.333 < df.loc[i].at['water to add'] < 10:
    #                 if 3*(df.loc[i].at['water to add']) < 10:
    #                     left_pipette.pick_up_tip()
    #                     left_pipette.aspirate(3*(df.loc[i].at['water to add']), location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
    #                     left_pipette.dispense(3*(df.loc[i].at['water to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0)
    #                     left_pipette.drop_tip()
    #                 else:
    #                     right_pipette.pick_up_tip()
    #                     right_pipette.aspirate(3*(df.loc[i].at['water to add']), location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
    #                     right_pipette.dispense(3*(df.loc[i].at['water to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0)
    #                     right_pipette.drop_tip()
    #             if 1 < df.loc[i].at['water to add'] < 3.333:
    #                 if 4*(df.loc[i].at['water to add']) < 10:
    #                     left_pipette.pick_up_tip()
    #                     left_pipette.aspirate(4*(df.loc[i].at['water to add']), location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
    #                     left_pipette.dispense(4*(df.loc[i].at['water to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0)
    #                     left_pipette.drop_tip()
    #                 else:
    #                     right_pipette.pick_up_tip()
    #                     right_pipette.aspirate(4*(df.loc[i].at['water to add']), location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
    #                     right_pipette.dispense(4*(df.loc[i].at['water to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0)
    #                     right_pipette.drop_tip()
    #             if df.loc[i].at['water to add'] < 1:
    #                 left_pipette.pick_up_tip()
    #                 left_pipette.aspirate(6*(df.loc[i].at['water to add']), location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
    #                 left_pipette.dispense(6*(df.loc[i].at['water to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0)
    #                 left_pipette.drop_tip()

    #             #right_pipette.blow_out()
        

    #     #add water to primer dilution tubes
    #         right_pipette.pick_up_tip()
    #         for i, row in oligos.iterrows():
    #             right_pipette.aspirate(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'], watertuberack['A1'], rate=2.0) #need to put 39uL of water into each dilution tube for primers,) #we need to find better way to loop through these commands
    #             right_pipette.dispense(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'], tuberack2[oligos.loc[i].at['well']], rate=2.0)
    #             #right_pipette.blow_out()
    #         right_pipette.drop_tip()    
            
    #     #add stock templates to dilution tubes
    #         for i, row in df.iterrows():
    #             if df.loc[i].at['water to add'] > 10:
    #                 left_pipette.pick_up_tip()
    #                 left_pipette.aspirate(df.loc[i].at['amount of template to add'], cold_tuberack[df.loc[i].at['template_well']], rate=2.0) #dilution well corresponds to stock well
    #                 left_pipette.dispense(df.loc[i].at['amount of template to add'], tuberack2[df.loc[i].at['template_well']], rate=2.0) #makes a 12.5ng/uL template
    #                 left_pipette.mix(3,5,tuberack2[df.loc[i].at['template_well']])
    #                 #left_pipette.blow_out()
    #                 left_pipette.drop_tip()
    #             if 3.333 < df.loc[i].at['water to add'] < 10:
    #                 left_pipette.pick_up_tip()
    #                 left_pipette.aspirate(3*(df.loc[i].at['amount of template to add']), cold_tuberack[df.loc[i].at['template_well']], rate=2.0) #dilution well corresponds to stock well
    #                 left_pipette.dispense(3*(df.loc[i].at['amount of template to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0) #makes a 12.5ng/uL template
    #                 left_pipette.mix(3,5,tuberack2[df.loc[i].at['template_well']])
    #                 #left_pipette.blow_out()
    #                 left_pipette.drop_tip()
    #             if 1 < df.loc[i].at['water to add'] < 3.333:
    #                 left_pipette.pick_up_tip()
    #                 left_pipette.aspirate(4*(df.loc[i].at['amount of template to add']), cold_tuberack[df.loc[i].at['template_well']], rate=2.0) #dilution well corresponds to stock well
    #                 left_pipette.dispense(4*(df.loc[i].at['amount of template to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0) #makes a 12.5ng/uL template
    #                 left_pipette.mix(3,5,tuberack2[df.loc[i].at['template_well']])
    #                 #left_pipette.blow_out()
    #                 left_pipette.drop_tip()
    #             if df.loc[i].at['water to add'] < 1:
    #                 left_pipette.pick_up_tip()
    #                 left_pipette.aspirate(6*(df.loc[i].at['amount of template to add']), cold_tuberack[df.loc[i].at['template_well']], rate=2.0) #dilution well corresponds to stock well
    #                 left_pipette.dispense(6*(df.loc[i].at['amount of template to add']), tuberack2[df.loc[i].at['template_well']], rate=2.0) #makes a 12.5ng/uL template
    #                 left_pipette.mix(3,5,tuberack2[df.loc[i].at['template_well']])
    #                 #left_pipette.blow_out()
    #                 left_pipette.drop_tip()

    #     #add stock templates for digests:
    #         # for i, row in digests.iterrows():
    #         #     left_pipette.pick_up_tip()
    #         #     left_pipette.aspirate(digests.loc[i].at['amount of template to add'], cold_tuberack[digests.loc[i].at['well']], rate=1.0) #dilution well corresponds to stock well
    #         #     left_pipette.dispense(digests.loc[i].at['amount of template to add'], tuberack2[digests.loc[i].at['well']], rate=1.0) #makes a 12.5ng/uL template
    #         #     #left_pipette.blow_out()
    #         #     left_pipette.drop_tip()
            
    #     #add stock primers to dilution tube
    #         for i, row in oligos.iterrows():
    #             left_pipette.pick_up_tip() #add in an iterrows function
    #             left_pipette.aspirate(oligos.loc[i].at['volume of stock primer to add'], cold_tuberack[oligos.loc[i].at['well']], rate=1.0)
    #             left_pipette.dispense(oligos.loc[i].at['volume of stock primer to add'], tuberack2[oligos.loc[i].at['well']], rate=1.0)
    #             left_pipette.mix(3,5,tuberack2[oligos.loc[i].at['well']])
    #             #left_pipette.blow_out()
    #             left_pipette.drop_tip()
            
    #     #mix contents with pipette tip (reps, max volume, location) for templates and primers
    #         # for i, row in df.iterrows():
    #         #     if df.loc[i].at['water to add'] > 8:
    #         #         right_pipette.pick_up_tip()
    #         #         right_pipette.mix(3,df.loc[i].at['water to add'],tuberack2[df.loc[i].at['template_well']])
    #         #         #right_pipette.blow_out()
    #         #         right_pipette.drop_tip()
    #         #     if df.loc[i].at['water to add'] < 8:
    #         #         right_pipette.pick_up_tip()
    #         #         right_pipette.mix(3,3*(df.loc[i].at['water to add']),tuberack2[df.loc[i].at['template_well']])
    #         #         #right_pipette.blow_out()
    #         #         right_pipette.drop_tip()

    #         # for i, row in digests.iterrows():
    #         #     right_pipette.pick_up_tip()
    #         #     right_pipette.mix(3,digests.loc[i].at['water to add'],tuberack2[digests.loc[i].at['well']])
    #         #     #right_pipette.blow_out()
    #         #     right_pipette.drop_tip()
                
    #         for i, row in oligos.iterrows():
    #             right_pipette.pick_up_tip()
    #             right_pipette.mix(3,oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'],tuberack2[oligos.loc[i].at['well']])
    #             #right_pipette.blow_out()
    #             right_pipette.drop_tip()

    #     #robot pauses so user can take out stock primers and put in DNPNI
    #         protocol.pause('Take all stock primers and templates out. Add Q5 to D6, BsaI to D5, and cutsmart to D4. Then proceed')
            
    #     #now mix dilute primers, dilute templates, Q5, and water in pcr tube within thermocycler
    #         tc_mod.open_lid()
            


    ##########################################################################################################################
    #pcr rxn
    ##########################################################################################################################

        x = 'PCR Mix'
        if x in Input_values['section'].values:
    
    #add water first
            for j, row in pcr.iterrows():
                right_pipette.pick_up_tip()
                right_pipette.aspirate(pcr.loc[j].at['total_water_toadd'], watertuberack['A1'], rate=2.0) #need to write a function to add up all volumes that are being added and figure out how much water to add in automated way
                right_pipette.dispense(pcr.loc[j].at['total_water_toadd'], pcrplate[pcr.loc[j].at['tube']], rate=2.0)
                right_pipette.blow_out()
                right_pipette.drop_tip()
            
        #add 1uL of BOTH (not each) primers
            for j, row in pcr.iterrows():
                left_pipette.pick_up_tip()
                left_pipette.aspirate(pcr.loc[j].at['primervol_x'], tuberack2[pcr.loc[j].at['well']], rate=2.0)
                left_pipette.dispense(pcr.loc[j].at['primervol_x'], pcrplate[pcr.loc[j].at['tube']], rate=2.0)
                left_pipette.mix(3,2,pcrplate[pcr.loc[j].at['tube']])
                #left_pipette.blow_out()            
                left_pipette.drop_tip()
                
                left_pipette.pick_up_tip()
                left_pipette.aspirate(pcr.loc[j].at['primervol_y'], tuberack2[pcr.loc[j].at['well2']], rate=2.0)            
                left_pipette.dispense(pcr.loc[j].at['primervol_y'], pcrplate[pcr.loc[j].at['tube']], rate=2.0)
                left_pipette.mix(3,2,pcrplate[pcr.loc[j].at['tube']])
                #left_pipette.blow_out()
                left_pipette.drop_tip()
            
        #add 1uL of each template
            for j, row in pcr.iterrows():
                left_pipette.pick_up_tip()
                left_pipette.aspirate(pcr.loc[j].at['amount of template to add'], tuberack2[pcr.loc[j].at['template_well']], rate=2.0)
                left_pipette.dispense(pcr.loc[j].at['amount of template to add'], pcrplate[pcr.loc[j].at['tube']], rate=2.0)
                left_pipette.mix(3,3,pcrplate[pcr.loc[j].at['tube']])
                #left_pipette.blow_out()
                left_pipette.drop_tip()

        #Add DMSO
            for j, row in pcr.iterrows():
                left_pipette.pick_up_tip()
                left_pipette.aspirate(DMSO, tuberack2['D6'], rate=2.0)
                left_pipette.dispense(DMSO, pcrplate[pcr.loc[j].at['tube']], rate=2.0)    
                left_pipette.blow_out()
                left_pipette.drop_tip() 

        #add Q5 to each reaction
        #keep Q5 in tuberack1['D6']                                            
            for j, row in pcr.iterrows():
                right_pipette.pick_up_tip()
                right_pipette.aspirate(Q5, cold_tuberack['D6'], rate=2.0)
                right_pipette.aspirate(Q5, pcrplate[pcr.loc[j].at['tube']], rate=2.0)
                #right_pipette.mix(3,Q5+3,pcrplate[pcr.loc[i].at['frag_pcr_tube']])
                right_pipette.blow_out()
                right_pipette.drop_tip()

        #mix up
            for j, row in pcr.iterrows():
                right_pipette.pick_up_tip()
                right_pipette.mix(3,Q5+3,pcrplate[pcr.loc[j].at['tube']])
                right_pipette.blow_out()
                right_pipette.drop_tip()
            
            tc_mod.deactivate()
            temp_module.deactivate()
            
            protocol.pause('move to gradient thermocycler. set gradiet to be between '+str(gradient.loc[0].at['temp'])+' and '+str(gradient.loc[7].at['temp'])+'. Extension time should be '+str((Length['Length']/1000)*30)+' seconds. Follow normal parameters for everything else. A1 is cool, A8 is hot.')

            temp_module.set_temperature(4)
            tc_mod.set_block_temperature(4)



    #Now run thermocycler to amplify DNA
        
    #these parameters can be altered for different pcr reactionsabs
    #should automate calculation of the parameters from j5 spreadsheets.
    #maybe use the median annealing temperature in the spreadsheet
        
            #for j, row in annealing_extension.iterrows():
        # tc_mod.close_lid()
        # tc_mod.set_lid_temperature(temperature = 105)
        # tc_mod.set_block_temperature(98, hold_time_seconds=30, block_max_volume=25)
        # profile = [
        #     {'temperature': 98, 'hold_time_seconds': 10},
        #     {'temperature': round(annealing_extension.loc[i].at['annealing_temp'],1), 'hold_time_seconds': 30},
        #     {'temperature': 72, 'hold_time_seconds': round(annealing_extension.loc[i].at['extension time'],1)}] #should automate calculation of annealing temp based on spreadsheet
        # tc_mod.execute_profile(steps=profile, repetitions=34, block_max_volume=25)
        # tc_mod.set_block_temperature(72, hold_time_minutes=5, block_max_volume=25)
        # tc_mod.set_block_temperature(4)
        # protocol.pause('wait until ready to continue')
        # tc_mod.open_lid()
            
        # for j, row in pcr.iterrows():
        #     if pcr.loc[j,'run'] == i:
        #         right_pipette.pick_up_tip()
        #         right_pipette.aspirate(Input_values.loc[0].at['pcrvol'],pcrplate[pcr.loc[j].at['frag_pcr_tube']],2)
        #         right_pipette.dispense(Input_values.loc[0].at['pcrvol'],cold_tuberack[pcr.loc[j].at['holding_tube']],2)
        #         #right_pipette.blow_out()
        #         right_pipette.drop_tip()

        # for i, row in pcr.iterrows():
        #     right_pipette.pick_up_tip()
        #     right_pipette.aspirate(Input_values.loc[0].at['pcrvol'],cold_tuberack[pcr.loc[i].at['holding_tube']],2)
        #     right_pipette.dispense(Input_values.loc[0].at['pcrvol'],pcrplate[pcr.loc[i].at['frag_pcr_tube']],2)
        #     right_pipette.blow_out()
        #     right_pipette.drop_tip()

        x = 'DPNI Digest'
        if x in Input_values['section'].values:
    
    #Now add DPNI for digestion

            for i, row in pcr.iterrows():
                right_pipette.pick_up_tip()
                right_pipette.aspirate(Input_values.loc[0].at['DPwater'], watertuberack['A1'], rate=2.0)
                right_pipette.dispense(Input_values.loc[0].at['DPwater'], pcrplate[pcr.loc[i].at['tube']], rate=2.0)
                #right_pipette.blow_out()
                right_pipette.drop_tip()

            for i, row in pcr.iterrows():
                left_pipette.pick_up_tip()
                left_pipette.aspirate(Input_values.loc[0].at['cutsmart'], cold_tuberack['D4'], rate=2.0)
                left_pipette.dispense(Input_values.loc[0].at['cutsmart'], pcrplate[pcr.loc[i].at['tube']], rate=2.0)
                #left_pipette.mix(3,10,pcrplate[pcr.loc[i].at['tube']])
                #left_pipette.blow_out()
                left_pipette.drop_tip() 

            for i, row in pcr.iterrows():
                left_pipette.pick_up_tip()
                left_pipette.aspirate(Input_values.loc[0].at['DPNI'], cold_tuberack['D3'], rate=2.0)
                left_pipette.dispense(Input_values.loc[0].at['DPNI'], pcrplate[pcr.loc[i].at['tube']], rate=2.0)
                left_pipette.mix(3,10,pcrplate[pcr.loc[i].at['tube']])
                #left_pipette.blow_out()
                left_pipette.drop_tip()

        #mix up
            for i, row in pcr.iterrows():
                right_pipette.pick_up_tip()
                right_pipette.mix(3,Q5+Input_values.loc[0].at['DPwater']+Input_values.loc[0].at['cutsmart'],pcrplate[pcr.loc[i].at['tube']])
                right_pipette.blow_out()
                right_pipette.drop_tip()

    #Do the bsa1 Digestion
    ##########################################################################################################################
    ##########################################################################################################################

    # # pick up water -> dispense into pcr tube within thermocycler -> get rid of tip
    #     for i, row in plasmid.iterrows():
    #         if plasmid.loc[i].at['Concentration'] > 1:
    #             right_pipette.pick_up_tip()
    #             right_pipette.aspirate(plasmid.loc[i].at['Volume of Water'],watertuberack['A1'],2)
    #             right_pipette.dispense(plasmid.loc[i].at['Volume of Water'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
    #             right_pipette.blow_out()
    #             right_pipette.drop_tip()

    # # pick up plasmid  -> dispense into pcr tube -> get rid of tip  no blow out because aeresol
        
    #     for i, row in plasmid.iterrows():
    #         if plasmid.loc[i].at['Volume of Plasmid'] < 10:
    #             left_pipette.pick_up_tip()
    #             left_pipette.aspirate(plasmid.loc[i].at['Volume of Plasmid'],tuberack2[plasmid.loc[i].at['Plasmid Location']],2) #location of plasmid
    #             left_pipette.dispense(plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
    #             left_pipette.mix(3,plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
    #             left_pipette.blow_out()
    #             left_pipette.drop_tip()

    #         if plasmid.loc[i].at['Volume of Plasmid'] in range(10, 100):
    #             right_pipette.pick_up_tip()
    #             right_pipette.aspirate(plasmid.loc[i].at['Volume of Plasmid'],tuberack2[plasmid.loc[i].at['Plasmid Location']],2) #location of plasmid
    #             right_pipette.dispense(plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
    #             right_pipette.mix(3,plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
    #             right_pipette.blow_out()
    #             right_pipette.drop_tip()

    # # pick up buffer  -> dispense into pcr tube -> get rid of tip

    #     for i, row in plasmid.iterrows():
    #         if plasmid.loc[i].at['Concentration'] > 1:
    #             left_pipette.pick_up_tip()
    #             left_pipette.aspirate(plasmid.loc[i].at['Buffer'],cold_tuberack['D4'],2)
    #             left_pipette.dispense(plasmid.loc[i].at['Buffer'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
    #             left_pipette.mix(3,plasmid.loc[i].at['Buffer'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
    #             left_pipette.blow_out()
    #             left_pipette.drop_tip()  


    # # pick up BsaI -> dispense into pcr tube -> get rid of tip

    #     for i, row in plasmid.iterrows():
    #         if plasmid.loc[i].at['Concentration'] > 1:
    #             left_pipette.pick_up_tip()
    #             left_pipette.aspirate(plasmid.loc[i].at['BSA1'],cold_tuberack['D5'],2)
    #             left_pipette.dispense(plasmid.loc[i].at['BSA1'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
    #             left_pipette.mix(3,plasmid.loc[i].at['BSA1'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
    #             left_pipette.blow_out()
    #             left_pipette.drop_tip()


    #     for i, row in plasmid.iterrows():
    #         if plasmid.loc[i].at['Concentration'] > 1:
    #             if plasmid.loc[i].at['total volume'] > float('10'):
    #                 right_pipette.pick_up_tip()
    #                 right_pipette.mix(3,plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
    #                 right_pipette.drop_tip()
    #             else:
    #                 left_pipette.pick_up_tip()
    #                 left_pipette.mix(3,plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
    #                 left_pipette.drop_tip()

    #  #mixes contents around using the pipette tip  (reps,max volume,location)

            temp_module.deactivate()
            tc_mod.close_lid()
            tc_mod.set_lid_temperature(105)
            tc_mod.set_block_temperature(37,0,60, block_max_volume = 50) #temp,seconds,minutes,ramprate(danger),max vol
            tc_mod.set_block_temperature(80,0,20, block_max_volume = 50)
            tc_mod.set_block_temperature(4, block_max_volume = 50)
            tc_mod.open_lid()

        x = 'Combine Fragments'
        if x in Input_values['section'].values:
        
        #tiprack3.reset_tipracks(self)
        #left_pipette.reset()
            tiprack3.reset()

            tiprack3 = protocol.load_labware("opentrons_96_tiprack_10ul", '6')
            #left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3])

            
            protocol.pause('REFILL TIP RACKS, and wait until its time to dispense the product')

            temp_module.set_temperature(4)

            #tc_mod.open_lid()

        #don't need to move out the digestion this way
            # for i, row in plasmid.iterrows():
            #     if plasmid.loc[i].at['Concentration'] > 1:
            #         if plasmid.loc[i].at['total volume'] > float('10'):
            #             right_pipette.pick_up_tip()
            #             right_pipette.aspirate(plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
            #             right_pipette.dispense(plasmid.loc[i].at['total volume'],tuberack2[plasmid.loc[i].at['final tube']],2)
            #             right_pipette.blow_out()
            #             right_pipette.drop_tip()
                
            #         else:
            #             left_pipette.pick_up_tip()
            #             left_pipette.aspirate(plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
            #             left_pipette.dispense(plasmid.loc[i].at['total volume'],tuberack2[plasmid.loc[i].at['final tube']],2)
            #             left_pipette.blow_out()
            #             left_pipette.drop_tip()


            # tc_mod.close_lid()
            # tc_mod.set_block_temperature(37, hold_time_minutes=15, block_max_volume=50)
            # tc_mod.set_block_temperature(80, hold_time_minutes=20, block_max_volume=50)
            # tc_mod.set_block_temperature(4)
            # tc_mod.deactivate_lid()
            # protocol.pause('hold until time to grab tubes')
            
            # tc_mod.open_lid()

        #Don't need to move out the digestion this way
        #Now replace first digested part
            
        #     for i, row in plasmid.iterrows():
        #         if plasmid.loc[i].at['Concentration'] > 1:
        #             if plasmid.loc[i].at['total volume'] > float('10'):
        #                 right_pipette.pick_up_tip()
        #                 right_pipette.aspirate(plasmid.loc[i].at['total volume'],tuberack2[plasmid.loc[i].at['final tube']],2)
        #                 right_pipette.dispense(plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
        #                 right_pipette.blow_out()
        #                 right_pipette.drop_tip()
                
        #             else:
        #                 left_pipette.pick_up_tip()
        #                 left_pipette.aspirate(plasmid.loc[i].at['total volume'],tuberack2[plasmid.loc[i].at['final tube']],2)
        #                 left_pipette.dispense(plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
        #                 left_pipette.blow_out()
        #                 left_pipette.drop_tip()


        ##########################################################################################################################
        # mix up IVA reactions 


            for i, row in GG_dfs.iterrows():
                x = GG_dfs.loc[i].at['gg#']
            
            #add all fragments to the GG tube
                for i, row in globals()[x].iterrows():
                    if globals()[x].loc[i].at['final amount to add'] < 10:
                        left_pipette.pick_up_tip()
                        left_pipette.aspirate(globals()[x].loc[i].at['final amount to add'], pcrplate[globals()[x].loc[i].at['frag_loc']])
                        left_pipette.dispense(globals()[x].loc[i].at['final amount to add'], pcrplate[globals()[x].loc[i].at['location_of_assembly']])
                        left_pipette.blow_out()
                        left_pipette.drop_tip()
                    else:
                        right_pipette.pick_up_tip()
                        right_pipette.aspirate(globals()[x].loc[i].at['final amount to add'], pcrplate[globals()[x].loc[i].at['frag_loc']])
                        right_pipette.dispense(globals()[x].loc[i].at['final amount to add'], pcrplate[globals()[x].loc[i].at['location_of_assembly']])
                        right_pipette.blow_out()
                        right_pipette.drop_tip()
        
            # one more mix
                # right_pipette.pick_up_tip()
                # right_pipette.mix(3,15,pcrplate[globals()[x].loc[0].at['location_of_assembly']])
                # right_pipette.blow_out()
                # right_pipette.drop_tip()
        
            print('all done')