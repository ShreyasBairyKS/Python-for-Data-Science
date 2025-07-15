# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:01:49 2023

@author: Manoj
"""

import pandas as pd
# read in the CSV file from a URL
#drinks =pd.read_csv('https://raw.githubusercontent.com/sinanuozdemir/principles_of_data_science/master/data/chapter_2/drinks.csv')
drinks =pd.read_csv('alcohol-consumption.csv')
# examine the data's first five rows
print(drinks.head())

print(drinks['country'].describe())
#print(drinks['continent'].describe())
print(drinks['beer_percentage'].describe())

#print(drinks['beer_servings'].describe())