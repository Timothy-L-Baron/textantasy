import textantasy_start
import textantasy_validators
import textantasy_ravine
import textantasy_forest
import textantasy_do_battle
import random
import string

#copies of lists
magic_items = ['amulet', 'armor']
weapons = ['wand', 'sword', 'axe']
races = ['human', 'dwarf', 'elf']

#forest stats
f_scout_probs = { 'human' : 55, 'elf' : 75, 'dwarf' : 35 }
f_charge_probs = { 'human' : 50, 'elf' : 50, 'dwarf' : 50 }
f_fight_probs = { 'human' : 50, 'elf' : 50, 'dwarf' : 50 }
f_bonus_penalties = {'armor' : 10, 'amulet' : 10, 'wand' : 10, 'axe' : 20, 'sword' : 15}
f_answers = ['scout', 'charge']


# A function for battles
def do_battle(race, weapon, magic):
    if race == 'elf':
        chance = f_fight_probs['elf']
        if magic == 'armor':
            chance = chance + f_bonus_penalties['armor']
        if weapon == 'axe':
            chance = chance + f_bonus_penalties['axe']
        if weapon == 'sword':
            chance = chance + f_bonus_penalties['sword']
        if weapon == 'wand':
            chance = chance + f_bonus_penalties['wand']
    if race == 'dwarf':
        chance = f_fight_probs['dwarf']
        if magic == 'armor':
            chance = chance + f_bonus_penalties['armor']
        if weapon == 'axe':
            chance = chance + f_bonus_penalties['axe']
        if weapon == 'sword':
            chance = chance + f_bonus_penalties['sword']
        if weapon == 'wand':
            chance = chance + f_bonus_penalties['wand']
    if race == 'human':
        chance = f_fight_probs['human']
        if magic == 'armor':
            chance = chance + f_bonus_penalties['armor']
        if weapon == 'axe':
            chance = chance + f_bonus_penalties['axe']
        if weapon == 'sword':
            chance = chance + f_bonus_penalties['sword']
        if weapon == 'wand':
            chance = chance + f_bonus_penalties['wand']
    return chance
