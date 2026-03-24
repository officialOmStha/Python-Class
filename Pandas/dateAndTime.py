import pandas as pd

df = pd.DataFrame({
    "Date": ["2024-01-01", "2023-05-10"]
})

df["Date"] = pd.to_datetime(df["Date"])

# Extract year
df["Year"] = df["Date"].dt.year

# Filter
print(df[df["Year"] == 2024])