# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:32:51 2023

@author: Manoj
"""

from sklearn import neighbors 
predictors = np.random.random(1000).reshape(500,2)
target = np.around(predictors.dot(np.array([0.4, 0.6])) +
np.random.random(500))
clf = neighbors.KNeighborsClassifier(n_neighbors=10)
knn = clf.fit(predictors,target)
knn.score(predictors, target)