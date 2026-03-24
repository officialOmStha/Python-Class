import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "Name": ["Ram", "Shyam", "Sita"],
    "Marks": [85, 90, 78]
})

df.plot(kind="bar", x="Name", y="Marks")
plt.show()