import numpy as np
import pandas as pd
import numpy.random as npr

# import dataframe from github repo
url = 'https://raw.githubusercontent.com/TV354/Hector/refs/heads/main/Dataframes/for Evaluation/2.csv'
df = pd.read_csv(url, index_col=0)


print(df.loc[df.index[0], 'Ball_X'])

