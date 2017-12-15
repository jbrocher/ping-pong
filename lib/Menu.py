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

    def simulate_game(self, pool):
        """Simulate a game between two players."""
        print('You chose to simulate a game:')
        print('Here is the current league:')
        league = League(pool)
        classement = league.printClassement()
        print(classement)
        print('Choose player 1:')
        p1 = self.choose_player(pool)
        print('Choose player 2:')
        p2 = self.choose_player(pool)
        player1 = p1[0][0]
        player2 = p2[0][0]
        game = Game(pool, player1, player2)
        return game.simulate()

    def exit(self, pool='data/unit-testing/players/players.json'):
        """Leave the menu."""
        print('Bye')
        sys.exit()
