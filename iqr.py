import pandas as pd
df = pd.Series([12, 15, 18, 20, 22, 25, 27, 30, 32, 35])
df.sort_values()
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(Q1, Q3, IQR)