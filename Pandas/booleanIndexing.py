import pandas as pd

df = pd.DataFrame({
    "Name": ["Ram", "Shyam", "Sita"],
    "Marks": [85, 60, 75],
    "Age": [18, 20, 17]
})

filtered = df[(df["Marks"] > 70) & (df["Age"] < 19)]
print(filtered)