#  Bar chart

import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 2]

plt.bar(categories, values)
plt.title("Bar Chart")
plt.show()