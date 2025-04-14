import numpy as np
import pandas as pd
import numpy.random as npr

n = 367
m = 4

dates = pd.date_range("20240101", periods = n)

df = pd.DataFrame(npr.randn(n,m), index=dates, columns=list("ABCD"))

#print(dates)
#print(df.to_numpy())

