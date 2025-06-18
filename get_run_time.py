import numpy as np
import pandas as pd
import numpy.random as npr

def grt(df, time):
    
    # game-runtime in ms
    grt = 0

    for i in range(0, time):
        if(df.loc[i, 'GameState'] != ('1' or '2' or '7' or '9')):
            grt += 10
    
    return(grt)