"""Define Interactions class.
Contains all the methods that create an interaction with the user"""
import glob


class Interactions:
    """Handle user interactions."""

    def welcoming(self, welcomefile='data/welcome.txt'):
        """Welcome screen"""
        with open(welcomefile, 'r') as welcome_file:
            welcome = welcome_file.read()
        print(welcome)

    def get_pools(self, poolpath='data/players/*.json'):
        poolnames = glob.glob(poolpath)
        return poolnames

    def get_pool_input(self, poolpath='data/players/*.json'):
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
