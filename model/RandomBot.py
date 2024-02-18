import random
from model.BotInterface import BotInterface

class RandomBot(BotInterface):
    def make_move(self, board):
        # needs there to be at least one empty cell in the board
        while True:
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            if board.is_valid_move(i, j):
                return (i, j)