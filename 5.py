import math

def check_winner(board):
    # Check rows, cols, diagonals
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    if ' ' not in board: return 'Tie'
    return None

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X': return 1
    if winner == 'O': return -1
    if winner == 'Tie': return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Test board: X to move
board = ['X', 'O', 'X', 
         'O', 'O', ' ', 
         ' ', ' ', ' ']
print("Best score for X:", minimax(board, 0, True))