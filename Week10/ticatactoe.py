def main():
    """
    Main function to run the Tic-Tac-Toe game.
    """
    board = create_board()
    current_player = "X"
    print_board(board)
    
    while True:
        row, col = get_player_move(board, current_player)
        make_move(board, row, col, current_player)
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        
        current_player = switch_player(current_player)

def create_board():
    """
    Create and return a 3x3 board initialized with spaces.
    """
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    """
    Print the current state of the board.
    """
    for row in board:
        print("|".join(row))
        print("-" * 5)

def get_player_move(board, player):
    """
    Prompt the player for a move and validate input.
    """
    while True:
        try:
            move = input(f"Player {player}, enter your move as row,col (0-2): ")
            row, col = map(int, move.split(","))
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column as two numbers between 0 and 2, separated by a comma.")

def make_move(board, row, col, player):
    """
    Place the player's marker on the board at the given position.
    """
    board[row][col] = player

def check_winner(board, player):
    """
    Check if the given player has won the game.
    """
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    """
    Check if the board is full.
    """
    return all(cell != " " for row in board for cell in row)

def switch_player(player):
    """
    Switch the current player.
    """
    return "O" if player == "X" else "X"

if __name__ == "__main__":
    main()
