import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Sita", "Gita"],
    "Age": [18, 19, 17, 18],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

# Single column
print(df["Name"])

# Multiple columns
print(df[["Name", "Marks"]])

# Using loc
print(df.loc[0])  

# Using iloc
print(df.iloc[1])

# Filter
print(df[df["Marks"] > 80])