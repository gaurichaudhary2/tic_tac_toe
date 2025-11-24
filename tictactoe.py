import random

def print_board(board):
    print("\n")
    for i in range(3):
        print(" ", board[i][0], "|", board[i][1], "|", board[i][2])
        if i < 2:
            print(" ---+---+---")
    print("\n")

def check_winner(board, player):
    # Rows, Cols, Diagonals
    win = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win

def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move(board):
    while True:
        try:
            pos = int(input("Enter position (1-9): "))
            if pos < 1 or pos > 9:
                print("Invalid! Enter number between 1-9.")
                continue
            
            r = (pos - 1) // 3
            c = (pos - 1) % 3

            if board[r][c] == " ":
                return r, c
            else:
                print("Position taken! Try again.")
        except:
            print("Invalid input!")

def computer_move(board):
    empty = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Choose mode:")
    print("1. Player vs Player")
    print("2. Player vs Computer")
    mode = input("Enter choice (1/2): ")

    current = "X"

    while True:
        print_board(board)
        print(f"Turn: {current}")

        if mode == "1" or (mode == "2" and current == "X"):
            r, c = get_player_move(board)
        else:
            print("Computer choosing...")
            r, c = computer_move(board)

        board[r][c] = current

        if check_winner(board, current):
            print_board(board)
            print(f"🎉 {current} wins!")
            break

        if board_full(board):
            print_board(board)
            print("😐 It's a draw!")
            break

        current = "O" if current == "X" else "X"

tic_tac_toe()
