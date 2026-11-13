# Quiz App - Created by Iram
# A Simple Python Quiz Application

print("=== Welcome to My Quiz App ===")
print("Created by Iram")
print("Each question carries 10 marks\n")

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["a) Lahore", "b) Islamabad", "c) Karachi", "d) Multan"],
        "answer": "b"
    },
    {
        "question": "Who created Python?",
        "options": ["a) Guido van Rossum", "b) Bill Gates", "c) Mark Zuckerberg", "d) Elon Musk"],
        "answer": "a"
    },
    {
        "question": "What is 2 + 2 * 2 = ?",
        "options": ["a) 6", "b) 8", "c) 4", "d) 10"],
        "answer": "a"
    },
    {
        "question": "What is the full form of HTML?",
        "options": ["a) Hyper Text Markup Language", "b) High Text Machine Language", "c) Hyper Tabular Markup Language", "d) None"],
        "answer": "a"
    }
]

score = 0

for q in questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    
    user_answer = input("Enter your answer (a/b/c/d): ").lower()
    
    if user_answer == q["answer"]:
        print("Correct Answer! +10\n")
        score += 10
    else:
        print(f"Wrong! Correct answer was: {q['answer']}\n")

print("=== Quiz Finished ===")
print(f"Your Total Score: {score} / {len(questions)*10}")

if score >= 30:
    print("Excellent! You are a genius!")
elif score >= 20:
    print("Good Job!")
else:
    print("No problem, try again!")