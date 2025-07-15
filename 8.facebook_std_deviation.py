# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:48:28 2023

@author: Manoj
"""
import numpy as np
import matplotlib.pyplot as plt

friends = [109, 1017, 1127, 418, 625, 957, 89, 950, 946, 797, 981, 125, 455, 731, 1640, 485, 1309, 472, 1132, 1773, 906, 531, 742, 621]

print(np.mean(friends)) #789.1
print(np.median(friends)) #769.5
print((np.max(friends)) - (np.min(friends))) #1684
print(np.std(friends)) # 425.2

y_pos = range(len(friends))
#plt.bar(y_pos, friends)
'''
plt.plot((0, 25), (789, 789), 'b-')
plt.plot((0, 25), (789+425, 789+425), 'g-')
plt.plot((0, 25), (789-425, 789-425), 'r-')
'''

z_scores = []
m = np.mean(friends) # average friends on Facebook
s = np.std(friends) # standard deviation friends on Facebook
for friend in friends:
    z = (friend - m)/s # z-score
    z_scores.append(z) # make a list of the scores for plotting
    
plt.bar(y_pos, z_scores)

plt.bar(y_pos, z_scores)
plt.plot((0, 25), (1, 1), 'g-')
plt.plot((0, 25), (0, 0), 'b-')
plt.plot((0, 25), (-1, -1), 'r-')