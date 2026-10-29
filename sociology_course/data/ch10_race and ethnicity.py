# Sociology Chapter 10: Race and Ethnicity Study Tool

flashcards = {
    "Race": "A category of people treated as distinct based on physical characteristics to which a society attaches social significance.",
    "Ethnicity": "Shared culture, such as language, ancestry, practices, and beliefs.",
    "Minority Group": "Any group of people who are singled out for differential and unequal treatment due to physical or cultural characteristics.",
    "Stereotype": "Oversimplified generalizations about groups of people.",
    "Prejudice": "Biased beliefs, thoughts, attitudes, and feelings about a group (an attitude).",
    "Discrimination": "Actions against a group of people based on race, ethnicity, or other characteristics (an action).",
    "Functionalist Perspective": "Views racial and ethnic inequalities through how they maintain social stability, though discrimination creates major dysfunctions.",
    "Conflict Theory Perspective": "Focuses on how the dominant group exploits subordinate groups to maintain power, wealth, and resources.",
    "Symbolic Interactionism": "Examines how race and ethnicity provide symbols that shape daily social interactions and personal identity construction.",
    "Pluralism": "An intergroup relationship model where a mix of cultures each retain their own identity (often called the 'salad bowl')."
}


def run_study_session():
    print("==================================================")
    print("   Sociology Chapter 10: Race & Ethnicity Quiz   ")
    print("==================================================")
    score = 0

    for term, definition in flashcards.items():
        print(f"\n[Term]: {term}")
        input("Press Enter to reveal the definition...")
        print(f"[Definition]: {definition}")

        feedback = input("\nDid you know this? Type 'y' for yes, 'n' for no: ").strip().lower()
        if feedback == 'y':
            score += 1

    print("\n==================================================")
    print(f"Session complete! Your score: {score} / {len(flashcards)}")
    print("==================================================")


if __name__ == "__main__":
    run_study_session()