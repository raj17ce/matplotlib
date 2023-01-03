import matplotlib.pyplot as plt 

###

# v = [1776, 876, 760, 2883, 215]
# l = ["Food", "Travel", "Entertainment", "University", "utilities"]

# plt.pie(v, labels=l, autopct="%1.1f")
# plt.legend(title = "My Expenses")
# plt.show()

###
# Q-1

names = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
values = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.title("Popularity of programming languages")
plt.pie(values, labels=names, autopct="%1.1f")

plt.show()