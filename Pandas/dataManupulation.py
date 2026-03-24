import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Sita", "Gita"],
    "Age": [18, 19, 17, 18],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

# Add column
df["Passed"] = df["Score"] > 40

# Delete column
df.drop("Age", axis=1, inplace=True)

# Apply function
df["Score"] = df["Score"].apply(lambda x: x + 5)

# Sort
df = df.sort_values(by="Score", ascending=False)

print(df)
