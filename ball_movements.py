import numpy as np
import pandas as pd
import numpy.random as npr

import Goal_botcount_ratio as gbr
import find_goals as fg
import bot_lists as bl

# import df
#df = pd.read_csv("C:/Users/timo_/Documents/Koop-Phase_Hector/Datensätze/2.csv")

url = 'https://https://github.com/TV354/Hector'
df = pd.read_csv(url, index_col=0)

# sides of different teams (+1 == right; -1 == left)
Y_side = +1
B_side = -1

goaltimes = fg.find_goals(df, Y_side, B_side)

# store registers of yellow bots X and Y coordinates in 2d array
array_Y_X_Y = [bl.bot_lists(df)[0], bl.bot_lists(df)[2]]
# store registers of blue bots X and Y coordinates in 2d array
array_B_X_Y = [bl.bot_lists(df)[1], bl.bot_lists(df)[3]]

# time checked (in delta_time * 10ms)
delta_time = 100

# list of times, balls
ball_owned = []

time = []
bot = []
position_x = []
position_y = []

temp = ''




for i in df.index:
    for l in range(0, len(array_Y_X_Y[0])):
        # If Ball_X is in a radius of half the bot`s width plus half the ball`s width plus 1.5cm
        if (df.loc[i, 'Ball_X'] <= (df.loc[i, array_Y_X_Y[0][l]] + 180/2 + 43/2 + 15))  and  (df.loc[i, 'Ball_X'] >= (df.loc[i, array_Y_X_Y[0][l]] - 180/2 - 43/2 - 15)):
            if (df.loc[i, 'Ball_Y'] <= (df.loc[i, array_Y_X_Y[1][l]] + 180/2 + 43/2 + 15))  and  (df.loc[i, 'Ball_Y'] >= (df.loc[i, array_Y_X_Y[1][l]] - 180/2 - 43/2 - 15)):
                
                # add point in time, bot name and bot position to ball_owned
                ball_owned.append([i, array_Y_X_Y[0][l], [df.loc[i, array_Y_X_Y[0][l]], df.loc[i, array_Y_X_Y[1][l]]]])


for i in df.index:
    for l in range(0, len(array_B_X_Y[0])):
        # If Ball_X is in a radius of half the bot`s width plus half the ball`s width plus 0.7cm
        if (df.loc[i, 'Ball_X'] <= (df.loc[i, array_B_X_Y[0][l]] + 180/2 + 43/2 + 10))  and  (df.loc[i, 'Ball_X'] >= (df.loc[i, array_B_X_Y[0][l]] - (180/2 + 43/2 + 10))):
            if (df.loc[i, 'Ball_Y'] <= (df.loc[i, array_B_X_Y[1][l]] + 180/2 + 43/2 + 10))  and  (df.loc[i, 'Ball_Y'] >= (df.loc[i, array_B_X_Y[1][l]] - (180/2 + 43/2 + 10))):
                
                for m in ball_owned:
                        
                    tempint = m[0]

                    if i < tempint:
                        
                        # add point in time, bot name and bot position to ball_owned
                        ball_owned.append([i, array_B_X_Y[0][l], [df.loc[i, array_B_X_Y[0][l]], df.loc[i, array_B_X_Y[1][l]]]])
                        break
                        


for i in ball_owned:
    time.append(i[0])
    bot.append(i[1])
    position_x.append(i[2][0])
    position_y.append(i[2][1])


ball_own = pd.DataFrame(
        {
            "time": time,
            "bot": bot,
            "position x": position_x,
            "position y": position_y,
        }
    )

passes = []
temp = bot[0]

for i in range(0, len(time)):
    
    if bot[i] != temp:
        passes.append([time[i], temp, bot[i]])
    temp = bot[i]

passes.sort(key=lambda x: x[0])        

for i in range (0, len(passes)):
    print(passes[i][0], "from", passes[i][1], "to", passes[i][2])
print(len(passes))