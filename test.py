"""test unitaires"""

from unittest import mock
import unittest
from lib.Elo import Elo
from lib.League import League
from lib.Interactions import Interactions
from lib.Menu import Menu


class EloTest(unittest.TestCase):
    """docstring for EloTest."""

    def testWinProbability(self):
        elo = Elo()
        elo1 = 500
        elo2 = 300
        prob = elo.winProbability(elo1 - elo2)
        self.assertEqual(
            0.76, prob, 'testComppute fails, actula prob : {}'.format(prob))

    def testCompute(self):
        elo = Elo()
        elo1 = 500
        elo2 = 300
        result = 1
        newElo = elo.compute(elo1, elo2, result)
        self.assertEqual(
            502.4, newElo, 'testComppute fails, actula elo : {}'.format(newElo))


class PingPongTest(unittest.TestCase):
    """Docstring for Pingpong Test."""

    def resetTestFile(self):
        """Reset pool file for tests."""
        with open("data/unit-testing/players/players.json", 'w') as testFile:
            testFile.write('[{"name": "JB", "elo": 500}, {"name": "Manel", "elo": 300}, {"name": "Guilhem", "elo": 3000}]')


class LeagueTest(PingPongTest):
    """docstring for EloTest."""

    def testWinProbability(self):
        self.resetTestFile()
        league = League("data/unit-testing/players/players.json")

        prob = league.winProbability(0, 1)
        self.assertEqual(
            0.76, prob, 'testComppute fails, actula prob : {}'.format(prob))

    def testSearchPlayerByname(self):
        self.resetTestFile()
        league = League("data/unit-testing/players/players.json")
        results = league.searchPlayerByName("JB")
        self.assertEqual(results, [(0, {
            "name": "JB",
            "elo": 500
        })])

    def testAddPlayer(self):
        self.resetTestFile()
        league = League("data/unit-testing/players/players.json")
        league.addPlayer({"name": "Biausser", "elo": 0})

        results = league.searchPlayerByName("Biausser")
        self.assertEqual(results, [(3, {
            "name": "Biausser",
            "elo": 0
        })])

        with self.assertRaises(ValueError):
            league.addPlayer({"name": "JB", "elo": 4})

    def testDelPlayer(self):
        self.resetTestFile()
        league = League("data/unit-testing/players/players.json")
        league.delPlayer("JB")
        self.assertEqual(league.searchPlayerByName("JB"), [])

    def testPrintClassement(self):
        self.resetTestFile()
        league = League("data/unit-testing/players/players.json")
        printed = league.printClassement()
        with open("data/unit-testing/print/players.txt") as myFile:
            self.assertEqual(printed, myFile.read())


# class InteractionsTest(PingPongTest):
#     """Docstring for InteractionsTest."""
#
#     @mock.patch('builtins.input', side_effect=['0'])
#     def testGetPoolInput(self, input):
#         """Test get_pool_input."""
#         self.resetTestFile()
#         interact = Interactions()
#         output = interact.get_pool_input(poolpath='data/unit-testing/players/*.json')
#         self.assertEqual(output, 'data/unit-testing/players/players.json')
#
#
# class MenuTest(PingPongTest):
#     """Docstring for MenuTest."""
#
#     @mock.patch('builtins.input', side_effect=['JB'])
#     def testChoosePlayer(self, input):
#         """Test choose_player."""
#         self.resetTestFile()
#         menu = Menu()
#         output = menu.choose_player(pool='data/unit-testing/players/players.json')
#         self.assertEqual(output, [(0, {'elo': 500, 'name': 'JB'})])
#
#     @mock.patch('builtins.input', side_effect=['JB', 'Manel'])
#     def testSimulateGame(self, input):
#         """Test simulate_game."""
#         self.resetTestFile()
#         menu = Menu()
#         output = menu.simulate_game(pool='data/unit-testing/players/players.json')
#         self.assertEqual(output, 'Player1 wins with 0.76 of probability')


unittest.main()
