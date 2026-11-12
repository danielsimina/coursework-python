# HUMN 1101 Chapter 4 Quick Study Tool

world_religions_glossary = {
    "Dharma": "Right behavior, duty, or social obligation in Hinduism.",
    "Moksha": "Liberation from the endless cycle of reincarnation (samsara).",
    "Nirvana": "The state of profound peace and liberation from suffering in Buddhism.",
    "Kaaba": "The sacred cubic shrine located in Mecca, central to Islamic pilgrimage.",
    "Covenant": "A sacred binding agreement between God and humanity (central to Judaism)."
}

print("--- HUMN Chapter 4 Flashcard Quiz ---")
for term, definition in world_religions_glossary.items():
    input(f"\nPress Enter to reveal definition for: {term}")
    print(f"-> {definition}")