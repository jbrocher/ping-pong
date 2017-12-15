"""Define class that create an interaction with the user."""

import glob
from lib.Menu import Menu

p = {}
p['0'] = 'get the elo score of a player (not yet)'
p['1'] = 'simulate a game'
p['10'] = 'leave'

actions = {}
menu = Menu()
actions['1'] = menu.simulate_game
actions['10'] = menu.exit


class Interactions:
    """Handle user interactions."""

    def welcoming(self, welcomefile='data/welcome.txt'):
        """Welcome screen."""
        with open(welcomefile, 'r') as welcome_file:
            welcome = welcome_file.read()
        print(welcome)

    def get_pools(self, poolpath='data/players/*.json'):
        """Display pools."""
        poolnames = glob.glob(poolpath)
        return poolnames

    def get_pool_input(self, poolpath='data/players/*.json'):
        """Get pool choice."""
        poolnames = self.get_pools(poolpath)
        n = len(poolnames)
        error = True
        while error:
            try:
                pool_number = int(input('Insert pool number:\n'))
            except ValueError:
                print('Not a valid number')
                continue
            if pool_number >= 0 and pool_number < n:
                error = False
                return poolnames[pool_number]
            print('Number not in range')


class MainMenu:
    """Contain methods about the main menu."""

    def __init__(self, possibilites=p):
        """Contain possibilites offered by the menu.

        - 0 : get my elo
        - 1 : simulate a game
        - 10: leave
        """
        self.possibilites = p
        self.actions = actions

    def possible_menu_inputs(self):
        """Display menu options."""
        for i in self.possibilites:
            print(i, ':', self.possibilites[i])

    def get_menu_input(self):
        """Ask user to choose an action."""
        menu_input = input('>>')
        if menu_input not in self.possibilites:
            print('Invalid input')
            self.get_menu_input()
        return menu_input

    def exec_menu(self, menu_input, pool='data/unit-testing/players/players.json'):
        """Execute the method corresponding to the function."""
        actions[menu_input](pool)
