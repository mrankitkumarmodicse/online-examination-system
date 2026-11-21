
# Online Examination System
# PS No. 67

# List and Dictionary
questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "b"
    },
    {
        "question": "Which data type stores key-value pairs in Python?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "c"
    },
    {
        "question": "Which operator is used for floor division?",
        "options": ["/", "//", "%", "**"],
        "answer": "b"
    },
    {
        "question": "Which function displays output on the screen?",
        "options": ["input()", "print()", "display()", "show()"],
        "answer": "b"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["^", "**", "//", "%"],
        "answer": "b"
    }
]

# Function to start examination
def start_exam():

    correct = 0
    wrong = 0
    skipped = 0

    print("================================")
    print("   ONLINE EXAMINATION SYSTEM")
    print("================================")

    for i in range(len(questions)):

        print("\nQ", i + 1, ".", questions[i]["question"])

        print("a.", questions[i]["options"][0])
        print("b.", questions[i]["options"][1])
        print("c.", questions[i]["options"][2])
        print("d.", questions[i]["options"][3])
        print("s. Skip")

        answer = input("Enter your answer: ").lower()

        if answer == "s":
            skipped = skipped + 1
            print("Question Skipped")

        elif answer == questions[i]["answer"]:
            correct = correct + 1
            print("Correct Answer!")

        elif answer == "a" or answer == "b" or answer == "c" or answer == "d":
            wrong = wrong + 1
            print("Wrong Answer!")

        else:
            print("Invalid Answer!")
            wrong = wrong + 1

    # Calculate marks
    total_marks = len(questions) * 2
    score = correct * 2
    percentage = (score / total_marks) * 100

    # Display result
    show_result(correct, wrong, skipped, score, total_marks, percentage)


# Function to display final result
def show_result(correct, wrong, skipped, score, total_marks, percentage):

    print("\n================================")
    print("       EXAMINATION RESULT")
    print("================================")

    print("Correct Answers:", correct)
    print("Wrong Answers:", wrong)
    print("Skipped Questions:", skipped)

    print("--------------------------------")
    print("Total Marks:", total_marks)
    print("Your Score:", score)
    print("Percentage:", percentage, "%")

    if percentage >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    print("================================")


# Main function
def main():
    print("Welcome to Online Examination")
    print("Total Questions:", len(questions))
    print("Marks Per Question: 2")
    print("Passing Percentage: 40%")

    start_exam()


# Run program
main()
