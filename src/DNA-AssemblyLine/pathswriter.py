
import os
import pandas as pd

path = os.getcwd()

df = pd.DataFrame({'opentrons_repo': [path]})

df.to_csv("paths.csv")
