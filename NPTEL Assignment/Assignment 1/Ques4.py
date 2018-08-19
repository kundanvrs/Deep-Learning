# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 02:04:24 2018

@author: Kundan
"""

import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('dataset.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=' ')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.scatter(x,y)
#plt.scatter(x, color='b')
plt.xlabel('x')
plt.ylabel('y')

plt.show()
