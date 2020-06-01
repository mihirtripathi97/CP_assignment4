


import numpy as np
import matplotlib.pyplot as plt




y = np.random.rand(10000)

plt.hist(y, range=(0.0, 1.0),bins= 20,density=True)
plt.title("PDF of 1000 uniform deviates between 0 and 1")
plt.xlabel("Xi")
plt.ylabel("PDF")


plt.show()
    






