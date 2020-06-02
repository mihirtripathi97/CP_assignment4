#BEFORE RUNNING THE CODE ENSURE TO HAVE "p10data.txt" in same folder as that of this code.

import numpy as np
from scipy.optimize import minimize
import emcee
import corner
from matplotlib import pyplot as plt





x = np.loadtxt("p10data.txt", delimiter = '&' ,skiprows = 5, usecols = 1)     #import data
y = np.loadtxt("p10data.txt", delimiter = '&' ,skiprows = 5, usecols = 2)
yerr = np.loadtxt("p10data.txt", delimiter = '&' ,skiprows = 5, usecols = 3)


def log_likelyhood(theta,x,y,yerr):
    
    a,b,c=theta
    
    y_pred = a*(x**2) + b*x + c
    
    sigma2=yerr**2
    
    return (0.5 * np.sum(((y - y_pred)**2 / sigma2) + np.log(2 * np.pi * sigma2)))

def log_prior(theta):
    
    a,b,c=theta 
    if -500<a<500 and -500<b<500 and -500<c<500:
        return(0)
    else:
        return(-np.inf)

#posterior pdf

def log_probability(theta,x,y,yerr):
    
    if  np.isinf(log_prior(theta)):
        return(-np.inf)
    else:
        return(log_prior(theta) - log_likelyhood(theta, x,y,yerr))
    

#initialise markov chain

guess = (1.0,1.0,1.0)

soln = minimize(log_likelyhood,guess,args=(x,y,yerr))   

#50 markov chains each starting from near the maxima of prob distribution.

nwalkers = 50
ndim = 3

pos = soln.x + 1e-4*np.random.randn(nwalkers,ndim)

sampler=emcee.EnsembleSampler(nwalkers,ndim,log_probability,args=(x,y,yerr))
sampler.run_mcmc(pos,4000)
samples=sampler.get_chain()




plt.figure(figsize=(16,6))

plt.subplot(311)
plt.plot(samples[:,:,0],c="k")   #a
plt.xlabel('Step number') 
plt.ylabel('a')
plt.title("Markov Chains")

plt.subplot(312)
plt.plot(samples[:,:,1],c = "k")  #b
plt.xlabel('Step number') 
plt.ylabel('b')

plt.subplot(313)
plt.plot(samples[:,:,2],c = "k")  #c
plt.xlabel('Step number') 
plt.ylabel('c')

plt.show()


data=np.zeros([3,4000*50])
for i in range(3):
    data[i,:] = np.hstack(samples[:,:,i])

data = np.transpose(data)

a = np.median(data[:,0])
b = np.median(data[:,1])
c = np.median(data[:,2])    

plt.figure()
corner.corner(data,labels=['a', 'b', 'c'],show_titles=True,truths=[a,b,c])
plt.show()

X = np.linspace(50,300,500) 

for i in range(200):
    k = int(4000*50*np.random.uniform())
    a_pr = data[k,0]
    b_pr = data[k,1]
    c_pr = data[k,2]
    plt.plot(X, a_pr*X**2+b_pr*X+c_pr, c = "C2")
    


plt.plot(X, a*X**2 + b*X + c, "k", label = "Best fit model")    
plt.errorbar(x, y, yerr=yerr,fmt = 'ok',label = 'Data')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


print('Meadian values of a,b,c:',[a,b,c])
print('Mean values of a,b,c:',[np.mean(data[:,0]),np.mean(data[:,1]),np.mean(data[:,2])])
print('Standered deviations for a,b,c:',[np.std(data[:,0]),np.std(data[:,1]),np.std(data[:,2])]) 






