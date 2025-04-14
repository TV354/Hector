import numpy as np
import pandas as pd


def bot_lists(df):

    array_Y_X = []
    array_B_X = []

    array_all = []

    array_Y_Y = []
    array_B_Y = []

    for i in df.columns:
        if 'X_BotID' in i:
            array_all.append(i)
    
    for i in array_all:
        if 'D_' in i:
            array_all.remove(i)
    
    for i in array_all:
        if ' Y' in i:
            array_Y_X.append(i)
        elif ' B' in i:
            array_B_X.append(i)


    for i in df.columns:
        if 'Y_BotID' in i:
            array_all.append(i)
    for i in array_all:
        if 'D_' in i:
            array_all.remove(i)
    for i in array_all:
        if ('Y_' in i) and (' Y' in i):
            array_Y_Y.append(i)
        elif ' B' in i:
            array_B_Y.append(i)

    array_B_X.sort()
    array_B_Y.sort()
    array_Y_X.sort()
    array_Y_Y.sort()
    
    return([array_Y_X, array_B_X, array_Y_Y, array_B_Y])