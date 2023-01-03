import numpy as np 
import matplotlib.pyplot as plt 

x = np.random.randint(10,10000,500)
y = np.random.randint(10,10000,500)

a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,4,5,6,7,8,9]

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("Scatter Plot")

plt.scatter(a, b, label="Random Data", color='b', marker='o')
plt.legend()

z = np.polyfit(a, b, 1)
p = np.poly1d(z)
plt.plot(a,p(a),"r--")

plt.show()