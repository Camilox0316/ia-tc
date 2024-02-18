class BotInterface:
    def make_move(self, board):
        """
        Realiza un movimiento en el tablero.
        :param board: El estado actual del tablero.
        :return: La posición (x, y) donde el bot quiere hacer su movimiento.
        """
        raise NotImplementedError
