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
