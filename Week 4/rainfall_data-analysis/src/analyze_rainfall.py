import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("MSE800/Week 4/rainfall_data-analysis/data/1924-to-1987_monthly-anually_rainfall.csv")

# Show basic info
print(df.info())
print(df.describe())

# Handle missing values (optional: interpolate or drop)
df_clean = df.copy()
df_clean.interpolate(inplace=True)

# Plot annual rainfall over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_clean, x='YEAR', y='ANNUAL', marker='o')
plt.title('Annual Rainfall (1924–1987)')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.tight_layout()
plt.show()

monthly_cols = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
                'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
monthly_avg = df_clean[monthly_cols].mean()

plt.figure(figsize=(10, 5))
monthly_avg.plot(kind='bar', color='skyblue')
plt.title('Average Monthly Rainfall (1924–1987)')
plt.ylabel('Rainfall (mm)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Heatmap of monthly rainfall by year
plt.figure(figsize=(14, 8))
sns.heatmap(df_clean[monthly_cols], cmap="YlGnBu", cbar_kws={'label': 'Rainfall (mm)'})
plt.title('Heatmap of Monthly Rainfall')
plt.xlabel('Month')
plt.ylabel('Year Index')
plt.tight_layout()
plt.show()
