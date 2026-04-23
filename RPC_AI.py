import random
from colorama import init, Fore, Style

init(autoreset=True)

moves = ["rock", "paper", "scissors"]

player_score = 0
ai_score = 0

# emoji mapping
emoji = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

def colored_move(move):
    symbol = emoji.get(move, "-")
    
    if move == "rock":
        return Fore.RED + symbol + " rock" + Style.RESET_ALL
    elif move == "paper":
        return Fore.BLUE + symbol + " paper" + Style.RESET_ALL
    elif move == "scissors":
        return Fore.GREEN + symbol + " scissors" + Style.RESET_ALL

def show_instructions():
    print(Fore.MAGENTA + Style.BRIGHT + "\n🎮 ROCK PAPER SCISSORS")
    print(Fore.YELLOW + "Instructions:")
    print("• Type: rock, paper, or scissors")
    print("• Type 'exit' to quit the game")
    print("• First to keep winning... wins 😏")
    print(Fore.CYAN + "-" * 35)

def get_player_move():
    while True:
        move = input(Fore.YELLOW + "Your move: ").lower()
        if move == "exit":
            return None
        if move in moves:
            return move
        else:
            print(Fore.RED + "Invalid input. Try again.")

def get_ai_move():
    return random.choice(moves)

# ✅ FIXED LOGIC (no emojis here)
def determine_winner(player, ai):
    if player == ai:
        return "tie"
    elif (
        (player == "rock" and ai == "scissors") or
        (player == "scissors" and ai == "paper") or
        (player == "paper" and ai == "rock")
    ):
        return "player"
    else:
        return "ai"


# show instructions once
show_instructions()

while True:
    print(Fore.CYAN + "\n--- New Round ---")

    player_move = get_player_move()
    if player_move is None:
        print(Fore.MAGENTA + "Game exited.")
        break

    ai_move = get_ai_move()

    print("You chose:", colored_move(player_move))
    print("AI chose:", colored_move(ai_move))

    result = determine_winner(player_move, ai_move)

    if result == "tie":
        print(Fore.YELLOW + "It's a tie!")
    elif result == "player":
        print(Fore.GREEN + "You win this round!")
        player_score += 1
    else:
        print(Fore.RED + "AI wins this round!")
        ai_score += 1

    print(Fore.CYAN + f"Score → You: {player_score} | AI: {ai_score}")