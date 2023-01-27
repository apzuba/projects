import sys
import time

from random import randint

#The function to update the game stats
def game_stats():
    defence = 2
    pocket_money = 0
    hard_damage = False

#The initial game stats settings
game_stats.defence = 3
game_stats.pocket_money = int(randint(25,55))
game_stats.hard_damage = False
