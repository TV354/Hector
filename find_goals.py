import numpy as np
import pandas as pd
import numpy.random as npr


def find_goals(df):
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
            
            # add current time to goaltimes
            goaltimes.append([i, "Y_side"])
            # increase the temp var to current goal count
            temp_Y = df.loc[i, 'Goal_Y']

        # if goal_B is bigger than temp (increases)
        if df.loc[i, 'Goal_B'] > temp_B:
                
            # add current time & side of goal to goaltimes
            goaltimes.append([i, "B_side"])
            # increase the temp var to current goal count
            temp_B = df.loc[i, 'Goal_B']
        
    return(goaltimes)


def find_goalsides(df, Y_side, B_side):
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
            if(grt.grt(df, i) <= 300000):
                # add current time & side of goal to goaltimes
                goaltimes.append([i, Y_side])
            if(grt.grt(df, i) >= 300000):
                # add current time & side of goal to goaltimes
                goaltimes.append([i, B_side])

            # increase the temp var to current goal count
            temp_Y = df.loc[i, 'Goal_Y']

        # if goal_B is bigger than temp (increases)
        if df.loc[i, 'Goal_B'] > temp_B:
                
            if(grt.grt(df, i) <= 300000):
                # add current time & side of goal to goaltimes
                goaltimes.append([i, B_side])
            if(grt.grt(df, i) >= 300000):
                # add current time & side of goal to goaltimes
                goaltimes.append([i, Y_side])

            # increase the temp var to current goal count
            temp_B = df.loc[i, 'Goal_B']
        
    return(goaltimes)
