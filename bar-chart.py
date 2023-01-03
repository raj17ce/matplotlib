import matplotlib.pyplot as plt

y = [3, 12, 5, 18, 45]
x = ["A", "B", "C", "D", "E"]
c = ['r', 'b', 'g', 'k', 'y']

plt.bar(x, y, color=c)
plt.title("Bar Chart")

plt.show()