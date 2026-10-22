import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def verify_fundamental_identities():
    """Verifies fundamental trigonometric identities computationally:

    1. Pythagorean Identity: sin^2(x) + cos^2(x) = 1
    2. Quotient Identity: tan(x) = sin(x) / cos(x)
    """
    angles_deg = [0, 30, 45, 60, 90, 120, 135, 150, 180]
    angles_rad = np.radians(angles_deg)

    results = []
    for deg, rad in zip(angles_deg, angles_rad):
        sin_val = np.sin(rad)
        cos_val = np.cos(rad)

        # Pythagorean Check: sin^2 + cos^2
        pythagorean = sin_val**2 + cos_val**2

        # Quotient Check: sin / cos (handling division by zero)
        tan_calc = (
            sin_val / cos_val if not np.isclose(cos_val, 0) else np.nan
        )

        results.append(
            {
                "Angle (Deg)": deg,
                "Angle (Rad)": round(rad, 4),
                "sin(x)": round(sin_val, 4),
                "cos(x)": round(cos_val, 4),
                "sin^2 + cos^2": round(pythagorean, 4),
                "sin/cos": (
                    round(tan_calc, 4) if not np.isnan(tan_calc) else "Undefined"
                ),
            }
        )

    df_identities = pd.DataFrame(results)
    print(
        "--- Chapter 5: Analytic Trigonometry - Fundamental Identities Verification ---"
    )
    print(df_identities.to_string(index=False))


def sum_and_difference_formulas_demo():
    """Demonstrates exact evaluation using Sum and Difference Formulas for cosine:

    cos(alpha - beta) = cos(alpha)cos(beta) + sin(alpha)sin(beta)
    Example: cos(15 deg) = cos(45 deg - 30 deg)
    """
    alpha_deg = 45
    beta_deg = 30
    target_deg = alpha_deg - beta_deg  # 15 degrees

    alpha_rad = np.radians(alpha_deg)
    beta_rad = np.radians(beta_deg)
    target_rad = np.radians(target_deg)

    # Calculate using identity expansion
    cos_identity = np.cos(alpha_rad) * np.cos(beta_rad) + np.sin(
        alpha_rad
    ) * np.sin(beta_rad)
    cos_direct = np.cos(target_rad)

    print("\n\n--- Sum and Difference Identity: cos(alpha - beta) ---")
    print(f"Target Angle: cos({target_deg}°) = cos({alpha_deg}° - {beta_deg}°)")
    print(
        f"  • Identity Expansion: cos({alpha_deg}°)cos({beta_deg}°) + sin({alpha_deg}°)sin({beta_deg}°)"
    )
    print(f"  • Computed Identity Value: {round(cos_identity, 6)}")
    print(f"  • Direct cos(15°) Value:   {round(cos_direct, 6)}")
    print(f"  • Identity Match:          {np.isclose(cos_identity, cos_direct)}")


def solve_trig_equation_demo():
    """Solves trigonometric equations on the interval [0, 2pi):

    Example: 2*sin(x) - 1 = 0 => sin(x) = 1/2
    Expected solutions: pi/6 (30 deg) and 5*pi/6 (150 deg)
    """
    x = np.linspace(0, 2 * np.pi, 1000)
    equation_lhs = 2 * np.sin(x) - 1

    # Find approximate roots where sign changes
    zero_crossings = np.where(np.diff(np.sign(equation_lhs)))[0]
    solutions_rad = x[zero_crossings]
    solutions_deg = np.degrees(solutions_rad)

    print("\n\n--- Trigonometric Equation Solver: 2*sin(x) - 1 = 0 ---")
    print("Interval: [0, 2π)")
    for i, (rad, deg) in enumerate(zip(solutions_rad, solutions_deg), 1):
        print(f"  • Solution {i}: x = {round(rad, 4)} rad ({round(deg, 1)}°)")


def plot_double_angle_identity():
    """Visualizes the Double-Angle Identity for sine:

    sin(2x) = 2*sin(x)*cos(x)
    Plots both LHS and RHS to demonstrate visual equivalence across [0, 2pi].
    """
    x = np.linspace(0, 2 * np.pi, 500)

    # LHS and RHS of Double-Angle Identity
    lhs = np.sin(2 * x)
    rhs = 2 * np.sin(x) * np.cos(x)

    fig, ax = plt.subplots(figsize=(9, 5))

    # Plot LHS as solid line, RHS as dashed line to show overlap
    ax.plot(
        x,
        lhs,
        label=r"LHS: \(\sin(2x)\)",
        color="#1f77b4",
        linewidth=2.5,
        zorder=2,
    )
    ax.plot(
        x,
        rhs,
        label=r"RHS: \(2\sin(x)\cos(x)\)",
        color="#e74c3c",
        linestyle="--",
        linewidth=2.5,
        zorder=3,
    )

    # Formatting and Styling
    ax.set_title(
        r"Analytic Trigonometry: Double-Angle Identity \(\sin(2x) = 2\sin(x)\cos(x)\) (Ch. 5)",
        fontsize=13,
        pad=15,
        fontweight="bold",
    )
    ax.set_xlabel("Angle x (Radians)", fontsize=11)
    ax.set_ylabel("Function Value", fontsize=11)

    # Set custom pi x-ticks
    ax.set_xticks(
        [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
        labels=["0", r"\(\frac{\pi}{2}\)", r"\(\pi\)", r"\(\frac{3\pi}{2}\)", r"\(2\pi\)"],
    )

    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(loc="upper right", fontsize=11)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    verify_fundamental_identities()
    sum_and_difference_formulas_demo()
    solve_trig_equation_demo()
    plot_double_angle_identity()