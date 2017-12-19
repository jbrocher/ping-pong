"""Contain Menu class."""


class Menu:
    """Menu actions."""

    def __init__(self, name, menus, parameters=[],  context={}):
        """Constructor."""
        self.name = name
        self.context = context
        self._menus = menus
        self.parameters = parameters

        if parameters==[]:
            n = len(menus)
            for i in range(1,n):
                self.parameters.append({"noParam":True})

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

    def printOptions(self):
        """Print the possibles options of the menu."""
        print(self.name)
        i = 0
        for menu in self._menus:
            if type(menu) is Menu:
                print("{} : {}".format(i, menu.name))
                i = i+1
            else:
                print("{} : {}".format(i, menu[0]))
                i = i+1

    def pick(self):
        """Ask for the choice and executes the action accoringly."""
        n = len(self._menus)
        choice = self.getIntUserInput(0, n, "Type your choice : ")
        parameters = self.parameters[choice]
        menu = self._menus[choice]

        if type(menu) is Menu:
            menu.context = self.context.copy()
            menu.context.update(parameters)
            menu.printOptions()
            menu.pick()
        else:
            menu[1](self.context)

    # def choose_player(self, pool):
    #     """Interaction to choose a player in a pool."""
    #     player = input('>>')
    #     league = League(pool)
    #     try:
    #         assert league.searchPlayerByName(player) != []
    #     except AssertionError:
    #         print('This player is not in the league')
    #         return self.choose_player(pool)
    #     except NameError:
    #         print('Player error!')
    #         return self.choose_player(pool)
    #     return league.searchPlayerByName(player)
    #
    # def simulate_game(self, pool):
    #     """Simulate a game between two players."""
    #     print('You chose to simulate a game:')
    #     print('Here is the current league:')
    #     league = League(pool)
    #     classement = league.printClassement()
    #     print(classement)
    #     print('Choose player 1:')
    #     p1 = self.choose_player(pool)
    #     print('Choose player 2:')
    #     p2 = self.choose_player(pool)
    #     player1 = p1[0][0]
    #     player2 = p2[0][0]
    #     game = Game(pool, player1, player2)
    #     return game.simulate()
    #
    # def exit(self, pool='data/unit-testing/players/players.json'):
    #     """Leave the menu."""
    #     print('Bye')
    #     sys.exit()
