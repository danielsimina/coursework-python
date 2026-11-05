# Sociology Study Tool: The Economy and Politics

flashcards = {
    # Politics & Government Concepts
    "Power": "The ability to exercise one's will over others, even in the face of resistance (Max Weber).",
    "Authority": "Power that people accept because it is perceived as legitimate rather than coercive.",
    "Traditional Authority": "Power legitimized by long-standing customs, traditions, and historical accepted practices (e.g., monarchies).",
    "Charismatic Authority": "Power legitimized by extraordinary personal qualities or magnetism of a leader (e.g., Martin Luther King Jr., Gandhi).",
    "Rational-Legal Authority": "Power legitimized by legal, written rules and regulations, such as a constitution or official laws (e.g., modern democracies).",
    "Power Elite": "A small group of wealthy, influential individuals (military, corporate, political leaders) who control top decision-making (C. Wright Mills).",

    # Economic Systems & Work
    "Economy": "The social institution through which a society's resources (goods and services) are produced, distributed, and consumed.",
    "Capitalism": "An economic system characterized by private ownership of assets, market competition, and the pursuit of profit.",
    "Socialism": "An economic system where the means of production are collectively/government owned to share wealth equally.",
    "Convergence Theory": "The theory that as capitalist and socialist nations industrialize, they gradually adopt features of each other's systems.",
    "Primary Sector": "The sector of the economy that extracts raw materials directly from nature (e.g., agriculture, mining, fishing).",
    "Secondary Sector": "The sector of the economy that turns raw materials into manufactured goods (e.g., auto assembly, construction).",
    "Tertiary Sector": "The sector of the economy that provides services rather than producing physical goods (e.g., healthcare, education, tech support)."
}

def run_study_session():
    print("==========================================================")
    print("   Sociology Quiz: The Economy & Politics              ")
    print("==========================================================")
    score = 0

    for term, definition in flashcards.items():
        print(f"\n[Term]: {term}")
        input("Press Enter to reveal definition...")
        print(f"[Definition]: {definition}")

        feedback = input("\nDid you know this? (y/n): ").strip().lower()
        if feedback == 'y':
            score += 1

    print("\n==========================================================")
    print(f"Session finished! Your final score: {score} / {len(flashcards)}")
    print("==========================================================")

if __name__ == "__main__":
    run_study_session()