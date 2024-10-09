import random

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print("|  " + "  |  ".join(row) + "  |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    valid_move = False
    while not valid_move:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            row, col = divmod(move, 3)
            if board[row][col] not in ['X', 'O']:
                board[row][col] = 'O'
                valid_move = True
            else:
                print("Square already taken!")
        else:
            print("Invalid move! Please enter a number between 1 and 9.")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in win_conditions:
        if all(board[row][col] == sign for row, col in condition):
            return True
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = random.choice(free_fields)
        board[move[0]][move[1]] = 'X'

def main():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    board[1][1] = 'X'  # Computer starts with the middle position
    game_over = False

    while not game_over:
        display_board(board)
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("You win!")
            game_over = True
            break
        if not make_list_of_free_fields(board):
            display_board(board)
            print("It's a tie!")
            game_over = True
            break
        draw_move(board)
        if victory_for(board, 'X'):
            display_board(board)
            print("Computer wins!")
            game_over = True
            break
        if not make_list_of_free_fields(board):
            display_board(board)
            print("It's a tie!")
            game_over = True
            break

if __name__ == "__main__":
    main()