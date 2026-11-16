# Online Examination System (PS No. 67)

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP%208-informational.svg)]()

> A console-based online examination application in Python 3. Built strictly according to the curriculum and engineering specifications of **Problem Statement No. 67** for the course *Programming Fundamentals and Logic Building Using Python (`RU-100-01-0021`)*.

---

## 📑 Table of Contents

- [Problem Statement Reference](#problem-statement-reference)
- [Architecture & Design](#architecture--design)
- [Question Bank & Data Structures](#question-bank--data-structures)
- [Scoring Engine & Mathematical Formulation](#scoring-engine--mathematical-formulation)
- [Project Structure](#project-structure)
- [Execution Guide](#execution-guide)
- [Test Case Scenarios Matrix](#test-case-scenarios-matrix)
- [Academic Metadata](#academic-metadata)

---

## Problem Statement Reference

* **PS No.**: 67
* **Project Title**: Online Examination System
* **Language**: Python 3
* **Concepts**: Lists, Dictionaries, Functions, Score Calculation
* **Exam Parameters**:
  * 5 Multiple-Choice Questions (MCQs)
  * Options: `a`, `b`, `c`, `d`
  * Scoring: 2 marks per correct answer; total 10 marks
  * Skip Code: `'s'` / `'S'` (0 marks awarded)
  * Wrong Answers: 0 marks awarded
  * Passing Criterion: At least $40.00\%$ (Minimum 4 marks / 2 correct questions)
* **Official Answer Key**:
  * **Q1**: `b`
  * **Q2**: `c`
  * **Q3**: `b`
  * **Q4**: `b`
  * **Q5**: `b`

---

## Architecture & Design

The solution implements a clean functional design separating Question Model, CLI Session Dispatcher, Input Sanitation, and Score Calculation:

```
┌────────────────────────────────────────────────────────┐
│                   CLI Controller                       │
│        (Session Loop & Student Question Prompter)      │
└───────────────────────────┬────────────────────────────┘
                            │
            ┌───────────────┴───────────────┐
            ▼                               ▼
┌────────────────────────┐      ┌────────────────────────┐
│  Validation Layer      │      │  Question Bank Model   │
│  - Case Normalization  │      │  - List of Dictionaries│
│  - Set Membership O(1) │◄────►│  - Questions & Options │
│  - Re-prompt on Error  │      │  - Ground Truth Keys   │
└────────────────────────┘      └────────────────────────┘
            │                               │
            └───────────────┬───────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│             Evaluation & Scoring Engine                │
│       - Metric Aggregation (Correct/Wrong/Skipped)     │
│       - Score Calculation: Correct * 2                 │
│       - Percentage: (Score / 10) * 100                 │
│       - Pass/Fail Boundary Check (>= 40.00%)           │
└───────────────────────────┬────────────────────────────┘
                            ▼
┌────────────────────────────────────────────────────────┐
│                  Presentation Layer                    │
│             - Console Result Summary Card              │
└────────────────────────────────────────────────────────┘
```

---

## Question Bank & Data Structures

Strictly complying with Bare Minimum Requirement #2, questions are stored as a **List of Dictionaries**:

```python
questions = [
    {
        "question": "Which of the following data structures is mutable in Python?",
        "options": {
            "a": "Tuple",
            "b": "List",
            "c": "String",
            "d": "Integer"
        },
        "answer": "b"
    },
    ...
]
```

---

## Scoring Engine & Mathematical Formulation

Let $N = 5$ (Total Questions) and $M = 2$ (Marks per Question):

$$\text{Total Maximum Marks} = N \times M = 5 \times 2 = 10$$

Let $C$ denote correct answers, $W$ wrong answers, and $S$ skipped questions:

$$N = C + W + S = 5$$

1. **Score Calculation**:
   $$\text{Score} = C \times 2$$
2. **Percentage**:
   $$\text{Percentage} = \left(\frac{\text{Score}}{10}\right) \times 100 = C \times 20.00\%$$
3. **Pass / Fail Logic**:
   $$\text{Result} = \begin{cases} \text{"Pass"}, & \text{if } \text{Percentage} \ge 40.00\% \ (\text{Score} \ge 4) \\ \text{"Fail"}, & \text{if } \text{Percentage} < 40.00\% \ (\text{Score} < 4) \end{cases}$$

---

## Project Structure

```
online-examination-system/
├── online_exam_system.py       # Core application (Single .py file)
├── README.md                   # System documentation
├── summary.md                  # Verification summary with real test screenshots
├── screenshots/                # Real terminal screenshots directory
│   ├── test_case_1_normal.png
│   ├── test_case_2_boundary.png
│   ├── test_case_3_invalid.png
│   └── test_case_4_skipped.png
└── .gitignore                  # Git ignore rules
```

---

## Execution Guide

Run the examination directly from your terminal:

```bash
cd "E:\Online Examination System"
python online_exam_system.py
```

---

## Test Case Scenarios Matrix

| Test Case | Category | Input Sequence | Key Output Verification | Result |
|---|---|---|---|:---:|
| **Test Case 1** | Normal Scenario | `b, c, a, b, b` | `Correct: 4 \| Wrong: 1 \| Skipped: 0`<br>`Score: 8/10 \| Percentage: 80.00% \| Result: Pass` | **PASS** |
| **Test Case 2** | Boundary / Minimum | `b, c, a, a, a` | `Correct: 2 \| Wrong: 3 \| Skipped: 0`<br>`Score: 4/10 \| Percentage: 40.00% \| Result: Pass` | **PASS** |
| **Test Case 3** | Invalid Input | Q1: `e` then `b` | `Invalid option. Enter a, b, c, d or s to skip.`<br>`Answer recorded for Q1: b` | **PASS** |
| **Test Case 4** | Different Scenario (Skip) | `b, s, b, s, b` | `Correct: 3 \| Wrong: 0 \| Skipped: 2`<br>`Score: 6/10 \| Percentage: 60.00% \| Result: Pass` | **PASS** |

---

## Academic Metadata

* **Institution:** Rungta International Skills University
* **School:** School of Computer Science and Engineering
* **Course:** Programming Fundamentals and Logic Building Using Python (`RU-100-01-0021`)
* **Problem Statement No.:** 67
* **Author:** Ankit Kumar Modi
