from c4.board import *
def print_status(board: list[list[str]]) -> None:
    print(f"now the board is\n{print(render(board))}")

def print_result(winner):
    print(f"now the end by by\nthe winner is {winner}")