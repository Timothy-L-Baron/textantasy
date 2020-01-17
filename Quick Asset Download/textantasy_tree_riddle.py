import textantasy_start
import textantasy_validators
import textantasy_ravine
import textantasy_forest
import textantasy_do_battle
import random


#copies of lists
magic_items = ['amulet', 'armor']
weapons = ['wand', 'sword', 'axe']
races = ['human', 'dwarf', 'elf']

tree_answers = ['left', 'right']

#tree riddle function
def tree_riddle(name, race):
    print('Sure enough, a talking tree is planted at the fork in the road\n')
    print('"Hello, brave {}, two paths lies before you."\n'.format(race))
    print('"One gives you a chance to enter the dungeon and save the kingdom and the other leads to certain death."')
    print('\n"The path you seek can be found in this riddle:"\n')
    print('"There are two brothers, one brother always tells the truth and the other brother always lies."')
    print('\nOne brother says to you "My brother would tell you to take the left path."')
    path = input("\nPlease choose your path - type 'left' or 'right':\n\n").lower()
    path = textantasy_validators.universal_validator_1(path, tree_answers)
    if path == 'left':
        print('\nYou have chosen unwisely.')
        print('\nThe moment you set foot down the path you are transported further down the path.')
        print('\nYou see at your feet the fried bones and equipment of the the sorceress.')
        print('\nBefore you can contemplate further a massive red dragon breathes a huge cone of fire at you.')
        print('\nYou have died and your game is over.\n')
        quit()
    if path == 'right':
        print('\nYou have chosen wisely. The dungeon lies ahead!\n')
