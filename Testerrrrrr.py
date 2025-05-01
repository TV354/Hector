#Title: Testerrrrrr

import numpy as np
import pandas as pd
import numpy.random as npr 

import find_goals as fg
import bot_lists as bl

data = pd.read_csv("C:/Users/Florian/Documents/Hector_Seminar/Kooperationsphase/ml_data_YELLOW0.csv")

print(bl.bot_lists(data))