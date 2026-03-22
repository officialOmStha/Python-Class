import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

fig, axs = plt.subplots(1, 2, figsize=(8, 4))

axs[0].plot(x, y)
axs[0].set_title("Line")

axs[1].bar(x, y)
axs[1].set_title("Bar")

fig.tight_layout()
plt.show()