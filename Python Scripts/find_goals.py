import numpy as np
import pandas as pd
import numpy.random as npr

df = pd.read_csv("C:/Users/timo_/Documents/Koop-Phase_Hector/Datensätze/2.csv")


def find_goals(df, Y_side, B_side):
    # times where goals scored
    goaltimes = []
    
    # temp vars for loop
    temp_Y = 0
    temp_B = 0

    # goal finding loop
    # loop through time
    for i in df.index:
        # if goal_Y is bigger than temp (increases)
        if df.loc[i, 'Goal_Y'] > temp_Y:
            
            # add current time & side of goal to goaltimes
            goaltimes.append([i, Y_side])
            # increase the temp var to current goal count
            temp_Y = df.loc[i, 'Goal_Y']

        # if goal_B is bigger than temp (increases)
        if df.loc[i, 'Goal_B'] > temp_B:
                
            # add current time & side of goal to goaltimes
            goaltimes.append([i, B_side])
            # increase the temp var to current goal count
            temp_B = df.loc[i, 'Goal_B']
        
    return goaltimes











