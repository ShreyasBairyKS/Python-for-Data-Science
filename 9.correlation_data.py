# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:18:23 2023

@author: Manoj
"""
import pandas as pd

friends = [109, 1017, 1127, 418, 625, 957, 89, 950, 946, 797,
981, 125, 455, 731, 1640, 485, 1309, 472, 1132, 1773, 906, 531,
742, 621]


happiness = [.8, .6, .3, .6, .6, .4, .8, .5, .4, .3, .3, .6, .2,
.8, 1, .6, .2, .7, .5, .3, .1, 0, .3, 1]

df = pd.DataFrame({'friends':friends, 'happiness':happiness})
print(df.head())

from sklearn import preprocessing
df_scaled = pd.DataFrame(preprocessing.scale(df), columns =
['friends_scaled', 'happiness_scaled'])
print(df_scaled.head())


df_scaled.plot(kind='scatter', x = 'friends_scaled', y =
'happiness_scaled')

# correlation between variables
print(df.corr())