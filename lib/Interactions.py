"""Define class that create an interaction with the user."""
import sys
from lib.Game import Game
from lib.League import League


class Interactions:
    """Handle user interactions."""

    def welcoming(self, welcomefile='data/welcome.txt'):
        """Welcome screen."""
        with open(welcomefile, 'r') as welcome_file:
            welcome = welcome_file.read()
        print(welcome)
    #
    # def get_pools(self, poolpath='data/players/*.json'):
    #     """Display pools."""
    #     poolnames = glob.glob(poolpath)
    #     return poolnames

    def getIntUserInput(self, n1, n2, message):
        """Retrieve an int from the user."""
        error = True
        while error:
            try:
                result = int(input(message))
            except ValueError:
                print('Not a valid number')
                continue
            if result >= n1 and result < n2:
                error = False
            else:
                print('Number not in range')
        return result

    # def get_pool_input(self, poolpath='data/players/*.json'):
    #     """Get pool choice."""
    #     poolnames = self.get_pools(poolpath)
    #     n = len(poolnames)
    #     error = True
    #     while error:
    #         try:
    #             pool_number = int(input('Insert pool number:\n'))
    #         except ValueError:
    #             print('Not a valid number')
    #             continue
    #         if pool_number >= 0 and pool_number < n:
    #             error = False
    #             return poolnames[pool_number]
    #         print('Number not in range')

    def simulateGame(self, context):
        """Interact with the user to simulate a game."""
        league = League(context["league"])
        print(league.printClassement())
        print("Pick two players")
        player1 = self.getIntUserInput(0, 1000, "pick player 1 :")
        player2 = self.getIntUserInput(0, 1000, "pick player 2 :")
        game = Game(context["league"], player1, player2)
        game.simulate()

    def exit(self, context):
        """Leave the menu."""
        print('Bye')
        sys.exit()
