import json


print("===== Social Engineering Awareness Quiz =====")
print("Training / Awareness Use Only\n")


questions = [
    {
        "question": "1. What is phishing?",
        "options": [
            "A. A type of computer hardware",
            "B. A fraudulent attempt to obtain sensitive information",
            "C. A programming language",
            "D. A backup method"
        ],
        "answer": "B"
    },
    {
        "question": "2. What should you do with a suspicious email link?",
        "options": [
            "A. Click it immediately",
            "B. Forward it to everyone",
            "C. Verify it before clicking",
            "D. Enter your password"
        ],
        "answer": "C"
    },
    {
        "question": "3. Which is a common phishing warning sign?",
        "options": [
            "A. Urgent language",
            "B. Normal greeting",
            "C. Known contact",
            "D. Expected message"
        ],
        "answer": "A"
    },
    {
        "question": "4. Should you share your OTP with someone who calls you?",
        "options": [
            "A. Yes",
            "B. Only if they say they are from a bank",
            "C. No",
            "D. Only during an emergency"
        ],
        "answer": "C"
    },
    {
        "question": "5. What is social engineering?",
        "options": [
            "A. Manipulating people to obtain information or access",
            "B. Building a computer",
            "C. Installing an operating system",
            "D. Creating a website"
        ],
        "answer": "A"
    },
    {
        "question": "6. What should you do if someone asks for your password?",
        "options": [
            "A. Share it",
            "B. Refuse and follow security procedures",
            "C. Send it by email",
            "D. Post it online"
        ],
        "answer": "B"
    },
    {
        "question": "7. Which sender should be treated carefully?",
        "options": [
            "A. An expected official sender",
            "B. A trusted contact",
            "C. An unknown sender",
            "D. Your own email"
        ],
        "answer": "C"
    },
    {
        "question": "8. What is baiting?",
        "options": [
            "A. Using an attractive offer or item to trick a person",
            "B. Updating software",
            "C. Creating a backup",
            "D. Encrypting a file"
        ],
        "answer": "A"
    },
    {
        "question": "9. What should you check before opening an attachment?",
        "options": [
            "A. Whether the source is trusted",
            "B. File color",
            "C. Screen brightness",
            "D. Computer wallpaper"
        ],
        "answer": "A"
    },
    {
        "question": "10. What is vishing?",
        "options": [
            "A. Voice-based social engineering or phishing",
            "B. A type of antivirus",
            "C. A network cable",
            "D. A file format"
        ],
        "answer": "A"
    },
    {
        "question": "11. What is smishing?",
        "options": [
            "A. Phishing through text messages",
            "B. A password manager",
            "C. A firewall",
            "D. A database"
        ],
        "answer": "A"
    },
    {
        "question": "12. What is the safest response to an unexpected password-reset message?",
        "options": [
            "A. Click the link",
            "B. Reply with your password",
            "C. Verify through the official service",
            "D. Share the message publicly"
        ],
        "answer": "C"
    }
]


score = 0
answers = []


for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Your answer: ").strip().upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
        result = "Correct"
    else:
        print("Incorrect. Correct answer:", q["answer"])
        result = "Incorrect"

    answers.append({
        "question": q["question"],
        "your_answer": user_answer,
        "correct_answer": q["answer"],
        "result": result
    })


total = len(questions)
percentage = (score / total) * 100


if percentage >= 80:
    level = "Excellent"
elif percentage >= 60:
    level = "Good"
else:
    level = "Needs Improvement"


print("\n===== Quiz Result =====")
print("Total Questions:", total)
print("Correct Answers:", score)
print("Incorrect Answers:", total - score)
print("Score:", f"{percentage:.2f}%")
print("Performance:", level)


report = {
    "quiz": "Social Engineering Awareness Quiz",
    "total_questions": total,
    "correct_answers": score,
    "incorrect_answers": total - score,
    "score_percentage": round(percentage, 2),
    "performance": level,
    "answers": answers
}


with open("awareness_quiz_report.json", "w") as file:
    json.dump(report, file, indent=4)


print("\nScore report saved as: awareness_quiz_report.json")
print("Quiz completed.")