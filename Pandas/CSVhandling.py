import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Sita", "Gita"],
    "Class": ["A", "A", "B", "B"],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

# Save CSV
df.to_csv("students.csv", index=False)

# Read CSV
df2 = pd.read_csv("students.csv")

print(df2.info())
print(df2.describe())