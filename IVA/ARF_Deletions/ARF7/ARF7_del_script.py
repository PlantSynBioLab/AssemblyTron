
##############################################################################################################
#variables:
#primer dilutions:
stkprm = 100 #concentration of the stock primer you are adding
stkvol = 1 #the volume of stock primer you are adding
dilprm = 2.5 #this is the concentration in uM that you want your working dilution to be

#pcr reaction
# need to get this from the df##Numprimers = 4 #this is how many primers go in each pcr reaction.
primerconcentration = 0.1 #this is the concentration you want each primer to be in the pcr reaction
pcrvol = 25 #this is the total volume of your pcr reaction 
templatengs = .5 #this is the concentration of template you want in your pcr rxn in ng/uL

#template dilutions tells you what the temps need to be diluted to initially so that you can just add 1 uL of template to the pcr:
#need to fill in stock template values further down the script
diltemp = (templatengs)*(pcrvol)/1

Q5 = 12.5 #How much Q5 to add
DPNI = 1 #How much DPNI to add
##########################################################################################################

#################################################################################################################

#!pip install pyarrow

#first import information from the j5 spreadsheet in order to perform appropriate steps
#import feather
import pyarrow.feather as ft
import pandas as pd
import numpy as np

###################################################################################################################

#Import oligo.feather
#path for my windows machine
path = 'C:/Users/jonbr/Documents/GitHub/opentrons/IVA/ARF_Deletions/ARF7/oligo.feather'

oligos = ft.read_feather(path)
oligos

oligos['ID Number'] = oligos['ID Number'].astype(int)
oligos

################################################################################################################

