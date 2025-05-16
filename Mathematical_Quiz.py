# Questions
# Options
# correct answer

# 1. Create a list called 'questions'
# 2. Each item in the 'question' should be a dictionary with the feature listed above.

question_bank = [
    {
        "Question": "what is the sum of 2 and 4?",
        "Options": ["a. 3", "b. 4", "c. 0", "d. 6"],
        "Answer": "d"
    },
    {
        "Question": "What is the sum of 9 and 7?",
        "Options": ["a. 7", "b. 12", "c. 16", "d. 14"],
        "Answer": "c"
    },
    {
        "Question": "What is the result of 6 times 8?",
        "Options": ["a. 90", "b. 74", "c. 62", "d. 48"],
        "Answer": "d"
    },
    {
        "Question": "A woman bought 17 oranges. She sold 8 of them. How many oranges are left?",
        "Options": ["a. 2", "b. 9", "c. 4", "d. 1"],
        "Answer": "b"
    }
]
score = 0
for que_set in question_bank:

    print(que_set["Question"])

    for option in que_set["Options"]:
        print(option)

    answer = input("Enter the correct answer(a to d):")

    if answer == que_set["Answer"]:
        print("You are right, Hurray!!\n")
        score += 1

    else:
        print("Error\n")

print(f"You scored {score} out of {len(question_bank)} questions correct.\n")

if score >= 2:
    print("You passed")

else:
    print("You failed.\n")

    print("Try again")
