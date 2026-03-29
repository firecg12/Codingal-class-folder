from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.geometry("600x600")
root.title("Rock Paper Scissors")

# Variables
Playerinput = ""
wins = 0
losses = 0

choices = ["rock", "paper", "scissors"]

# Score label
score_label = Label(root, text="Wins: 0 | Losses: 0", font=("Arial", 12))
score_label.pack(pady=10)
rules_label = Label(root, text=f"THIS IS RPS, \nClick on one of the buttons to pick what you want \nif your lucky u earn a win if not u loose and a score is added to the losses\n BEST OF LUCK!", font=("Arial", 12))
rules_label.pack(pady=30)

def play(user_choice):
    global Playerinput, wins, losses

    Playerinput = user_choice
    computer = random.choice(choices)

    if Playerinput == computer:
        result = "It's a tie!"
    elif (Playerinput == "rock" and computer == "scissors") or \
         (Playerinput == "paper" and computer == "rock") or \
         (Playerinput == "scissors" and computer == "paper"):
        result = "You win!"
        wins += 1
    else:
        result = "You lose!"
        losses += 1

    # Update score on screen
    score_label.config(text=f"Wins: {wins} | Losses: {losses}")

    messagebox.showinfo(
        "Result",
        f"You chose: {Playerinput}\nComputer chose: {computer}\n{result}"
    )

# Buttons
rock_btn = Button(root, text="ROCK", command=lambda: play("rock"), bg="red", width=10)
paper_btn = Button(root, text="PAPER", command=lambda: play("paper"), bg="blue", width=10)
scissors_btn = Button(root, text="SCISSORS", command=lambda: play("scissors"), bg="green", width=10)

rock_btn.pack(pady=10)
paper_btn.pack(pady=10)
scissors_btn.pack(pady=10)

root.mainloop()