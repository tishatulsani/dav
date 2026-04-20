
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("data.csv")

# Select multiple independent variables and one dependent variable
X = df[["x1", "x2", "x3"]]   # multiple independent variables
y = df["y"]                  # dependent variable

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict values
y_pred = model.predict(X)

# Print coefficients
print(model.coef_)
print(model.intercept_)

#VISUALIZE HARD CODE
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from mpl_toolkits.mplot3d import Axes3D

# # Load dataset
# df = pd.read_csv("multiple.csv")

# # Independent & dependent variables
# X = df[["x1", "x2"]]
# y = df["y"]

# # Train model
# model = LinearRegression()
# model.fit(X, y)

# # Print equation
# print(f"y = {model.intercept_:.2f} + "
#       f"{model.coef_[0]:.2f}*x1 + {model.coef_[1]:.2f}*x2")

# # -------- 3D Visualization -------- #

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Scatter plot (actual data)
# ax.scatter(df["x1"], df["x2"], y)

# # Create grid for surface
# x1_range = np.linspace(df["x1"].min(), df["x1"].max(), 10)
# x2_range = np.linspace(df["x2"].min(), df["x2"].max(), 10)

# x1_grid, x2_grid = np.meshgrid(x1_range, x2_range)

# # Predict values for grid (plane)
# y_grid = (model.intercept_ +
#           model.coef_[0] * x1_grid +
#           model.coef_[1] * x2_grid)

# # Plot surface (regression plane)
# ax.plot_surface(x1_grid, x2_grid, y_grid, alpha=0.3)

# # Labels
# ax.set_xlabel("x1")
# ax.set_ylabel("x2")
# ax.set_zlabel("y")

# plt.title("Multiple Linear Regression (3D)")
# plt.show()
