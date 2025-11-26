def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i] == col: return False
        
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j: return False
        
    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, 8)):
        if board[i] == j: return False
    return True

def solve_n_queens(board, row):
    if row >= 8: return True # All queens placed
    
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            if solve_n_queens(board, row + 1):
                return True
            board[row] = -1 # Backtrack
    return False

board = [-1] * 8
if solve_n_queens(board, 0):
    print("Queens positions (row indices):", board)