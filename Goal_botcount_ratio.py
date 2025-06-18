import numpy as np
import pandas as pd
import numpy.random as npr

import find_goals as fg
import bot_lists as bl
import get_run_time as grt






def get_sides(df):

    # get times of scored goal
    goaltimes = fg.find_goals(df)


    
    if(goaltimes[1] == "Y_side"):
        if(df.loc[goaltimes[0], 'Ball_X'] > 0):
            Y_side = +1
            B_side = -1
        elif(df.loc[goaltimes[0], 'Ball_X'] < 0):
            Y_side = -1
            B_side = +1
        if(grt.grt(df, goaltimes[0]) >= 300000):
            Y_side *= -1
            B_side *= -1
    else:
        if(df.loc[goaltimes[0], 'Ball_X'] > 0):
            Y_side = -1
            B_side = +1
        elif(df.loc[goaltimes[0], 'Ball_X'] < 0):
            Y_side = +1
            B_side = -1
        if(grt.grt(df, goaltimes[0]) >= 300000):
            Y_side *= -1
            B_side *= -1

    # sides of respective teams at the beginning of the match (+1 == right; -1 == left)    
    return([Y_side, B_side])
        






# parameters: dataframe, sides of respective teams, percentage of field to count bots in
def Goal_botcount_ratio(df, n):

    Y_side = get_sides(df)[0]
    Y_side = get_sides(df)[1]

    # rightmost position of the robots
    max_x = n/100 * 6000

    array_Y = bl.bot_lists(df)[0]
    array_B = bl.bot_lists(df)[1]

    # times where goals scored
    goaltimes = fg.find_goalsides(df, Y_side, B_side)

    # count of bots in n´th part of the field
    botcount_Y = 0
    botcount_B = 0

    # times of goals
    time = []
    # side of goal
    side = []
    # botcount of blue/yellow in nth part of field
    botcount_B_list = []
    botcount_Y_list = []

    t_array = []

    # bot counting loop
    # loop through times of goalscoring
    for i in goaltimes:
        
        # loop through individual bots
        for j in array_Y:
            # if bot is in n´th part of the side of the field where goal was scored at time of goal
            if df.loc[i[0], j] >= max_x * i[1]:
                # increase the count of bots in the n´th quarter of the field
                botcount_Y += 1
        
        # loop through individual bots    
        for l in array_B:
            # if bot is in n´th part of the side of the field where goal was scored at time of goal
            if df.loc[i[0], l] >= max_x * i[1]:
                # increase the count of bots in the n´th quarter of the field
                botcount_B += 1

        time.append(i[0])
        if (i[1] == Y_side):
            if (grt.grt(df, i[0]) <= 300000):
                side.append("Y_side")
            else:
                side.append("B_side")
        if (i[1] == B_side):
            if (grt.grt(df, i[0]) <= 300000):
                side.append("B_side")
            else:
                side.append("Y_side")
        botcount_B_list.append(botcount_B)
        botcount_Y_list.append(botcount_Y)

        # reset botcounts for next iteration of time loop
        botcount_Y = 0
        botcount_B = 0


    ratio = pd.DataFrame(
        {
            "time": time,
            "side": side,
            "botcount blue": botcount_B_list,
            "botcount yellow": botcount_Y_list,
        }
    )

    return(ratio)

#print(Goal_botcount_ratio(df, Y_side, B_side))