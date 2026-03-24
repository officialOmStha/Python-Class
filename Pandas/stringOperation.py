import pandas as pd

df = pd.DataFrame({
    "Name": ["ram", "shyam", "sita"]
})

df["Name"] = df["Name"].str.upper()
print(df)

df["Name"] = df["Name"].str.replace("A", "@")
print(df)