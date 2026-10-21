import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def solve_linear_trig_equation():
    """Solves linear trigonometric equations:

    Example: 2*sin(x) - np.sqrt(3) = 0  =>  sin(x) = sqrt(3)/2
    Primary Interval: [0, 2pi)
    Solutions: pi/3 (60 deg) and 2pi/3 (120 deg)
    General Solutions: x = pi/3 + 2k*pi, x = 2pi/3 + 2k*pi
    """
    x = np.linspace(0, 2 * np.pi, 2000)
    lhs = 2 * np.sin(x) - np.sqrt(3)

    # Detect zero crossings (sign changes)
    zero_crossings = np.where(np.diff(np.sign(lhs)))[0]
    solutions_rad = x[zero_crossings]
    solutions_deg = np.degrees(solutions_rad)

    print("--- Section 5.5: Trigonometric Equations - Linear Form ---")
    print("Equation: 2*sin(x) - √3 = 0  =>  sin(x) = √3/2")
    print("Primary interval: [0, 2π)\n")

    results = []
    for i, (rad, deg) in enumerate(zip(solutions_rad, solutions_deg), 1):
        # Format fraction of pi
        pi_factor = rad / np.pi
        results.append(
            {
                "Solution": f"x{i}",
                "Radians": round(rad, 4),
                "Exact (Rad)": f"{round(pi_factor, 3)}π",
                "Degrees": f"{round(deg, 1)}°",
                "General Form": f"{round(pi_factor, 3)}π + 2kπ",
            }
        )

    df_results = pd.DataFrame(results)
    print(df_results.to_string(index=False))


def solve_quadratic_trig_equation():
    """Solves trigonometric equations in quadratic form:

    Example: 2*sin^2(x) - sin(x) - 1 = 0
    Factored: (2*sin(x) + 1)(sin(x) - 1) = 0
      1) sin(x) = -1/2  => x = 7pi/6, 11pi/6
      2) sin(x) = 1     => x = pi/2
    """
    x = np.linspace(0, 2 * np.pi, 2000)
    lhs = 2 * (np.sin(x) ** 2) - np.sin(x) - 1

    zero_crossings = np.where(np.diff(np.sign(lhs)))[0]
    solutions_rad = x[zero_crossings]
    solutions_deg = np.degrees(solutions_rad)

    print("\n\n--- Trigonometric Equations - Quadratic Form ---")
    print("Equation: 2*sin²(x) - sin(x) - 1 = 0")
    print("Factored Form: (2*sin(x) + 1)(sin(x) - 1) = 0")
    print("Primary interval: [0, 2π)\n")

    results = []
    for i, (rad, deg) in enumerate(zip(solutions_rad, solutions_deg), 1):
        pi_factor = rad / np.pi
        results.append(
            {
                "Solution": f"x{i}",
                "Radians": round(rad, 4),
                "Exact Fraction": f"{round(pi_factor, 3)}π",
                "Degrees": f"{round(deg, 1)}°",
            }
        )

    df_results = pd.DataFrame(results)
    print(df_results.to_string(index=False))


def solve_using_identities():
    """Solves trigonometric equations requiring fundamental identities:

    Example: 4*cos^2(x) + 4*sin(x) - 5 = 0
    Substitute cos^2(x) = 1 - sin^2(x):
      4(1 - sin^2(x)) + 4*sin(x) - 5 = 0
      4*sin^2(x) - 4*sin(x) + 1 = 0
      (2*sin(x) - 1)^2 = 0  => sin(x) = 1/2
      Solutions: x = pi/6, 5pi/6
    """
    x = np.linspace(0, 2 * np.pi, 2000)
    lhs = 4 * (np.cos(x) ** 2) + 4 * np.sin(x) - 5

    # Since (2*sin(x) - 1)^2 reaches 0 without crossing negative,
    # find local minima close to 0
    minima_indices = np.where(np.isclose(lhs, 0, atol=1e-3))[0]

    # Cluster indices to extract distinct solutions
    solutions_rad = []
    if len(minima_indices) > 0:
        clusters = np.split(
            minima_indices, np.where(np.diff(minima_indices) > 5)[0] + 1
        )
        solutions_rad = [x[c[len(c) // 2]] for c in clusters]

    print("\n\n--- Trigonometric Equations - Using Pythagorean Identity ---")
    print("Equation: 4*cos²(x) + 4*sin(x) - 5 = 0")
    print("Identity Substitution: cos²(x) = 1 - sin²(x)")
    print("Simplified Form: (2*sin(x) - 1)² = 0  =>  sin(x) = 1/2")

    for i, rad in enumerate(solutions_rad, 1):
        deg = np.degrees(rad)
        pi_factor = rad / np.pi
        print(
            f"  • Solution {i}: x = {round(rad, 4)} rad ({round(pi_factor, 3)}π) = {round(deg, 1)}°"
        )


def plot_trig_equation_solutions():
    """Visualizes 2*sin^2(x) - sin(x) - 1 = 0 and highlights its roots on [0, 2pi]."""
    x = np.linspace(0, 2 * np.pi, 1000)
    y = 2 * (np.sin(x) ** 2) - np.sin(x) - 1

    # Roots: pi/2, 7pi/6, 11pi/6
    root_x = np.array([np.pi / 2, 7 * np.pi / 6, 11 * np.pi / 6])
    root_y = np.zeros_like(root_x)

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        x,
        y,
        label=r"$y = 2\sin^2(x) - \sin(x) - 1$",
        color="#1f77b4",
        linewidth=2.5,
    )
    ax.axhline(0, color="black", linestyle="--", linewidth=1, label="y = 0")

    # Plot solution points
    ax.scatter(
        root_x,
        root_y,
        color="#e74c3c",
        s=70,
        zorder=5,
        label=r"Solutions on $[0, 2\pi)$",
    )

    # Annotate roots
    labels = [r"$\frac{\pi}{2}$", r"$\frac{7\pi}{6}$", r"$\frac{11\pi}{6}$"]
    for rx, label in zip(root_x, labels):
        ax.annotate(
            f"x = {label}",
            (rx, 0),
            textcoords="offset points",
            xytext=(0, 15),
            ha="center",
            fontsize=10,
            fontweight="bold",
            bbox=dict(
                boxstyle="round,pad=0.3", fc="yellow", alpha=0.5, ec="none"
            ),
        )

    ax.set_title(
        r"Section 5.5: Solving $2\sin^2(x) - \sin(x) - 1 = 0$",
        fontsize=13,
        pad=15,
        fontweight="bold",
    )
    ax.set_xlabel("Angle x (Radians)", fontsize=11)
    ax.set_ylabel("y", fontsize=11)

    ax.set_xticks(
        [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
        labels=["0", r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"],
    )

    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(loc="upper right", fontsize=10)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    solve_linear_trig_equation()
    solve_quadratic_trig_equation()
    solve_using_identities()
    plot_trig_equation_solutions()