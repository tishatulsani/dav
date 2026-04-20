import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset_logi.csv")

# Use one numeric feature and build a binary target from available labels
x = df["efficiency_score"].to_numpy(dtype=float)

# Treat "High Efficiency" as class 1, all other labels as class 0
y_labels = df["calorie_efficiency"].astype(str).str.strip().to_numpy()
y = (y_labels == "High Efficiency").astype(float)

# Initialize weights
w = 0.0
b = 0.0
lr = 0.01

# Sigmoid function
def sigmoid(z):
    z = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z))

# Training (simple loop)
for i in range(100):
    z = w * x + b
    y_pred = sigmoid(z)
    
    # Gradient
    dw = ((y_pred - y) * x).mean()
    db = (y_pred - y).mean()
    
    # Update
    w -= lr * dw
    b -= lr * db

print(w, b)

# Plot: sampled data points and fitted logistic curve
sample_size = min(5000, x.shape[0])
rng = np.random.default_rng(42)
sample_idx = rng.choice(x.shape[0], size=sample_size, replace=False)

x_line = np.linspace(x.min(), x.max(), 300)
y_line = sigmoid(w * x_line + b)

plt.figure(figsize=(10, 6))
plt.scatter(x[sample_idx], y[sample_idx], alpha=0.15, s=10, label="Sampled Data")
plt.plot(x_line, y_line, color="red", linewidth=2, label="Logistic Curve")
plt.xlabel("Efficiency Score")
plt.ylabel("Probability of High Efficiency")
plt.title("Logistic Regression from Scratch")
plt.legend()
plt.grid(alpha=0.2)
plt.show()