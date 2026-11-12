def rise_of_west_quiz():
    print("==========================================================================")
    print(" HUMN 1101: Chapter 5 - The Rise of the West & the Wider World Study Tool")
    print("==========================================================================\n")

    quiz_questions = [
        {
            "question": "1. What term describes the massive global exchange of plants, animals, cultures, populations, and technology between the Eastern and Western Hemispheres following 1492?",
            "options": [
                "A) The Silk Road Exchange",
                "B) The Columbian Exchange",
                "C) The Triangular Route",
                "D) The Mercantile Transfer"
            ],
            "answer": "B",
            "explanation": "The Columbian Exchange fundamentally reshaped world agriculture, demographics, and ecology by connecting the Americas, Europe, Africa, and Asia."
        },
        {
            "question": "2. Which intellectual movement emphasized individual human capability, classical learning, and worldly observation, providing the foundation for Western expansion?",
            "options": [
                "A) Renaissance Humanism",
                "B) Scholasticism",
                "C) Feudalism",
                "D) Monasticism"
            ],
            "answer": "A",
            "explanation": "Renaissance Humanism shifted attention toward worldly discovery, scientific inquiry, and individual potential, fueling global exploration."
        },
        {
            "question": "3. Which economic policy dominated European nations during this era, holding that national power depended on accumulating bullion (gold/silver) through a positive balance of trade?",
            "options": [
                "A) Laissez-faire capitalism",
                "B) Mercantilism",
                "C) Socialism",
                "D) Manorialism"
            ],
            "answer": "B",
            "explanation": "Mercantilism drove European imperial expansion as states sought colonies for raw materials and captive consumer markets."
        },
        {
            "question": "4. What technological synthesis allowed European navigators to embark on transoceanic voyages during the Age of Discovery?",
            "options": [
                "A) Steam turbines and metal hulls",
                "B) Caravel ships, lateen sails, magnetic compass, and astrolabe",
                "C) Paddleboats and waterwheels",
                "D) Rowed galleys and iron claddings"
            ],
            "answer": "B",
            "explanation": "By combining European hull design with Islamic/Arab lateen sails and Chinese navigational technology (compass), ocean travel became viable."
        },
        {
            "question": "5. How did Western artistic representations of non-European cultures often change during the initial centuries of global contact?",
            "options": [
                "A) Total rejection of foreign aesthetics and goods",
                "B) Fascination and assimilation of exotic luxury items (e.g., porcelain, silk, lacquered wood)",
                "C) Complete adoption of Asian religious iconography in Western cathedrals",
                "D) Immediate isolation from foreign trade networks"
            ],
            "answer": "B",
            "explanation": "Western elites highly prized Asian textiles, Chinese porcelain, and foreign craftsmanship, integrating these styles into European luxury art."
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

    print("==========================================================================")
    print(f" Quiz Complete! Your Score: {score}/{len(quiz_questions)}")
    percentage = (score / len(quiz_questions)) * 100
    print(f" Percentage: {percentage:.1f}%")
    print("==========================================================================")


if __name__ == "__main__":
    rise_of_west_quiz()