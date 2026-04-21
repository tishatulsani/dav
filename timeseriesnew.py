import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("/Users/geetmulki/Desktop/davpractical/dav/timeseries.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

# Trend (rolling mean)
df["trend"] = df["value"].rolling(window=5).mean()

# Exponential smoothing
df["smooth"] = df["value"].ewm(span=5).mean()

# Simple forecasting
df["forecast"] = df["value"].shift(1)

# Print first few rows (NEW)
print(df.head())

# Plot
plt.figure(figsize=(10, 5))  # NEW

plt.plot(df["value"], label="Original", color="black")
plt.plot(df["trend"], label="Trend", color="blue")
plt.plot(df["smooth"], label="Smoothed", color="green")

plt.title("Time Series Analysis")  # NEW
plt.xlabel("Date")                # NEW
plt.ylabel("Value")               # NEW

plt.legend()
plt.grid(True)  # NEW

plt.show()
