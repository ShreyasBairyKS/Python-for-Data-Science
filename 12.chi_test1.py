# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:41:43 2023

@author: Manoj
"""
import numpy as np
import scipy.stats as stats
observed = [102, 178, 186, 34]
expected = [156, 165.5, 147, 31.5]
chi_squared, p_value = stats.chisquare(f_obs= observed, f_exp=expected)
print(chi_squared, p_value)


observed = np.array([[134, 54],[110, 48]])
# built a 2x2 matrix as seen in the table above
chi_squared, p_value, degrees_of_freedom, matrix = stats.chi2_contingency(observed= observed)
print(chi_squared, p_value)
# (0.04762692369491045, 0.82724528704422262)