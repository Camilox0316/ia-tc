import colorsys
from pyamaze import maze,agent
from queue import PriorityQueue
from random import randint
MAZE_SIZE = 15
def manhattan_distance(goal:tuple, current:tuple) -> int :
    """
    Returns the Manhattan distance between two points.
    Input: goal, current -> tuple(x,y)
    Output: int
    """
    return abs(goal[0]-current[0]) + abs(goal[1]-current[1])


def A_Star(pmaze:maze, goal:tuple, agent:tuple) -> tuple:
    """
    A* algorithm to solve a maze.
    Input: maze -> maze object
    Output: list of tuples
    """
    # Definición de los puntos cardinales con sus respectivas direcciones en coordenadas (x, y).
    cardinal_points:dict = {"N":(-1,0), "S":(1,0), "E":(0,1), "W":(0,-1)}

    # Inicialización de g_score para cada celda del laberinto con infinito; g(n) representa el costo desde el inicio hasta n.
    g_score:dict ={cell:float('inf') for cell in pmaze.grid}
    # Establece el g_score del agente (posición inicial) a 0.
    g_score[agent] = 0

    # Inicialización de f_score para cada celda con infinito; f(n) = g(n) + h(n), donde h es la heurística (distancia de Manhattan aquí).
    f_score={cell:float('inf') for cell in pmaze.grid}
    # Establece el f_score del agente usando la distancia de Manhattan hasta la meta.
    f_score[agent]=manhattan_distance(agent,(goal))

    # Crea una cola de prioridad para gestionar los nodos abiertos durante la búsqueda A*.
    open_set = PriorityQueue()
    # Añade el nodo inicial (agente) a la cola con su f y g scores como prioridades.
    open_set.put((manhattan_distance(agent, goal), manhattan_distance(agent, goal), agent))

    # Diccionario para rastrear el camino de A*.
    star_path = {}

    # Bucle que se ejecuta mientras haya nodos por explorar en open_set.
    while not open_set.empty():
        # Obtiene el nodo actual de la cola, que tiene la menor f_score.
        current = open_set.get()[2]
        # Si el nodo actual es la meta, termina el bucle.
        if current == goal:
            break
        
        # Explora los nodos vecinos en todas las direcciones cardinales.
        for direction in "ESNW":
            # Verifica si la dirección es válida (no hay pared).
            if pmaze.maze_map[current][direction]:
                # Calcula la nueva celda basada en la dirección actual.
                change = cardinal_points[direction]
                new_cell = (current[0]+change[0],current[1]+change[1])
                # Verifica que la nueva celda esté dentro de los límites del laberinto.
                if 1 <= new_cell[0] <= MAZE_SIZE and 1 <= new_cell[1] <= MAZE_SIZE:
                    # Calcula el g_score tentativo para la nueva celda.
                    possible_g_score = g_score[current] + 1
                    # Calcula el f_score tentativo sumando el g_score con la heurística hasta la meta.
                    possible_f_score = possible_g_score + manhattan_distance(new_cell, goal)
                    # Si el f_score tentativo es menor, actualiza g_score, f_score y añade la celda a open_set.
                    if possible_f_score < f_score[new_cell]:
                        g_score[new_cell] = possible_g_score
                        f_score[new_cell] = possible_f_score
                        open_set.put((possible_f_score, manhattan_distance(new_cell, goal), new_cell))
                        # Rastrea el camino de cada celda.
                        star_path[new_cell] = current

    # Recupera el camino final siguiendo el rastro desde la meta hasta el agente.
    final_path = {}
    cell = goal

    # Itera hacia atrás desde la meta hasta el agente, construyendo el camino.
    while cell != agent:
        final_path[star_path[cell]] = cell
        cell = star_path[cell]
    # Retorna un diccionario vacío si no se encuentra un camino.
    return final_path

# Función para crear un laberinto con una posición de meta y agente aleatorias.
def createMaze(size:int)->dict:
    myMaze = maze(size,size)
    myGoal = setGoal(myMaze, size)
    agentPosition = setAgent(myGoal, size)
    myX = agentPosition[0]
    myY = agentPosition[1]
    myAgent = agent(myMaze,x=myX, y=myY, footprints=True)
    return {"maze":myMaze,"goal":myGoal,"agent":agentPosition, "realAgent":myAgent}

# Función para establecer la meta en el laberinto de manera aleatoria.
def setGoal(pmaze:maze, size:int)->tuple:
    x = randint(1, size)
    y = randint(1, size)
    pmaze.CreateMaze(x,y)
    return x,y

# Función para establecer la posición del agente de manera aleatoria, asegurando que no sea la misma que la meta.
def setAgent(goal:tuple, size:int)->tuple:
    while True:
        x = randint(1, size)
        y = randint(1, size)
        if (x,y) != goal:
            break
    return x,y 

# Función principal que crea el laberinto, ejecuta A* y traza el camino.
def main():
    myMaze = createMaze(MAZE_SIZE)
    path = A_Star(myMaze["maze"], myMaze["goal"], myMaze["agent"])
    myMaze["maze"].tracePath({myMaze["realAgent"] : myMaze["maze"].path})
    myMaze["maze"].run()
    
    return 
if __name__ == "__main__":
    main()