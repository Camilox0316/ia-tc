from pyamaze import maze,agent
from queue import PriorityQueue
from random import randint

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
    pmaze.run()
    g_score={cell:float('inf') for cell in pmaze.grid} # g(n) = cost of the path from the start node to n
    g_score[agent]=0
    f_score={cell:float('inf') for cell in pmaze.grid} # f(n) = g(n) + h(n)
    f_score[agent]=manhattan_distance(agent,(goal))

    print(f"Esto es g_score: {g_score}")
    print(f"Esto es f_score: {f_score}")
    return 

def createMaze(size:int)->dict:
    myMaze = maze(size,size)
    myGoal = setGoal(myMaze, size)
    agentPosition = setAgent(myGoal, size)
    myX = agentPosition[0]
    myY = agentPosition[1]
    myAgent = agent(myMaze,x=myX, y=myY, footprints=True)
    return {"maze":myMaze,"goal":myGoal,"agent":agentPosition}

def setGoal(pmaze:maze, size:int)->tuple:
    x = randint(1, size)
    y = randint(1, size)
    pmaze.CreateMaze(x,y)
    return x,y

def setAgent(goal:tuple, size:int)->tuple:
    while True:
        x = randint(1, size)
        y = randint(1, size)
        if (x,y) != goal:
            break
    return x,y 


def main():
    myMaze = createMaze(10)
    A_Star(myMaze["maze"], myMaze["goal"], myMaze["agent"])
    
    return

if __name__ == "__main__":
    main()