import customtkinter as ctk

class TicTacToeInterface(ctk.CTkToplevel):
    def __init__(self, parent, tic_tac_toe):
        super().__init__(parent)
        self.tic_tac_toe = tic_tac_toe  # Suponiendo que tic_tac_toe es tu objeto de juego
        self.title("Juego Tic Tac Toe")
        self.geometry("400x400")

        self.create_widgets()

    def create_widgets(self):
        # Crear y posicionar los botones del tablero 3x3
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = ctk.CTkButton(self, text="", width=100, height=100,
                                       command=lambda i=i, j=j: self.update_board(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
        
        # Botón para pasar el turno
        self.pass_turn_button = ctk.CTkButton(self, text="Pasar Turno", command=self.pass_turn)
        self.pass_turn_button.grid(row=3, column=0, columnspan=3, pady=20)

    def update_board(self, i, j):
        # Actualiza el tablero en base a la lógica de tu juego
        # Por ejemplo, podrías marcar el movimiento en el objeto TicTacToe y luego actualizar la interfaz
        print(f"Botón presionado: {i}, {j}")
        # Aquí iría el código para actualizar tu objeto TicTacToe y reflejar esos cambios en la interfaz

    def pass_turn(self):
        # Lógica para pasar el turno
        print("Turno pasado")
        # Aquí podrías actualizar el estado de tu objeto TicTacToe para cambiar el turno

# Suponiendo que tienes una instancia de tu juego TicTacToe llamada tic_tac_toe
# tic_tac_toe = TicTacToe()

# Para demostrar, crearíamos la interfaz así:
# root = ctk.CTk()
# game_interface = TicTacToeInterface(root, tic_tac_toe)
# game_interface.mainloop()
