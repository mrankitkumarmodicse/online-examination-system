"""
Online Examination System (Problem Statement No. 67)
Course: Programming Fundamentals and Logic Building Using Python (RU-100-01-0021)
Author: Ankit Kumar Modi

A console-based examination application featuring:
- Question bank stored as a list of dictionaries (keys: question, options, answer)
- 5 Multiple-Choice Questions (MCQs) with options (a-d), 2 marks each (Total: 10 marks)
- Answer Key: Q1-b, Q2-c, Q3-b, Q4-b, Q5-b
- Skip mechanism ('s'/'S') for omitting questions without penalty (0 marks)
- Input validation loop rejecting invalid choices with prescriptive guidance
- Result calculation engine computing Correct, Wrong, Skipped, Score, Percentage, and Pass/Fail (>= 40%)
"""

import sys
from typing import Dict, List, Any


def get_questions() -> List[Dict[str, Any]]:
    """
    Returns the examination question bank.
    Stored strictly as a list of dictionaries with keys:
    - question: str
    - options: dict mapping option key ('a', 'b', 'c', 'd') to option text
    - answer: str (the correct option key)

    Answer Key Specification:
    Q1 -> 'b', Q2 -> 'c', Q3 -> 'b', Q4 -> 'b', Q5 -> 'b'
    """
    return [
        {
            "question": "Which of the following data structures is mutable in Python?",
            "options": {
                "a": "Tuple",
                "b": "List",
                "c": "String",
                "d": "Integer",
            },
            "answer": "b",
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": {
                "a": "func",
                "b": "define",
                "c": "def",
                "d": "function",
            },
            "answer": "c",
        },
        {
            "question": "Which built-in function returns the length of a list or dictionary?",
            "options": {
                "a": "count()",
                "b": "len()",
                "c": "size()",
                "d": "length()",
            },
            "answer": "b",
        },
        {
            "question": "Which method is used to add an item to the end of a list?",
            "options": {
                "a": "insert()",
                "b": "append()",
                "c": "extend()",
                "d": "push()",
            },
            "answer": "b",
        },
        {
            "question": "What is the output of integer division 10 // 3 in Python?",
            "options": {
                "a": "3.33",
                "b": "3",
                "c": "1",
                "d": "3.0",
            },
            "answer": "b",
        },
    ]


VALID_CHOICES = {"a", "b", "c", "d", "s"}
PASS_PERCENTAGE = 40.0
MARKS_PER_QUESTION = 2


def validate_option(user_input: str) -> bool:
    """
    Validates whether the user's input is a valid option key or skip code.
    Allowed values: 'a', 'b', 'c', 'd', 's' (case-insensitive).
    """
    if not user_input:
        return False
    return user_input.strip().lower() in VALID_CHOICES


def prompt_question_answer(q_num: int, q_data: Dict[str, Any]) -> str:
    """
    Presents a question with options, continuously validates user input,
    and returns the sanitized valid answer.
    """
    print(f"\nQuestion {q_num}: {q_data['question']}")
    for opt_key, opt_text in q_data["options"].items():
        print(f"  {opt_key}) {opt_text}")

    while True:
        try:
            raw_input = input("Enter your choice (a, b, c, d or 's' to skip): ")
        except (EOFError, KeyboardInterrupt):
            print("\nExam interrupted by user. Exiting.")
            sys.exit(0)

        choice = raw_input.strip().lower()
        if validate_option(choice):
            print(f"Answer recorded for Q{q_num}: {choice}")
            return choice
        else:
            print("Invalid option. Enter a, b, c, d or s to skip.")


def calculate_results(
    answers: List[str],
    questions: List[Dict[str, Any]],
    marks_per_q: int = MARKS_PER_QUESTION,
    pass_pct: float = PASS_PERCENTAGE
) -> Dict[str, Any]:
    """
    Calculates correct, wrong, and skipped counts, score, percentage,
    and the final Pass/Fail status based on questions and student answers.
    """
    total_questions = len(questions)
    total_marks = total_questions * marks_per_q

    correct_count = 0
    wrong_count = 0
    skipped_count = 0

    for idx, q_data in enumerate(questions):
        student_ans = answers[idx].strip().lower() if idx < len(answers) else "s"
        correct_ans = q_data["answer"].strip().lower()

        if student_ans == "s":
            skipped_count += 1
        elif student_ans == correct_ans:
            correct_count += 1
        else:
            wrong_count += 1

    score = correct_count * marks_per_q
    percentage = (score / total_marks) * 100.0 if total_marks > 0 else 0.0
    result = "Pass" if percentage >= pass_pct else "Fail"

    return {
        "total_questions": total_questions,
        "marks_per_q": marks_per_q,
        "total_marks": total_marks,
        "correct": correct_count,
        "wrong": wrong_count,
        "skipped": skipped_count,
        "score": score,
        "percentage": percentage,
        "result": result,
    }


def display_summary(results: Dict[str, Any]) -> None:
    """
    Displays the formatted examination result summary strictly matching the specification:
    Correct: X | Wrong: Y | Skipped: Z
    Score: X/10 | Percentage: XX.XX% | Result: Pass/Fail
    """
    print("\n" + "=" * 50)
    print("           ONLINE EXAM RESULT SUMMARY")
    print("=" * 50)
    print(f"Correct: {results['correct']} | Wrong: {results['wrong']} | Skipped: {results['skipped']}")
    print(f"Score: {results['score']}/{results['total_marks']} | Percentage: {results['percentage']:.2f}% | Result: {results['result']}")
    print("=" * 50)


def run_exam() -> None:
    """
    Executes the complete online examination workflow:
    1. Loads question bank
    2. Prompts student question by question with input validation
    3. Computes final scores and metrics
    4. Displays result summary banner
    """
    questions = get_questions()
    recorded_answers: List[str] = []

    print("============================================================")
    print("       ONLINE EXAMINATION SYSTEM - PS No. 67")
    print("============================================================")
    print("Total Questions: 5 | Marks per Question: 2 | Total Marks: 10")
    print("Passing Criteria: 40% (Minimum 4 Marks / 2 Correct)")
    print("Instructions: Enter a, b, c, d to answer, or 's' to skip.")
    print("-" * 60)

    for i, q_data in enumerate(questions, start=1):
        ans = prompt_question_answer(i, q_data)
        recorded_answers.append(ans)

    results = calculate_results(recorded_answers, questions)
    display_summary(results)


def main() -> None:
    """
    Main entrypoint for console execution.
    """
    run_exam()


if __name__ == "__main__":
    main()
