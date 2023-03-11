

import random

def print_board(board):
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("---+---+---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("---+---+---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")

def check_win(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
       (board[4] == player and board[5] == player and board[6] == player) or \
       (board[7] == player and board[8] == player and board[9] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[3] == player and board[6] == player and board[9] == player) or \
       (board[1] == player and board[5] == player and board[9] == player) or \
       (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False

def play_game():
    board = [" "] * 10
    board[5] = "X"
    print_board(board)
    while True:
        user_move = int(input("Enter your move (1-9): "))
        if board[user_move] != " ":
            print("That square is already occupied. Try again.")
            continue
        board[user_move] = "O"
        if check_win(board, "O"):
            print_board(board)
            print("Congratulations, you win!")
            break
        if " " not in board:
            print_board(board)
            print("The game ends in a draw.")
            break
        machine_move = random.randint(1, 9)
        while board[machine_move] != " ":
            machine_move = random.randint(1, 9)
        board[machine_move] = "X"
        print_board(board)
        if check_win(board, "X"):
            print("Sorry, you lose.")
            break

play_game()