from board import *
def in_bounds(board: list[list[str]], row: int, col: int) -> bool:
    full = column_is_full(board,col)
    if full == True:
        print("its full")
        return False
    if row > len(board[0]):
        return False
    return True

def has_winner_from(board: list[list[str]], row: int, col: int) -> bool:
    try:
        if board[row][col] == board[row][col+1] and board[row][col] == board[row][col+2] and board[row][col] == board[row][col+3]:
            return True
        if board[row][col] == board[row][col]