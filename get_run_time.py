import numpy as np
import pandas as pd
import numpy.random as npr



def grt(df, time):
    
    # game-runtime in ms
    grt = 0

    # check all timestamps up to a given point in time
    for i in range(df.index[0], time, 10000000):

        # if the game is running count passing time
        if((df.loc[i, 'GameState'] != '1') and (df.loc[i, 'GameState'] != '2') and (df.loc[i, 'GameState'] != '7') and (df.loc[i, 'GameState'] != '9')):
            grt += 10
    # return time passed
    return(grt)


