def rome_legacy_quiz():
    print("==========================================================")
    print(" HUMN 1101: Chapter 3 - The Power & Glory of Rome")
    print("==========================================================\n")

    quiz_questions = [
        {
            "question": "1. What key architectural innovation enabled Roman engineers to build vast, span-defying structures like the Colosseum and Pantheon?",
            "options": [
                "A) Post-and-lintel timber framing",
                "B) Volute capitals and fluted shafts",
                "C) The round arch, vaulting, and concrete (opus caementicium)",
                "D) Flying buttresses and pointed arches"
            ],
            "answer": "C",
            "explanation": "Roman concrete combined with rounded arches and barrel/groin vaults allowed architects to construct massive, durable, interior-focused public spaces."
        },
        {
            "question": "2. What artistic style is famous in Republican Roman portraiture for showing every wrinkle, scar, and flaw to convey wisdom, civic duty, and age?",
            "options": [
                "A) Idealism",
                "B) Verism (Veristic Portraiture)",
                "C) Mannerism",
                "D) Impressionism"
            ],
            "answer": "B",
            "explanation": "Verism emphasizes hyper-realism and stern maturity, honoring ancestors and civic gravitas during the Roman Republic."
        },
        {
            "question": "3. Which epic poem by Virgil was commissioned under Augustus to glorify Rome's divine destiny and establish its mythic origins?",
            "options": [
                "A) The Iliad",
                "B) The Odyssey",
                "C) The Metamorphoses",
                "D) The Aeneid"
            ],
            "answer": "D",
            "explanation": "Virgil wrote the Aeneid to trace Rome's roots to the Trojan prince Aeneas, serving as an imperial propaganda centerpiece for Augustus."
        },
        {
            "question": "4. What monumental temple in Rome features a massive domed ceiling with a central open oculus, dedicated to all the gods?",
            "options": [
                "A) The Parthenon",
                "B) The Pantheon",
                "C) The Ara Pacis",
                "D) The Arch of Titus"
            ],
            "answer": "B",
            "explanation": "Rebuilt by Emperor Hadrian, the Pantheon features a coffered dome with an open circular skylight (oculus) at its apex."
        },
        {
            "question": "5. Which Hellenistic philosophy was most embraced by Roman leaders (like Emperor Marcus Aurelius) due to its emphasis on duty, self-discipline, and natural law?",
            "options": [
                "A) Epicureanism",
                "B) Stoicism",
                "C) Cynicism",
                "D) Skepticism"
            ],
            "answer": "B",
            "explanation": "Stoicism aligned perfectly with Roman traditional virtues (virtus, pietas, and gravitas), emphasizing duty over personal desire."
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

    print("==========================================================")
    print(f" Quiz Complete! Your Score: {score}/{len(quiz_questions)}")
    percentage = (score / len(quiz_questions)) * 100
    print(f" Percentage: {percentage:.1f}%")
    print("==========================================================")


if __name__ == "__main__":
    rome_legacy_quiz()