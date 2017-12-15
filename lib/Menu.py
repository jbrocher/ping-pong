"""Contain Menu class."""


from lib.League import League
from lib.Game import Game
import sys


class Menu:
    """Menu actions."""

    def choose_player(self, pool):
        """Interaction to choose a player in a pool."""
        player = input('>>')
        league = League(pool)
        try:
            assert league.searchPlayerByName(player) != []
        except AssertionError:
            print('This player is not in the league')
            return self.choose_player(pool)
        except NameError:
            print('Player error!')
            return self.choose_player(pool)
        return league.searchPlayerByName(player)
