import random

#Function that prints the game board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

#Function that lets players play again
def play_again():
    while True:
        choice = input("Play again? Yes or no? ").lower()

        if choice == "yes" or choice == "y":
            return True

        if choice == "no" or choice == "n":
            return False

        print("Please enter yes or no.")

#Function that lets players choose X or O
def choose_player_marker():
    while True:
        marker = input("\nDo you want to be X or O? ").upper()

        if marker == "X" or marker == "O":
            return marker

        print("Please choose X or O.")

#Function that appears to clear the screen and keeps just the current board.
def clear_screen():
    print("\n" * 50)

#Function that allows player to choose moves.
def get_player_move(board, player):
    while True:
        move = input(f"Player {player}, choose a spot 1-9: ")

        if not move.isdigit():
            print("Please enter a whole number.\n")
            continue

        move = int(move)

        if move < 1 or move > 9:
            print("Please choose a number from 1 to 9.\n")
            continue

        index = move - 1

        if board[index] == "X" or board[index] == "O":
            print("That spot is already taken.\n")
            continue

        board[index] = player
        break

#Function for computer playing on easy mode.
def easy_computer_move(board, computer_marker):
    available_spots = []

    for spot in board:
        if spot != "X" and spot != "O":
            available_spots.append(spot)

    choice = random.choice(available_spots)
    board[int(choice) - 1] = computer_marker

#Function for computer playing on medium mode.
def medium_computer_move(board, computer_marker,player_marker):
     available_spots = []

     for spot in board:
         if spot != "X" and spot != "O":
             available_spots.append(spot)

     choice = random.choice(available_spots)
     board[int(choice) - 1] = computer_marker

#Function for determining computer playing on hard mode.
def hard_computer_move(board, computer_marker, player_marker):
    available_spots = []

    for spot in board:
        if spot != "X" and spot != "O":
            available_spots.append(spot)

    choice = random.choice(available_spots)
    board[int(choice) - 1] = computer_marker

#Function that determines computer's move.
def computer_move(board, computer_marker, player_marker, difficulty):

    if difficulty == "easy":
        easy_computer_move(board, computer_marker)

    elif difficulty == "medium":
        medium_computer_move(board, computer_marker, player_marker)

    elif difficulty == "hard":
        hard_computer_move(board, computer_marker, player_marker)




#Function for determining win conditions.
def check_winner(board):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_combinations:
        a, b, c = combo

        if board[a] == board[b] == board[c]:
            return board[a]

    for spot in board:
        if spot != "X" and spot != "O":
            return None

    return "DRAW"

#Function that sets difficulty of the game
def choose_difficulty():
    while True:
        print("Choose a difficulty:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")

        difficulty = input("Enter 1, 2, or 3: ")

        if difficulty == "1":
            return "easy"

        elif difficulty == "2":
            return "medium"

        elif difficulty == "3":
            return "hard"

        else:
            print("Please enter 1, 2, or 3.\n")

#Main function that determines the hub for actions taken.
def main():
    play = True
    print("Welcome to Tic Tac Toe!\n")
    while play:
        board = ["1", "2", "3",
                 "4", "5", "6",
                 "7", "8", "9"]

        game_over = False

        difficulty = choose_difficulty()
        player_marker = choose_player_marker()

        if player_marker == "X":
            computer_marker = "O"
        else:
            computer_marker = "X"

        if computer_marker == "X":
            computer_move(board, computer_marker, player_marker, difficulty)

        while not game_over:
            clear_screen()
            print_board(board)

            get_player_move(board, player_marker)
            winner = check_winner(board)

            if winner:
                clear_screen()
                print_board(board)

                if winner == "DRAW":
                    print("Draw!\n")
                else:
                    print(f"{winner} wins!\n")

                game_over = True
                continue

            computer_move(board, computer_marker, player_marker, difficulty)
            winner = check_winner(board)

            if winner:
                clear_screen()
                print_board(board)

                if winner == "DRAW":
                    print("Draw!\n")
                else:
                    print(f"{winner} wins!\n")

                game_over = True
                continue

        play = play_again()

        if play == False:
            print("Good game. Goodbye!\n")
        else:
            print("Okay, let's go again!\n")

if __name__ == "__main__":
    main()