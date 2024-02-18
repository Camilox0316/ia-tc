import customtkinter as ctk
import MenuGato
# Función para el evento de clic en el botón Maze
def open_maze():
    print("Abrir Maze")

# Función para el evento de clic en el botón Tic Tac Toe
def open_tic_tac_toe():
   # Función para el evento de clic en el botón Tic Tac Toecls
    print("Abrir Tic Tac Toe")
    MenuGato.open_tic_tac_toe_mode_selection(root)  

# Configurar el estilo de customtkinter
ctk.set_appearance_mode("dark")  # Opciones: "light", "dark"
ctk.set_default_color_theme("blue")  # Opciones disponibles en la documentación

# Crear la ventana principal
root = ctk.CTk()
root.title("Tarea 1 Grupo *")
root.geometry("400x300")

# Título de la página
title = ctk.CTkLabel(root, text="Tarea 1 Grupo *", font=("Roboto", 20))

title.pack(pady=30)

# Botón para Maze
maze_button = ctk.CTkButton(root, text="Maze", command=open_maze)
maze_button.pack(pady=10)

# Botón para Tic Tac Toe
tic_tac_toe_button = ctk.CTkButton(root, text="Tic Tac Toe", command=open_tic_tac_toe)
tic_tac_toe_button.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
