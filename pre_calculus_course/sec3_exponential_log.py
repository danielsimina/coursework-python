import math
import matplotlib.pyplot as plt
import numpy as np


def exponential_and_log_demo():
    """Calculates exponential growth and logarithmic values."""
    # 1. Compound Interest Example: A = P * e^(rt)
    principal = 1000  # Initial investment ($)
    rate = 0.05  # 5% interest rate
    years = 10

    # e^(r * t)
    amount = principal * math.exp(rate * years)

    print(f"--- Compound Interest (Continuous) ---")
    print(
        f"${principal} invested at {rate*100}% for {years} years: ${amount:.2f}\n"
    )

    # 2. Logarithm Calculations
    x_val = 100
    ln_val = math.log(x_val)  # Natural log (base e)
    log10_val = math.log10(x_val)  # Base 10 log
    log2_val = math.log2(x_val)  # Base 2 log

    print(f"--- Logarithm Calculations for x = {x_val} ---")
    print(f"ln({x_val}): {ln_val:.4f}")
    print(f"log10({x_val}): {log10_val:.4f}")
    print(f"log2({x_val}): {log2_val:.4f}\n")


def plot_exp_and_log():
    """Plots y = e^x and y = ln(x) to visualize inverse functions."""
    # Values for e^x
    x_exp = np.linspace(-2, 2.5, 500)
    y_exp = np.exp(x_exp)

    # Values for ln(x) (x must be > 0)
    x_log = np.linspace(0.05, 12, 500)
    y_log = np.log(x_log)

    # Values for reflection line y = x
    x_ref = np.linspace(-2, 12, 500)

    # Setup Plot
    plt.figure(figsize=(9, 7))

    plt.plot(x_exp, y_exp, label="y = e^x (Exponential)", color="blue", lw=2)
    plt.plot(
        x_log, y_log, label="y = ln(x) (Natural Log)", color="green", lw=2
    )
    plt.plot(
        x_ref,
        x_ref,
        label="y = x (Reflection Line)",
        color="gray",
        linestyle="--",
        alpha=0.7,
    )

    # Highlights
    plt.scatter([0, 1], [1, 0], color="red", zorder=5)
    plt.annotate(
        "(0, 1) y-intercept",
        (0, 1),
        textcoords="offset points",
        xytext=(-60, 10),
    )
    plt.annotate(
        "(1, 0) x-intercept",
        (1, 0),
        textcoords="offset points",
        xytext=(10, -15),
    )

    # Styling
    plt.title("Inverse Relationship: Exponential vs. Logarithmic")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="black", linewidth=0.8, linestyle=":")
    plt.axvline(0, color="black", linewidth=0.8, linestyle=":")
    plt.xlim(-3, 10)
    plt.ylim(-3, 10)
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.show()


if __name__ == "__main__":
    exponential_and_log_demo()
    plot_exp_and_log()