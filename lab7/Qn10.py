# Subplots (Multiple Charts in One Window)
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Line")

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title("Bar")

plt.show()