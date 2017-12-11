"""This module defines the 'Game' class, used to create a game between two,
players."""

from lib.League import League


class Game:
    """class that simulate and apply game results"""

    def __init__(self, players, player1, player2):

        self.players = League(players)
        self.player1 = player1
        self.player2 = player2

    def simulate(self):
        """
        Give the expected result of the game base on the elo of each player.
        """
        winProbability = self.players.winProbability(self.player1, self.player2)
        if winProbability >= 0.5:
            event = "wins"
            probability = winProbability
        else:
            event = "loses"
            probability = 1 - winProbability
        print("Player1 {} with {} of probability".format(event, probability))

    def result(self, result):
        """apply the elo modification depeding on the result of the game"""
        self.players.applyResult(self.player1, self.player2, result)
        self.players.printClassement()
