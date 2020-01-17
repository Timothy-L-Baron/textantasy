#dungeon module

import textantasy_validators
import random

#copies of lists
magic_items = ['amulet', 'armor']
weapons = ['wand', 'sword', 'axe']
races = ['human', 'dwarf', 'elf']

#forest info
d_chop_probs = { 'human' : 20, 'elf' : 10, 'dwarf' : 30 }
d_chop_bonus = {'wand' : 30, 'sword' : 60}
d_race_probs = { 'human' : 60, 'elf' : 50, 'dwarf' : 60 }
d_fight_probs = { 'human' : 85, 'elf' : 35, 'dwarf' : 80 }
d_bonus_penalties = {'armor' : 10, 'amulet' : 10, 'wand' : 50, 'axe' : 85, 'sword' : 75}
d_answers = ['scout', 'charge']
roll = ['roll']



#create a function for navigating the dungeon
def dungeon(name, race, weapon, magic):
    print('A small stone building stands before you.\n')
    print('An oaken door bars your way in.\n')
    print('You face the door, {} in hand.\n'.format(weapon))
    if weapon == 'axe':
        print("\nNice job finding the 'axe' easter egg.\n")
        print('The door is no problem for the axe. You chop it down and go inside.\n')
        print('Moist cool air flows up from the dungeon as you enter.\n')
    if weapon == 'sword':
        print("\nYour only hope is to force the door open with your {})".format(weapon))
        fight = d_chop_probs[race] + d_chop_bonus[weapon]
        print("Your chance for success is {}%.\n".format(fight))
        r_roll = input("Please type 'roll' to continue: \n\n").lower()
        r_roll = textantasy_validators.universal_validator_1(r_roll, roll)
        r_roll = random.randint(1,100)
        if r_roll <= fight:
            print('\nAfter several chops you break the door down with the {}.'.format(weapon))
            print('\nMoist cool air flows up from the dungeon as you enter. ')
        if r_roll > fight:
            print('\nYou chop at the door with your {}, but the door is too strong and you break the sword\n'.format(weapon))
            print('\nYour game is over.\n')
            quit()
    if weapon == 'wand':
        print("Your only hope is to force the door open with your {})\n".format(weapon))
        fight = d_chop_probs[race] + d_chop_bonus[weapon]
        print("Your chance for success is {}%.\n".format(fight))
        r_roll = input("Please type 'roll' to continue: \n\n").lower()
        r_roll = textantasy_validators.universal_validator_1(r_roll, roll)
        r_roll = random.randint(1,100)
        if r_roll <= fight:
            print('\nYou aim the {} at the door. A massive lgithing bolt shoots forth and destroys the door in its entirety'.format(weapon))
            print('\nMoist cool air flows up from the dungeon as you enter.')
        if r_roll > fight:
            print('\nYou aim the {} at the door and some flowers spill out of the tip, apparently from nowehere'.format(weapon))
            print('\nThe wand seems to be out of charges.\n')
            print('Your game is over.\n')
            quit()
