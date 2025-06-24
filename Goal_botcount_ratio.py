import numpy as np
import pandas as pd
import numpy.random as npr

import find_goals as fg
import bot_lists as bl
import get_run_time as grt






def get_og_sides(df):

    # get times of scored goal
    goaltimes = fg.find_goals(df)
    
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

    # sides of respective teams at the beginning of the match (+1 == right; -1 == left)    
    return([Y_side, B_side])
        






# parameters: dataframe, sides of respective teams, percentage of field to count bots in
def Goal_botcount_ratio(df, n):

    Y_side = get_og_sides(df)[0]
    B_side = get_og_sides(df)[1]

    # rightmost position of the robots
    max_x = n/100 * 6000

    array_Y = bl.bot_lists(df)[0]
    array_B = bl.bot_lists(df)[1]

    # times where goals scored
    goaltimes = fg.find_goalsides(df, Y_side, B_side)

    # count of bots in n´th part of the field
    botcount_Y = 0
    botcount_B = 0

    # array for creation of df
    gbr_array = []

    t_array = []

    # bot counting loop
    # loop through times of goalscoring
    for i in goaltimes:
        
        # loop through individual bots
        for j in array_Y:
            # if bot is in n´th part of the side of the field where goal was scored at time of goal
            if df.iloc[i[0]][j] >= max_x * i[1]:
                # increase the count of bots in the n´th quarter of the field
                botcount_Y += 1
        
        # loop through individual bots    
        for l in array_B:
            # if bot is in n´th part of the side of the field where goal was scored at time of goal
            if df.iloc[i[0]][l] >= max_x * i[1]:
                # increase the count of bots in the n´th quarter of the field
                botcount_B += 1

        # update the sides of the teams after the halftime sideswap
        if((grt.grt(df, i[0]) >= 300000) and (checked_before == false)):
            
            Y_side *= -1
            B_side *= -1
            
            checked_before = true
        
        # check for every timestamp which team was attacking and defending and add that info to the df
        if (i[1] == Y_side):
            gbr_array.append([i[0], "B_goal", botcount_B, botcount_Y])
            
        elif (i[1] == B_side):
            gbr_array.append([i[0], "Y_goal", botcount_Y, botcount_B])        
            
        # debug condition    
        else:
            print("Numerical Values of sides are not -1 or 1")

        # reset botcounts for next iteration of time loop
        botcount_Y = 0
        botcount_B = 0


    # create the df
    ratio = pd.DataFrame(gbr_array, columns=['time', 'goal', 'attacker count', 'defender count'])

    # output the df
    return(ratio)

#print(Goal_botcount_ratio(df, Y_side, B_side))