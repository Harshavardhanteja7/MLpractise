import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Historical project data
pages = [5, 12, 8, 3, 12, 5, 8, 12, 3, 5, 8, 12, 5, 3, 8, 12, 5, 8, 3, 12]
days_left = [14, 7, 5, 21, 7, 14, 5, 7, 21, 14, 5, 7, 14, 21, 5, 7, 14, 5, 21, 7]
rate = [8000, 22000, 18000, 5000, 22000, 8000, 18000, 22000, 5000, 8000,
        18000, 22000, 8000, 5000, 18000, 22000, 8000, 18000, 5000, 22000]

# Prepare feature matrix and target variable
X = np.array([pages, days_left]).T
y = np.array(rate)

# Train regression model
model = LinearRegression()
model.fit(X, y)

# Predict rate for a new project
new_project = [10, 2]  # [pages, days_left]
predicted_rate = model.predict([new_project])

# Display model results
print(f"Predicted Rate: ₹{predicted_rate[0]:.0f}")
print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)
print("Model Score (R²):", model.score(X, y))

# Visualize historical data
plt.scatter(pages, rate, label="Training Data")

plt.xlabel("Pages")
plt.ylabel("Rate (INR)")
plt.title("Pages vs Project Rate")
plt.legend()
plt.show()