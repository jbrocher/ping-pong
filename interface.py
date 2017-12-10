"""Interface between game and user."""

from lib.Interactions import Interactions

interact = Interactions()
interact.welcoming()

# The user has to choose a pool
print('You have to choose a pool among the following files:')
pool_list = interact.get_pools()
for i in range(len(pool_list)):
    print (i, ':', pool_list[i])

poolfile = interact.get_pool_input()
