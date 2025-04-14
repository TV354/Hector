import numpy as np
import pandas as pd
import numpy.random as npr

df = pd.read_csv("C:/Users/timo_/Documents/Koop-Phase_Hector/Datensätze/2.csv")

max = -1
min = -1
cur = 0

for i in range(0, 6280):
    cur = df.loc[i, 'Ball_X']
    if cur > max:
        max = cur
    if cur < min:
        min = cur

#print(df.columns)
#print(df.loc[100 : 1000, ['X_BotID 2 Y', 'Y_BotID 2 Y']])
#print("max", max, "min", min,)
#print(df.loc[6279, ['Goal_B', 'Goal_Y']])
print(df)