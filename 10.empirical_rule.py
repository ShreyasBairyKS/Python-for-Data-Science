# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 13:02:07 2023

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


# finding the percentage of people within one standard deviation of the mean
within_1_std = df_scaled[(df_scaled['friends_scaled'] <= 1) & (df_scaled['friends_scaled'] >= -1)].shape[0] 
print(within_1_std / float(df_scaled.shape[0])) #0.75


# finding the percentage of people within two standard deviations of the mean
within_2_std = df_scaled[(df_scaled['friends_scaled'] <= 2) &
(df_scaled['friends_scaled'] >= -2)].shape[0]
print(within_2_std / float(df_scaled.shape[0]))
# 0.916


# finding the percentage of people within three standard deviations of the mean
within_3_std = df_scaled[(df_scaled['friends_scaled'] <= 3) &
(df_scaled['friends_scaled'] >= -3)].shape[0]
print(within_3_std / float(df_scaled.shape[0]))
# 1.0