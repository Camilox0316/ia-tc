import customtkinter as ctk
from view.GatoGame import TicTacToeInterface
from view.Simulation import Simulation
from model.MinMaxBot import MinMaxBot
from model.RandomBot import RandomBot

class TicTacToeModeSelectionWindow:
    def __init__(self, root):
        self.root = root
        self.create_mode_selection_window()

    def create_mode_selection_window(self):
        # Ocultar la ventana principal
        self.root.withdraw()

        # Crear una nueva ventana para la selección de modo de juego
        self.mode_selection_window = ctk.CTkToplevel()
        self.mode_selection_window.title("Modo de Juego Tic Tac Toe")
        self.mode_selection_window.geometry("300x400")

        # Agregar botones para cada modo de juego
        minimax_vs_random_button = ctk.CTkButton(self.mode_selection_window, text="Minimax vs Random",
                                                  command=lambda: self.start_game("Minimax vs Random"))
        minimax_vs_random_button.pack(pady=10)

        random_vs_minimax_button = ctk.CTkButton(self.mode_selection_window, text="Random vs Minimax",
                                                 command=lambda: self.start_game("Random vs Minimax"))
        random_vs_minimax_button.pack(pady=10)

        minimax_vs_minimax_button = ctk.CTkButton(self.mode_selection_window, text="Minimax vs Minimax",
                                                  command=lambda: self.start_game("Minimax vs Minimax"))
        minimax_vs_minimax_button.pack(pady=10)

        simulation_button = ctk.CTkButton(self.mode_selection_window, text="Simulación",
                                          command=self.open_simulation_interface)
        simulation_button.pack(pady=10)

        # Definir la acción al cerrar la ventana de selección
        self.mode_selection_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def start_game(self, mode):
        tic_tac_toe = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        if mode == "Minimax vs Random":
            bot1 = MinMaxBot(1)
            bot2 = RandomBot()
            print(f"Iniciando juego en modo: {mode}")
            game_interface = TicTacToeInterface(self.mode_selection_window,  bot1, bot2)
            game_interface.grab_set()  # Hace que la ventana de juego sea modal
        elif mode == "Random vs Minimax":
            bot1 = RandomBot()
            bot2 = MinMaxBot(3)
            print(f"Iniciando juego en modo: {mode}")
            game_interface = TicTacToeInterface(self.mode_selection_window,  bot1, bot2)
            game_interface.grab_set()  # Hace que la ventana de juego sea modal
        else:
            bot1 = MinMaxBot(1)
            bot2 = MinMaxBot(2)
            print(f"Iniciando juego en modo: {mode}")
            game_interface = TicTacToeInterface(self.mode_selection_window,  bot1, bot2)
            game_interface.grab_set()


    def open_simulation_interface(self):
        # Cierra la ventana de selección de modo de juego antes de abrir la de simulación
        simulation_interface = Simulation(self.root)
        simulation_interface.grab_set()

    def on_closing(self):
        self.root.deiconify()  # Mostrar la ventana principal nuevamente
        self.mode_selection_window.destroy()
