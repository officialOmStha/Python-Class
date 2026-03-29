import pandas as pd
import numpy as np
import random
import string
import matplotlib.pyplot as plt

# -------------------------------
# 1. Create Dataset (100+ rows)
# -------------------------------

def random_name():
    return ''.join(random.choices(string.ascii_uppercase, k=5))

def random_address():
    return "Street-" + str(random.randint(1, 50))

def random_phone():
    prefixes = ["98", "97", "95", "96", "94"]
    return random.choice(prefixes) + ''.join(random.choices(string.digits, k=8))

data = []
for _ in range(120):  # 100+ rows
    data.append([
        random_name(),
        random_address(),
        random.randint(18, 60),
        random_phone()
    ])

df = pd.DataFrame(data, columns=["Name", "Address", "Age", "Phone"])

# Introduce missing values
for _ in range(10):
    df.loc[random.randint(0, 119), "Age"] = np.nan
    df.loc[random.randint(0, 119), "Phone"] = np.nan

# -------------------------------
# a. Show first two rows
# -------------------------------
print("First two rows:")
print(df.head(2))

# -------------------------------
# b. Find missing values
# -------------------------------
print("\nMissing values:")
print(df.isnull().sum())

# -------------------------------
# c. Fill missing values
# -------------------------------
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Phone"] = df["Phone"].fillna("9800000000")

# -------------------------------
# d. Filter phone not starting with 98,97,95
# -------------------------------
filtered_df = df[~df["Phone"].astype(str).str.startswith(("98", "97", "95"))]

print("\nFiltered Data:")
print(filtered_df.head())

# -------------------------------
# e. Save clean data to CSV
# -------------------------------
df.to_csv("clean_data.csv", index=False)
print("\nCSV file saved as clean_data.csv")

# -------------------------------
# f. Visualizations
# -------------------------------

# Bar Graph (Top age counts)
df["Age"].astype(int).value_counts().head(10).plot(kind='bar')
plt.title("Age Frequency")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Pie Chart (Top addresses)
df["Address"].value_counts().head(5).plot(kind='pie', autopct='%1.1f%%')
plt.title("Address Distribution")
plt.ylabel("")
plt.show()

# Line Graph (Age trend)
df["Age"].reset_index(drop=True).plot(kind='line')
plt.title("Age Trend")
plt.xlabel("Index")
plt.ylabel("Age")
plt.show()

# Box Plot (Age)
plt.boxplot(df["Age"])
plt.title("Box Plot of Age")
plt.show()

# -------------------------------
# g. Scatter Plot
# -------------------------------
plt.scatter(range(len(df)), df["Age"])
plt.title("Scatter Plot (Index vs Age)")
plt.xlabel("Index")
plt.ylabel("Age")
plt.show()