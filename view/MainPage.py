import customtkinter as ctk
from view.MenuGato import TicTacToeModeSelectionWindow

class MainApplication(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Tarea 1 Grupo *")
        self.geometry("400x300")
        
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        # Configurar el estilo de customtkinter
        ctk.set_appearance_mode("dark")  # Opciones: "light", "dark"
        ctk.set_default_color_theme("blue")  # Opciones disponibles en la documentación

    def create_widgets(self):
        # Título de la página
        title = ctk.CTkLabel(self, text="Tarea 1 Grupo *", font=("Roboto", 20))
        title.pack(pady=30)

        # Botón para Maze
        maze_button = ctk.CTkButton(self, text="Maze", command=self.open_maze)
        maze_button.pack(pady=10)

        # Botón para Tic Tac Toe
        tic_tac_toe_button = ctk.CTkButton(self, text="Tic Tac Toe", command=self.open_tic_tac_toe)
        tic_tac_toe_button.pack(pady=10)

    def open_maze(self):
        # Función para el evento de clic en el botón Maze
        print("Abrir Maze")

    def open_tic_tac_toe(self):
        # Función para el evento de clic en el botón Tic Tac Toe
        print("Abrir Tic Tac Toe")
        TicTacToeModeSelectionWindow(self)

# Ejecutar la aplicación si este archivo es el script principal ejecutado
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
