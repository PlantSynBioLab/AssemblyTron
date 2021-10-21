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
from datetime import date
 
#for this to work you need to run the python script on the same day that you make the new directory
#today = date.today()
#starter_date = str(today.strftime('%Y%m%d'))
#if folder was created on diff date:
#starter_date = 'typedatehere'
#pwd = str(os.getcwd())

def walk_up_folder(path, depth=1):
    _cur_depth = 1        
    while _cur_depth < depth:
        path = os.path.dirname(path)
        _cur_depth += 1
    return path   
#walk_up_folder(os.getcwd(), 2)+

paths = pandas.read_csv(walk_up_folder(os.getcwd(), 3)+'/robotpaths.csv',engine = 'python', encoding='utf-8-sig')

#paths = pandas.read_csv('/data/user_storage/robotpaths.csv',engine = 'python', encoding='utf-8-sig')
paths



#Input_values = pandas.read_csv('Input.csv') 
Input_values = pandas.read_csv('Input.csv',engine = 'python', encoding='utf-8-sig') 
Input_values
Date = str(int(Input_values.loc[0].at['Date']))
Date

Q5 = (0.5*Input_values.loc[0].at['pcrvol'])
diltemp = (Input_values.loc[0].at['templatengs'])*(Input_values.loc[0].at['pcrvol'])/1


###############################################################################################################################################
#oligos
os.chdir(paths.loc[0].at['opentrons_repo']+'Golden_Gate/'+Date+'_GoldenGate')
oligos = pandas.read_csv('oligo.csv')
oligos


oligos['ID Number'] = oligos['ID Number'].astype(int)
oligos

if len(oligos.columns) < 9:
    oligos['well'] = ''
    oligos['stock primer concentration'] = ''
    oligos['volume of stock primer to add'] = ''
    oligos['concentration of diluted primer'] = ''
    oligos['volume of diluted primer'] = '' #this is a calculated value
    oligos['how much of the diluted primer is left'] = '' #also a calculated value
oligos

#custom 4x6 well plate dictionary. hardcoded specifically for the labware used. 
#this could easily be replace with another well specification dictionary

id2well = {}
id2well['0'] = 'A1'
id2well['1'] = 'A2'
id2well['2'] = 'A3'
id2well['3'] = 'A4'
id2well['4'] = 'A5'
id2well['5'] = 'A6'
id2well['6'] = 'B1'
id2well['7'] = 'B2'
id2well['8'] = 'B3'
id2well['9'] = 'B4'
id2well['10'] = 'B5'
id2well['11'] = 'B6'
id2well['12'] = 'C1'
id2well['13'] = 'C2'
id2well['14'] = 'C3'
id2well['15'] = 'C4'
id2well['16'] = 'C5'
id2well['17'] = 'C6'
id2well['18'] = 'D1'
id2well['19'] = 'D2'
id2well['20'] = 'D3'
id2well['21'] = 'D4'
id2well['22'] = 'D5'
id2well['23'] = 'D6'

for i, row in oligos.iterrows():
    oligos.loc[i,'well'] = id2well[str(i)] #this only works because the index matces the id number. id number is a floating value
    oligos.loc[i,'stock primer concentration'] = Input_values.loc[0].at['stkprm']
    oligos.loc[i,'volume of stock primer to add'] = Input_values.loc[0].at['stkvol']
    oligos.loc[i,'concentration of diluted primer'] = Input_values.loc[0].at['dilprm']

    
for i, row in oligos.iterrows():
    oligos.loc[i,'volume of diluted primer'] = row['stock primer concentration']*row['volume of stock primer to add']/row['concentration of diluted primer']
    

oligos['amount primer to add to frag amplification'] = Input_values.loc[0].at['pcrvol']*Input_values.loc[0].at['primerconc']/oligos['concentration of diluted primer']
oligos

oligos.to_csv('output_'+Date+'_oligo_GoldenGate.csv')

###################################################################################################################################################################################
#assembly

#read in assembly pieces as dataframe .... might not need this info
#os.chdir("C:/Users/jonbr/Documents/GitHub/opentrons/Golden_Gate/Part1_PCR_Mason/")
assembly = pandas.read_csv('assembly.csv')
assembly

for i, row in assembly.iterrows():
    assembly.loc[i,'pcr_frag_tube'] = id2well[str(i)]
assembly

assembly.to_csv('output_'+Date+'_assembly_GoldenGate.csv')

##############################################################################################################################################################################################
#digests

#os.chdir("C:/Users/jonbr/Documents/GitHub/opentrons/Golden_Gate/Part1_PCR_Mason/")
os.getcwd()
digests = pandas.read_csv('digests.csv')
digests
#digest_conc=138 #automate digest concentration entry with inputs.py
digest_conc = Input_values.loc[0].at['concdigesttemp']
digests['digest_conc']=digest_conc
digests
startnum = len(oligos['well'])
for i, row in digests.iterrows():
    digests.loc[i,'well'] = id2well[str(startnum+ i)]
digests

next_startnum = startnum+len(digests['well'])
digests

for i, row in digests.iterrows():
    digests.loc[i,'amount of template to add'] = 1


for i, row in digests.iterrows():
   
        digests.loc[i,'concentration of template (ng/uL)'] = diltemp

digests['volume of dilute template prepared'] = digests['digest_conc']*Input_values.loc[0].at['stkvol']/digests['concentration of template (ng/uL)']

digests['water to add']= digests['volume of dilute template prepared']-digests['amount of template to add']
digests

for i, row in digests.iterrows():
    digests.loc[i,'frag_pcr_tube'] = id2well[str(i)]
digests

digests.to_csv('output_'+Date+'_digests_GoldenGate.csv')

##################################################################################################################################
#pcr

#os.chdir("C:/Users/jonbr/Documents/GitHub/opentrons/Golden_Gate/Part1_PCR_Mason/")
pcr = pandas.read_csv('pcr.csv')
pcr.columns = pcr.columns.str.replace("'","")
pcr

pcr[['Reaction ID Number','Forward Oligo ID Number','Reverse Oligo ID Number']] = pcr[['Reaction ID Number','Forward Oligo ID Number','Reverse Oligo ID Number']].astype(int)
pcr


#if bumpback > 0:
#    pcr.index = np.arange(1, len(pcr) + 1)
pcr

#here we create an object with each unique template from the
templates = pcr["Primary Template"]
unique_templates = templates.drop_duplicates(keep = 'first', inplace = False)
unique_templates

df = pandas.DataFrame(unique_templates)

df = df.reset_index()
df = df.drop('index', 1)

df['Template Concentration'] = ''
df

#enter template concentrations here
df['Template Concentration'] = Input_values['template concentrations'] #all you have to do is input the template concentrations in the right order

#df = df[df.line_race != 0]


startnum = len(oligos['well'])

for i, row in df.iterrows():
    df.loc[i,'template_well'] = id2well[str(next_startnum+i)]
    


for i, row in df.iterrows():
    df.loc[i,'amount of template to add'] = 1


for i, row in df.iterrows():
   
        df.loc[i,'concentration of template (ng/uL)'] = diltemp

df['volume of dilute template prepared'] = df['Template Concentration']*Input_values.loc[0].at['stkvol']/df['concentration of template (ng/uL)']

df['water to add']= df['volume of dilute template prepared']-df['amount of template to add']


#df['volume of dilute template prepared'] = df['volume of dilute template prepared'].astype(float)
#df['concentration of template (ng/uL)'] = df['concentration of template (ng/uL)'].astype(float)
#df['amount of template to add'] = df['amount of template to add'].astype(float)

#df['water to add'] = df['water to add'].astype(int)
#df['concentration of template (ng/uL)'] = df['concentration of template (ng/uL)'].astype(int)
#df['volume of dilute template prepared'] = df['volume of dilute template prepared'].astype(int)
#df['amount of template to add'] = df['amount of template to add'].astype(int)

df['water to add'].astype(np.float32)
df['amount of template to add'].astype(np.float32)
df['concentration of template (ng/uL)'].astype(np.float32)
df['volume of dilute template prepared'].astype(np.float32)

#df['amount of template to add'] = pd.Series.astype(df['amount of template to add'], dtype=float)
#df['concentration of template (ng/uL)'] = pd.Series.astype(df['concentration of template (ng/uL)'], dtype=float)
#df['volume of dilute template prepared'] = pd.Series.astype(df['volume of dilute template prepared'], dtype=float,)
df

#if bumpback > 0:
#    df.index = np.arange(0+bumpback, len(df) + bumpback)
    
df
#df.to_csv('output_'+Date+'_templates_IVA.csv')

#df.dtypes

#this line of code integrates the template concentrations into the pcr df
pcr_plustemplates = pandas.merge(pcr,df,on='Primary Template')
pcr_plustemplates

if len(pcr_plustemplates.columns) == 17:

    for i, row in pcr_plustemplates.iterrows():
   
        pcr_plustemplates.loc[i,'concentration of template (ng/uL)'] = diltemp

pcr_plustemplates['volume of dilute template prepared'] = pcr_plustemplates['Template Concentration']*Input_values.loc[0].at['stkvol']/pcr_plustemplates['concentration of template (ng/uL)']

pcr_plustemplates

wellinfo = oligos[['ID Number','well']]
wellinfo

wellinfo = wellinfo.rename(columns={'ID Number':'Forward Oligo ID Number'})
pcr_plustemplates = pcr_plustemplates.merge(wellinfo, on= 'Forward Oligo ID Number')
wellinfo = wellinfo.rename(columns={'Forward Oligo ID Number':'Reverse Oligo ID Number','well':'well2'})
pcr_plustemplates = pcr_plustemplates.merge(wellinfo, on= 'Reverse Oligo ID Number')
pcr_plustemplates

pcr_plustemplates['total_water_toadd'] = Input_values.loc[0].at['pcrvol']-Q5-1-1-1
pcr_plustemplates

pcrstart  = len(digests['well'])
for i, row in pcr_plustemplates.iterrows():
    pcr_plustemplates.loc[i,'frag_pcr_tube'] = id2well[str(i+pcrstart)]
pcr_plustemplates

pcr_plustemplates.to_csv('output_'+Date+'_pcr_GoldenGate.csv')

#######################################################################################################################################################################################################################
#combinations

#os.chdir("C:/Users/jonbr/Documents/GitHub/opentrons/Golden_Gate/Part1_PCR_Mason/")
os.getcwd()
combinations = pandas.read_csv('combinations.csv')
combinations


pieces = [columns for columns in combinations if columns.startswith('Assembly Piece ID Number Bin ')]
frame = combinations[pieces]
#frame2 = frame.transpose()
frame

frame += startnum
frame
frame= frame.values.astype(str)
frame = pandas.DataFrame(frame)
frame
result_1 = frame.replace(id2well)
result_1

combinations_plustemplocs = pandas.concat([combinations, result_1], axis=1)
combinations_plustemplocs

pieces = [columns for columns in combinations if columns.startswith('Assembly Piece ID Number Bin ')]
frame = combinations[pieces]
frame2 = frame.transpose()
frame2

#need to remove the row of linearized fragments from the digest when calculating pcr parameters
if assembly.loc[0].at['Reaction Type'] == 'Digest Linearized':
    frame2 = frame2.drop(frame2.index[0])
    frame2 -= 1
frame2

pcr_info = [columns for columns in pcr_plustemplates if columns.startswith('Mean Oligo Tm (3')]
morepcr_info = [columns for columns in pcr_plustemplates if columns.startswith('Delta Oligo Tm (3')]
anotherpcr_info = [columns for columns in pcr_plustemplates if columns.startswith('Length')]
pcr_info = pcr_info + morepcr_info + anotherpcr_info
pcr_info

for column in frame2:
    listoffrags = frame2[column].to_list()
    listoffrags
    
    tablee = pcr_plustemplates[pcr_info]
    tablee = tablee.iloc[listoffrags, :]
    
    if column == 0:
        params0 = tablee.copy()
    if column == 1:
        params1 = tablee.copy()
    if column == 2:
        params2 = tablee.copy()
    if column == 3:
        params3 = tablee.copy()
    if column == 4:
        params4 = tablee.copy()
    if column == 5:
        params5 = tablee.copy()
    if column == 6:
        params6 = tablee.copy()
    if column == 7:
        params7 = tablee.copy()
    if column == 8:
        params8 = tablee.copy()
    if column == 9:
        params9 = tablee.copy()
    if column == 10:
        params10 = tablee.copy()
    if column == 11:
        params11 = tablee.copy()

        
params0

#so looks like this script will be limited for finding pcr conditions for just 2 construct. have to update for more

Lengthparams0 = params0.nlargest(1,'Length')
Lengthparams0['Length'] = (Lengthparams0['Length']/1000)*30
lengthlist = Lengthparams0['Length'].to_list()

Lengthparams1 = params1.nlargest(1,'Length')
Lengthparams1['Length'] = (Lengthparams1['Length']/1000)*30
lengthlist1 = Lengthparams1['Length'].to_list()

Lengthparams2 = params2.nlargest(1,'Length')
Lengthparams2['Length'] = (Lengthparams2['Length']/1000)*30
lengthlist2 = Lengthparams2['Length'].to_list()

Lengthparams3 = params3.nlargest(1,'Length')
Lengthparams3['Length'] = (Lengthparams3['Length']/1000)*30
lengthlist3 = Lengthparams3['Length'].to_list()

#Lengthparams2 = params2.nlargest(1,'Length')
#   Lengthparams2['Length'] = (Lengthparams2['Length']/1000)*60
 #   lengthlist = Lengthparams2['Length'].to_list()
  #  print(lengthlist)

#Lengthparams3 = params0.nlargest(1,'Length')
#Lengthparams0['Length'] = (Lengthparams0['Length']/1000)*60
#lengthlist = Lengthparams0['Length'].to_list()
#print(lengthlist)

#Lengthparams0 = params0.nlargest(1,'Length')
#Lengthparams0['Length'] = (Lengthparams0['Length']/1000)*60
#lengthlist = Lengthparams0['Length'].to_list()
#print(lengthlist)

finallengthlist = lengthlist + lengthlist1 +lengthlist2 + lengthlist3
finallengthlist

combinations['Extension_time_sec'] = finallengthlist
combinations

extens = combinations.nlargest(1,'Extension_time_sec')
extension_final = extens['Extension_time_sec']
extension_final

#solved the problem of not being able to loop through multiple dataframes
params_tables = {'parmx': ['params0','params1','params2','params3']}
params_tables = pandas.DataFrame(data=params_tables)
params_tables

annealing=[]
for i, row in params_tables.iterrows():
    x = params_tables.loc[i].at['parmx']
#locals()[x]
    locals()[x]['Upper_temp'] = locals()[x]['Mean Oligo Tm (3 Only)'] + locals()[x]['Delta Oligo Tm (3Only)']
    locals()[x]['Lower_temp'] = locals()[x]['Mean Oligo Tm (3 Only)'] - locals()[x]['Delta Oligo Tm (3Only)']
    Lowest_high = locals()[x].nsmallest(1,'Upper_temp')
    Lowest_high
    Highest_low = locals()[x].nlargest(1,'Lower_temp')
    Highest_low
    LH = Lowest_high['Upper_temp']
    HL=Highest_low['Lower_temp']
    A = LH-HL
    if A.all() > 0:
        annealing_temp = Lowest_high['Upper_temp']
    if A.all() < 0:
        annealing_temp = (Lowest_high['Upper_temp']+Highest_low['Lower_temp'])/2
    annealing.append(annealing_temp)
#dfff = np.array(annealing)
dfff = pandas.DataFrame(annealing)
dfff = dfff.sum(axis=1)
avg_annealing = dfff.mean() 
avg_annealing

Annealing_and_extension = pandas.DataFrame({'Annealing temp': avg_annealing,
                   'extension time (seconds)': extension_final})
Annealing_and_extension = Annealing_and_extension.reset_index()
Annealing_and_extension = Annealing_and_extension.drop(columns = ['index'])
Annealing_and_extension

Annealing_and_extension.to_csv('output_'+Date+'_Annealing_extension.csv')

################################################################################################################################################
#continued combination processing to set up actual Golden Gate assembly dataframes

#os.chdir("C:/Users/jonbr/Documents/Github/opentrons/Golden_Gate/Part2_Assembly_Cam")
#os.getcwd()
#fragments = pandas.read_csv('fragments.csv')
#fragments

#put final goldengate assembly products on row C for good measure

id2wellpcr = {}
id2wellpcr['0'] = 'A1'
id2wellpcr['1'] = 'A2'
id2wellpcr['2'] = 'A3'
id2wellpcr['3'] = 'A4'
id2wellpcr['4'] = 'A5'
id2wellpcr['5'] = 'A6'
id2wellpcr['6'] = 'A7'
id2wellpcr['7'] = 'A8'
id2wellpcr['8'] = 'A9'
id2wellpcr['9'] = 'A10'
id2wellpcr['10'] = 'A11'
id2wellpcr['11'] = 'A12'
id2wellpcr['12'] = 'B1'
id2wellpcr['13'] = 'B2'


combinations


ID_tube = assembly[['Reaction ID Number','pcr_frag_tube']]

ID_tube = ID_tube.rename(columns={'Reaction ID Number':'Assembly Piece ID Number Bin 0'})
combinations = combinations.merge(ID_tube, on= 'Assembly Piece ID Number Bin 0')
ID_tube = ID_tube.rename(columns={'Assembly Piece ID Number Bin 0':'Assembly Piece ID Number Bin 1'})
combinations = combinations.merge(ID_tube, on= 'Assembly Piece ID Number Bin 1')
ID_tube = ID_tube.rename(columns={'Assembly Piece ID Number Bin 1':'Assembly Piece ID Number Bin 2'})
combinations = combinations.merge(ID_tube, on= 'Assembly Piece ID Number Bin 2')

combinations

combs_short = combinations[['pcr_frag_tube_x','pcr_frag_tube_y','pcr_frag_tube']] #,'pcr_frag_tube_y','pcr_frag_tube'
combs_short

combs_short = combs_short.transpose()
combs_short

gg1 = pandas.DataFrame()
gg2 = pandas.DataFrame()
gg3 = pandas.DataFrame()
gg4 = pandas.DataFrame()

dil_tu = {}
dil_tu['A1'] = 'B1'
dil_tu['A2'] = 'B2'
dil_tu['A3'] = 'B3'
dil_tu['A4'] = 'B4'
dil_tu['A5'] = 'B5'
dil_tu['A6'] = 'B6'
dil_tu['A7'] = 'B7'
dil_tu['A8'] = 'B8'

e = len(combs_short.columns)
next_tc_tube = len(assembly.index)
GG_dfs = {'gg#': ['gg1','gg2','gg3','gg4']}
GG_dfs = pandas.DataFrame(data=GG_dfs)
####################################################################
#Get rid of this
ngdesired = 100
################################################################################
    
for i, row in GG_dfs.iterrows():
    x = GG_dfs.loc[i].at['gg#']
    locals()[x] = combs_short[[i]]
    locals()[x].loc[:,'conc_assumed']= 60

    bps = assembly[['Sequence Length','pcr_frag_tube']]

    bps = bps.rename(columns={'pcr_frag_tube':i})
    locals()[x] = locals()[x].merge(bps, on= i)
    
    backbone_length=locals()[x]["Sequence Length"].max()
    backbone_length
        
    locals()[x] = locals()[x].rename(columns={0:'frag_loc',1:'frag_loc',2:'frag_loc',3:'frag_loc',4:'frag_loc',5:'frag_loc'})
    
       #for i, row in plasmid.iterrows():
       #     plasmid.loc[i,'final tube'] = pcr2final[str(i)]
           
        
    for i, row in locals()[x].iterrows():
        locals()[x].loc[i,'dil_tube'] = dil_tu[locals()[x].loc[i,'frag_loc']]
        
    for i, row in locals()[x].iterrows():
        locals()[x].loc[i,"equimolar ratio"]=locals()[x].loc[i,"Sequence Length"]/backbone_length
        locals()[x].loc[i,"inverse of conc"]=1/locals()[x].loc[i,"conc_assumed"]
        locals()[x].loc[i,"initial required amount"]=Input_values.loc[0].at['ngdesired']*locals()[x].loc[i,"equimolar ratio"]*locals()[x].loc[i,"inverse of conc"]
    
        if locals()[x].loc[i,"initial required amount"] > 1: 
            locals()[x].loc[i,"H20 to add to 1uL of fragment"] = np.nan
        if locals()[x].loc[i,"initial required amount"] < 1:
            locals()[x].loc[i,"H20 to add to 1uL of fragment"]=(2/locals()[x].loc[i,"initial required amount"])-1    
    
        locals()[x].loc[i,"new Conc"] = locals()[x].loc[i,"conc_assumed"]/(locals()[x].loc[i,"H20 to add to 1uL of fragment"]+1)
        locals()[x].loc[i,"new required amount"] = Input_values.loc[0].at['ngdesired']*locals()[x].loc[i,"equimolar ratio"]*(1/locals()[x].loc[i,"new Conc"])
    
        locals()[x].loc[i,"final amount to add"] = ''
        if locals()[x].loc[i,"initial required amount"] > 1:
            locals()[x].loc[i,"final amount to add"] = locals()[x].loc[i,"initial required amount"]
        else:
            locals()[x].loc[i,"final amount to add"] = locals()[x].loc[i, "new required amount"]
                
#GG_dfs = {'gg#': ['gg1','gg2','gg3','gg4']}
#GG_dfs = pandas.DataFrame(data=GG_dfs)
    
#for i, row in GG_dfs.iterrows():
    #x = GG_dfs.loc[i].at['gg#']
    #for i, row in locals()[x].iterrows():
        locals()[x].loc[i,'location_of_assembly'] = id2wellpcr[str(next_tc_tube)]
    


    next_tc_tube = next_tc_tube + 1

combinations.to_csv('output_'+Date+'_combinations.csv')

dt = {'dispense_tube': ['C3','C4','C5','C6']}
dis_tube = pandas.DataFrame(data=dt)

#########################################################################################################################
#plasmid dataframe object for the digestion
plasmid = pandas.DataFrame()
plasmid['Plasmid'] = Input_values['pwldigesttemp']
plasmid['Concentration'] = Input_values['concdigesttemp']
#plasmid = pandas.DataFrame(plasmid)
plasmid

plasmid['Buffer'] = float('5')
plasmid['BSA1'] = float('1')
plasmid['Volume of Plasmid'] = ''
plasmid['Volume of Water'] = ''

plasmid['Volume of Plasmid'] = (1/(plasmid['Concentration'])) * 1000 * 1
plasmid['Volume of Water'] = 50- plasmid['Volume of Plasmid'] - plasmid['Buffer'] - plasmid['BSA1']

plasmid['total volume'] = float(50)


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
plasmid

for i, row in plasmid.iterrows():
    plasmid.loc[i,'Plasmid Location'] = id2well[str(i+startnum)]
plasmid

pcr2final= {}
pcr2final['0'] = 'D6'
pcr2final['1'] = 'D5'
pcr2final['2'] = 'D4'
pcr2final['3'] = 'D3'
pcr2final['4'] = 'D2'
pcr2final['5'] = 'D1'
pcr2final['6'] = 'C6'
pcr2final['7'] = 'C5'
pcr2final['8'] = 'C4'

plasmid['final tube'] = ''

for i, row in plasmid.iterrows():
    plasmid.loc[i,'final tube'] = pcr2final[str(i)]
plasmid


#########################################################################################################################################
#########actual commands#############3

from opentrons import protocol_api

#Metadata is a dictionary of data that is read by the server and returned to the opentrons app. 
#give yourself credit. you are required to specify the 'apiLevel' herefrom opentrons import protocol_api
metadata = {
    'protocolName': 'ARF7 Deletions Protocol',
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
    tiprack2 = protocol.load_labware('opentrons_96_tiprack_300ul','6')
    tiprack3 = protocol.load_labware("opentrons_96_tiprack_10ul", '5')
#tuberack1 = protocol.load_labware('opentrons_24_tuberack_generic_2ml_screwcap','1') #holds stock primers and templates
    watertuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical','3') #holds molec bio grad H2O
    tuberack2 = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap','2') # holds dilute primers and templates
    
    tc_mod = protocol.load_module('Thermocycler Module')
    pcrplate = tc_mod.load_labware('nest_96_wellplate_100ul_pcr_full_skirt')
    temp_module = protocol.load_module('temperature module', 1)
    cold_tuberack = temp_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', label='Temperature-Controlled Tubes')
    temp_module.set_temperature(4)
    print(temp_module.temperature)
    tc_mod.open_lid()

#########Some notes:    
#specify the order of stock primers and template in tuberack1 here:
#good place to add the pop-up window
#A1-D3 = stock primers
#D4-D5 = stock templates
#stock tubes and dilution tubes need to be set up in the same order
#as of now Q5 is in 
    
#pipettes
    right_pipette = protocol.load_instrument('p300_single','right',tip_racks=[tiprack1, tiprack2])
    left_pipette = protocol.load_instrument('p10_single','left',tip_racks = [tiprack3])
    
##################################COMMANDS####################################
    
#add water to template dilution tubes. ***df is the template description dataframe
#Since we are just moving water I will use the same pipette tip to save plastic

#add water for templates
    right_pipette.pick_up_tip()
    for i, row in df.iterrows():
        right_pipette.aspirate(volume = df.loc[i].at['water to add'], location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
        right_pipette.dispense(df.loc[i].at['water to add'], tuberack2[df.loc[i].at['template_well']], rate=2.0)
        right_pipette.blow_out()
#digestions water
    for i, row in digests.iterrows():
        right_pipette.aspirate(volume = digests.loc[i].at['water to add'], location = watertuberack['A1'], rate=2.0) #total vol dilute template - vol stock template to add
        right_pipette.dispense(digests.loc[i].at['water to add'], tuberack2[digests.loc[i].at['well']], rate=2.0)
        right_pipette.blow_out()

#add water to primer dilution tubes
    for i, row in oligos.iterrows():
        right_pipette.aspirate(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'], watertuberack['A1'], rate=2.0) #need to put 39uL of water into each dilution tube for primers,) #we need to find better way to loop through these commands
        right_pipette.dispense(oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'], tuberack2[oligos.loc[i].at['well']], rate=2.0)
        right_pipette.blow_out()
    right_pipette.drop_tip()    
    
#add stock templates to dilution tubes
    for i, row in df.iterrows():
        left_pipette.pick_up_tip()
        left_pipette.aspirate(df.loc[i].at['amount of template to add'], cold_tuberack[df.loc[i].at['template_well']], rate=2.0) #dilution well corresponds to stock well
        left_pipette.dispense(df.loc[i].at['amount of template to add'], tuberack2[df.loc[i].at['template_well']], rate=2.0) #makes a 12.5ng/uL template
        left_pipette.blow_out()
        left_pipette.drop_tip()

#add stock templates for digests:
    for i, row in digests.iterrows():
        left_pipette.pick_up_tip()
        left_pipette.aspirate(digests.loc[i].at['amount of template to add'], cold_tuberack[digests.loc[i].at['well']], rate=2.0) #dilution well corresponds to stock well
        left_pipette.dispense(digests.loc[i].at['amount of template to add'], tuberack2[digests.loc[i].at['well']], rate=2.0) #makes a 12.5ng/uL template
        left_pipette.blow_out()
        left_pipette.drop_tip()
    
#add stock primers to dilution tube
    for i, row in oligos.iterrows():
        left_pipette.pick_up_tip() #add in an iterrows function
        left_pipette.aspirate(oligos.loc[i].at['volume of stock primer to add'], cold_tuberack[oligos.loc[i].at['well']], rate=2.0)
        left_pipette.dispense(oligos.loc[i].at['volume of stock primer to add'], tuberack2[oligos.loc[i].at['well']], rate=2.0)
        left_pipette.blow_out()
        left_pipette.drop_tip()
    
#mix contents with pipette tip (reps, max volume, location) for templates and primers
    for i, row in df.iterrows():
        right_pipette.pick_up_tip()
        right_pipette.mix(3,df.loc[i].at['water to add'],tuberack2[df.loc[i].at['template_well']])
        right_pipette.blow_out()
        right_pipette.drop_tip()

    for i, row in digests.iterrows():
        right_pipette.pick_up_tip()
        right_pipette.mix(3,digests.loc[i].at['water to add'],tuberack2[digests.loc[i].at['well']])
        right_pipette.blow_out()
        right_pipette.drop_tip()
        
    for i, row in oligos.iterrows():
        right_pipette.pick_up_tip()
        right_pipette.mix(3,oligos.loc[i].at['volume of diluted primer']-oligos.loc[i].at['volume of stock primer to add'],tuberack2[oligos.loc[i].at['well']])
        right_pipette.blow_out()
        right_pipette.drop_tip()

#robot pauses so user can take out stock primers and put in DNPNI
    protocol.pause('Take all stock primers and templates out. Add Q5 to D6, BsaI to D5, and cutsmart to D4. Then proceed')
    
#now mix dilute primers, dilute templates, Q5, and water in pcr tube within thermocycler
    tc_mod.open_lid()
    
#Do the Digestion
##########################################################################################################################
##########################################################################################################################



# pick up water -> dispense into pcr tube within thermocycler -> get rid of tip
    
    
    for i, row in plasmid.iterrows():
        if plasmid.loc[i].at['Concentration'] > 1:
            right_pipette.pick_up_tip()
            right_pipette.aspirate(plasmid.loc[i].at['Volume of Water'],watertuberack['A1'],2)
            right_pipette.dispense(plasmid.loc[i].at['Volume of Water'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
            right_pipette.blow_out()
            right_pipette.drop_tip()

# pick up plasmid  -> dispense into pcr tube -> get rid of tip  no blow out because aeresol
    
    for i, row in plasmid.iterrows():
        if plasmid.loc[i].at['Volume of Plasmid'] < 10:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(plasmid.loc[i].at['Volume of Plasmid'],tuberack2[plasmid.loc[i].at['Plasmid Location']],2) #location of plasmid
            left_pipette.dispense(plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
            left_pipette.mix(3,plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
            left_pipette.blow_out()
            left_pipette.drop_tip()

        if plasmid.loc[i].at['Volume of Plasmid'] in range(10, 100):
            right_pipette.pick_up_tip()
            right_pipette.aspirate(plasmid.loc[i].at['Volume of Plasmid'],tuberack2[plasmid.loc[i].at['Plasmid Location']],2) #location of plasmid
            right_pipette.dispense(plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
            right_pipette.mix(3,plasmid.loc[i].at['Volume of Plasmid'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
            right_pipette.blow_out()
            right_pipette.drop_tip()

# pick up buffer  -> dispense into pcr tube -> get rid of tip

    for i, row in plasmid.iterrows():
        if plasmid.loc[i].at['Concentration'] > 1:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(plasmid.loc[i].at['Buffer'],cold_tuberack['D4'],2)
            left_pipette.dispense(plasmid.loc[i].at['Buffer'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
            left_pipette.mix(3,plasmid.loc[i].at['Buffer'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
            left_pipette.blow_out()
            left_pipette.drop_tip()  


# pick up BsaI -> dispense into pcr tube -> get rid of tip

    for i, row in plasmid.iterrows():
        if plasmid.loc[i].at['Concentration'] > 1:
            left_pipette.pick_up_tip()
            left_pipette.aspirate(plasmid.loc[i].at['BSA1'],cold_tuberack['D5'],2)
            left_pipette.dispense(plasmid.loc[i].at['BSA1'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
            left_pipette.mix(3,plasmid.loc[i].at['BSA1'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
            left_pipette.blow_out()
            left_pipette.drop_tip()


    for i, row in plasmid.iterrows():
        if plasmid.loc[i].at['Concentration'] > 1:
            if plasmid.loc[i].at['total volume'] > float('10'):
                right_pipette.pick_up_tip()
                right_pipette.mix(3,plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
                right_pipette.drop_tip()
            else:
                left_pipette.pick_up_tip()
                left_pipette.mix(3,plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']])
                left_pipette.drop_tip()

 #mixes contents around using the pipette tip  (reps,max volume,location)


    tc_mod.close_lid()
    tc_mod.set_lid_temperature(105)
    tc_mod.set_block_temperature(37,0,30, block_max_volume = 50) #temp,seconds,minutes,ramprate(danger),max vol
    tc_mod.set_block_temperature(80,0,20, block_max_volume = 50)
    tc_mod.set_block_temperature(4, block_max_volume = 50)

    protocol.pause('wait until its time to dispense the product')

    tc_mod.open_lid()

    for i, row in plasmid.iterrows():
        if plasmid.loc[i].at['Concentration'] > 1:
            if plasmid.loc[i].at['total volume'] > float('10'):
                right_pipette.pick_up_tip()
                right_pipette.aspirate(plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
                right_pipette.dispense(plasmid.loc[i].at['total volume'],tuberack2[plasmid.loc[i].at['final tube']],2)
                right_pipette.blow_out()
                right_pipette.drop_tip()
        
            else:
                left_pipette.pick_up_tip()
                left_pipette.aspirate(plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
                left_pipette.dispense(plasmid.loc[i].at['total volume'],tuberack2[plasmid.loc[i].at['final tube']],2)
                left_pipette.blow_out()
                left_pipette.drop_tip()

##########################################################################################################################
##########################################################################################################################


#add water first
    for i, row in pcr_plustemplates.iterrows():
        
        right_pipette.pick_up_tip()
        right_pipette.aspirate(pcr_plustemplates.loc[i].at['total_water_toadd'], watertuberack['A1'], rate=2.0) #need to write a function to add up all volumes that are being added and figure out how much water to add in automated way
        right_pipette.dispense(pcr_plustemplates.loc[i].at['total_water_toadd'], pcrplate[pcr_plustemplates.loc[i].at['frag_pcr_tube']], rate=2.0)
        right_pipette.blow_out()
        right_pipette.drop_tip()
    
#add 1uL of BOTH (not each) primers
    for i, row in oligos.iterrows():
        left_pipette.pick_up_tip()
        left_pipette.aspirate(oligos.loc[i].at['amount primer to add to frag amplification'], tuberack2[pcr_plustemplates.loc[i].at['well']], rate=2.0)
        left_pipette.dispense(oligos.loc[i].at['amount primer to add to frag amplification'], pcrplate[pcr_plustemplates.loc[i].at['frag_pcr_tube']], rate=2.0)
        left_pipette.blow_out()            
        left_pipette.drop_tip()
        
        left_pipette.pick_up_tip()
        left_pipette.aspirate(oligos.loc[i].at['amount primer to add to frag amplification'], tuberack2[pcr_plustemplates.loc[i].at['well2']], rate=2.0)            
        left_pipette.dispense(oligos.loc[i].at['amount primer to add to frag amplification'], pcrplate[pcr_plustemplates.loc[i].at['frag_pcr_tube']], rate=2.0)
        left_pipette.blow_out()
        left_pipette.drop_tip()
    
#add 1uL of each template
    for i, row in combinations.iterrows():
        left_pipette.pick_up_tip()
        left_pipette.aspirate(pcr_plustemplates.loc[i].at['amount of template to add'], tuberack2[pcr_plustemplates.loc[i].at['template_well']], rate=2.0)
        left_pipette.dispense(pcr_plustemplates.loc[i].at['amount of template to add'], pcrplate[pcr_plustemplates.loc[i].at['frag_pcr_tube']], rate=2.0)
        left_pipette.blow_out()
        left_pipette.drop_tip()
    
#add Q5 to each reaction
#keep Q5 in tuberack1['D6']                                            
    for i, row in pcr_plustemplates.iterrows():
        right_pipette.pick_up_tip()
        right_pipette.aspirate(Q5, cold_tuberack['D6'], rate=2.0)
        right_pipette.aspirate(Q5, pcrplate[pcr_plustemplates.loc[i].at['frag_pcr_tube']], rate=2.0)
        right_pipette.blow_out()
        right_pipette.drop_tip()

#mix up
    for i, row in pcr_plustemplates.iterrows():
        right_pipette.pick_up_tip()
        right_pipette.mix(3,Q5+3,pcrplate[pcr_plustemplates.loc[i].at['frag_pcr_tube']])
        right_pipette.blow_out()
        right_pipette.drop_tip()
    
#Now run thermocycler to amplify DNA
    
#these parameters can be altered for different pcr reactionsabs
#should automate calculation of the parameters from j5 spreadsheets.
#maybe use the median annealing temperature in the spreadsheet
    
    tc_mod.set_lid_temperature(temperature = 105)
    tc_mod.set_block_temperature(98, hold_time_seconds=30, block_max_volume=25)
    profile = [
        {'temperature': 98, 'hold_time_seconds': 10},
        {'temperature': round(Annealing_and_extension.loc[0].at['Annealing temp'],1), 'hold_time_seconds': 30},
        {'temperature': 72, 'hold_time_seconds': round(Annealing_and_extension.loc[0].at['extension time (seconds)'],1)}] #should automate calculation of annealing temp based on spreadsheet
    tc_mod.execute_profile(steps=profile, repetitions=34, block_max_volume=25)
    tc_mod.set_block_temperature(72, hold_time_minutes=5, block_max_volume=25)
    tc_mod.set_block_temperature(4)
    tc_mod.open_lid()

#Now replace first digested part
    
    for i, row in plasmid.iterrows():
        if plasmid.loc[i].at['Concentration'] > 1:
            if plasmid.loc[i].at['total volume'] > float('10'):
                right_pipette.pick_up_tip()
                right_pipette.aspirate(plasmid.loc[i].at['total volume'],tuberack2[plasmid.loc[i].at['final tube']],2)
                right_pipette.dispense(plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
                right_pipette.blow_out()
                right_pipette.drop_tip()
        
            else:
                left_pipette.pick_up_tip()
                left_pipette.aspirate(plasmid.loc[i].at['total volume'],tuberack2[plasmid.loc[i].at['final tube']],2)
                left_pipette.dispense(plasmid.loc[i].at['total volume'],pcrplate[digests.loc[i].at['frag_pcr_tube']],2)
                left_pipette.blow_out()
                left_pipette.drop_tip()

#Now add DPNI for digestion

    for i, row in assembly.iterrows():
        right_pipette.pick_up_tip()
        right_pipette.aspirate(Input_values.loc[0].at['DPwater'], watertuberack['A1'], rate=2.0)
        right_pipette.dispense(Input_values.loc[0].at['DPwater'], pcrplate[assembly.loc[i].at['pcr_frag_tube']], rate=2.0)
        right_pipette.drop_tip()

    for i, row in assembly.iterrows():
        left_pipette.pick_up_tip()
        left_pipette.aspirate(Input_values.loc[0].at['cutsmart'], cold_tuberack['D4'], rate=2.0)
        left_pipette.dispense(Input_values.loc[0].at['cutsmart'], pcrplate[assembly.loc[i].at['pcr_frag_tube']], rate=2.0)
        left_pipette.drop_tip() 

    for i, row in assembly.iterrows():
        left_pipette.pick_up_tip()
        left_pipette.aspirate(Input_values.loc[0].at['DPNI'], cold_tuberack['D3'], rate=2.0)
        left_pipette.dispense(Input_values.loc[0].at['DPNI'], pcrplate[assembly.loc[i].at['pcr_frag_tube']], rate=2.0)
        left_pipette.drop_tip()

    tc_mod.close_lid()
    tc_mod.set_block_temperature(37, hold_time_minutes=15, block_max_volume=50)
    tc_mod.set_block_temperature(80, hold_time_minutes=20, block_max_volume=50)
    tc_mod.set_block_temperature(4)
    tc_mod.deactivate_lid()
    protocol.pause('hold until time to grab tubes')
    
    tc_mod.open_lid()
##########################################################################################################################
#set up goldengate

    #mix the T4 BSA combo
    left_pipette.pick_up_tip()
    left_pipette.aspirate(10,cold_tuberack['D2'])
    left_pipette.dispense(10,cold_tuberack['C4'])
    left_pipette.blow_out()
    left_pipette.drop_tip()
    
    left_pipette.pick_up_tip()
    left_pipette.aspirate(1,cold_tuberack['C6'])
    left_pipette.dispense(1,cold_tuberack['C4'])
    left_pipette.blow_out()
    left_pipette.mix(3,10,cold_tuberack['C4'])
    left_pipette.drop_tip()

#for i in range(0,e):
    
    for i, row in GG_dfs.iterrows():
        x = GG_dfs.loc[i].at['gg#']
        #wawa = 15 - round(locals()[x].loc[:,'final amount to add'].sum(),2) - 1 - 1 - 1.65

        #how much water you need to add
        left_pipette.pick_up_tip()
        left_pipette.aspirate(15 - round(globals()[x]['final amount to add'].sum(),2) - 1 - 1 - 1.65, watertuberack['A1'])
        left_pipette.dispense(15 - round(globals()[x]['final amount to add'].sum(),2) - 1 - 1 - 1.65, pcrplate[globals()[x].loc[0].at['location_of_assembly']])
        left_pipette.blow_out()
        left_pipette.drop_tip()
    
    #now add all fragments to the GG tube
        for i, row in globals()[x].iterrows():
            left_pipette.pick_up_tip()
            if globals()[x].loc[i].at['initial required amount'] <1:
                left_pipette.aspirate(globals()[x].loc[i].at['H20 to add to 1uL of fragment'], watertuberack['A1'])
                left_pipette.dispense(globals()[x].loc[i].at['H20 to add to 1uL of fragment'], pcrplate[globals()[x].loc[i].at['dil_tube']])
                left_pipette.blow_out()
                left_pipette.drop_tip()
                
                left_pipette.pick_up_tip()
                left_pipette.aspirate(1, pcrplate[globals()[x].loc[i].at['frag_loc']])
                left_pipette.dispense(1, pcrplate[globals()[x].loc[i].at['dil_tube']])
                left_pipette.blow_out()
                left_pipette.mix(3,globals()[x].loc[i].at['H20 to add to 1uL of fragment'],pcrplate[globals()[x].loc[i].at['dil_tube']])
                left_pipette.drop_tip()
                
                left_pipette.pick_up_tip()
                left_pipette.aspirate(globals()[x].loc[i].at['final amount to add'], pcrplate[globals()[x].loc[i].at['dil_tube']])
                left_pipette.dispense(globals()[x].loc[i].at['final amount to add'], pcrplate[globals()[x].loc[i].at['location_of_assembly']])
                left_pipette.drop_tip()
                
            else:
                left_pipette.aspirate(globals()[x].loc[i].at['initial required amount'], pcrplate[globals()[x].loc[i].at['frag_loc']])
                left_pipette.dispense(globals()[x].loc[i].at['initial required amount'], pcrplate[globals()[x].loc[i].at['location_of_assembly']])
                left_pipette.drop_tip()
   
    
    #pipette the T4 BSA combo into GG assemblies
        left_pipette.pick_up_tip()
        left_pipette.aspirate(1.65,cold_tuberack['C4'])
        left_pipette.dispense(1.65,pcrplate[globals()[x].loc[0].at['location_of_assembly']])
        left_pipette.blow_out()
        left_pipette.mix(3,8,pcrplate[globals()[x].loc[0].at['location_of_assembly']])
        left_pipette.drop_tip()
    
    #pipette the BsaI in
        left_pipette.pick_up_tip()
        left_pipette.aspirate(1,cold_tuberack['D5'])
        left_pipette.dispense(1,pcrplate[globals()[x].loc[0].at['location_of_assembly']])
        left_pipette.blow_out()
        left_pipette.mix(3,9,pcrplate[globals()[x].loc[0].at['location_of_assembly']])
        left_pipette.drop_tip()
    
    #pipette the T4 ligase in
        left_pipette.pick_up_tip()
        left_pipette.aspirate(1,cold_tuberack['C5'])
        left_pipette.dispense(1,pcrplate[globals()[x].loc[0].at['location_of_assembly']])
        left_pipette.blow_out()
        left_pipette.mix(3,9,pcrplate[globals()[x].loc[0].at['location_of_assembly']])
        left_pipette.drop_tip()
    
    #one more mix
        right_pipette.pick_up_tip()
        right_pipette.mix(3,15,pcrplate[globals()[x].loc[0].at['location_of_assembly']])
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
    
#for i in range(0,e):
    
    for i, row in GG_dfs.iterrows():
        x = GG_dfs.loc[i].at['gg#']
    
        right_pipette.pick_up_tip()
        right_pipette.aspirate(15,pcrplate[globals()[x].loc[0].at['location_of_assembly']])
        right_pipette.dispense(15,tuberack2[dis_tube.loc[i].at['dispense_tube']])
        right_pipette.blow_out()
        right_pipette.drop_tip()
    

    print('all done')