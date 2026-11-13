# SOCI 1101 Introduction to Sociology: Chapter 12 - Families and Aging

chapter_12_overview = {
    "Module": "SOCI 1101: Introduction to Sociology",
    "Chapter": "12 - Families and Aging",
    "Core_Topics": [
        "1. Marriage and Family Across Cultures",
        "2. Variations in Family Life",
        "3. Challenges Families Face",
        "4. Aging and the Elderly",
        "5. Theoretical Perspectives on Family & Aging"
    ]
}

key_concepts = {
    "Family Definitions": {
        "Family of Orientation": "The family into which a person is born and raised.",
        "Family of Procreation": "The family formed through marriage/partnership and having or adopting children.",
        "Nuclear Family": "Two parents (traditionally married) and their children living in a single household.",
        "Extended Family": "A household that includes parents, children, and other relatives (grandparents, aunts, uncles)."
    },
    "Marriage Patterns": {
        "Monogamy": "Marriage between two partners (Serial monogamy: marrying multiple times, one at a time).",
        "Polygamy": "Marriage to more than one partner at the same time.",
        "Polygyny": "One man married to multiple women.",
        "Polyandry": "One woman married to multiple men.",
        "Endogamy vs. Exogamy": "Marrying within vs. outside one's social group, caste, or category."
    },
    "Kinship & Residence": {
        "Bilateral Descent": "Tracing kinship through both mother's and father's sides (common in the U.S.).",
        "Patrilineal / Matrilineal": "Tracing kinship exclusively through the father's or mother's line.",
        "Neolocal Residence": "Newlyweds establish an independent household separate from both families."
    },
    "Aging & Gerontology": {
        "Gerontology": "The scientific study of aging and the elderly.",
        "Social Gerontology": "The study of the social aspects of aging (roles, attitudes, ageism).",
        "Ageism": "Prejudice and discrimination based on a person's age.",
        "Cohort": "A group of people who share a statistical or demographic trait (e.g., Baby Boomers).",
        "Sandwich Generation": "Adults caring for both their aging parents and their own dependent children."
    },
    "Sociological Perspectives": {
        "Functionalism": "Families perform essential functions (socialization, emotional support, regulating sexual behavior); Disengagement Theory (elderly gradually withdraw from roles).",
        "Conflict Theory": "Families perpetuate social inequality (inheritance, gender roles); Modernization Theory (industrialization lowers the social status of the elderly).",
        "Symbolic Interactionism": "Family roles are socially constructed through daily interaction; Activity Theory (elderly stay happier when active and socially engaged)."
    }
}

print(f"=== {chapter_12_overview['Module']} ===")
print(f"Chapter: {chapter_12_overview['Chapter']}\n")

for category, terms in key_concepts.items():
    print(f"--- {category} ---")
    for term, definition in terms.items():
        print(f"  * {term}: {definition}")
    print()