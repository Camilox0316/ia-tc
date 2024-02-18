import customtkinter as ctk

class TicTacToeInterface(ctk.CTkToplevel):
    def __init__(self, parent, tic_tac_toe):
        super().__init__(parent)
        self.tic_tac_toe = tic_tac_toe
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
        print("Turno pasado")

# Suponiendo que tienes una instancia de tu juego TicTacToe llamada tic_tac_toe
# tic_tac_toe = [[0,0,0],[0,0,0],[0,0,0]]  # Ejemplo de matriz 3x3 para el juego

# Para demostrar, crearíamos la interfaz así:
# root = ctk.CTk()
# game_interface = TicTacToeInterface(root, tic_tac_toe)
# game_interface.mainloop()
