import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV file
df = pd.read_csv("gaming_dataset.csv")

# Display dataset
print("----- Gaming Dataset -----")
print(df)

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nDataset Information")
df.info()

print("\nData Types")
print(df.dtypes)

print("\nAverage Gaming Statistics")
print(df[["Gaming Hours", "Games Played", "Win Percentage"]].mean())

print("\nHighest Gaming Statistics")
print(df[["Gaming Hours", "Games Played", "Win Percentage"]].max())

print("\nLowest Gaming Statistics")
print(df[["Gaming Hours", "Games Played", "Win Percentage"]].min())

# -------------------------------
# BAR CHART
# -------------------------------
plt.figure(figsize=(10, 5))
sns.barplot(data=df)
plt.title("Games Played by Each Player")
plt.xlabel("Player")
plt.ylabel("Games Played")
plt.xticks(rotation=60)
plt.tight_layout()
plt.show()

# -------------------------------
# PIE CHART
# -------------------------------
performance_count = df["Performance"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    performance_count.values,
    labels=performance_count.index,
    autopct="%1.1f%%"
)
plt.title("Player Performance Distribution")
plt.show()

# -------------------------------
# SCATTER PLOT
# -------------------------------
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Games Played",
    y="Win Percentage",
    hue="Performance",
    s=100
)
plt.title("Games Played vs Win Percentage")
plt.xlabel("Games Played")
plt.ylabel("Win Percentage")
plt.tight_layout()
plt.show()

# -------------------------------
# LINE CHART
# -------------------------------
plt.figure(figsize=(10, 5))
plt.plot(
    df["Player"],
    df["Gaming Hours"],
    marker="o"
)
plt.title("Gaming Hours of Each Player")
plt.xlabel("Player")
plt.ylabel("Gaming Hours")
plt.xticks(rotation=60)
plt.tight_layout()
plt.show()

# -------------------------------
# BOX PLOT
# -------------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df[["Gaming Hours", "Games Played", "Win Percentage"]]
)
plt.title("Gaming Statistics Distribution")
plt.ylabel("Values")
plt.tight_layout()
plt.show()

print("\nPerformance Count")
print(df["Performance"].value_counts())
