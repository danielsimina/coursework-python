import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_right_triangle_application(
    distance_ft: float, angle_elevation_deg: float
):
    """Calculates and visualizes a right triangle application (e.g., height from distance and angle)."""
    angle_rad = np.radians(angle_elevation_deg)

    # Calculate height (h = d * tan(theta)) and hypotenuse
    height = distance_ft * np.tan(angle_rad)
    hypotenuse = distance_ft / np.cos(angle_rad)

    # Corner coordinates: Base (0,0), Object Base (d, 0), Object Top (d, h)
    x_coords = [0, distance_ft, distance_ft, 0]
    y_coords = [0, 0, height, 0]

    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot triangle edges
    ax.plot(
        x_coords,
        y_coords,
        color="#2c3e50",
        linewidth=2.5,
        label="Triangle Geometry",
    )
    ax.fill(x_coords, y_coords, color="#3498db", alpha=0.15)

    # Highlight key segments
    ax.plot(
        [0, distance_ft],
        [0, 0],
        color="#27ae60",
        linewidth=3,
        label=f"Distance = {distance_ft:.1f} ft",
    )
    ax.plot(
        [distance_ft, distance_ft],
        [0, height],
        color="#e74c3c",
        linewidth=3,
        label=f"Height = {height:.2f} ft",
    )
    ax.plot(
        [0, distance_ft],
        [0, height],
        color="#8e44ad",
        linewidth=2,
        linestyle="--",
        label=f"Hypotenuse = {hypotenuse:.2f} ft",
    )

    # Annotate angle of elevation arc
    arc_theta = np.linspace(0, angle_rad, 50)
    arc_r = distance_ft * 0.2
    ax.plot(
        arc_r * np.cos(arc_theta),
        arc_r * np.sin(arc_theta),
        color="#d35400",
        linewidth=2,
    )
    ax.text(
        arc_r * 1.2 * np.cos(angle_rad / 2),
        arc_r * 1.2 * np.sin(angle_rad / 2),
        f"{angle_elevation_deg}°",
        fontsize=11,
        fontweight="bold",
        color="#d35400",
    )

    # Formatting
    ax.set_title(
        "Section 4.8: Right Triangle Application (Angle of Elevation)",
        fontsize=13,
        pad=15,
        fontweight="bold",
    )
    ax.set_xlabel("Horizontal Distance (ft)", fontsize=11)
    ax.set_ylabel("Vertical Height (ft)", fontsize=11)
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(loc="upper left", fontsize=10)
    ax.set_aspect("equal", adjustable="datalim")

    plt.tight_layout()
    plt.show()


def plot_navigation_bearing(
    speed_mph: float, time_hours: float, bearing_angle_deg: float
):
    """Calculates and plots a 2D vector path for navigation bearings (measured clockwise from North)."""
    total_distance = speed_mph * time_hours
    bearing_rad = np.radians(bearing_angle_deg)

    # Bearing measured clockwise from North:
    # North component (y) = distance * cos(bearing)
    # East component (x)  = distance * sin(bearing)
    north_comp = total_distance * np.cos(bearing_rad)
    east_comp = total_distance * np.sin(bearing_rad)

    fig, ax = plt.subplots(figsize=(7, 7))

    # Draw cardinal axes
    ax.axhline(0, color="gray", linestyle="--", linewidth=1)
    ax.axvline(0, color="gray", linestyle="--", linewidth=1)

    # Plot vector trajectory
    ax.annotate(
        "",
        xy=(east_comp, north_comp),
        xytext=(0, 0),
        arrowprops=dict(facecolor="#2980b9", edgecolor="#2980b9", width=2, headwidth=8),
    )

    # Plot component vectors (East & North)
    ax.plot(
        [0, east_comp],
        [0, 0],
        color="#e67e22",
        linestyle=":",
        linewidth=2,
        label=f"East Component = {east_comp:.2f} mi",
    )
    ax.plot(
        [east_comp, east_comp],
        [0, north_comp],
        color="#27ae60",
        linestyle=":",
        linewidth=2,
        label=f"North Component = {north_comp:.2f} mi",
    )

    # Compass Rose / Direction Labels
    offset = max(total_distance * 1.1, 10)
    ax.text(0, offset * 0.9, "N", fontsize=12, fontweight="bold", ha="center")
    ax.text(0, -offset * 0.9, "S", fontsize=12, fontweight="bold", ha="center")
    ax.text(offset * 0.9, 0, "E", fontsize=12, fontweight="bold", va="center")
    ax.text(-offset * 0.9, 0, "W", fontsize=12, fontweight="bold", va="center")

    # Formatting
    ax.set_xlim(-offset, offset)
    ax.set_ylim(-offset, offset)
    ax.set_title(
        f"Section 4.8: Navigation Bearing Path (N {bearing_angle_deg}° E)",
        fontsize=13,
        pad=15,
        fontweight="bold",
    )
    ax.set_xlabel("East / West Distance (miles)", fontsize=11)
    ax.set_ylabel("North / South Distance (miles)", fontsize=11)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(loc="lower left", fontsize=10)
    ax.set_aspect("equal", adjustable="box")

    plt.tight_layout()
    plt.show()


def plot_simple_harmonic_motion_comparison():
    """Visualizes and compares two SHM systems with different amplitudes and frequencies."""
    t = np.linspace(0, 4, 1000)

    # System 1: a = 6, f = 0.5 Hz (omega = pi)
    d1 = 6 * np.cos(np.pi * t)

    # System 2: a = 3, f = 1.0 Hz (omega = 2*pi)
    d2 = 3 * np.cos(2 * np.pi * t)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7), sharex=True)

    # Subplot 1
    ax1.plot(
        t,
        d1,
        color="#1f77b4",
        linewidth=2,
        label=r"\(d_1 = 6\cos(\pi t)\) (\(a=6\), \(f=0.5\) Hz)",
    )
    ax1.axhline(0, color="black", linestyle="--", linewidth=0.8, alpha=0.6)
    ax1.set_ylabel("Displacement (cm)", fontsize=11)
    ax1.set_title(
        "Simple Harmonic Motion Comparison", fontsize=13, fontweight="bold"
    )
    ax1.grid(True, linestyle="--", alpha=0.6)
    ax1.legend(loc="upper right")

    # Subplot 2
    ax2.plot(
        t,
        d2,
        color="#e74c3c",
        linewidth=2,
        label=r"\(d_2 = 3\cos(2\pi t)\) (\(a=3\), \(f=1.0\) Hz)",
    )
    ax2.axhline(0, color="black", linestyle="--", linewidth=0.8, alpha=0.6)
    ax2.set_xlabel("Time t (seconds)", fontsize=11)
    ax2.set_ylabel("Displacement (cm)", fontsize=11)
    ax2.grid(True, linestyle="--", alpha=0.6)
    ax2.legend(loc="upper right")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # 1. Right Triangle Plot
    plot_right_triangle_application(distance_ft=100.0, angle_elevation_deg=35.0)

    # 2. Bearing Vector Plot
    plot_navigation_bearing(
        speed_mph=25.0, time_hours=2.0, bearing_angle_deg=40.0
    )

    # 3. Multi-Panel SHM Waveform Comparison
    plot_simple_harmonic_motion_comparison()