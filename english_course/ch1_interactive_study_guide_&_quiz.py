# English 1101 - Chapter 1 Interactive Study Guide & Quiz
# Core Concepts: Rhetorical Situation, Writing Process, Rhetorical Appeals

def show_chapter_overview():
    print("=" * 65)
    print(" ENGLISH 1101: CHAPTER 1 - INTRODUCTION TO RHETORIC & WRITING ")
    print("=" * 65)
    print("\n1. THE RHETORICAL SITUATION")
    print("   • Writer: Who is creating the text and what is their background/bias?")
    print("   • Audience: Who is the intended reader or listener?")
    print("   • Purpose: Why is the text being written (to inform, persuade, entertain)?")
    print("   • Exigence: What urgent issue or 'spark' motivated the text?")
    print("   • Context & Genre: The environment, culture, and format of the text.")

    print("\n2. THE WRITING PROCESS (Recursive)")
    print("   • Invention / Prewriting: Brainstorming, outlining, and research.")
    print("   • Drafting: Getting ideas down on paper without immediate self-editing.")
    print("   • Revising: Reorganizing, refining arguments, and strengthening evidence.")
    print("   • Editing & Proofreading: Fixing grammar, punctuation, and mechanics.")

    print("\n3. RHETORICAL APPEALS (Aristotle)")
    print("   • Ethos: Appeal to credibility, ethics, and character.")
    print("   • Pathos: Appeal to emotion, values, and imagination.")
    print("   • Logos: Appeal to logic, reasoning, and evidence.")
    print("   • Kairos: Appeal to timing, opportunity, and the cultural moment.")
    print("=" * 65)


def run_quiz():
    score = 0
    questions = [
        {
            "q": "What term refers to the urgent imperfection or 'spark' that motivates a writer to create a text?",
            "options": ["A) Ethos", "B) Exigence", "C) Genre", "D) Logos"],
            "answer": "B"
        },
        {
            "q": "Which rhetorical appeal focuses on the credibility, character, and authority of the speaker/writer?",
            "options": ["A) Ethos", "B) Pathos", "C) Logos", "D) Kairos"],
            "answer": "A"
        },
        {
            "q": "During which stage of the writing process should you primarily focus on big-picture organization, structure, and thesis development?",
            "options": ["A) Proofreading", "B) Editing", "C) Revising", "D) Formatting"],
            "answer": "C"
        }
    ]

    print("\n--- ENGLISH 1101 CHAPTER 1 PRACTICE QUIZ ---")
    for i, item in enumerate(questions, 1):
        print(f"\nQuestion {i}: {item['q']}")
        for opt in item['options']:
            print(opt)
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        if ans == item['answer']:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {item['answer']}.")

    print(f"\nQuiz Finished! Your score: {score}/{len(questions)}")


if __name__ == "__main__":
    show_chapter_overview()
    choice = input("\nWould you like to take the Chapter 1 interactive quiz? (y/n): ").strip().lower()
    if choice == 'y':
        run_quiz()
    else:
        print("Good luck with your English 1101 studies!")