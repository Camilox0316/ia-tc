import customtkinter as ctk
from controller.GameController import GameController
class Simulation(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Simulación de Juegos")
        self.geometry("400x400")

        # Initialize the result lists
        self.min_max_random_results = []
        self.random_min_max_results = []
        self.min_max_min_max_results = []

        self.create_widgets()

    def create_widgets(self):

        # Botón para realizar la simulación
        self.run_simulation_button = ctk.CTkButton(self, text="Iniciar Simulación", command=self.run_simulation)
        self.run_simulation_button.grid(row=1, column=0, columnspan=4, pady=20)

        # Crear tabla para mostrar los resultados
        self.results_labels = []
        headers = ["Estilo de Juego", "P1 Gana", "P2 Gana", "Empate"]
        for i, header in enumerate(headers):
            label = ctk.CTkLabel(self, text=header)
            label.grid(row=2, column=i)
            self.results_labels.append(label)
        
        # Filas de resultados para cada estilo de juego
        for i in range(3):  # Tres estilos de juego
            for j in range(len(headers)):  # Cuatro columnas
                result_label = ctk.CTkLabel(self, text="%")
                result_label.grid(row=3+i, column=j)
                # Añadir las etiquetas de resultado a la lista correspondiente
                if i == 0:
                    self.min_max_random_results.append(result_label)
                elif i == 1:
                    self.random_min_max_results.append(result_label)
                elif i == 2:
                    self.min_max_min_max_results.append(result_label)

    def run_simulation(self):
        # Lógica para realizar las simulaciones y actualizar los resultados
        gc = GameController()
        results= gc.simulateGames()
        self.update_results(results)
        pass

    def update_results(self, results):
        for i, result_set in enumerate(results):
            if i == 0:
                for j, result in enumerate(result_set):
                    self.min_max_random_results[j].configure(text=str(result))
            elif i == 1:
                for j, result in enumerate(result_set):
                    self.random_min_max_results[j].configure(text=str(result))
            elif i == 2:
                for j, result in enumerate(result_set):
                    self.min_max_min_max_results[j].configure(text=str(result))
        pass

# Código para crear y mostrar la ventana de simulación
# root = ctk.CTk()
# simulation_interface = SimulationInterface(root)
# simulation_interface.grab_set()
# simulation_interface.mainloop()
