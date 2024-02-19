from model.BotInterface import BotInterface
from model.BoardMemo import BoardMemo
import random # to choose a random move if we have multiple best moves

class MinMaxBot(BotInterface):
    def __init__(self, token, memo=None):
        self.token = token
        if memo is None:
            self.memo = BoardMemo()
        else:
            self.memo = memo

    def minMax(self, game, isMax):
        # returns the current evaluation of the game
        memoized = self.memo.get(game.getBoard())
        if memoized is not None:
            return memoized

        winner = game.is_win()

        if winner:
            val = 1 if winner == self.token else -1
            self.memo.put(game.getBoard(), val)
            return val
        
        if game.is_draw():
            val = 0
            self.memo.put(game.getBoard(), val)
            return val
        
        if isMax:
            best = float('-inf')
            for (i, j) in game.get_available_moves():
                game.make_move(i, j)
                best = max(best, self.minMax(game, not isMax))
                game.undo_move(i, j)
            self.memo.put(game.getBoard(), best)
            return best
        else:
            best = float('inf')
            for (i, j) in game.get_available_moves():
                game.make_move(i, j)
                best = min(best, self.minMax(game, not isMax))
                game.undo_move(i, j)
            self.memo.put(game.getBoard(), best)
            return best
        
    def make_move(self, board):
        best = float('-inf')
        moves_and_evaluations = []
        for (i, j) in board.get_available_moves():
            board.make_move(i, j)
            move = self.minMax(board, False)
            board.undo_move(i, j)
            moves_and_evaluations.append((i, j, move))
            best = max(best, move)
        best_moves = [(i, j) for (i, j, move) in moves_and_evaluations if move == best]            
        return random.choice(best_moves) # if there are multiple best moves, choose one at random