class TicTacToe:
    def __init__(self, board=None, current_player=1):
        if board is None: 
            self.board = [[None for _ in range(3)] for _ in range(3)]
        else: 
            self.board = board
        # 1 -> X, 2 -> O
        self.current_player = current_player

    def is_valid_move(self, row, col):
        return self.board[row][col] is None

    def is_win(self):
        # returns the winner if the last move was a winning move, else False
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return self.board[0][2]
        return False
    
    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.current_player = 2 if self.current_player == 1 else 1
            return True
        return False
    
    def undo_move(self, row, col):
        self.board[row][col] = None
        self.current_player = 2 if self.current_player == 1 else 1
    
    def is_draw(self):
        # only works after is_win
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True
    
    def prettyprint(self):
        print("-------")
        for row in self.board:
            print("|", end="")
            for cell in row:
                if cell == 1:
                    print("X|", end="")
                elif cell == 2:
                    print("O|", end="")
                else:
                    print(" |", end="")
            print()
            print("-------")
        print()

    def get_new_ttt(self, row, col):
        new_board = [[cell for cell in row] for row in self.board]
        new_board[row][col] = self.current_player
        return TicTacToe(new_board, 2 if self.current_player == 1 else 1)
    
    def get_available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]
    
    def getBoard(self):
        return str(self.board)