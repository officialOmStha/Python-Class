import numpy as np
import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Sita", "Gita"],
    "Age": [18, 19, 17, 18],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

df.loc[2, "Marks"] = np.nan

print(df.isnull())

# Fill missing with mean
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Rename column
df.rename(columns={"Marks": "Score"}, inplace=True)

print(df)