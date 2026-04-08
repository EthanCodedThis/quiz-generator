## CompTIA A+ 220-1202Practice Exam generator

from pathlib import Path
import random

BASE_DIR = Path(__file__).resolve().parent

QUESTION_FILES = [
    BASE_DIR / "a+_core2_questions1.txt",
    BASE_DIR / "a+_core2_questions2.txt"
]
    
VALID_ANSWERS = ["A", "B", "C", "D"]

def load_questions(file_paths):
    questions = []
    for file_path in file_paths:
        try:
            with open(file_path,"r", encoding="utf-8") as file:
                text = file.read().strip()
        except FileNotFoundError:
            print(f"COULD NOT FIND FILE: {file_path}")
            continue

        if not text:
            print(f"FILE IS EMPTY: {file_path}")
            continue

        blocks = text.split("\n\n")

        for block in blocks:
            lines = [line.strip() for line in block.splitlines() if line.strip()]

            if len(lines) <6:
                print(f"INVALID QUESTION FORMAT IN FILE: {file_path}")
                continue

            question_text = lines[0].replace("QUESTION: ","")
            choice_a = lines[1].replace("A: ","")
            choice_b = lines[2].replace("B: ","")
            choice_c = lines[3].replace("C: ","")
            choice_d = lines[4].replace("D: ","")
            correct_answer = lines[5].replace("ANSWER: ","").upper()

            if correct_answer not in VALID_ANSWERS:
                print(f"INVALID CORRECT ANSWER IN FILE: {file_path}")
                continue

            question = {
                "question": question_text,
                "choices":{
                    "A": choice_a,
                    "B": choice_b,
                    "C": choice_c,
                    "D": choice_d

                },
                "answer": correct_answer
            }
            questions.append(question)
    return questions
def ask_for_quiz_size(total_available_questions):
    while True:
        raw = input(f"HOW MANY QUESTIONS WOULD YOU LIKE IN YOUR QUIZ? (5-{total_available_questions}):\n").strip()

        if not raw.isdigit():
            print("PLEASE ENTER A VALID NUMBER.")
            continue

        amount = int(raw)

        if 5 <= amount <= total_available_questions:
            return amount
        
        print(f"PLEASE ENTER A NUMBER BETWEEN 5 AND {total_available_questions}.")

## shuffles the answers and figures out the new correct answer

def shuffle_choices(question):
    options = []

    for letter, text in question["choices"].items():
        options.append({
            "text": text,
            "is_correct": letter == question["answer"]
        })

    random.shuffle(options)

    new_choices = {}
    new_answer = ""

    for new_letter, option in zip(VALID_ANSWERS, options):
        new_choices[new_letter] = option["text"]

        if option["is_correct"]:
            new_answer = new_letter

    return {
        "question": question["question"],
        "choices": new_choices,
        "answer": new_answer
    }
    

def run_quiz(selected_questions):
    wrong_questions = []
    score = 0

    for number, item in enumerate(selected_questions, start=1):
        print()
        print(f"Question {number}: {item['question']}")
        print(f"A: {item['choices']['A']}")
        print(f"B: {item['choices']['B']}")
        print(f"C: {item['choices']['C']}")
        print(f"D: {item['choices']['D']}")

        user_answer = input("Your answer: ").strip().upper()

        while user_answer not in VALID_ANSWERS:
            user_answer = input("Please enter A, B, C, or D: ").strip().upper()

        if user_answer == item["answer"]:
            score += 1
        else:
            wrong_questions.append({
                "question": item["question"],
                "your_answer": user_answer,
                "correct_answer": item["answer"],
                "choices": item["choices"]
            })

    return score, wrong_questions
    
def show_results(score, quiz_size, wrong_questions):
    percentage = (score / quiz_size) * 100

    print()
    print("="*60)
    print(f"SCORE: {score}/{quiz_size}")
    print(f"PERCENTAGE: {percentage:.2f}%")

    if wrong_questions:
        print()
        print("REVIEW OF INCORRECT ANSWERS:")
       
        for item in wrong_questions:
            correct_letter = item["correct_answer"]
            correct_text = item["choices"][correct_letter]
            print("-"*60)
            print(f"QUESTION: {item['question']}")
            print(f"YOUR ANSWER: {item['your_answer']}")
            print(f"CORRECT ANSWER: {correct_letter}: {correct_text}")
    else:
        print("ALL ANSWERS WERE CORRECT! GREAT JOB!")


def main():
    questions = load_questions(QUESTION_FILES)

    if not questions:
        print("NO QUESTIONS LOADED. PLEASE CHECK THE FILES.")
        return
    
    print(f"LOADED {len(questions)} QUESTIONS.")

    quiz_size = ask_for_quiz_size(len(questions))
    selected_questions = random.sample(questions, quiz_size)

    randomized_questions = []
    for question in selected_questions:
        randomized_questions.append(shuffle_choices(question))

    score, wrong_questions = run_quiz(randomized_questions)
    show_results(score, quiz_size, wrong_questions)

if __name__ == "__main__":
    main()