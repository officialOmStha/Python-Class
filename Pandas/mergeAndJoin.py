import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["Ram", "Shyam"]
})

df2 = pd.DataFrame({
    "ID": [1, 2],
    "Marks": [85, 90]
})

merged = pd.merge(df1, df2, on="ID")
print(merged)

# Concatenate
concat = pd.concat([df1, df2], axis=1)
print(concat)