import numpy as np
import pandas as pd
import numpy.random as npr

# read data
url = 'https://raw.githubusercontent.com/TV354/Hector/refs/heads/main/Dataframes/2.csv'
df = pd.read_csv(url, index_col=0)

# define variables with the balls min and max coordinates of both X and Y 
label = "4 Y"
min_x = df[f'D_X_BotID {label}'].min()
max_x = df[f'D_X_BotID {label}'].max()
min_y = df[f'D_Y_BotID {label}'].min()
max_y = df[f'D_Y_BotID {label}'].max()

# display variables 
print(f"Min X: {min_x}")
print(f"Max X: {max_x}")
print(f"Min Y: {min_y}")
print(f"Max Y: {max_y}")

# list