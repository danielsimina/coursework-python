# MATH 1113 Precalculus - Section 2.4: Fitting Linear Models to Data
import numpy as np

# Sample Data: Advertising Spend ($k) vs. Sales Revenue ($k)
x = np.array([2, 4, 6, 8, 10])  # Independent variable (Ad Spend)
y = np.array([12, 18, 23, 30, 35]) # Dependent variable (Sales)

# 1. Compute line of best fit: y = mx + b (Least Squares Regression)
m, b = np.polyfit(x, y, 1)

# 2. Compute correlation coefficient (r)
r = np.corrcoef(x, y)[0, 1]

print(f"Line of Best Fit: y = {m:.2f}x + {b:.2f}")
print(f"Correlation Coefficient (r): {r:.4f}")

# 3. Make a prediction for x = 7 ($7,000 ad spend)
y_pred = m * 7 + b
print(f"Predicted Sales for $7k spend: ${y_pred:.2f} thousand")