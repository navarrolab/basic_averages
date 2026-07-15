import pandas as pd
df = pd.Series([5, 7, 8, 9, 10, 12, 14, 15, 45])
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
outliers_l = Q1 - 1.5*IQR
outliers_u = Q3 + 1.5*IQR
outliers = df[(df < outliers_l) | (df > outliers_u)]
outliers_count = len(outliers)
if outliers_count>0:
    print('выбросы есть')
else:
    print('выбросов нет')