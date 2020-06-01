

import timeit

set_up = '''
import numpy as np
import matplotlib.pyplot as plt

a = 1864525
c = 1013904223
m = 529967296
x = 1
n = 10000

'''


mycode  = '''

I = []
results = []
for i in range(n):
    I.append(i)
    x = (a*x+c)%m
    R = x/m
    results.append(R)
    
'''
t = timeit.timeit(setup = set_up,stmt = mycode,number = 500)/500
print("Time taken by the method used in first question to generate 10000 random numbers is : %.5e" % t,"s" )

set_up = '''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
'''

mycode ='''

y = []    
y = np.random.rand(10000)
'''
t = timeit.timeit(setup = set_up,stmt = mycode,number = 500)/500
print("Time taken by the method used in second question to generate 10000 random numbers is : %.5e" % t,"s" )

