# Monolith class to handle board memoization
class BoardMemo:
    def __init__(self):
        self.memo = {}
    
    def get(self, board):
        return self.memo.get(board, None)
        

    def put(self, board, value):
        self.memo[board] = value
