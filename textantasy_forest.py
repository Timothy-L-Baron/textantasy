#forest function
import textantasy_start
import textantasy_validators
import textantasy_ravine
import textantasy_forest
import random
import string

#copies of lists
magic_items = ['amulet', 'armor']
weapons = ['wand', 'sword']
races = ['human', 'dwarf', 'elf']

#forest info
f_bridge_probs = { 'human' : 75, 'elf' : 85, 'dwarf' : 40 }
f_climb_probs = { 'human' : 75, 'elf' : 50, 'dwarf' : 85 }
f_bonus_penalties = {'armor' : -10, 'amulet' : 10}
f_answers = ['bridge', 'climb']
roll = ['roll']


# create the forest function in which the player will fight a goblin and face a question from a dragon [bodies of captain and sorceress found at dragon]
def forest(race, weapon, magic):
    print('forest test')
    print(race, weapon, magic)
