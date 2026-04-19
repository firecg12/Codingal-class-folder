import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    
    print(colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).upper()
    
    return ('X', 'O') if symbol == 'X' else ('O', 'X')

def player_move(board, symbol):
    while True:
        try:
            move = int(input(Fore.GREEN + "Enter your move (1-9): " + Style.RESET_ALL))
            if move in range(1, 10) and board[move - 1].isdigit():
                board[move - 1] = symbol
                break
            else:
                print(Fore.RED + "That spot is taken or invalid." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input. Enter a number 1-9." + Style.RESET_ALL)

def ai_move(board, ai_symbol, player_symbol):
    # Try to win
    for i in range(9):
        if board[i].isdigit():
            temp = board.copy()
            temp[i] = ai_symbol
            if check_win(temp, ai_symbol):
                board[i] = ai_symbol
                return

    # Block player
    for i in range(9):
        if board[i].isdigit():
            temp = board.copy()
            temp[i] = player_symbol
            if check_win(temp, player_symbol):
                board[i] = ai_symbol
                return

    # Random move
    available = [i for i in range(9) if board[i].isdigit()]
    board[random.choice(available)] = ai_symbol

def check_win(board, symbol):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i] == symbol for i in combo) for combo in wins)

def check_full(board):
    return all(not cell.isdigit() for cell in board)

def tic_tac_toe():
    print(Fore.CYAN + "Welcome to X and O!" + Style.RESET_ALL)
    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)

    while True:
        board = ['1','2','3','4','5','6','7','8','9']
        player_symbol, ai_symbol = player_choice()
        turn = 'Player'
        game_running = True

        while game_running:
            display_board(board)

            if turn == 'Player':
                player_move(board, player_symbol)

                if check_win(board, player_symbol):
                    display_board(board)
                    print(Fore.GREEN + f"Congratulations {player_name}, you win!" + Style.RESET_ALL)
                    game_running = False
                elif check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a tie!" + Style.RESET_ALL)
                    game_running = False
                else:
                    turn = 'AI'

            else:
                ai_move(board, ai_symbol, player_symbol)

                if check_win(board, ai_symbol):
                    display_board(board)
                    print(Fore.RED + "AI wins! Better luck next time." + Style.RESET_ALL)
                    game_running = False
                elif check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a tie!" + Style.RESET_ALL)
                    game_running = False
                else:
                    turn = 'Player'

        again = input(Fore.GREEN + "Play again? (y/n): " + Style.RESET_ALL).lower()
        if again != 'y':
            print(Fore.CYAN + "Thanks for playing!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    tic_tac_toe()