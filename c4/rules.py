from c4.board import *
def in_bounds(board: list[list[str]], col: int) -> bool:
    full = column_is_full(board,col)
    if full == True:
        print("its full")
        return False
    if col > len(board[0])-1:
        print("the column is worng choich agein")
        return False
    return True

def has_winner_from(board: list[list[str]]) -> bool:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "_":

               try:
                 if len({board[i][j],board[i][j+1],board[i][j+2],board[i][j+3]})  == 1:
                    return True
               except:
                   pass
               try:
                   if len({board[i][j],board[i+1][j + 1],board[i+2][j + 2],board[i+3][j+3]}) == 1:
                       return True
               except:
                   pass
               try:
                   if len({board[i][j],board[i][j - 1],board[i][j - 2],board[i][j-3]}) == 1:
                       return True
               except:
                   pass
               try:
                   if len({board[i][j],board[i+1][j - 1],board[i+2][j-2],board[i+3][j-3]}) == 1:
                       return True
               except:
                      pass
               try:
                   if len({board[i][j],board[i+1][j],board[i+2][j],board[i+3][j]}) == 1:
                    print("ello")
                    return True
               except:
                pass
    print("false")
    return False

def is_full(board: list[list[str]]) -> bool:
    for i in range(len(board[0])):
        column = column_is_full(board,i)
        if column == False:
            return True
    return False

def game_over(board: list[list[str]]):
    full  = is_full(board)
    if full == False:
        print("no budy is won")
        return True
    return False



try:
    print(t)
except:
    pass