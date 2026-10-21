import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def sex_vs_gender_concepts():
    """Prints a comparison table highlighting the core distinction between

    Sex (biological characteristics) and Gender (socially learned roles).
    """
    concepts_data = [
        {
            "Dimension": "Sex",
            "Basis": "Biological / Anatomical",
            "Key Elements": "Chromosomes, hormones, physiological traits",
            "Sociological Nature": "Universal / Inborn characteristics",
        },
        {
            "Dimension": "Gender",
            "Basis": "Social / Cultural",
            "Key Elements": "Gender identity, gender expression, gender roles",
            "Sociological Nature": "Learned through socialization; context dependent",
        },
        {
            "Dimension": "Gender Identity",
            "Basis": "Internal Self-Perception",
            "Key Elements": "Perception of oneself as male, female, or another gender",
            "Sociological Nature": "Core component of personal identity",
        },
        {
            "Dimension": "Gender Roles",
            "Basis": "Cultural Expectations",
            "Key Elements": "Behaviors, activities, and traits prescribed by society",
            "Sociological Nature": "Reinforced by socialization agents (family, media)",
        },
    ]

    df_concepts = pd.DataFrame(concepts_data)
    print("--- Chapter 9: Sex vs. Gender Sociological Distinctions ---")
    print(df_concepts.to_string(index=False))


def analyze_gender_wage_gap():
    """Models occupational data examining median annual earnings and gender wage gaps."""
    occupational_data = {
        "Occupational Sector": [
            "Software Development",
            "Software Development",
            "Financial Management",
            "Financial Management",
            "Elementary Teaching",
            "Elementary Teaching",
            "Registered Nursing",
            "Registered Nursing",
        ],
        "Gender Group": [
            "Men",
            "Women",
            "Men",
            "Women",
            "Men",
            "Women",
            "Men",
            "Women",
        ],
        "Median Earnings ($)": [
            118000,
            98000,
            125000,
            95000,
            64000,
            58000,
            82000,
            76000,
        ],
    }

    df_wage = pd.DataFrame(occupational_data)
    print("\n\n--- Occupational Earnings Breakdown ---")
    print(df_wage.to_string(index=False))
    return df_wage


def plot_gender_wage_gap(df):
    """Generates a grouped bar chart visualizing median annual earnings by gender across sectors."""
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot grouped bar chart using Seaborn
    sns.barplot(
        data=df,
        x="Occupational Sector",
        y="Median Earnings ($)",
        hue="Gender Group",
        palette=["#2b5c8f", "#e74c3c"],
        ax=ax,
    )

    # Formatting plot
    ax.set_title(
        "Sociological Analysis: Gender Earnings Disparities by Sector (Chapter 9)",
        fontsize=13,
        pad=15,
        fontweight="bold",
    )
    ax.set_xlabel("Occupational Sector", fontsize=11)
    ax.set_ylabel("Median Annual Earnings ($)", fontsize=11)
    ax.set_ylim(0, 140000)

    # Add wage gap annotation
    ax.annotate(
        "Gender Wage Gap\nInfluenced by occupational segregation,\ncaregiving expectations, and structural factors",
        xy=(1, 110000),
        xytext=(1.2, 120000),
        arrowprops=dict(facecolor="black", shrink=0.05, width=1, headwidth=5),
        fontsize=9,
        bbox=dict(
            boxstyle="round,pad=0.3", fc="#fff2cc", ec="#d6b656", alpha=0.9
        ),
    )

    # Format y-axis ticks as currency
    ax.yaxis.set_major_formatter("${x:,.0f}")
    ax.legend(title="Gender Group", loc="upper right")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    sex_vs_gender_concepts()
    df_wage = analyze_gender_wage_gap()
    plot_gender_wage_gap(df_wage)