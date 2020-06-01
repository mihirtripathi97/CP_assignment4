


import numpy as np
from matplotlib import pyplot as plt

def f(x):
    if (x<7 and x>3):
        return(1)
    else: 
        return(1e-12)

n=100000
th=[0]

for i in range(n):
    
    th_prm = th[i] + np.random.normal()
    r = np.random.rand() 
    
    if f(th_prm)/f(th[i]) > r:
        th.append(th_prm)
    else:
        th.append(th[i])  
        
        
x=np.linspace(3,7,50)
y=[]

for i in range(50):
    y.append(f(x[i])/4)

plt.plot(x,y,label = "PDF",c="k")
plt.hist(th,range=(3,7),density=True)
plt.title("Comparision between histogram and PDF")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(15,4))
plt.plot(th[0:5000])
plt.ylim(0,9)
plt.title("Markov chain")
plt.show()        







