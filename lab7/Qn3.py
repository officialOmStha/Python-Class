# Horizontal Bar Chart

import matplotlib.pyplot as plt

categories = ['A', 'B', 'C']
values = [5, 8, 3]

plt.barh(categories, values)
plt.title("Horizontal Bar Chart")
plt.show()