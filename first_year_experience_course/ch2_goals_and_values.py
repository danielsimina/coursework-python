#!/usr/bin/env python3
"""
FYES 1000 - Chapter 2: Goal Setting, Values & Career Alignment
Author: College Success & Software Development Integration
"""


def smart_goal_builder():
    print("\n--- 1. SMART Goal Constructor ---")
    print("Transform a vague idea into an actionable academic goal.")

    specific = input("1. Specific (What exactly do you want to accomplish?): ").strip()
    measurable = input("2. Measurable (How will you measure success/track progress?): ").strip()
    attainable = input("3. Attainable (What action steps make this realistic?): ").strip()
    relevant = input("4. Relevant (Why does this goal align with your major/career?): ").strip()
    time_bound = input("5. Time-bound (What is your exact deadline?): ").strip()

    print("\n" + "=" * 50)
    print("  YOUR SMART GOAL STATEMENT")
    print("=" * 50)
    print(f"By {time_bound}, I will {specific.lower()} by doing the following: {attainable.lower()}.")
    print(f"Progress Metric: {measurable}")
    print(f"Core Purpose: {relevant}")


def values_alignment_check():
    print("\n--- 2. Core Values & Career Alignment ---")
    print("Rank how important each core work value is to your long-term satisfaction (1 = Low, 5 = High):")

    values = {
        "Autonomy & Self-Reliance": "Working independently, solving problems on your own terms.",
        "High Income Potential": "Financial security and strong ROI on your degree.",
        "Continuous Learning": "Mastering complex systems, technical tools, and theoretical logic.",
        "Work-Life Balance": "Maintaining distinct boundaries between work and personal life.",
        "Social Impact": "Directly helping individuals or improving community outcomes."
    }

    ratings = {}
    for val, desc in values.items():
        while True:
            try:
                score = int(input(f"\n* {val} ({desc})\n  Rating (1-5): "))
                if 1 <= score <= 5:
                    ratings[val] = score
                    break
                print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Enter an integer.")

    print("\n--- Top Priority Values ---")
    sorted_values = sorted(ratings.items(), key=lambda x: x[1], reverse=True)
    for val, score in sorted_values:
        print(f"  [{score}/5] {val}")

    top_value = sorted_values[0][0]
    print(f"\nKey Takeaway: Ensure your target academic pathways directly support '{top_value}'.")


def locus_of_control_assessment():
    print("\n--- 3. Locus of Control Self-Check ---")
    print("Indicate whether you agree (a) or (b) for each scenario:")

    scenarios = [
        {
            "a": "My course grades reflect my preparation, execution, and study habits.",
            "b": "My course grades depend mostly on how tough the instructor or exam is."
        },
        {
            "a": "When I struggle with a concept, I change my study strategies or seek support.",
            "b": "When I struggle with a concept, it usually means I lack natural talent in that subject."
        },
        {
            "a": "I control my weekly schedule by prioritizing high-value tasks early.",
            "b": "Unexpected events and outside demands constantly derail my plans."
        }
    ]

    internal_count = 0
    for idx, s in enumerate(scenarios, 1):
        print(f"\nScenario {idx}:")
        print(f"  (a) {s['a']}")
        print(f"  (b) {s['b']}")
        choice = input("Select (a) or (b): ").strip().lower()
        if choice == 'a':
            internal_count += 1

    print(f"\nResult: {internal_count} / {len(scenarios)} internal-locus choices.")
    if internal_count >= 2:
        print("  * Mindset: Strong Internal Locus of Control. You take active ownership of academic outcomes.")
    else:
        print(
            "  * Mindset: External Locus of Control orientation. Work on shifting focus to factors directly within your influence.")


def main():
    while True:
        print("\n==============================================")
        print("  FYES 1000 Chapter 2: Goals & Mindset Hub    ")
        print("==============================================")
        print("1. Construct a SMART Goal")
        print("2. Run Values & Career Alignment Check")
        print("3. Assess Locus of Control")
        print("4. Exit")

        choice = input("\nSelect an option (1-4): ").strip()

        if choice == '1':
            smart_goal_builder()
        elif choice == '2':
            values_alignment_check()
        elif choice == '3':
            locus_of_control_assessment()
        elif choice == '4':
            print("\nExiting. Stay focused on your goals!")
            break
        else:
            print("\nInvalid choice. Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()