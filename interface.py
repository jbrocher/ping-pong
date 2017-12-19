"""Interface between game and user."""

from lib.Interactions import Interactions
from lib.Menu import Menu

interact = Interactions()

# Main menu creation

mainMenuParameters = [{"league": "data/players/players.json"}, {"league": "data/players/players0.json"}]

subMenu1 = Menu("player.json", [("simulate", interact.simulateGame), ("exit", interact.exit)])
subMenu2 = Menu("player0.json", [("simulate", interact.simulateGame), ("exit", interact.exit)])

mainMenu = Menu("Leagues", [subMenu1, subMenu2], mainMenuParameters, {"context": True})


interact.welcoming()
mainMenu.printOptions()
mainMenu.pick()
# # The user has to choose a pool
# print('You have to choose a pool among the following files:')
# pool_list = interact.get_pools()
# for i in range(len(pool_list)):
#     print (i, ':', pool_list[i])
#
# poolfile = interact.get_pool_input()
# print("Vale, we're going to work with pool:", poolfile)
#
# while True:
#     print("\nWhat do you want to do next?")
#     menu.possible_menu_inputs()
#     menu_choice = menu.get_menu_input()
#     menu.exec_menu(menu_choice, poolfile)
