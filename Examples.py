import pandas as pd                                                                      

# create data
data = {
    'column_1': [1, 2, "s"],
    'column_2': [3, "p", 1]
}

# create dataframe from data
df = pd.DataFrame(data)

# save second element of first column
searched = df.loc[1, 'column_1']

# output the dataframe
print(searched)






