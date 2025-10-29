from itertools import count


def create_board(cols: int = 7, rows: int = 6) -> list[list[str]]:
    board = []
    for i in range(rows):
        board.append([])
        for j in range(cols):
            board[i].append("_")
    return board

def column_is_full(board: list[list[str]], col: int) -> bool:
    count = 0
    for i in range(len(board)):
        if len(board[i][col]) > 0:
            count+=1
    if count == len(board):
        return True
    return False

def drop_disc(board: list[list[str]], col: int, mark: str) -> tuple[int,int] | None:
    disc = column_is_full(board,col)
    if disc == True:
        return None
    for i in range(len(board)):
        if len(board[i][col]) > 0:
            board[i-1][col]+=mark
            break
        if i == len(board)-1:
            board[i][col]+=mark
    return board

def legal_moves(board: list[list[str]]) -> list[int]:
    colms = []
    for i in range(len(board[0])):
        full = column_is_full(board,i)
        if full == False:
            colms.append(i)
    return colms

def render(board: list[list[str]], one_based_cols: bool = True) -> str:
    str1 = ""
    for i in range(len(board)+1):
        if i > 0:
            str1+="\n"
        for j in range(len(board[0])):
            if i == 0:
                str1+=str(j+1)
                str1+=" "
            else:
                str1+=board[i-1][j]
                str1+=" "

    return str1



