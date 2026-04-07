import matplotlib.pyplot as plt

x = ["A", "B", "C", "D"]
y = [20, 80, 33, 42]

plt.subplot(1,2,1)
plt.pie(y, labels=x)
plt.title("Pie Chart")
plt.xlabel("Basis")
plt.ylabel("Cost")


plt.subplot(1,2,2)
plt.bar(x,y)
plt.title("Bar Chart")
plt.xlabel("Basis")
plt.ylabel("Cost")

plt.show()