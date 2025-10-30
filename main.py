
from c4.ai import *
from c4.io import *

def play(cols: int = 7, rows: int = 6, ai: str = "heuristic", player_starts: bool = True, one_based_cols: bool = True) -> None:
    name = input("what is your name")
    board = create_board(cols,rows)

    while True:
         print(render(board))
         print("turn is",name)
         choich = int(input("where do you want to drok the disk"))
         choich-=1
         bound = in_bounds(board,choich)
         if bound == False:
             continue
         disc = drop_disc(board,choich,"x")
         done = has_winner_from(board)
         if done == True:
             print(f"{name} you win")

             print(render(board))
             break
         full = game_over(board)
         if full == True:
             print_result("None")
             break

         print(f"the {ai} das")
         choich = choose_move_random(board)
         disc = drop_disc(board,choich,"o")
         done = has_winner_from(board)
         if done == True:
             print(f"{ai} is win")

             print(render(board))

             break
         full = game_over(board)
         if full == True:
             print_result("none")
             break
play()
