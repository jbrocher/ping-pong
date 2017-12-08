"""This module defines the 'Game' class, used to create a game between two,
players."""

from League import League

class Game(object):
    """class that simulate and apply game results"""

    def __init__(self, players, player1, player2):

        self.players = League(players)
        self.player1 = player1
        self.player2 = player2


    def simulate(self):
        """Give the expected result of the game based
        on the elo of each player."""

        winProbability = self.players.winProbability(self.player1, self.player2)
        event = "wins" if winProbability >= 50 else "loses"
        probability = winProbability if winProbability >= 50 else 100 - winProbability
        print("Player1 {} with {} of probability".format(event, probability))

    def result(self,result):
        """apply the elo modification depeding on the result of the game"""

        self.players.modify(self.player1, self.player2, result)
        self.players.printClassement()
