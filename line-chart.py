import matplotlib.pyplot as plt
import numpy as np

###
# normal

# l1 = [1,2,3,4,5]
# l2 = [1,2,3,4,5]

# plt.plot(l1,l2)
# plt.show()

###
# saving to png

# x = np.linspace(-1,1,50)
# print(x)

# y1 = 2*x+1
# y2 = 2**x

# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.savefig("line.png", format='png')

###
# setting axis, ticks, grid, labels

# values = [5,2,9,4,2,3,9,7,6,5,4,5,6,4,5,2]

# plt.xlim([0,10])
# plt.ylim([0,10])

# plt.xlabel("weight")
# plt.ylabel("value")

# plt.xticks([0,2,4,5,8,10])
# plt.yticks([0,2,4,5,8,10])

# plt.title("Line Chart")

# plt.grid(True)

# plt.plot(values,values)
# plt.show()

###

# Q-1

# a = [1,2,3,4]
# b = [1,4,9,16]

# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")

# plt.plot(a,b)
# plt.show()

###
# Styling lines

# values1 = [5,8,9,4,1,6,7,2,3,8]
# values2 = [8,3,2,7,6,1,4,9,8,5]

# plt.plot(range(1,11),values1, c='r', lw='1', ls='--', marker=">")
# plt.plot(range(1,11),values2, c='b', lw='2', ls=':', marker="o")

# plt.show()

###
# Setting legend, annotation, labels

# values1 = [5,8,9,4,1,6,7,2,3,8]
# values2 = [8,3,2,7,6,1,4,9,8,5]

# plt.plot(range(1,11),values1)
# plt.plot(range(1,11),values2)

# plt.xlabel("Roll-No")
# plt.ylabel("CPI")

# plt.legend(['CX','CY'])
# plt.annotate(xy=[5,1], text='Lowest CPI')

# plt.show()