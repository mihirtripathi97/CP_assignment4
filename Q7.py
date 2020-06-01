


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scpst


Sr = [2,3,4,5,6,7,8,9,10,11,12]
e_ct =  [4,8,12,16,20,24,20,16,12,8,4]
o_ct1 = [4,10,10,13,20,18,18,11,13,14,13]
o_ct2 = [3,7,11,15,19,24,21,17,13,9,5]

v1 = 0
v2 = 0

for i in range(11):
    v1 = v1 + ((o_ct1[i] - e_ct[i])**2)/e_ct[i]
    v2 = v2 + ((o_ct2[i] - e_ct[i])**2)/e_ct[i]
    
#print(V1)
#print(V2)

p1 = (1.0 - scpst.chi2.cdf(v1, 10.0))*100
p2 = (1.0 - scpst.chi2.cdf(v2, 10.0))*100

print("Probability for v1 being greater then ",round(v1,3),"is :",round(p1,3),"%")
print("Probability for v2 being greater then ",round(v2,3),"is :",round(p2,3),"%")

print("Hence acording to chi square test both obersved random number sets are not sufficiently random.")




    





