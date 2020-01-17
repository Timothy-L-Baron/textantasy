#final battle

import textantasy_validators
import textantasy_do_battle
import random
import string

#copies of lists
magic_items = ['amulet', 'armor']
weapons = ['wand', 'sword', 'axe']
races = ['human', 'dwarf', 'elf']

#final battle info
fin_race_probs = { 'human' : 60, 'elf' : 50, 'dwarf' : 60 }
fin_fight_probs = { 'human' : 85, 'elf' : 35, 'dwarf' : 80 }
fin_bonus_penalties = {'armor' : 10, 'amulet' : 10, 'wand' : 50, 'axe' : 85, 'sword' : 75}
fin_answers = ['scout', 'charge']
roll = ['roll']

def final_battle(name, race, weapon, magic):
    print('You enter the dungeon and hear a cacophony of misery coming from below.\n')
    print('You head to the nearest staircase and sneak down\n')
    print('Your breath freezes in your throat when you get to the bottom.\n')
    print('There are several cells filled with people. You recognize several of them as local townspeople\n')
    print('You take a step forward to unlock the first cell, but hear the jangle of armor behind you.\n')
    print('Captain Jarod steps into the room from a secret passage.\n')
    print('"Your meddling ends here {}!""\n'.format(name.capitalize()))
    print("Your {} and {} can't save you now!\n".format(weapon, magic))
    if weapon == 'wand':
        print('The captain looks nervously at your wand\n')
    print('The captain draws his sword. You must fight!')
    fight = textantasy_do_battle.do_battle2(race, weapon, magic)
    if fight >= 100:
        fight = 99
    print('\nYour chance for success is: {}%.'.format(fight))
    print('\nYour roll [between 1 - 100] must be less than or equal to {} to succeed\n'.format(fight))
    r_roll = input("Please type 'roll' to continue: \n\n").lower()
    r_roll = textantasy_validators.universal_validator_1(r_roll, roll)
    r_roll = random.randint(1,100)
    print('\nYou rolled {}'.format(r_roll))
    if r_roll <= fight:
        print('\nYou defeat the evil captain with your {}.'.format(weapon))
        print('\nYou free the townspeople and lead them back to town.')
        print('\nThe king grants you a knighthood and makes you the new captain of the guard.')
        print('\nA new statue is built in the center of town.\n')
        print("The statue depicts you with your {} and {}. Below the statue a plaque reads '[] Town Hero'.\n".format(weapon, magic, name))
    if r_roll > fight:
        print('\nYou fight valiantly with your {}, but the captain defeats you in battle!'.format(weapon))
        print('\nYour game is over.\n')
        quit()










"""if race == 'elf':
    chance = fin_scout_probs['elf']
    if magic == 'armor':
        chance = chance + f_bonus_penalties['armor']
    if magic == 'amulet':
        chance = chance + f_bonus_penalties['amulet']
if race == 'dwarf':
    chance = fin_scout_probs['dwarf']
    if magic == 'armor':
        chance = chance + f_bonus_penalties['armor']
    if magic == 'amulet':
        chance = chance + f_bonus_penalties['amulet']
if race == 'human':
    chance = fin_scout_probs['human']
    if magic == 'armor':
        chance = chance + f_bonus_penalties['armor']
    if magic == 'amulet':
        chance = chance + f_bonus_penalties['amulet']
print('\nYour chance for success, brave ' + race + ', is {}%.'.format(chance))
print('\nYour roll [between 1 - 100] must be less than or equal to {} to succeed\n'.format(chance))
r_roll = input("Please type 'roll' to continue: \n\n").lower()
r_roll = textantasy_validators.universal_validator_1(r_roll, roll)
r_roll = random.randint(1,100)
print('\nYou rolled {}'.format(r_roll))
if r_roll <= chance:
    print('\nYou manage to creep forward enough to get a good look without being seen.')
    print('\nA disgusting goblin appears to be having a conversation with a tree at a fork in the road.')
    print('\nThe branches of the tree wave like human arms as it speaks from a hole in its trunk below two peeping eyes.')
    print("\nNice job being patient. The goblin rubs a bracelet on his wrist and 'poof' disappears. Now about that tree .....\n")
if r_roll > chance:
    print('\nYour foot drags across some loose gravel.')
    print('\nA disgusting goblin turns, looks, and charges.')
    print('\nYou must fight it.')
    print("\nReady your {} and prepare to do battle. If you're wearing armor your chance to survive is greater.".format(weapon))   """
