import matplotlib.pyplot as plt 
import numpy as np 

x = 100 * np.random.randn(10000)
plt.hist(x, bins=10, align='mid', label='CPI', histtype="bar")

plt.title("CPI Histogram")
plt.legend()
plt.show()