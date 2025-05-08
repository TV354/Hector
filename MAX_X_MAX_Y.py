import numpy as np
import pandas as pd
import numpy.random as npr

# read data
url = 'https://raw.githubusercontent.com/TV354/Hector/refs/heads/main/Dataframes/2.csv'
df = pd.read_csv(url, index_col=0)

# define variables with the balls min and max coordinates of both X and Y 
min_x = df['D_X_BotID 6 Y'].min()
max_x = df['D_X_BotID 6 Y'].max()
min_y = df['D_Y_BotID 6 Y'].min()
max_y = df['D_Y_BotID 6 Y'].max()

# display variables 
print(f"Min X: {min_x}")
print(f"Max X: {max_x}")
print(f"Min Y: {min_y}")
print(f"Max Y: {max_y}")
