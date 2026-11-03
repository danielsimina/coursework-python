import matplotlib.pyplot as plt
import numpy as np


def test_symmetry():
    """Tests algebraic symmetry for even and odd functions."""
    # Even function: f(-x) = f(x) -> Symmetry over Y-axis
    # Odd function:  f(-x) = -f(x) -> Symmetry through Origin

    x_test = 3
    f_even = lambda x: x**2
    f_odd = lambda x: x**3

    print("--- Chapter 1: Function Symmetry ---")
    print(
        f"Even Test f(x)=x²  : f({x_test}) = {f_even(x_test)}, f({-x_test}) = {f_even(-x_test)} (Equal -> Y-Axis Symmetry)"
    )
    print(
        f"Odd Test  g(x)=x³  : g({x_test}) = {f_odd(x_test)}, g({-x_test}) = {f_odd(-x_test)} (Opposite -> Origin Symmetry)\n"
    )


def plot_transformations_and_symmetry():
    """Plots parent vs. transformed functions and even vs. odd symmetry."""
    x = np.linspace(-3, 3, 500)

    # Functions for Plot 1: Transformations
    y_parent = x**2  # Parent: f(x) = x^2
    y_trans = 2 * (x - 1) ** 2 - 3  # g(x) = 2(x - 1)^2 - 3

    # Functions for Plot 2: Symmetry
    y_even = x**2  # Even Function
    y_odd = x**3  # Odd Function

    # Setup 1x2 subplot layout
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- Plot 1: Transformations ---
    ax1.plot(x, y_parent, label="Parent: f(x) = x²", color="gray", ls="--")
    ax1.plot(
        x,
        y_trans,
        label="Transformed: g(x) = 2(x - 1)² - 3",
        color="crimson",
        lw=2,
    )
    ax1.scatter(
        [1],
        [-3],
        color="red",
        zorder=5,
        label="Vertex Shift (1, -3)",
    )

    ax1.set_title("Function Transformations (Shifts & Stretches)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_ylim(-4, 8)
    ax1.axhline(0, color="black", lw=0.8, ls=":")
    ax1.axvline(0, color="black", lw=0.8, ls=":")
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # --- Plot 2: Even vs. Odd Symmetry ---
    ax2.plot(x, y_even, label="Even: f(x) = x² (Y-Axis)", color="blue", lw=2)
    ax2.plot(
        x, y_odd, label="Odd: g(x) = x³ (Origin)", color="darkgreen", lw=2
    )

    ax2.set_title("Symmetry: Even vs. Odd Functions")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_ylim(-8, 8)
    ax2.axhline(0, color="black", lw=0.8, ls=":")
    ax2.axvline(0, color="black", lw=0.8, ls=":")
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    test_symmetry()
    plot_transformations_and_symmetry()