import customtkinter as ctk
import GatoGame

def open_tic_tac_toe_mode_selection(root):
    # Ocultar la ventana principal
    root.withdraw()

    # Crear una nueva ventana para la selección de modo de juego
    mode_selection_window = ctk.CTkToplevel()
    mode_selection_window.title("Modo de Juego Tic Tac Toe")
    mode_selection_window.geometry("300x400")

# Función para iniciar el juego o simulación
    def start_game(mode,root):
        tic_tac_toe = [[0,0,0],[0,0,0],[0,0,0]]
        print(f"Iniciando juego en modo: {mode}")  # Reemplaza esta línea con la llamada a tu juego
        game_interface = GatoGame.TicTacToeInterface(root, tic_tac_toe)
        game_interface.grab_set()  # Hace que la ventana de juego sea modal

    # Agregar botones para cada modo de juego
    minimax_vs_random_button = ctk.CTkButton(mode_selection_window, text="Minimax vs Random", command=lambda: start_game("Minimax vs Random", mode_selection_window))
    minimax_vs_random_button.pack(pady=10)

    random_vs_minimax_button = ctk.CTkButton(mode_selection_window, text="Random vs Minimax", command=lambda: start_game("Random vs Minimax", mode_selection_window))
    random_vs_minimax_button.pack(pady=10)

    minimax_vs_minimax_button = ctk.CTkButton(mode_selection_window, text="Minimax vs Minimax", command=lambda: start_game("Minimax vs Minimax", mode_selection_window))
    minimax_vs_minimax_button.pack(pady=10)


    simulation_button = ctk.CTkButton(mode_selection_window, text="Simulación", command=lambda: print("Simulación"))
    simulation_button.pack(pady=10)

    # Definir la acción al cerrar la ventana de selección
    def on_closing():
        root.deiconify()  # Mostrar la ventana principal
        mode_selection_window.destroy()

    mode_selection_window.protocol("WM_DELETE_WINDOW", on_closing)
