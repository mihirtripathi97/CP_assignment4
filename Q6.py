

import numpy as np
import matplotlib.pyplot as plt

def g(x):
    y=[]
    for i in range(len(x)):
        y.append(1.5*np.exp(-x[i]))
        
    
    return(y)

def f(x):
    
    return(np.exp(-(x*x/2))*np.sqrt(2/np.pi))


    
x = np.random.rand(10000)
x = -np.log(x)  # gives random numbers with pdf equal to g(x)
y = np.random.rand(10000)*g(x)

X = np.linspace(np.min(x),np.max(x),10000)
Y = g(X)

fx = []
for i in range(len(X)):
    fx.append(f(X[i]))
    
y_good = y[y < f(x)]
x_good = x[y < f(x)]
    



#plt.scatter(x_good,y_good,c = 'k',label = "Points")
plt.hist(x_good, range=(0, 4.0),bins = 40, density=True,label="Histogram")
plt.title("PDF of 10000 random numbers with required distribution")
#plt.plot(X,Y,c="r")
plt.plot(X,fx,c="g",label = "PDF")
plt.xlabel("X")
plt.ylabel("PDF")
plt.grid(True)
plt.legend()
plt.show()






