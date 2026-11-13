# ARTS 1111: Art Appreciation - Chapter 1 Interactive Study Tool

import random


def show_study_guide():
    print("\n" + "=" * 65)
    print("        ARTS 1111: ART APPRECIATION - CHAPTER 1 STUDY GUIDE        ")
    print("=" * 65)
    print("1. Etymology:")
    print("   - 'Humanities' < Latin 'humanus' (human, cultured, refined).")
    print("   - 'Art' < Latin 'ars' (ability/skill) & French 'art'.")
    print("\n2. Essentials of Art:")
    print("   - Human-made, creative (not purely imitative), satisfies human needs,")
    print("     and is expressed through a chosen medium.")
    print("\n3. Subject & Form:")
    print("   - Representational Art: Depicts recognizable objects/scenes.")
    print("   - Non-Representational Art: Focuses on pure form, color, and line.")
    print("   - Form: The physical structure and visual elements.")
    print("   - Content: The underlying meaning or message.")
    print("=" * 65)


def run_quiz():
    questions = [
        {
            "prompt": "What does the Latin word 'ars' mean?",
            "options": ["A) Beauty or truth", "B) Ability or practical skill", "C) Emotion or soul",
                        "D) Culture or history"],
            "answer": "B"
        },
        {
            "prompt": "Which type of art portrays recognizable objects, people, or real-world scenes?",
            "options": ["A) Non-representational art", "B) Abstract art", "C) Representational (Objective) art",
                        "D) Conceptual art"],
            "answer": "C"
        },
        {
            "prompt": "The term 'Humanities' is derived from the Latin word 'humanus', which means:",
            "options": ["A) Human, cultured, and refined", "B) Wild and untamed", "C) Scientific and logical",
                        "D) Ancient and sacred"],
            "answer": "A"
        },
        {
            "prompt": "What refers to the physical elements, design, and structure of a work of art?",
            "options": ["A) Content", "B) Form", "C) Context", "D) Function"],
            "answer": "B"
        }
    ]

    score = 0
    random.shuffle(questions)

    print("\n" + "=" * 65)
    print("         WELCOME TO THE CHAPTER 1 PRACTICE QUIZ          ")
    print("=" * 65)

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['prompt']}")
        for opt in q['options']:
            print(opt)
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        if ans == q['answer']:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {q['answer']}.")

    print("\n" + "=" * 65)
    print(f"Quiz Complete! Your score: {score}/{len(questions)}")
    print("=" * 65)


if __name__ == "__main__":
    while True:
        print("\n--- ARTS 1111 Chapter 1 Menu ---")
        print("1. View Study Guide Summary")
        print("2. Take Practice Quiz")
        print("3. Exit")
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            show_study_guide()
        elif choice == "2":
            run_quiz()
        elif choice == "3":
            print("Exiting study tool. Good luck with your coursework!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")