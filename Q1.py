


import numpy as np
import matplotlib.pyplot as plt

a = 1864525
c = 1013904223
m = 529967296
x = 1
n = 10000
I = []

results = []
for i in range(n):
    I.append(i)
    x = (a*x+c)%m
    R = x/m
    results.append(R)


plt.hist(results, range=(0.0, 1.0),density=True)
plt.show()







