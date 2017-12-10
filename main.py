"""test unitaires"""

import unittest
from lib.Elo import Elo
from lib.League import League


class EloTest(unittest.TestCase):
    """docstring for EloTest."""

    def testWinProbability(self):
        elo = Elo()
        elo1 = 500
        elo2 = 300
        prob = elo.winProbability(elo1-elo2)
        self.assertEqual(0.76, prob, 'testComppute fails, actula prob : {}'.format(prob))

    def testCompute(self):
        elo=Elo()
        elo1 = 500
        elo2 = 300
        result = 1
        newElo = elo.compute(elo1,elo2,result)
        self.assertEqual(502.4, newElo, 'testComppute fails, actula elo : {}'.format(newElo))


class LeagueTest(unittest.TestCase):
    """docstring for EloTest."""

    def testWinProbability(self):
        league = League("data/players.json")


        prob = league.winProbability("JB", "Manel")
        self.assertEqual(0.76, prob, 'testComppute fails, actula prob : {}'.format(prob))




unittest.main()
