import numpy as np


def model_exponential_growth():
    # Initial population P_0 = 1000, growth rate r = 5% (0.05) per year
    P0 = 1000
    r = 0.05

    # Time vector from year 0 to 20
    t = np.linspace(0, 20, 100)
    P = P0 * np.exp(r * t)

    print(f"Initial Population: {P0}")
    print(f"Growth Rate: {r * 100}%")
    print(f"Population at t = 10 years: {P0 * np.exp(r * 10):.2f}")
    print(f"Population at t = 20 years: {P0 * np.exp(r * 20):.2f}")


model_exponential_growth()