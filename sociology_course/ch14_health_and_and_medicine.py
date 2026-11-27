# SOCI 1101: Introduction to Sociology - Chapter 14: Health and Medicine
# Key sociological concepts, perspectives, and study quiz

chapter_14 = {
    "course": "SOCI 1101: Introduction to Sociology",
    "chapter": "Chapter 14: Health and Medicine",
    "core_concepts": {
        "Health": "A state of complete physical, mental, and social well-being, not merely the absence of disease or infirmity (WHO).",
        "Medicine": "The social institution concerned with combating disease and improving health.",
        "Social Epidemiology": "The study of how health and disease are distributed across a population based on social factors (class, race, gender, age).",
        "Medicalization": "The process by which non-medical problems become defined and treated as medical conditions (e.g., ADHD, alcoholism).",
        "Sick Role": "Talcott Parsons's concept describing patterned expectations for people who are ill (exempt from normal duties, not blamed, expected to seek help and get well)."
    },
    "theoretical_perspectives": {
        "Structural Functionalism": "Views health as essential for social stability; focuses on the sick role and institutional functions of medicine.",
        "Conflict Theory": "Examines inequalities in healthcare access, profit motives in pharmaceuticals/insurance, and how socioeconomic status shapes health outcomes.",
        "Symbolic Interactionism": "Focuses on how illness and health are socially constructed, doctor-patient interactions, and stigma surrounding certain conditions."
    },
    "social_determinants": [
        "Socioeconomic status (income, education, occupation)",
        "Race and ethnicity (structural racism, environmental hazards, bias in care)",
        "Gender (differences in life expectancy, help-seeking behaviors, reproductive health)",
        "Age and geography (urban vs. rural healthcare access, aging populations)"
    ]
}

quiz = [
    {
        "q": "Which sociological perspective emphasizes how socioeconomic inequality leads to disparities in health and healthcare access?",
        "a": "Conflict theory"
    },
    {
        "q": "Defining a behavioral or social issue as a medical condition requiring treatment is called what?",
        "a": "Medicalization"
    },
    {
        "q": "Who introduced the concept of the 'sick role' in medical sociology?",
        "a": "Talcott Parsons"
    }
]

for term, desc in chapter_14["core_concepts"].items():
    print(f"{term}: {desc}")