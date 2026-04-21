# Exploratory Data Analysis (EDA) in Python

# Step 1: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load dataset
# Replace 'data.csv' with your file name
df = pd.read_csv("/Users/geetmulki/Desktop/davpractical/dav/edadata.csv")

print("\nFirst 5 rows of dataset:")
print(df.head())

# Step 3: Dataset information
print("\nDataset Info:")
print(df.info())

# Step 4: Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Step 5: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 6: Handle missing values (replace with mean)
df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nMissing values handled.")

# Step 7: Correlation matrix
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

# Step 8: Heatmap visualization
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Step 9: Histogram for numeric columns
df.hist(figsize=(10,8))
plt.suptitle("Histogram of Dataset Features")
plt.show()

# Step 10: Boxplot for outlier detection
plt.figure(figsize=(8,6))
sns.boxplot(data=df.select_dtypes(include=np.number))
plt.title("Boxplot for Outlier Detection")
plt.show()

# Step 11: Scatter plot (first two numeric columns)
numeric_cols = df.select_dtypes(include=np.number).columns

if len(numeric_cols) >= 2:
    sns.scatterplot(x=df[numeric_cols[0]], y=df[numeric_cols[1]])
    plt.title("Scatter Plot")
    plt.show()

print("\nEDA Completed Successfully ✅")