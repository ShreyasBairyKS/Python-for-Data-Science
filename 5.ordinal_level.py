# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 22:50:13 2023

@author: Manoj
"""

import numpy
results = [5, 4, 3, 4, 5, 3, 2, 5, 3, 2, 1, 4, 5, 3, 4, 4, 5, 4,
2, 1, 4, 5, 4, 3, 2, 4, 4, 5, 4, 3, 2, 1]
sorted_results = sorted(results)
print(sorted_results)

print (numpy.mean(results)) # == 3.4375
print (numpy.median(results)) # == 4.0


#The reason that the mean would not be as mathematically viable is because if we
#subtract/add two scores, say a score of four minus a score of two, the
#difference of two does not really mean anything. If addition/subtraction
#among the scores doesn't make sense, the mean won't make sense either.