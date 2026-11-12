def greek_legacy_quiz():
    print("==================================================")
    print(" HUMN 1101: Chapter 2 - The Greek Legacy Study Tool")
    print("==================================================\n")

    quiz_questions = [
        {
            "question": "1. What core aesthetic and cultural movement emphasized order, balance, symmetry, and human reason in ancient Greece?",
            "options": ["A) Romanticism", "B) Classicism", "C) Baroque", "D) Mannerism"],
            "answer": "B",
            "explanation": "Classicism prioritizes harmony, balance, proportion, and rational order, serving as the artistic foundation of ancient Greece."
        },
        {
            "question": "2. Which classical Greek architectural order is characterized by simple, heavy capitals and no individual base?",
            "options": ["A) Ionic", "B) Corinthian", "C) Doric", "D) Tuscan"],
            "answer": "C",
            "explanation": "The Doric order is the simplest and sturdiest of the Greek architectural orders, featuring plain cushion-like capitals."
        },
        {
            "question": "3. What sculptural technique, meaning 'counterpoise,' introduced natural weight-shift and realism to Greek statues?",
            "options": ["A) Contrapposto", "B) Relief carving", "C) Frieze detailing", "D) Encaustic painting"],
            "answer": "A",
            "explanation": "Contrapposto has the figure shift its weight onto one foot, creating a natural, relaxed, and lifelike curve in the spine and hips."
        },
        {
            "question": "4. Which Greek philosopher taught through rigorous questioning (the Socratic method) and was condemned for corrupting the youth?",
            "options": ["A) Aristotle", "B) Plato", "C) Socrates", "D) Pythagoras"],
            "answer": "C",
            "explanation": "Socrates pioneered dialectic questioning to stimulate critical thinking and uncover underlying moral definitions."
        },
        {
            "question": "5. What term describes the ancient Greek worldview that placed human beings, human experience, and human reason at the center of inquiry ('man is the measure of all things')?",
            "options": ["A) Theocentrism", "B) Humanism", "C) Stoicism", "D) Hedonism"],
            "answer": "B",
            "explanation": "Humanism celebrates human potential, intellectual capability, and individual agency."
        }
    ]

    score = 0

    for item in quiz_questions:
        print(item["question"])
        for opt in item["options"]:
            print(f"  {opt}")

        user_answer = input("\nEnter your answer (A, B, C, or D): ").strip().upper()

        if user_answer == item["answer"]:
            print("✔ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {item['answer']}.")
            print(f"Explanation: {item['explanation']}\n")

    print("==================================================")
    print(f" Quiz Complete! Your Score: {score}/{len(quiz_questions)}")
    percentage = (score / len(quiz_questions)) * 100
    print(f" Percentage: {percentage}%")
    print("==================================================")


if __name__ == "__main__":
    greek_legacy_quiz()