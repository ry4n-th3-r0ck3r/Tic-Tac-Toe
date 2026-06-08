import random

#Function that prints the game board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

#Function that appears to clear the screen and keeps just the current board.
def clear_screen():
    print("\n" * 50)

#Function that allows player to choose moves.
def get_player_move(board, player):
    while True:
        move = input(f"Player {player}, choose a spot 1-9: ")

        if not move.isdigit():
            print("Please enter a whole number.")
            continue

        move = int(move)

        if move < 1 or move > 9:
            print("Please choose a number from 1 to 9.")
            continue

        index = move - 1

        if board[index] == "X" or board[index] == "O":
            print("That spot is already taken.")
            continue

        board[index] = player
        break

#Function that determines computer's move.
def computer_move(board):
    available_spots = []

    for spot in board:
        if spot != "X" and spot != "O":
            available_spots.append(spot)

    choice = random.choice(available_spots)
    board[int(choice) - 1] = "O"

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

    return None

#Main function that determines the hub for actions taken.
def main():
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]
    current_player = "X"

    game_over = False

    while not game_over:
        clear_screen()
        print_board(board)

        get_player_move(board, current_player)
        winner = check_winner(board)

        if winner:
            clear_screen()
            print_board(board)
            print(f"{winner} wins!")
            game_over = True
            continue

        computer_move(board)
        winner = check_winner(board)

        if winner:
            clear_screen()
            print_board(board)
            print(f"{winner} wins!")
            game_over = True

if __name__ == "__main__":
    main()