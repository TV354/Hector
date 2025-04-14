import numpy as np
import pandas as pd
import numpy.random as npr

import find_goals as fg
import bot_lists as bl

# import df
df = pd.read_csv("C:/Users/timo_/Documents/Koop-Phase_Hector/Datensätze/2.csv")


# sides of different teams (+1 == right; -1 == left)
Y_side = +1
B_side = -1


def Goal_botcount_ratio(df, Y_side, B_side):

    # n´th part of the field (counted from mid)
    n = 50
    # rightmost position of the robots
    max_x = n/100 * 6000

    array_Y = bl.bot_lists(df)[0]
    array_B = bl.bot_lists(df)[1]

    # times where goals scored
    goaltimes = fg.find_goals(df, Y_side, B_side)

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
        side.append(i[1])
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