#!/usr/bin/env python3
"""
FYES 1000 - Chapter 1: Navigating College Resources & Transition Tool
Author: College Success & Software Development Integration
"""


def evaluate_readiness():
    print("\n--- 1. College Readiness & Mindset Assessment ---")
    print("Answer the following questions (scale: 1 = Never, 5 = Always):")

    questions = [
        "I take primary ownership of tracking syllabus deadlines without external reminders.",
        "I comfortably approach instructors during office hours for clarification.",
        "I balance daily personal commitments with dedicated independent study blocks.",
        "I use digital tools (calendar, task manager) to manage my weekly workflow."
    ]

    scores = []
    for i, q in enumerate(questions, 1):
        while True:
            try:
                score = int(input(f"Q{i}. {q} (1-5): "))
                if 1 <= score <= 5:
                    scores.append(score)
                    break
                print("Please enter a rating between 1 and 5.")
            except ValueError:
                print("Invalid entry. Please enter a number.")

    avg_score = sum(scores) / len(scores)
    print(f"\nOverall Self-Direction Score: {avg_score:.2f} / 5.00")

    if avg_score >= 4.0:
        print("  * Insight: You show high self-direction, typical of successful college transitions.")
    elif avg_score >= 2.5:
        print(
            "  * Insight: You're building solid habits. Focus on proactive syllabus tracking and instructor outreach.")
    else:
        print(
            "  * Insight: High school expectations rely heavily on external structure; focus on self-advocacy and weekly planning.")


def campus_resources_directory():
    print("\n--- 2. Campus Support Resources Lookup ---")
    print("Key college resources and their primary roles:")

    resources = {
        "Academic Advising": "Course selection, degree pathway tracking, and graduation requirements.",
        "Tutoring / Learning Center": "Free academic support, peer tutoring, and subject-specific assistance.",
        "Student Success Center": "Study skill coaching, time management support, and academic recovery tools.",
        "Library Services": "Academic research databases, quiet study spaces, citations, and interlibrary loans.",
        "Financial Aid": "Scholarships, FAFSA assistance, work-study opportunities, and tuition counseling.",
        "Accessibility / Disability Services": "Academic accommodations and auxiliary aids for qualified students."
    }

    for idx, (name, desc) in enumerate(resources.items(), 1):
        print(f"  {idx}. {name}: {desc}")


def syllabus_breakdown():
    print("\n--- 3. Course Syllabus Breakdown Helper ---")
    try:
        assignments_weight = float(input("Enter total percentage for homework/assignments (%): "))
        exams_weight = float(input("Enter total percentage for exams/quizzes (%): "))
        final_weight = float(input("Enter percentage for the final project/exam (%): "))
    except ValueError:
        print("Invalid numerical input.")
        return

    total = assignments_weight + exams_weight + final_weight
    print(f"\nTotal Weight Accounted For: {total}%")

    if abs(total - 100.0) > 0.01:
        print("  * Note: The weights provided do not sum to 100%. Check your syllabus breakdown.")
    else:
        print("  * Weight Distribution Validated:")
        print(f"    - Daily Workflow (Assignments): {assignments_weight}%")
        print(f"    - Major Milestones (Exams): {exams_weight}%")
        print(f"    - Final Assessment: {final_weight}%")


def main():
    while True:
        print("\n==============================================")
        print("  FYES 1000 Chapter 1: College Transition Hub  ")
        print("==============================================")
        print("1. Run Self-Directed Readiness Assessment")
        print("2. View Essential Campus Resources Directory")
        print("3. Syllabus Grade Weight Breakdown")
        print("4. Exit")

        choice = input("\nSelect an option (1-4): ").strip()

        if choice == '1':
            evaluate_readiness()
        elif choice == '2':
            campus_resources_directory()
        elif choice == '3':
            syllabus_breakdown()
        elif choice == '4':
            print("\nExiting. Good luck with your semester goals!")
            break
        else:
            print("\nInvalid choice. Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()