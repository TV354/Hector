import numpy as np
import pandas as pd
import numpy.random as npr

# read data
df = pd.read_csv('C:/Users/Florian/Documents/Hector_Seminar/Kooperationsphase/ml_data_YELLOW0.csv')

# define variables with the balls min and max coordinates of both X and Y 
min_x = df['D_X_BotID 0 Y'].min()
max_x = df['D_X_BotID 0 Y'].max()
min_y = df['D_Y_BotID 0 Y'].min()
max_y = df['D_Y_BotID 0 Y'].max()

# display variables 
print(f"Min X: {min_x}")
print(f"Max X: {max_x}")
print(f"Min Y: {min_y}")
print(f"Max Y: {max_y}")
