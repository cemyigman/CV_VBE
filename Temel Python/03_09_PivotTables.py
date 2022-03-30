import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import seaborn as sns

# %%
titanic = sns.load_dataset('titanic')

# %%
titanic = pd.DataFrame(titanic)
print(titanic.head())

# %%
#################
# Manual pivoting
#################
pivot1 = titanic.groupby('sex')[['survived']].count()

# %%
a = {'survived': ['sum', 'count', 'mean'], 'age': ['mean']}

# %%
pivot2 = titanic.groupby('sex').aggregate(a)

# %%
a2 = {'survived': ['describe']}
pivot3 = titanic.groupby('class').agg(a2)

# %%
# idxmax ve idxmin maximum ve minimum degerlere ait index i bulmak icin kullanilir.
agg_func_max_min = {'fare': ['idxmax', 'idxmin']}
pivot9 = titanic.groupby(['embark_town']).agg(agg_func_max_min)
print(titanic.loc[[258, 378]])
# v print(titanic.loc[258])

# %%
#################
# Pivoting Using Pivot Table
#################
pivot4 = titanic.pivot_table('survived', index='sex', columns='class')

# %%
# Multi-Level Pivoting
age = pd.cut(titanic['age'], [0, 18, 80])
pivot5 = titanic.pivot_table('survived', ['sex', age], 'class')

# %%
# qcut(x) --> calculates quantiles based on x
fare = pd.qcut(titanic['fare'], 2)
pivot6 = titanic.pivot_table('survived', ['sex', age], [fare, 'class'])

# %%
pivot7 = titanic.pivot_table(index='sex', columns='class',
                             aggfunc={'survived': sum, 'fare': 'mean'})

# %%
# Totals along each group
pivot8 = titanic.pivot_table('survived', index='sex', columns='class', margins=True)

# %%
###############
# 12 Mart 2022
###############
agg_ = {'survived': ['sum', 'mean']}
pivot9 = titanic.pivot_table(values='survived',
                             index='sex',
                             columns='class',
                             aggfunc=agg_,
                             margins=False,
                             dropna=False,
                             fill_value='CEM',
                             margins_name='Toplam',
                             sort=True
                             )
# %%
url = 'https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv'
births = pd.read_csv(url)
# index_col=0,
# parse_dates=[0]
print(births.head())

# %%
births['decade'] = (births['year'] // 10) * 10

pivot1 = births.pivot_table(values='births', index='decade', columns='gender', aggfunc='sum')
pivot1['M/F Rate'] = pivot1['M'] / pivot1['F']

pivot1.insert(len(pivot1.columns) - 1, 'new col 1', pd.Series(pivot1['M'] / pivot1['F'], dtype='f'))
# %%

# pivot1 = pivot1.drop('new col 1')
pivot1 = pivot1.drop('new col 1', axis=1)

# %%
# Pivotun Grafigi
sns.set()  # gorsel unsurlarda seaborn kutuphanesinin kullanilmasi icin
print(plt.style.available)
plt.style.use('ggplot')
plt.interactive(True)

# %%
births.pivot_table('births', index='year', columns='gender', aggfunc='sum').plot()
plt.title('Number of Total Births per Decade', fontsize=16)
plt.ylabel('Total Births', fontsize=12)
plt.xlabel('Decade', fontsize=12)
plt.show()

# %%
####################################
# Outlier Detection and Elimination
####################################
# Interquartile Range Method
quartiles = np.percentile(births['births'], [25, 50, 75])
iqr = quartiles[2] - quartiles[0]
cut_off = 1.5 * iqr
lower = quartiles[0] - cut_off
upper = quartiles[2] + cut_off
births1 = births.query('(births > @lower) & (births < @upper)')

# %%
# Second Method
mu = quartiles[1]
sig = 0.74 * (quartiles[2] - quartiles[0])
births2 = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')

#%%
births = births1
# %%
# Create a 'date' variable
births['day'] = births['day'].astype(int)
# %%
births['day'] = births['day'].fillna(99)
births['day'] = births['day'].astype(int)
births.isna().sum()

# %%
births.index = pd.to_datetime(10000 * births.year +
                              100 * births.month +
                              births.day, format='%Y%m%d')
#, errors='coerce'
#%%
births['dayIndex'] = births.index.dayofweek

#%%
births.pivot_table('births', index='dayofweek',columns='decade', aggfunc='mean').plot()
plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
plt.title('mean births by day', fontsize=16)
plt.ylabel('Total Births', fontsize=12)
plt.xlabel('Decade', fontsize=12)
plt.show()

#%%
# Takvim bunu bazinda ortalama dogum adetleri
births_by_date = births.pivot_table('births', [births.index.month, births.index.day])
print(births_by_date.head())

#%%
# Adding a dummy year to make plot easier
births_by_date.index = [pd.datetime(2012, month, day)
                        for (month, day) in births_by_date.index]
births_by_date.head()

#%%
print(plt.style.available)
plt.style.use('bmh')
fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax);

#%%


















