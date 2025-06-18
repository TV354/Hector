import numpy as np
import pandas as pd
import numpy.random as npr

# import dataframe from github repo
url = 'https://raw.githubusercontent.com/TV354/Hector/refs/heads/main/Dataframes/Evaluation/2.csv'
df = pd.read_csv(url, index_col=0)


import get_run_time as grt


print(df.loc[25967000000, 'Ball_X'])

