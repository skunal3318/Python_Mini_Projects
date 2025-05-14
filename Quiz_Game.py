'''Quiz Game
Concepts Used: Dictionaries, Loops, Conditionals

Description: Create a simple quiz with multiple questions. Track the score based on correct answers.'''

my_dict = {
    "Question 1": {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
        "answer": "A"
    },
    "Question 2": {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
        "answer": "B"
    },
}

def display_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)


def check_answer(question_data, user_answer):
    if user_answer.upper() == question_data["answer"]:
        return True
    else:
        return False
    
def main():
    score = 0
    total_questions = len(my_dict)
    for question_key, question_data in my_dict.items():
        display_question(question_data)
        user_answer = input("Your answer (A/B/C/D): ")
        
        if check_answer(question_data, user_answer):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question_data['answer']}.")
            print()

    print(f"Your total score is {score} out of {total_questions}.")
if __name__ == "__main__":
    main()
    

