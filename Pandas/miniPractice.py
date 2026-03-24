import pandas as pd

df = pd.read_csv("students.csv")

# Clean
df.dropna(inplace=True)

# Add column
df["Passed"] = df["Marks"] > 40

# Group
print(df.groupby("Passed")["Marks"].mean())