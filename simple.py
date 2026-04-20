import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset_slr.csv")

# Select independent and dependent variables
x = df["YearsExperience"].to_numpy(dtype=float)
y = df["Salary"].to_numpy(dtype=float)

# Train model using least squares
x_mean = np.mean(x)
y_mean = np.mean(y)

numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)

if denominator == 0:
    raise ValueError("Cannot fit regression: all YearsExperience values are identical.")

m = numerator / denominator
b = y_mean - m * x_mean

# Print equation (NEW)
print(f"Regression Equation: y = {m:.2f}x + {b:.2f}")

# Predict values
y_pred = m * x + b

# Predict for a new value (NEW)
new_exp = 5
predicted_salary = m * new_exp + b
print(f"Predicted salary for {new_exp} years experience: {predicted_salary:.2f}")

# Plot graph
plt.scatter(x, y, color="green")   # changed color

# Sort before plotting line
sort_idx = np.argsort(x)
plt.plot(x[sort_idx], y_pred[sort_idx], color="blue")  # changed color

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression")

plt.grid(True)  # NEW

plt.show()