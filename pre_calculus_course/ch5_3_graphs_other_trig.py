import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def analyze_sec5_3_properties():
    """Prints a comparison table of period, domain restrictions, and vertical asymptotes

    for Tan(x), Cot(x), Sec(x), and Csc(x) as covered in Section 5.3.
    """
    properties_data = [
        {
            "Function": "y = tan(x)",
            "Standard Period": "π (180°)",
            "Domain / Restrictions": "x ≠ π/2 + kπ",
            "Vertical Asymptotes": "x = ±π/2, ±3π/2, ...",
            "Range": "(-∞, ∞)",
        },
        {
            "Function": "y = cot(x)",
            "Standard Period": "π (180°)",
            "Domain / Restrictions": "x ≠ kπ",
            "Vertical Asymptotes": "x = 0, ±π, ±2π, ...",
            "Range": "(-∞, ∞)",
        },
        {
            "Function": "y = sec(x)",
            "Standard Period": "2π (360°)",
            "Domain / Restrictions": "x ≠ π/2 + kπ",
            "Vertical Asymptotes": "x = ±π/2, ±3π/2, ...",
            "Range": "(-∞, -1] ∪ [1, ∞)",
        },
        {
            "Function": "y = csc(x)",
            "Standard Period": "2π (360°)",
            "Domain / Restrictions": "x ≠ kπ",
            "Vertical Asymptotes": "x = 0, ±π, ±2π, ...",
            "Range": "(-∞, -1] ∪ [1, ∞)",
        },
    ]

    df_props = pd.DataFrame(properties_data)
    print("--- Section 5.3: Properties of Other Trigonometric Functions ---")
    print(df_props.to_string(index=False))


def plot_sec5_3_multi_panel():
    """Generates a 2x2 multi-panel plot showing Tan(x), Cot(x), Sec(x), and Csc(x)

    with asymptote masking and dashed vertical asymptote guidelines.
    """
    # Domain over [-2pi, 2pi]
    x = np.linspace(-2 * np.pi, 2 * np.pi, 2000)

    # 1. Tangent
    y_tan = np.tan(x)
    y_tan[np.abs(y_tan) > 10] = np.nan  # Mask vertical asymptotes

    # 2. Cotangent
    with np.errstate(divide="ignore", invalid="ignore"):
        y_cot = 1.0 / np.tan(x)
    y_cot[np.abs(y_cot) > 10] = np.nan

    # 3. Secant (1 / cos(x))
    with np.errstate(divide="ignore", invalid="ignore"):
        y_sec = 1.0 / np.cos(x)
    y_sec[np.abs(y_sec) > 10] = np.nan

    # 4. Cosecant (1 / sin(x))
    with np.errstate(divide="ignore", invalid="ignore"):
        y_csc = 1.0 / np.sin(x)
    y_csc[np.abs(y_csc) > 10] = np.nan

    # Create 2x2 grid plot
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # Shared formatting helper
    def format_subplot(ax, title, y_limit=(-5, 5)):
        ax.set_title(title, fontsize=12, fontweight="bold")
        ax.set_ylim(y_limit)
        ax.axhline(0, color="black", linewidth=0.8, linestyle="-")
        ax.axvline(0, color="black", linewidth=0.8, linestyle="-")
        ax.set_xticks(
            [
                -2 * np.pi,
                -3 * np.pi / 2,
                -np.pi,
                -np.pi / 2,
                0,
                np.pi / 2,
                np.pi,
                3 * np.pi / 2,
                2 * np.pi,
            ],
            labels=[
                r"$-2\pi$",
                r"$-\frac{3\pi}{2}$",
                r"$-\pi$",
                r"$-\frac{\pi}{2}$",
                "0",
                r"$\frac{\pi}{2}$",
                r"$\pi$",
                r"$\frac{3\pi}{2}$",
                r"$2\pi$",
            ],
        )
        ax.grid(True, linestyle="--", alpha=0.5)

    # Plot 1: Tangent
    axes[0, 0].plot(x, y_tan, color="#1f77b4", linewidth=2, label=r"$y = \tan(x)$")
    for k in [-1.5, -0.5, 0.5, 1.5]:
        axes[0, 0].axvline(k * np.pi, color="red", linestyle=":", alpha=0.6)
    format_subplot(axes[0, 0], r"Tangent: $y = \tan(x)$")
    axes[0, 0].legend(loc="upper right")

    # Plot 2: Cotangent
    axes[0, 1].plot(x, y_cot, color="#2ca02c", linewidth=2, label=r"$y = \cot(x)$")
    for k in [-2, -1, 0, 1, 2]:
        axes[0, 1].axvline(k * np.pi, color="red", linestyle=":", alpha=0.6)
    format_subplot(axes[0, 1], r"Cotangent: $y = \cot(x)$")
    axes[0, 1].legend(loc="upper right")

    # Plot 3: Secant
    axes[1, 0].plot(x, y_sec, color="#9467bd", linewidth=2, label=r"$y = \sec(x)$")
    # Overlay light cosine wave to show reciprocal relationship
    axes[1, 0].plot(x, np.cos(x), color="gray", linestyle="--", alpha=0.5, label=r"$y = \cos(x)$")
    for k in [-1.5, -0.5, 0.5, 1.5]:
        axes[1, 0].axvline(k * np.pi, color="red", linestyle=":", alpha=0.6)
    format_subplot(axes[1, 0], r"Secant: $y = \sec(x)$", y_limit=(-6, 6))
    axes[1, 0].legend(loc="upper right")

    # Plot 4: Cosecant
    axes[1, 1].plot(x, y_csc, color="#e377c2", linewidth=2, label=r"$y = \csc(x)$")
    # Overlay light sine wave to show reciprocal relationship
    axes[1, 1].plot(x, np.sin(x), color="gray", linestyle="--", alpha=0.5, label=r"$y = \sin(x)$")
    for k in [-2, -1, 0, 1, 2]:
        axes[1, 1].axvline(k * np.pi, color="red", linestyle=":", alpha=0.6)
    format_subplot(axes[1, 1], r"Cosecant: $y = \csc(x)$", y_limit=(-6, 6))
    axes[1, 1].legend(loc="upper right")

    fig.suptitle("Blitzer Precalculus Sec 5.3: Graphs of Other Trigonometric Functions", fontsize=14, y=0.98)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    analyze_sec5_3_properties()
    plot_sec5_3_multi_panel()