"""This module encapsulate the 'league' class, that represents the player
ranking"""
import json

from lib.Elo import Elo


class League:
    """encapsulate the pool of player we're dealing with and their ranking"""
    def __init__(self, playersFile):

        with open(playersFile, 'r') as myFile:
            self.fileName = playersFile
            self.players = json.loads(myFile.read())
            self.elo = Elo()

    def winProbability(self, player1, player2):

        return self.elo.winProbability(self.players[player1]["elo"] - self.players[player2]["elo"])

    def applyResult(self, player1, player2, result):

        self.players[player1]["elo"] = self.elo.compute(self.players[player1]["elo"],self.players[player2]["elo"],result)
        # if player 1 gets result, player 2 should get 1-result
        self.players[player2]["elo"] = self.elo.compute(self.players[player2]["elo"],self.players[player1]["elo"], 1-result)
        self.save()

    def save(self):
        with open(self.fileName, 'w') as myFile:
            myFile.write(json.dumps(self.players))

    def printClassement(self):
        print(json.dumps(self.players))
