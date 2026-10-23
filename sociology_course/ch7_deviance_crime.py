import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def strain_theory_analysis():
    """Models Robert Merton's Strain Theory typology based on acceptance or rejection

    of cultural goals and institutionalized means.
    """
    strain_data = [
        {
            "Mode of Adaptation": "Conformity",
            "Cultural Goals": "Accepts",
            "Institutional Means": "Accepts",
            "Sociological Description": "Pursues societal goals through legitimate, approved paths.",
        },
        {
            "Mode of Adaptation": "Innovation",
            "Cultural Goals": "Accepts",
            "Institutional Means": "Rejects",
            "Sociological Description": "Uses illegal/unconventional means (e.g., crime) to attain success.",
        },
        {
            "Mode of Adaptation": "Ritualism",
            "Cultural Goals": "Rejects",
            "Institutional Means": "Accepts",
            "Sociological Description": "Abandons goal of wealth/success but rigidly follows rules.",
        },
        {
            "Mode of Adaptation": "Retreatism",
            "Cultural Goals": "Rejects",
            "Institutional Means": "Rejects",
            "Sociological Description": "Withdraws from society (e.g., severe addiction, living off-grid).",
        },
        {
            "Mode of Adaptation": "Rebellion",
            "Cultural Goals": "Replaces",
            "Institutional Means": "Replaces",
            "Sociological Description": "Rejects social structure and advocates for radical new values.",
        },
    ]

    df_strain = pd.DataFrame(strain_data)
    print("--- Chapter 7: Robert Merton's Strain Theory Typology ---")
    print(df_strain.to_string(index=False))


def crime_categories_data():
    """Generates crime rate and financial cost comparison data across crime categories."""
    crime_data = {
        "Crime Category": [
            "Property Crime",
            "Violent Crime",
            "White-Collar Crime",
            "Corporate Crime",
        ],
        "Annual Estimated Cost ($ Billions)": [16, 42, 500, 800],
        "Public Fear Index (0-100)": [70, 95, 30, 25],
        "Incarceration Rate Index (0-100)": [75, 90, 20, 10],
    }
    return pd.DataFrame(crime_data)


def plot_deviance_and_crime_analysis(df):
    """Generates a comparison bar chart illustrating the disparity between public perception

    (fear/incarceration) and economic impact of street crime vs. corporate crime.
    """
    sns.set_theme(style="whitegrid")
    fig, ax1 = plt.subplots(figsize=(10, 6))

    color = "#2b5c8f"
    ax1.set_xlabel("Crime Category", fontsize=11, fontweight="bold")
    ax1.set_ylabel(
        "Estimated Economic Cost ($ Billions)",
        color=color,
        fontsize=11,
        fontweight="bold",
    )

    # Seaborn barplot with hue assigned and legend disabled to avoid FutureWarnings
    sns.barplot(
        data=df,
        x="Crime Category",
        y="Annual Estimated Cost ($ Billions)",
        hue="Crime Category",
        palette="Blues_d",
        legend=False,
        ax=ax1,
    )
    ax1.tick_params(axis="y", labelcolor=color)

    # Annotate White-Collar & Corporate Crime gap
    ax1.annotate(
        "High Economic Impact\nLow Prosecution / Media Visibility",
        xy=(3, 800),
        xytext=(2.1, 650),
        arrowprops=dict(facecolor="black", shrink=0.05, width=1, headwidth=5),
        fontsize=9,
        bbox=dict(
            boxstyle="round,pad=0.3", fc="#fef9e7", ec="#f1c40f", alpha=0.9
        ),
    )

    ax1.set_title(
        "Sociological Analysis: Crime Impact vs. Public Perception (Chapter 7)",
        fontsize=13,
        pad=15,
        fontweight="bold",
    )
    ax1.yaxis.set_major_formatter("${x:,.0f}B")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    strain_theory_analysis()
    df_crime = crime_categories_data()
    plot_deviance_and_crime_analysis(df_crime)