"""This module encapsulate the 'league' class, that represents the player ranking."""
import json

from lib.Elo import Elo


class League:
    """Encapsulate the pool of player we're dealing with and their ranking."""

    def __init__(self, playersFile):
        """Contrsuctor."""
        with open(playersFile, 'r') as myFile:
            self.fileName = playersFile
            self._players = json.loads(myFile.read())
            self._elo = Elo()

    def _getPlayers(self):
        """Accessor for the players attribute.

        It should not be public,
        so we call printClassement() instead
        """
        self.printClassement()

    def _setPlayers(self, arg):
        """Setter for players.

        players should no be modified directly
        """
        raise AttributeError("self._players is private, please use the approiate function")

    def _getElo(self):
        """Accessor for the elo attribute.

        Private attribute, acceding it raises an execption
        """
        raise AttributeError("self._elo is private")

    def _setElo(self, arg):
        """Setter for self._elo.

        elo should no be modified
        """
        raise AttributeError("self._elo is private")

    def sortByElo(self):
        return sorted(self._players, key=lambda player: player["elo"], reverse=True)

    def winProbability(self, player1, player2):
        """Return the probability of win of player 1 over player 2."""
        return self._elo.winProbability(self._players[player1]["elo"] - self._players[player2]["elo"])

    def applyResult(self, player1, player2, result):
        """Modify the ranking and elo of each player acccording to the result of the game."""
        self._players[player1]["elo"] = self._elo.compute(self._players[player1]["elo"], self._players[player2]["elo"], result)
        # if player 1 gets result, player 2 should get 1-result
        self._players[player2]["elo"] = self._elo.compute(self._players[player2]["elo"], self._players[player1]["elo"], 1-result)
        self.save()

    def save(self):
        """Save the game state into the league json file."""
        with open(self.fileName, 'w') as myFile:
            myFile.write(json.dumps(self.sortByElo()))

    def printClassement(self):
        """Return the ranking as a string."""
        toPrint = ""
        rank = 0
        ranking = self.sortByElo()
        for player in ranking:
            toPrint = toPrint + "{}. {} ({})\n".format(rank, player["name"], player["elo"])
            rank = rank + 1
        return toPrint

    def searchPlayerByName(self, playerName):
        """Search the player in the League based on his name.

        Returns a list of result as tuples (position, player) where position is the
        position in the list, and player is the dictionnary of the player
        """
        results = []
        for i, player in enumerate(self._players):
            if player["name"] == playerName:
                results.append((i, player))
        return results

    def delPlayer(self, playerName):
        """Delete the player identified by playerName."""
        searchResult = self.searchPlayerByName(playerName)

        if len(searchResult) == 1:
            del self._players[searchResult[0][0]]
        elif len(searchResult) == 0:
            raise ValueError("no player with this name")
        else:
            raise ValueError("wrong value")

    def addPlayer(self, player):
        """Add a player to the league and save the league.

        arguments
        player -- dictionnary containing the player data
        """
        if self.searchPlayerByName(player["name"]) != []:
            raise ValueError("A player with this name already exists")
        else:
            self._players.append(player)
            self.save()

    players = property(_getPlayers, _setPlayers)
    elo = property(_getElo, _setElo)
