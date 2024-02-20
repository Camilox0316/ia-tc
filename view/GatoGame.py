import customtkinter as ctk
from model.TicTacToe import TicTacToe
class TicTacToeInterface(ctk.CTkToplevel):
    def __init__(self, parent, Bot1, Bot2):
        super().__init__(parent)
        self.isEnd = False
        self.Turno = 1
        self.game = TicTacToe()
        self.Bot1 = Bot1
        self.Bot2 = Bot2
        self.title("Juego Tic Tac Toe")
        self.geometry("400x400")

        self.create_widgets()

    def create_widgets(self):
        # Crear un marco para centrar los botones del tablero en la ventana
        board_frame = ctk.CTkFrame(self)
        board_frame.place(relx=0.5, rely=0.5, anchor='center')  # Esto centra el marco en la ventana

        # Crear y posicionar los botones del tablero 3x3 dentro del marco
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = ctk.CTkButton(board_frame, text="", width=100, height=100,
                                       command=lambda i=i, j=j: self.update_board(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
        
        # Crear y posicionar el botón para pasar el turno
        self.pass_turn_button = ctk.CTkButton(board_frame, text="Pasar Turno", command=self.pass_turn)
        self.pass_turn_button.grid(row=3, column=1, pady=20)  # Centrar el botón bajo el tablero

    def update_board(self, i, j):
        print(f"Botón presionado: {i}, {j}")

    def pass_turn(self):
        if self.isEnd == False:
            game = self.game
            if self.Turno == 1: 
                self.Turno = 0
                row, column = self.Bot1.make_move(game)
                game.make_move(row, column)
                if game.is_win() or game.is_draw():
                    self.refresh_board()
                    self.isEnd = True
                    return 1
                
            else:
                self.Turno = 1
                row, col = self.Bot2.make_move(game)
                game.make_move(row, col)
                if game.is_win() or game.is_draw():
                    self.refresh_board()
                    self.isEnd = True
                    return 0
            self.refresh_board()  # Actualiza la interfaz gráfica para reflejar el estado actual del tablero

    def refresh_board(self):
        board = self.game.getBoard()
        if isinstance(board, str):
            board = eval(board)  # Solo si es absolutamente necesario y getBoard() devuelve una cadena

        print("Estructura del tablero:", board)

        for i in range(3):
            for j in range(3):
                cell = board[i][j]  # Accede directamente al valor de la celda

                if cell is None:
                    self.buttons[i][j].configure(text="")
                elif cell == 1:
                    self.buttons[i][j].configure(text="X")
                elif cell == 2:
                    self.buttons[i][j].configure(text="O")