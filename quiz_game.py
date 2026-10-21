questions = [
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C",
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. int", "B. bool", "C. str", "D. list"],
        "answer": "B",
    },
    {
        "question": "What does len('Python') return?",
        "options": ["A. 5", "B. 6", "C. 7", "D. Error"],
        "answer": "B",
    },
    {
        "question": "Which symbol starts a comment in Python?",
        "options": ["A. //", "B. <!--", "C. #", "D. **"],
        "answer": "C",
    },
    {
        "question": "Which collection stores key-value pairs?",
        "options": ["A. tuple", "B. set", "C. list", "D. dictionary"],
        "answer": "D",
    },
]

score = 0
print("===== PYTHON QUIZ =====")

for number, item in enumerate(questions, start=1):
    print(f"\nQ{number}. {item['question']}")
    for option in item["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", item["answer"])

print(f"\nFinal score: {score}/{len(questions)}")
