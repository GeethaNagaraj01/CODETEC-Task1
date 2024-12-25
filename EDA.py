import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('my_dataset.csv')
print("First few rows of the dataset:")
print(df.head())
print("\nMissing values in the dataset:")
print(df.isnull().sum())
print("\nSummary statistics of the dataset:")
print(df.describe())
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], kde=True, bins=10, color='blue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Age', y='Salary', data=df, color='red')
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()
# Heatmap of correlations (only numeric columns)
plt.figure(figsize=(8, 5))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
