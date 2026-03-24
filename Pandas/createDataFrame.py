import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Sita", "Gita"],
    "Age": [18, 19, 17, 18],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)