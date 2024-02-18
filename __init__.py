from model.TicTacToe import TicTacToe
from model.RandomBot import RandomBot

def main():
    board = TicTacToe() 
    board.prettyprint()
    bot = RandomBot()
    
    while True: 
        move = bot.make_move(board)
        board.make_move(*move)
        board.prettyprint()
        if board.is_win():
            print("X wins!")
            break
        if board.is_draw():
            print("Draw!")
            break
        move = bot.make_move(board)
        board.make_move(*move)
        board.prettyprint()
        if board.is_win():
            print("O wins!")
            break
        if board.is_draw():
            print("Draw!")
            break    


    pass
if __name__ == "__main__":
    main()


