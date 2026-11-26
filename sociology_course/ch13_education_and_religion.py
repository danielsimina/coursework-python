questions = [
    {
        "q": "Sorting students into different academic tracks based on perceived ability or test scores is known as:",
        "options": ["a) Tracking", "b) Secularization", "c) Ecclesia", "d) Liberation theology"],
        "answer": "a",
        "explain": "Tracking groups students into distinct educational paths and is often analyzed by conflict theorists for reinforcing inequality."
    },
    {
        "q": "Which concept describes unwritten norms, values, and behavioral expectations taught in schools?",
        "options": ["a) Credentialism", "b) Hidden curriculum", "c) Profane", "d) Protestant ethic"],
        "answer": "b",
        "explain": "The hidden curriculum consists of implicit social rules and authority norms learned alongside formal subjects."
    },
    {
        "q": "In Durkheim's sociology of religion, objects or practices set apart as extraordinary and awe-inspiring are:",
        "options": ["a) Profane", "b) Sectarian", "c) Sacred", "d) Denominational"],
        "answer": "c",
        "explain": "Durkheim distinguished the sacred (revered, set apart) from the profane (everyday, ordinary)."
    },
    {
        "q": "An increase in the minimum educational degree required to enter a given occupation is called:",
        "options": ["a) Correspondence principle", "b) Self-fulfilling prophecy", "c) Credentialism", "d) Secularization"],
        "answer": "c",
        "explain": "Credentialism occurs when employers require higher credentials even when job tasks have not changed accordingly."
    }
]

def run_quiz(bank):
    score = 0
    print("=== SOCI 1101 Ch. 13: Education & Religion Quiz ===\n")
    for i, item in enumerate(bank, 1):
        print(f"{i}. {item['q']}")
        for opt in item["options"]:
            print(f"   {opt}")
        choice = input("Your answer (a/b/c/d): ").strip().lower()
        if choice == item["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Not quite — answer is '{item['answer']}'. {item['explain']}\n")
    print(f"Final Score: {score}/{len(bank)}")

if __name__ == "__main__":
    run_quiz(questions)