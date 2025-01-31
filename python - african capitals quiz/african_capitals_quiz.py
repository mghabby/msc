import random  # I want the questions to appear in random order each time they're asked.
from difflib import SequenceMatcher  # I found something online called SequenceMatcher which I used to help with checking spelling variations.

# I created this program allows users to answer questions about African capital cities and keeps track of their scores.

def display_quiz_review(user_name, correct_answers, incorrect_answers):
    """
    Function to display a detailed review of the user's quiz performance.
    Shows which answers were correct and which were incorrect.
    """
    print(f"\n--- {user_name}'s Quiz Review ---")  # The title I have for the review
    print("Correct Answers:")  # The header I have for correct answers section
    for question, user_answer, correct_answer in correct_answers:  # Loop through each correct answer
        print(f"- {question} (Your answer: {user_answer})")  # Display each correct question and the user's answer

    print("\nIncorrect Answers:")  # Header for incorrect answers section
    for question, user_answer, correct_answer in incorrect_answers:  # Loop through each incorrect answer
        print(f"- {question} (Your answer: {user_answer}) | Correct answer: {correct_answer}")  # Display the question, user's wrong answer, and the correct one


def get_number_of_questions(quiz_data):
    """
    Function to prompt the user to choose how many questions they want to answer.
    It ensures that the user inputs a number between 5 and the maximum available questions.
    """
    while True:  # Repeat until the player provides a valid input
        try:
            # Ask the player how many questions they want to answer
            num_questions = int(input(f"How many questions would you like to answer? (5 to {len(quiz_data)}): "))
            if 5 <= num_questions <= len(quiz_data):  # Check if the input is within the valid range (I set a minimum of 5qs and max of 20)
                return num_questions  # Return the valid number of questions
            else:
                raise ValueError  # Raise an error to trigger the except block if out of range
        except ValueError:  # Catch invalid inputs (non-integer or out of range)
            print(f"Invalid input! Please enter a number between 5 and {len(quiz_data)}.")  # Show an error message


def check_answer(user_answer, correct_answer):
    """
    Function to check if the user's answer is correct.
    Also considers minor spelling mistakes by using SequenceMatcher.
    """
    # Convert both user's answer and correct answer to lowercase to ignore case sensitivity
    user_answer = user_answer.strip().lower()
    correct_answer = correct_answer.strip().lower()

    # If the answers match exactly, return True
    if user_answer == correct_answer:
        return True

    # Calculate similarity between user's answer and correct answer using SequenceMatcher
    similarity = SequenceMatcher(None, user_answer, correct_answer).ratio()
    return similarity >= 0.8  # Return True if the similarity is 80% or higher


def main():
    """Main function to run the African Capitals Quiz program."""
    print("Welcome to the African Capitals Quiz!")  # Greet the user

    # Define a dictionary of quiz questions and their correct answers
    quiz_data = {
        "What is the capital of Nigeria?": "Abuja",
        "What is the capital of Egypt?": "Cairo",
        "What is the capital of Kenya?": "Nairobi",
        "What is the capital of Ghana?": "Accra",
        "What is the capital of Ethiopia?": "Addis Ababa",
        "What is the capital of South Africa?": "Pretoria",
        "What is the capital of Uganda?": "Kampala",
        "What is the capital of Tanzania?": "Dodoma",
        "What is the capital of Botswana?": "Gaborone",
        "What is the capital of Senegal?": "Dakar",
        "What is the capital of Zimbabwe?": "Harare",
        "What is the capital of Zambia?": "Lusaka",
        "What is the capital of Morocco?": "Rabat",
        "What is the capital of Algeria?": "Algiers",
        "What is the capital of Tunisia?": "Tunis",
        "What is the capital of Libya?": "Tripoli",
        "What is the capital of Mali?": "Bamako",
        "What is the capital of Namibia?": "Windhoek",
        "What is the capital of Ivory Coast?": "Yamoussoukro",
        "What is the capital of Sudan?": "Khartoum"
    }

    # Dictionary to store the scores for each user
    user_scores = {}

    # Ask if the user wants to start the quiz
    start_quiz = input("Would you like to start the quiz? (yes/no): ").lower()

    # If the user does not want to start, exit the program
    if start_quiz not in ["yes", "y"]:
        print("Okay, maybe next time!")
        exit()  # Exit the program

    # Loop to allow multiple users to take the quiz one after another
    while start_quiz in ["yes", "y"]:
        # Ask for the user's name
        user_name = input("Please enter your name: ").strip()
        while not user_name:  # Ensure that the user provides a non-empty name
            user_name = input("Name cannot be empty. Please enter your name: ").strip()

        # If a user with the same name has taken the quiz, add an attempt number to the name
        if user_name in user_scores:
            user_attempts = len([key for key in user_scores.keys() if key.startswith(user_name)])
            user_name = f"{user_name}_Attempt_{user_attempts + 1}"

        # Ask the user how many questions they want to answer
        num_questions = get_number_of_questions(quiz_data)

        # Randomly select the number of questions the user wants to answer from the quiz data
        selected_questions = dict(random.sample(list(quiz_data.items()), num_questions))
        questions_list = list(selected_questions.items())  # Convert to a list to shuffle the order
        random.shuffle(questions_list)  # Shuffle the questions for random order

        # Initialize variables to track the user's score and answers
        score = 0  # Score starts at 0
        correct_answers = []  # Store questions the user got right
        incorrect_answers = []  # Store questions the user got wrong

        # Loop through the shuffled questions
        for question, correct_answer in questions_list:
            user_answer = input(question + " ")  # Ask the user the question

            if check_answer(user_answer, correct_answer):  # Check if the answer is correct
                print("Correct!")
                score += 1  # Increase score for each correct answer
                correct_answers.append((question, user_answer, correct_answer))
            else:
                print(f"Incorrect! The correct answer is {correct_answer}.")
                incorrect_answers.append((question, user_answer, correct_answer))

        percentage_score = (score / len(selected_questions)) * 100  # Calculate the percentage score
        user_scores[user_name] = (score, len(selected_questions), percentage_score)  # Store the user's score

        # Display the user's final score and a detailed review
        print(f"\n{user_name}, your final score is {score} out of {len(selected_questions)} ({percentage_score:.2f}%).\n")
        display_quiz_review(user_name, correct_answers, incorrect_answers)

        # Ask if another user wants to take the quiz
        start_quiz = input("Would someone else like to take the quiz? (yes/no): ").lower()

    # Display Final Results for all users
    print("\n--- Final Results ---")
    sorted_users = sorted(user_scores.items(), key=lambda item: item[1][2], reverse=True)  # Sort by percentage
    highest_percentage = sorted_users[0][1][2]  # Get the highest percentage score
    top_scorers = [user for user, data in sorted_users if data[2] == highest_percentage]  # Get users with the highest score

    print(f"Highest Score: {' and '.join(top_scorers)} with {highest_percentage:.2f}%.")  # Display top scorer(s), if someone attempted twice, each attempt is displayed
    
    # Calculate and display the average score
    average_score = sum([data[0] for data in user_scores.values()]) / sum([data[1] for data in user_scores.values()]) * 100
    print(f"Average Score of All Users: {average_score:.2f}%")  # Display the average score

    print("{:<15} {:<10} {:<10} {:<15}".format("User Name", "Score", "Questions", "Percentage"))  # Table headers
    print("-" * 55)  # Separator line
    for user, (score, total_questions, percentage) in sorted_users:  # Loop through all users
        print(f"{user:<15} {score:<10} {total_questions:<10} {percentage:.2f}%")  # Display user results in a table format


# Start the quiz by calling the main function
main()  # This is the starting point of the quiz program
