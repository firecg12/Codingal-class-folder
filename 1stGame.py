import time
import random

SECRET_NUMBER = random.randint(1, 100)
MAX_ATTEMPTS = 15

def Start():
    global player_name, stopwatch_start

    while True:
        try:
            player_name = input("Enter your name: ").strip()
            if player_name:
                break
            print("Name cannot be empty.")
        except EOFError:
            print("\nInput cancelled. Exiting game.")
            exit()

    print(f"Hello, {player_name}! Welcome to the Number Guessing Game.")

    if SECRET_NUMBER % 2 == 0:
        print("\nHint: The number is even.")
    else:
        print("\nHint: The number is odd.")

    print(f"You have {MAX_ATTEMPTS} attempts to guess the number.")
    print("Let's begin!")
    stopwatch_start = time.time()

def Play():
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
        except EOFError:
            print("\nGame interrupted. Goodbye!")
            return
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        if guess < 1 or guess > 100:
            print("Number must be between 1 and 100.")
            continue

        attempts += 1

        if guess < SECRET_NUMBER:
            print("Too low! Try again.")
        elif guess > SECRET_NUMBER:
            print("Too high! Try again.")
        else:
            elapsed = time.time() - stopwatch_start
            print(
                f"\nCongratulations, {player_name}! "
                f"You guessed the number in {attempts} attempts "
                f"and {elapsed:.2f} seconds!"
            )
            return

    print(f"\nGame over! The number was {SECRET_NUMBER}.\n Try again next time {player_name}!")

Start()
Play()
