import numpy as np
import pandas as pd
import numpy.random as npr

import get_run_time as grt


def find_goals_old(df):
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





def find_goals(df):

    # times where goals scored
    goaltimes = []

    for s in ("Y", "B"): 

        # find the column of the checked team
        goal_column = f"Goal_{s}"   # 'Goal_Y' or 'Goal_B'

        # get the number of goals scored by the team at the end of the game
        max_goals = df.iloc[len(df.index) - 1][goal_column]

        # goalcounter
        i = 1

        # bounds for binary search
        high = len(df.index) - 1 
        low  = 0

        ## binary search for goaltimes

        # binary search until the amount of goals of a team equals the amount of goals they scored in the whole game
        while (len([g for g in goaltimes if g[1] == f"{s}_goal"]) < max_goals):

            # timestamp for check
            mid = (high + low) // 2

            # goal found
            if ((df.iloc[mid - 1][goal_column] != i) and (df.iloc[mid][goal_column] == i)):
                # save time of goal and team scoring goal
                goaltimes.append([mid, f"{s}_goal"])
                # search for time of next goal
                i += 1
                # prepare variables for binary search for time of next goal
                low  = mid
                high = len(df.index) - 1

            # checked goalcount to high
            elif (df.iloc[mid][goal_column] >= i):
                # check "left" of current position
                high = mid - 1
            
            # checked goalcount to low
            elif (df.iloc[mid][goal_column] < i):
                # check "right" of current position
                low = mid + 1

    # output the times of goals and the team which scored the goal
    return goaltimes



def get_og_sides(df):

    # sides of respective teams at the beginning of the match (+1 == right; -1 == left)
    Y_side = 0
    B_side = 0

    # get times of scored goal
    goaltimes = find_goals(df)
    
    # if the first goal scored
    if(goaltimes[0][1] == "Y_goal"):
        if   (df.iloc[goaltimes[0][0]]['Ball_X'] > 0):
            Y_side = -1
            B_side = +1
        elif (df.iloc[goaltimes[0][0]]['Ball_X'] < 0):
            Y_side = +1
            B_side = -1
        if   (grt.grt(df, goaltimes[0][0]) >= 300000):
            Y_side *= -1
            B_side *= -1
    else:
        if   (df.iloc[goaltimes[0][0]]['Ball_X'] > 0):
            Y_side = +1
            B_side = -1
        elif (df.iloc[goaltimes[0][0]]['Ball_X'] < 0):
            Y_side = -1
            B_side = +1
        if   (grt.grt(df, goaltimes[0][0]) >= 300000):
            Y_side *= -1
            B_side *= -1

    return([Y_side, B_side])



def find_goalsides(df, Y_side, B_side):

    # get the actual times of goals from other function    
    goaltimes = find_goals(df)

    # loop through output of other function
    for i in range(0, len(goaltimes)):

        ## substitute the strings with numbers ##
        
        if(goaltimes[i][1] == "Y_goal"):
            if(grt.grt(df, goaltimes[i][0]) <= 300000):
                # add current time & side of goal to goaltimes
                goaltimes[i] = [goaltimes[i][0], B_side]
            if(grt.grt(df, goaltimes[i][0]) >= 300000):
                # add current time & side of goal to goaltimes
                goaltimes[i] = [goaltimes[i][0], B_side * -1]
        
        if(goaltimes[i][1] == "B_goal"):
            if(grt.grt(df, goaltimes[i][0]) <= 300000):
                # add current time & side of goal to goaltimes
                goaltimes[i] = [goaltimes[i][0], Y_side]
            if(grt.grt(df, goaltimes[i][0]) >= 300000):
                # add current time & side of goal to goaltimes
                goaltimes[i] = [goaltimes[i][0], Y_side * -1]
    
    # output the new array
    return(goaltimes)

















