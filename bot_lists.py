import numpy as np
import pandas as pd


def bot_lists(df):

    array_Y_X = []
    array_B_X = []

    array_all = []

    array_Y_Y = []
    array_B_Y = []

    # loop through labels of df columns
    for i in df.columns:
        if 'X_BotID' in i:
            array_all.append(i)
    # remove destination columns
    for i in array_all:
        if 'D_' in i:
            array_all.remove(i)
    
    # seperate labels by team
    for i in array_all:
        if ' Y' in i:
            array_Y_X.append(i)
        elif ' B' in i:
            array_B_X.append(i)


    # loop through labels of df columns
    for i in df.columns:
        if 'Y_BotID' in i:
            array_all.append(i)
    # remove destination columns
    for i in array_all:
        if 'D_' in i:
            array_all.remove(i)
    
    # seperate labels by team
    for i in array_all:
        if ('Y_' in i) and (' Y' in i):
            array_Y_Y.append(i)
        elif ('Y_' in i) and (' B' in i):
            array_B_Y.append(i)

    # sort resulting arrays
    array_B_X.sort()
    array_B_Y.sort()
    array_Y_X.sort()
    array_Y_Y.sort()
    
    # return array of X-coord.-labels of yellow teams bots, X-coord.-labels of blue teams bots, Y-coord.-labels of yellow teams bots, Y-coord.-labels of blue teams bots
    return([array_Y_X, array_B_X, array_Y_Y, array_B_Y])