# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 12:21:49 2023

@author: Manoj
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
import math
#%matplotlib inline

np.random.seed(1234)

long_breaks = stats.poisson.rvs(loc=10, mu=60, size=3000)
# represents 3000 people who take about a 60 minute break
#pd.Series(long_breaks).hist()

short_breaks = stats.poisson.rvs(loc=10, mu=15, size=6000)
# represents 6000 people who take about a 15 minute break
#pd.Series(short_breaks).hist()

breaks = np.concatenate((long_breaks, short_breaks))
# put the two arrays together to get our "population" of 9000 people
#pd.Series(breaks).hist()

print(breaks.mean())
# 39.99 minutes is our parameter.

sample_breaks = np.random.choice(a = breaks, size=100)
# taking a sample of 100 employees

print(breaks.mean() - sample_breaks.mean())
# difference between means 
'''
employee_races = (["white"]*2000) + (["black"]*1000) +\
(["hispanic"]*1000) + (["asian"]*3000) +\
(["other"]*3000)

#take a random sample of 1,000 people

demo_sample = random.sample(employee_races, 1000) 
for race in set(demo_sample):
    print( race + " proportion estimate:" )
    print( demo_sample.count(race)/1000. )
    
    
#pd.DataFrame(breaks).hist(bins=50,range=(5,100))


#Sampling Distributions
point_estimates = []
for x in range(500):         # Generate 500 samples
    sample = np.random.choice(a= breaks, size=100) #take a sample of 100 points
    point_estimates.append( sample.mean() )
    
pd.DataFrame(point_estimates).hist()

print(breaks.mean() - np.array(point_estimates).mean())

#CONFIDENCE INTERVAL
sample_size = 100
sample = np.random.choice(a= breaks, size = sample_size)

sample_mean = sample.mean() # sample mean

sample_stdev = sample.std() # sample standard deviation

sigma = sample_stdev/math.sqrt(sample_size)  
# population Standard deviation estimate

print(stats.t.interval(confidence= 0.95,              # Confidence level
                 df= sample_size - 1,       # Degrees of freedom
                 loc = sample_mean,         # Sample mean
                 scale = sigma))             # Standard deviation estimate


#make confidence interval
def makeConfidenceInterval():
    sample_size = 100
    sample = np.random.choice(a= breaks, size = sample_size)

    sample_mean = sample.mean()
    # sample mean

    sample_stdev = sample.std()    
    # sample standard deviation

    sigma = sample_stdev/math.sqrt(sample_size)  
    # population Standard deviation estimate

    return stats.t.interval(confidence=0.95,              # Confidence level
                     df= sample_size - 1,       # Degrees of freedom
                     loc = sample_mean,         # Sample mean
                     scale = sigma)             # Standard deviation estimate

times_in_interval = 0.
for i in range(10000):
    interval = makeConfidenceInterval()
    if 39.99 >= interval[0] and 39.99 <= interval[1]:
    # if 39.99 falls in the interval
        times_in_interval += 1

print(times_in_interval / 10000)


for confidence in (.5, .8, .85, .9, .95, .99):
    confidence_interval = stats.t.interval(confidence=confidence,
                      df= sample_size - 1,      
                     loc = sample_mean,
                     scale = sigma)  
    length_of_interval = round(confidence_interval[1] -confidence_interval[0], 2)
# the length of the confidence interval
print("confidence {0} has a interval of size {1}".format(confidence, length_of_interval))
'''
long_breaks_in_engineering = stats.poisson.rvs(loc=10, mu=55,size=100)
short_breaks_in_engineering = stats.poisson.rvs(loc=10, mu=15,size=300)
engineering_breaks = np.concatenate((long_breaks_in_engineering,short_breaks_in_engineering))
#print(breaks.mean()) # 39.99
#print(engineering_breaks.mean())


t_statistic, p_value = stats.ttest_1samp(a= engineering_breaks, popmean= breaks.mean())
print(t_statistic, p_value)