
import numpy as np

def f(x,y):
    if ( (x*x + y*y) <= 1):
        return(1)
    else:
        return(0)

x = np.random.rand(100000)
y = np.random.rand(100000)


A = 0
for i in range(100000):

    if(x[i]**2 + y[i]**2 <= 1):
        A = A+1
A = 4*A/100000
print("Area of 2 dimentional unit sphere:",A)

n=100000
x=np.zeros([n,10])
for i in range(10):
    x[:,i]=np.random.random(n)
A=0    
for i in range(n):
    if sum(x[i,:]**2)<1:
        A=A+1
V=2**10*A/n
print('Volume of 10 dimentional unit sphere:',V)





