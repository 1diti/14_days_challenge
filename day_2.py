# -*- coding: utf-8 -*-
"""day 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e8bxSDrIEOV56PWmfQ0BiqjPb5lUQyMz
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

price = [100, 250, 310, 600, 850]
size = [1000, 2300, 3000, 5700, 8100]

size2 = np.array(size).reshape((-1, 1))

regr = linear_model.LinearRegression()
regr.fit(size2, price)
print('Coefficients: \n', regr.coef_)
print('intercept: \n', regr.intercept_)

def graph(formula, x_range):
   x = np.array(x_range)
   y = eval(formula)
   plt.plot(x, y)

graph('regr.coef_*x + regr.intercept_', range(1000, 10000))
print (regr.score(size2, price))

plt.scatter(size,price, color='black')
plt.ylabel('price')
plt.xlabel('size ')
plt.show()