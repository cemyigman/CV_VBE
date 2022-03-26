import numpy as np
import pandas as pd
import seaborn as sns


# %%
rng = np.random.RandomState(0)
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': rng.randint(0, 10, 6)},
                  columns=['key', 'data1', 'data2'])
print(df)

#%%
df2 = df.groupby('key').sum()
print("df2: ", df2)
# select XXX.key, SUM(XXX.data1), SUM(XXX.data2) FROM XXX GROUP BY XXX.key

#%%
df.groupby('key').aggregate([np.min, np.mean, np.max])


#%%
# Specifying the split key
L = [0, 1, 0, 1, 2, 0]
df3 = df.groupby(L).sum()


#%%
# Group by using a dictionary
df4 = df.set_index('key')
print(df4)
mapping = {'A': 'Bursa', 'B': 'Ankara', 'C': 'Ankara'}
df5 = df4.groupby(mapping).sum()


#%%
# Any Python function
df6 = df4.groupby(str.lower).mean()


#%%
df7 = df2.groupby([str.lower, mapping]).mean()









