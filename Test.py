import numpy as np
import pandas as pd
import numpy.random as npr

import bot_lists as bl

# import dataframe from github repo
url = 'https://raw.githubusercontent.com/TV354/Hector/refs/heads/main/Dataframes/Evaluation/2.csv'
df = pd.read_csv(url, index_col=0)

print(len(df.columns))

print(bl.bot_lists(df))
