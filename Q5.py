#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


x1 = np.random.rand(10000)
np.random.seed(23)
x2 = np.random.rand(10000)

X = np.linspace(-4,4,10000)
Y = np.exp(-(X*X)/2)/(np.sqrt(2*np.pi))

y1 = np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)    #from Box Muller algo.
#y2 = np.sqrt(-2*np.log(x1)) * np.sin(2*np.pi*x2)

plt.hist(y1, range=(-4.0, 4.0),bins = 45, density=True)
plt.title("PDF of 10000 random numbers with gaussian probability distribution.")
plt.plot(X,Y)
plt.xlabel("Xi")
plt.ylabel("PDF")
plt.grid(True)

plt.show()


# In[ ]:





# In[ ]:




