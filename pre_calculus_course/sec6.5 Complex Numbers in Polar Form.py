import cmath
import numpy as np


# ==========================================
# 1. Conversions
# ==========================================

def to_polar(a, b):
    """Converts a rectangular complex number (a + bi) to polar form (r, theta in degrees)."""
    z = complex(a, b)
    r = abs(z)
    theta_rad = cmath.phase(z)
    theta_deg = np.degrees(theta_rad)
    if theta_deg < 0:
        theta_deg += 360  # Keep angle between 0° and 360°
    return round(r, 4), round(theta_deg, 4)


def to_rectangular(r, theta_deg):
    """Converts polar form r(cos(theta) + i*sin(theta)) to rectangular (a + bi)."""
    theta_rad = np.radians(theta_deg)
    a = r * np.cos(theta_rad)
    b = r * np.sin(theta_rad)
    # Format cleanly as a complex number
    return complex(round(a, 4), round(b, 4))


# ==========================================
# 2. Operations in Polar Form
# ==========================================

def multiply_polar(r1, theta1_deg, r2, theta2_deg):
    """Multiplies two complex numbers in polar form: multiply r, add angles."""
    r_out = r1 * r2
    theta_out = (theta1_deg + theta2_deg) % 360
    return round(r_out, 4), round(theta_out, 4)


def divide_polar(r1, theta1_deg, r2, theta2_deg):
    """Divides two complex numbers in polar form: divide r, subtract angles."""
    if r2 == 0:
        raise ValueError("Division by zero modulus.")
    r_out = r1 / r2
    theta_out = (theta1_deg - theta2_deg) % 360
    return round(r_out, 4), round(theta_out, 4)


def demoivre_power(r, theta_deg, n):
    """Applies De Moivre's Theorem for z^n: r^n(cos(n*theta) + i*sin(n*theta))."""
    r_out = r ** n
    theta_out = (theta_deg * n) % 360
    return round(r_out, 4), round(theta_out, 4)


# ==========================================
# Demonstration
# ==========================================
if __name__ == "__main__":
    print("--- 1. Rectangular to Polar ---")
    r, theta = to_polar(3, 4)
    print(f"3 + 4i -> r = {r}, theta = {theta}°")

    print("\n--- 2. Polar to Rectangular ---")
    rect = to_rectangular(5, 53.13)
    print(f"5(cos(53.13°) + i*sin(53.13°)) -> {rect}")

    print("\n--- 3. De Moivre's Theorem (Power) ---")
    # Let's find (2(cos(30°) + i*sin(30°)))^3
    r_res, th_res = demoivre_power(2, 30, 3)
    print(f"[2(cis 30°)]^3 -> r = {r_res}, theta = {th_res}°")