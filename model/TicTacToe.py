class TicTacToe:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        # 1 -> X, 2 -> O
        self.current_player = 1

    def is_valid_move(self, row, col):
        return self.board[row][col] is None

    def invert(self): 
        # for minmax, invert the board (1 -> 2, 2 -> 1)
        return [[(1 if cell == 2 else 2) if cell is not None else None for cell in row] for row in self.board]

    def is_win(self):
        # returns true if the last move was a winning move
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return True
        return False
    
    def make_move(self, row, col):
        if self.isValidMove(row, col):
            self.board[row][col] = self.current_player
            self.current_player = 2 if self.current_player == 1 else 1
            return True
        return False
    
    def is_draw(self):
        # only works after is_win
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True    