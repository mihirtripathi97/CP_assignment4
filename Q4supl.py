#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

x1,x2 = np.loadtxt("Q4data.txt",usecols=(0,1),unpack= True)
X = np.linspace(0,3,10000)
Y = 2*np.exp(-X/0.5)

plt.hist(x1, range=(0, 1),bins = 10, density=True)
plt.title("PDF of 10000 random numbers with uniform probability distribution.")

plt.xlabel("X")
plt.ylabel("PDF")
plt.grid(True)

plt.show()

plt.hist(x2,range=(0, 3) , bins = 50, density=True)
plt.title("PDF of 10000 random numbers with exponential distribution with mean 0.5.")
plt.plot(X,Y,label = "Probability Distribution function.")
plt.xlabel("X")
plt.ylabel("PDF")
plt.grid(True)
plt.legend()
plt.show()


# In[ ]:




