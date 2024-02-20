from controller.GameController import GameController
from view.MainPage import MainApplication


def main():    
    gc = GameController()
    gc.simulateGames()

    pass
if __name__ == "__main__":
    MainApplication().mainloop()



