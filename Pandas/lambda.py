import pandas as pd

df = pd.DataFrame({
    "Marks": [80, 90, 70]
})

df["Marks"] = df["Marks"].apply(lambda x: x + 5)
print(df)