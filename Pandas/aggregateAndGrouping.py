import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Sita", "Gita"],
    "Class": ["A", "A", "B", "B"],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print(df["Marks"].mean())
print(df["Marks"].sum())

# Group by
grouped = df.groupby("Class")["Marks"].mean()
print(grouped)