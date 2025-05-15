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
        "Question": "What is your age?",
        "Options": ["a. 7", "b. 12", "c. 18", "d. 14"],
        "Answer": "b"
    },
    {
        "Question": "Which college are you in?",
        "Options": ["a. KNUST", "b. UNER", "c. UG", "d. Obuasi Campus"],
        "Answer": "a"
    },
    {
        "Question": "Which year are you in?",
        "Options": ["a. 2", "b. 6", "c. 4", "d. 1"],
        "Answer": "b"
    }
]

for que_set in question_bank:
    print(que_set["Question"])
    for option in que_set["Options"]:
        print(option)
