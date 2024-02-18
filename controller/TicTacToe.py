from model import BotInterface
class TicTacToe:
    def __init__(self, player1: BotInterface, player2: BotInterface):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1

    def play_game(self):
        print("Soy Tic tac toe")
        # Lógica para jugar el juego, alternando entre los bots.
        pass
    def print_board(self):
        for row in self.board:
            row_display = "|"
            for cell in row:
                if cell is None:
                    row_display += "   |"
                else:
                    row_display += f" {cell} |"
            print(row_display)
            print("-------------")  # Asume un tablero de 3x3
