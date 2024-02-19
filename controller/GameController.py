from model.TicTacToe import TicTacToe
from model.RandomBot import RandomBot
class GameController: 

    def simulateGames(self):
        randomBot = RandomBot()
        minMaxBot = RandomBot() # not implemented yet
        wins, losses, draws = self.tournament(minMaxBot, randomBot)
        print("MinMaxBot vs RandomBot")
        print("Wins:", wins)
        print("Losses:", losses)
        print("Draws:", draws)
        wins, losses, draws = self.tournament(randomBot, minMaxBot)
        print("RandomBot vs MinMaxBot")
        print("Wins:", wins)
        print("Losses:", losses)
        print("Draws:", draws)
        wins, loses, draws = self.tournament(minMaxBot, minMaxBot)
        print("MinMaxBot vs MinMaxBot")
        print("Wins:", wins)
        print("Losses:", losses)
        print("Draws:", draws)

    def tournament(self, bot1, bot2, n=500):
        bot1_wins = 0
        bot2_wins = 0
        draws = 0
        for _ in range(n):
            result = self.simulate(bot1, bot2)
            if result == 1:
                bot1_wins += 1
            elif result == 2:
                bot2_wins += 1
            else:
                draws += 1
        return bot1_wins, bot2_wins, draws

    def simulate(self, bot1, bot2):
        game = TicTacToe()
        while True:
            # bot1's turn
            row, col = bot1.make_move(game)
            game.make_move(row, col)
            if game.is_win():
                return 1
            if game.is_draw():
                return 0
            # bot2's turn
            row, col = bot2.make_move(game)
            game.make_move(row, col)
            if game.is_win():
                return 2
            if game.is_draw():
                return 0