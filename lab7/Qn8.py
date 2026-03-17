# Area Chart
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 15, 20, 25]

plt.fill_between(x, y)
plt.title("Area Chart")
plt.show()