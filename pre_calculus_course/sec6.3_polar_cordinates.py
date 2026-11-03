import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Coordinate Conversion Functions
# ==========================================

def polar_to_rectangular(r, theta_deg):
    """Converts polar coordinates (r, theta) to rectangular (x, y)."""
    theta_rad = np.radians(theta_deg)
    x = r * np.cos(theta_rad)
    y = r * np.sin(theta_rad)
    return round(x, 4), round(y, 4)

def rectangular_to_polar(x, y):
    """Converts rectangular coordinates (x, y) to polar (r, theta in degrees)."""
    r = np.sqrt(x**2 + y**2)
    theta_rad = np.arctan2(y, x)
    theta_deg = np.degrees(theta_rad)
    # Ensure angle is between 0 and 360 degrees
    if theta_deg < 0:
        theta_deg += 360
    return round(r, 4), round(theta_deg, 4)

# Test conversions
print("--- Coordinate Conversions ---")
print(f"Polar (r=4, 60°) to Rectangular: {polar_to_rectangular(4, 60)}")
print(f"Rectangular (x=3, y=4) to Polar: {rectangular_to_polar(3, 4)}")
print("-" * 30)

# ==========================================
# 2. Plotting a Polar Equation (Rose Curve)
# ==========================================
# Equation: r = 4 * cos(3 * theta)

theta = np.linspace(0, 2 * np.pi, 1000)
r = 4 * np.cos(3 * theta)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(6, 6))
ax.plot(theta, r, color='crimson', linewidth=2)
ax.set_title("Polar Plot Example: Rose Curve ($r = 4 \\cos(3\\theta)$)", va='bottom', fontsize=12)
ax.grid(True)

# Display the plot
plt.show()