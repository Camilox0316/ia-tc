import customtkinter as ctk

# Función para abrir la ventana de selección de modo de juego de Tic Tac Toe
def open_tic_tac_toe_mode_selection():
    # Crear una nueva ventana
    mode_selection_window = ctk.CTkToplevel()
    mode_selection_window.title("Modo de Juego Tic Tac Toe")
    mode_selection_window.geometry("300x400")

    # Agregar botones para cada modo de juego
    minimax_vs_random_button = ctk.CTkButton(mode_selection_window, text="Minimax vs Random", command=lambda: print("Minimax vs Random"))
    minimax_vs_random_button.pack(pady=10)

    random_vs_minimax_button = ctk.CTkButton(mode_selection_window, text="Random vs Minimax", command=lambda: print("Random vs Minimax"))
    random_vs_minimax_button.pack(pady=10)

    minimax_vs_minimax_button = ctk.CTkButton(mode_selection_window, text="Minimax vs Minimax", command=lambda: print("Minimax vs Minimax"))
    minimax_vs_minimax_button.pack(pady=10)

    simulation_button = ctk.CTkButton(mode_selection_window, text="Simulación", command=lambda: print("Simulación"))
    simulation_button.pack(pady=10)
