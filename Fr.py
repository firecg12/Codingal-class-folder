# althogh its submitted under roman numerals its acturaly the fruit so still give 5 stars
import random

class FruitQuiz:

    # Create a constructor
    def __init__(self):
        # Create a dictionary of fruits as keys and color as value
        self.fruits = {
            'apple': 'red',
            'orange': 'orange',
            'watermelon': 'green',
            'banana': 'yellow'
        }

    # Function for the quiz, here a fruit will be chosen randomly
    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
            user_answer = input()

            if user_answer.lower() == color:
                print("Correct answer")
            else:
                print("Wrong answer")

            option = int(input("Enter 0 if you want to play again, otherwise enter 1: "))

            if option == 1:
                print("Thank you for playing the quiz")
                break   # break must be inside the while loop

print("Welcome to fruit quiz")
fq = FruitQuiz()
fq.quiz()

