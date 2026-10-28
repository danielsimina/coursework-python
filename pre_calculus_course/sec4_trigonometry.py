import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def calculate_unit_circle_point(angle_deg):
    """Calculates coordinates (x, y) = (cos(theta), sin(theta)) on the unit circle

    for any angle in degrees, along with exact trigonometric ratios.
    """
    angle_rad = np.radians(angle_deg)
    x_coord = np.cos(angle_rad)
    y_coord = np.sin(angle_rad)

    tan_val = (
        np.tan(angle_rad) if not np.isclose(np.cos(angle_rad), 0) else np.nan
    )
    cot_val = (
        1 / np.tan(angle_rad)
        if not np.isclose(np.sin(angle_rad), 0)
        else np.nan
    )

    print(f"\n--- Unit Circle Evaluation: θ = {angle_deg}° ({angle_rad:.4f} rad) ---")
    print(f"  • Point Coordinates (x, y): ({x_coord:.4f}, {y_coord:.4f})")
    print(f"  • cos(θ) = {x_coord:.4f}")
    print(f"  • sin(θ) = {y_coord:.4f}")
    print(
        f"  • tan(θ) = {f'{tan_val:.4f}' if not np.isnan(tan_val) else 'Undefined'}"
    )
    print(
        f"  • cot(θ) = {f'{cot_val:.4f}' if not np.isnan(cot_val) else 'Undefined'}"
    )


def verify_fundamental_trig_values():
    """Evaluates trigonometric functions across standard unit circle angles:

    Calculates sin(x), cos(x), tan(x), and cot(x) for common angles in standard position.
    """
    angles_deg = [0, 30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
    angles_rad = np.radians(angles_deg)

    results = []
    for deg, rad in zip(angles_deg, angles_rad):
        sin_val = np.sin(rad)
        cos_val = np.cos(rad)

        tan_calc = (
            sin_val / cos_val if not np.isclose(cos_val, 0) else np.nan
        )
        cot_calc = (
            cos_val / sin_val if not np.isclose(sin_val, 0) else np.nan
        )

        results.append(
            {
                "Angle (Deg)": deg,
                "Angle (Rad)": round(rad, 4),
                "sin(x)": round(sin_val, 4),
                "cos(x)": round(cos_val, 4),
                "tan(x)": (
                    round(tan_calc, 4) if not np.isnan(tan_calc) else "Undefined"
                ),
                "cot(x)": (
                    round(cot_calc, 4) if not np.isnan(cot_calc) else "Undefined"
                ),
            }
        )

    df_trig = pd.DataFrame(results)
    print("\n--- Chapter 4: Trigonometric Functions - Unit Circle Values ---")
    print(df_trig.to_string(index=False))


def plot_multi_panel_trig_waves():
    """Generates a 2x2 multi-panel plot for sin(x), cos(x), tan(x), and cot(x)

    with asymptote masking to prevent vertical line artifacts.
    """
    x = np.linspace(0, 2 * np.pi, 1000)

    # 1. Sine Wave
    sin_y = np.sin(x)

    # 2. Cosine Wave
    cos_y = np.cos(x)

    # 3. Tangent Wave with Asymptote Masking (Asymptotes at pi/2, 3pi/2)
    tan_y = np.tan(x)
    tan_y[np.abs(tan_y) > 10] = (
        np.nan
    )  # Mask out large values near vertical asymptotes

    # 4. Cotangent Wave with Asymptote Masking (Asymptotes at 0, pi, 2pi)
    cot_y = 1.0 / np.tan(x)
    cot_y[np.abs(cot_y) > 10] = (
        np.nan
    )  # Mask out large values near vertical asymptotes

    # Initialize 2x2 subplot layout
    fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharex=True)
    fig.suptitle(
        "Chapter 4: Multi-Panel Trigonometric Wave Functions & Asymptotes",
        fontsize=14,
        fontweight="bold",
    )

    x_ticks = [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi]
    x_labels = [
        "0",
        r"\(\frac{\pi}{2}\)",
        r"\(\pi\)",
        r"\(\frac{3\pi}{2}\)",
        r"\(2\pi\)",
    ]

    # Panel 1: sin(x)
    axes[0, 0].plot(x, sin_y, color="#1f77b4", linewidth=2, label=r"\(y = \sin(x)\)")
    axes[0, 0].set_title(r"Sine: \(y = \sin(x)\)", fontsize=11, fontweight="bold")
    axes[0, 0].set_ylim(-1.5, 1.5)
    axes[0, 0].grid(True, linestyle="--", alpha=0.6)
    axes[0, 0].legend(loc="upper right")

    # Panel 2: cos(x)
    axes[0, 1].plot(x, cos_y, color="#e74c3c", linewidth=2, label=r"\(y = \cos(x)\)")
    axes[0, 1].set_title(
        r"Cosine: \(y = \cos(x)\)", fontsize=11, fontweight="bold"
    )
    axes[0, 1].set_ylim(-1.5, 1.5)
    axes[0, 1].grid(True, linestyle="--", alpha=0.6)
    axes[0, 1].legend(loc="upper right")

    # Panel 3: tan(x) with Asymptotes
    axes[1, 0].plot(x, tan_y, color="#2ca02c", linewidth=2, label=r"\(y = \tan(x)\)")
    axes[1, 0].axvline(
        x=np.pi / 2, color="gray", linestyle=":", alpha=0.7, label="Asymptote"
    )
    axes[1, 0].axvline(x=3 * np.pi / 2, color="gray", linestyle=":", alpha=0.7)
    axes[1, 0].set_title(
        r"Tangent: \(y = \tan(x)\)", fontsize=11, fontweight="bold"
    )
    axes[1, 0].set_ylim(-5, 5)
    axes[1, 0].grid(True, linestyle="--", alpha=0.6)
    axes[1, 0].legend(loc="upper right")

    # Panel 4: cot(x) with Asymptotes
    axes[1, 1].plot(x, cot_y, color="#9467bd", linewidth=2, label=r"\(y = \cot(x)\)")
    axes[1, 1].axvline(
        x=np.pi, color="gray", linestyle=":", alpha=0.7, label="Asymptote"
    )
    axes[1, 1].set_title(
        r"Cotangent: \(y = \cot(x)\)", fontsize=11, fontweight="bold"
    )
    axes[1, 1].set_ylim(-5, 5)
    axes[1, 1].grid(True, linestyle="--", alpha=0.6)
    axes[1, 1].legend(loc="upper right")

    # Format shared x-axis ticks
    for ax in axes.flat:
        ax.set_xticks(x_ticks)
        ax.set_xticklabels(x_labels)

    axes[1, 0].set_xlabel("Angle x (Radians)", fontsize=10)
    axes[1, 1].set_xlabel("Angle x (Radians)", fontsize=10)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Interactive unit circle evaluation for a target angle (e.g., 60 deg or 135 deg)
    calculate_unit_circle_point(angle_deg=60)

    # Table of standard unit circle values
    verify_fundamental_trig_values()

    # Multi-panel plot for sin, cos, tan, cot with asymptote masking
    plot_multi_panel_trig_waves()