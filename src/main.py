import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

data = pd.read_csv('/content/Cricket_Player_Statistics.csv')

# Convert the DataFrame to a Tabular format
table = tabulate(data, headers='keys', tablefmt='grid')
print(table)

# Use NumPy to find the highest score
data['Highest Score'] = data['Highest Score'].str.replace('*', '', regex=False)
data['Highest Score'] = pd.to_numeric(data['Highest Score'], errors='coerce')   
highest_score = np.max(data['Highest Score'].to_numpy())
print("The highest score among all players is:", highest_score)

# Use NumPy to find the highest number of fifties
data['Fifties'] = pd.to_numeric(data['Fifties'], errors='coerce')
highest_fifties = np.max(data['Fifties'].to_numpy())
print("The highest number of fifties among all players is:", highest_fifties)

# Use NumPy to find the highest number of sixes
data['Sixes'] = pd.to_numeric(data['Sixes'], errors='coerce')
highest_sixes = np.max(data['Sixes'].to_numpy())
print("The highest number of sixes by any player is:", highest_sixes)

# Use NumPy to find the highest number of fours
data['Fours'] = pd.to_numeric(data['Fours'], errors='coerce')
highest_fours = np.max(data['Fours'].to_numpy())
print("The highest number of fours by any player is:", highest_fours)

# Use NumPy to find the highest strike rate
data['Strike Rate'] = pd.to_numeric(data['Strike Rate'], errors='coerce')
highest_strike_rate = np.max(data['Strike Rate'].to_numpy())
print("The highest strike rate among all players is:", highest_strike_rate)

# Filter players with an Average Score Per Match above 40 and Calculate the Average Score Per Match
data['Average Score Per Match'] = data['Total Runs'] / data['Matches Played']
high_avg_players = data[data['Average Score Per Match'] > 40]
print("\nPlayers with Average Score Per Match above 40:\n", high_avg_players)

# Sort the DataFrame by Total Runs in descending order
sorted_data = data.sort_values(by='Total Runs', ascending=False)
print("\nDataFrame sorted by Total Runs:\n", sorted_data)

# Visualizing the data using Matplotlib
# 1. Total Runs by Players
plt.figure(figsize=(12, 6))
plt.bar(data["Player"], data["Total Runs"], color="skyblue")
plt.title("Total Runs by Players", fontsize=16)
plt.xlabel("Player", fontsize=12)
plt.ylabel("Total Runs", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Strike Rate Comparison
plt.figure(figsize=(12, 6))
plt.plot(data["Player"], data["Strike Rate"], marker="o", color="red", label="Strike Rate")
plt.title("Strike Rate Comparison", fontsize=16)
plt.xlabel("Player", fontsize=12)
plt.ylabel("Strike Rate", fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# 3. Fours vs Sixes
plt.figure(figsize=(12, 6))
plt.scatter(data["Fours"], data["Sixes"], color="black", s=100, alpha=0.6)
plt.title("Fours vs Sixes", fontsize=16)
plt.xlabel("Fours", fontsize=12)
plt.ylabel("Sixes", fontsize=12)
plt.tight_layout()
plt.show()

# 4. Centuries and Fifties
plt.figure(figsize=(12, 6))
width = 0.35
x = range(len(data["Player"]))
plt.bar(x,data["Centuries"], width=width, label="Centuries", color="orange")
plt.bar([i + width for i in x], data["Fifties"], width=width, label="Fifties", color="purple")
plt.title("Centuries and Fifties by Players", fontsize=16)
plt.xlabel("Player", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.xticks([i + width/2 for i in x], data["Player"], rotation=45)
plt.legend()
plt.tight_layout()
plt.show()