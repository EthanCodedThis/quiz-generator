# Quiz Generator

A Python quiz generator that reads multiple-choice questions from text files, asks the user a chosen number of questions, checks their answers, shows their score, and reviews missed questions at the end.

## Features

- Loads questions from one or more `.txt` files
- Lets the user choose quiz length
- Randomly selects questions
- Randomly shuffles answer choices
- Grades the quiz automatically
- Shows score and percentage
- Displays missed questions with correct answers

## Question File Format

Use exactly this format for every question:

QUESTION: [question text]
A: [choice A]
B: [choice B]
C: [choice C]
D: [choice D]
ANSWER: [single letter only]

Leave one blank line between questions.

## Example

QUESTION: Which Windows command displays IP configuration information?
A: ping
B: ipconfig
C: tracert
D: netstat
ANSWER: B

## How to Run

1. Put your question files in the same folder as the Python script
2. Put your txt file name in the QUESTION_FILES list where it currently says "a+_core2_questions1&2.txt"
3. Open a terminal in that folder
4. Run:

```bash
python Exam_generator.py

