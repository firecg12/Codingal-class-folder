import requests
import html
import time
import random


url = "https://opentdb.com/api.php?amount=1&type=multiple"


def get_random_trivia():
    response = requests.get(url)

    if response.status_code == 200:
        trivia_data = response.json()

        result = trivia_data['results'][0]
        question = html.unescape(result['question'])
        correct_answer = html.unescape(result['correct_answer'])
        incorrect_answers = [
            html.unescape(answer)
            for answer in result['incorrect_answers']
        ]

        options = incorrect_answers + [correct_answer]
        random.shuffle(options)

        return question, correct_answer, options

    else:
        return None, None, None


def main():
    print("Welcome to the Random Trivia Generator!")

    while True:
        user_input = input(
            "Press Enter to get a new trivia question or type 'exit' or 'q' to quit: "
        ).strip().lower()

        if user_input in ('q', 'exit'):
            print("Goodbye!")
            break

        question, correct_answer, options = get_random_trivia()

        if question is None:
            print("Failed to fetch trivia. Please try again later.")
            continue

        print(f"\nQuestion: {question}")
        # display the options in a random order
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        # Add a slight delay so ppl can read the question and options before the countdown starts 
        #show visual 20 second countdown before showing the answer that actually gives the user time to think about the answer
        for i in range(20, 0, -1):
            print(f"Time remaining: {i} seconds", end='\r')
            time.sleep(1)

        print(f"Correct Answer: {correct_answer}")


if __name__ == "__main__":
    main()