import matplotlib.pyplot as plt
import numpy as np


def polynomial_demo():
    """Calculates roots and values for a 3rd-degree polynomial."""
    # Polynomial: f(x) = x^3 - 3x^2 - x + 3
    # Coefficients: [1, -3, -1, 3]
    coefficients = [1, -3, -1, 3]
    roots = np.roots(coefficients)

    print("--- Chapter 2: Polynomial Functions ---")
    print("Function: f(x) = x^3 - 3x^2 - x + 3")
    print(f"Roots (x-intercepts): {roots}\n")


def plot_polynomial_and_rational():
    """Plots a cubic polynomial and a rational function with asymptotes."""
    # 1. Polynomial setup: f(x) = x^3 - 3x^2 - x + 3
    x_poly = np.linspace(-2, 4, 500)
    y_poly = x_poly**3 - 3 * (x_poly**2) - x_poly + 3

    # 2. Rational setup: g(x) = (2x + 1) / (x - 2)
    # Vertical asymptote at x = 2 (divide domain to avoid zero-division artifact lines)
    x_rat1 = np.linspace(-4, 1.95, 250)
    x_rat2 = np.linspace(2.05, 8, 250)

    y_rat1 = (2 * x_rat1 + 1) / (x_rat1 - 2)
    y_rat2 = (2 * x_rat2 + 1) / (x_rat2 - 2)

    # Setup 1x2 subplot layout
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- Plot 1: Polynomial Function ---
    ax1.plot(x_poly, y_poly, label="f(x) = x³ - 3x² - x + 3", color="purple", lw=2)
    ax1.scatter([-1, 1, 3], [0, 0, 0], color="red", zorder=5, label="Roots (-1, 1, 3)")
    ax1.set_title("Polynomial Function")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.axhline(0, color="black", lw=0.8, ls=":")
    ax1.axvline(0, color="black", lw=0.8, ls=":")
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # --- Plot 2: Rational Function ---
    ax2.plot(x_rat1, y_rat1, color="teal", lw=2, label="g(x) = (2x + 1) / (x - 2)")
    ax2.plot(x_rat2, y_rat2, color="teal", lw=2)
    # Asymptotes: Vertical at x = 2, Horizontal at y = 2
    ax2.axvline(2, color="crimson", ls="--", label="Vertical Asymptote (x = 2)")
    ax2.axhline(2, color="orange", ls="--", label="Horizontal Asymptote (y = 2)")

    ax2.set_title("Rational Function")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_ylim(-10, 10)
    ax2.axhline(0, color="black", lw=0.8, ls=":")
    ax2.axvline(0, color="black", lw=0.8, ls=":")
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    polynomial_demo()
    plot_polynomial_and_rational()