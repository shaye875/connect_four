import random

from c4.rules import *
def choose_move_random(board: list[list[str]]) -> int:
    while True:
      ran = random.randint(0,len(board[0])-1)
      bool = in_bounds(board,ran)
      if bool == True:
          return ran


