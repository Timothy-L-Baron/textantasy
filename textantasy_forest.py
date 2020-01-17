#forest function
import textantasy_start
import textantasy_validators
import textantasy_ravine
import textantasy_do_battle
import random
import string

#copies of lists
magic_items = ['amulet', 'armor']
weapons = ['wand', 'sword', 'axe']
races = ['human', 'dwarf', 'elf']

#forest info
f_scout_probs = { 'human' : 55, 'elf' : 75, 'dwarf' : 35 }
f_charge_probs = { 'human' : 65, 'elf' : 65, 'dwarf' : 65 }
f_fight_probs = { 'human' : 85, 'elf' : 35, 'dwarf' : 80 }
f_bonus_penalties = {'armor' : 10, 'amulet' : 10, 'wand' : 50, 'axe' : 85, 'sword' : 75}
f_answers = ['scout', 'charge']
roll = ['roll']


# create the forest function in which the player will fight a goblin and face a question from a dragon [bodies of captain and sorceress found at dragon]
def forest(race, weapon, magic):
    print("\nThere's only one path through the forest and the forest is far too dense for travel off the path.")
    print('\nYou walk forward, {} in hand, and hoping the {} provides some protection from what lies ahead!\n'.format(weapon, magic))
    print('After walking about a mile you think you see something. (Hint: elves have better vision than dwarves)')
    choice = input("\nDo you want to stop and scout or charge forward and hope to surprise whatever is there)\n\n - please  type 'scout' or 'charge'\n\n").lower()
    choice = textantasy_validators.universal_validator_1(choice, f_answers)

    if choice == 'scout':
        print('\nYou duck down by the side of the road and crawl forward.')
        print("\nYou must roll a 'sneak & look' roll")
        if race == 'elf':
            chance = f_scout_probs['elf']
            if magic == 'armor':
                chance = chance + f_bonus_penalties['armor']
            if magic == 'amulet':
                chance = chance + f_bonus_penalties['amulet']
        if race == 'dwarf':
            chance = f_scout_probs['dwarf']
            if magic == 'armor':
                chance = chance + f_bonus_penalties['armor']
            if magic == 'amulet':
                chance = chance + f_bonus_penalties['amulet']
        if race == 'human':
            chance = f_scout_probs['human']
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
            print("\nNice job being patient. The rubs a bracelet on his wrist and 'poof' disappears. Now about that tree .....")
        if r_roll > chance:
            print('\nYour foot drags across some loose gravel.')
            print('\nA disgusting goblin turns, looks, and charges.')
            print('\nYou must fight it.')
            print("\nReady your {} and prepare to do battle. If you're wearing armor your chance to survive is greater.".format(weapon))
            fight = textantasy_do_battle.do_battle(race, weapon, magic)
            if fight == 100:
                fight = 99
            print('\nYour chance for success is: {}%.'.format(fight))
            print('\nYour roll [between 1 - 100] must be less than or equal to {} to succeed\n'.format(fight))
            r_roll = input("Please type 'roll' to continue: \n\n").lower()
            r_roll = textantasy_validators.universal_validator_1(r_roll, roll)
            r_roll = random.randint(1,100)
            print('\nYou rolled {}'.format(r_roll))
            if r_roll <= fight:
                print('\nYou defeat the vile beast with your {}.'.format(weapon))
                print('\nNow about that tree you thought you saw the little beast talking to ........ ')
            if r_roll > fight:
                print('\nYou fight valiantly with your {}, but the goblin smites you in battle!'.format(weapon))
                print('\nYour game is over.\n')
                quit()

    if choice == 'charge':
        bonus = 0
        print('\nYou charge down the road.')
        print("\nYou must roll a 'surpise attack' roll!")
        print("\nIf you succeed you get a bonus to your attack!")
        if race == 'elf':
            chance = f_charge_probs['elf']
            if magic == 'armor':
                chance = chance + f_bonus_penalties['armor']
            if magic == 'amulet':
                chance = chance + f_bonus_penalties['amulet']
        if race == 'dwarf':
            chance = f_charge_probs['dwarf']
            if magic == 'armor':
                chance = chance + f_bonus_penalties['armor']
            if magic == 'amulet':
                chance = chance + f_bonus_penalties['amulet']
        if race == 'human':
            chance = f_charge_probs['human']
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
            print('\nYou manage to catch a disgusting goblin off guard!.')
            print('\nAs you charge the creature it occurs to you he may have been talking to a tree .... ?')
            print('\nCongratulations, your bold action gets you a 10% bonus to your attack roll\n')
            print('Prepare to fight!\n')
            bonus = 10
        if r_roll > chance:
            print("\nYou weren't quick enough.")
            print('\nA disgusting goblin immediately turns to face you. You get no bonus. Was he talking to a tree?')
            print('\nYou must fight it.')
            print("Ready your {} and prepare to do battle. If you're wearing armor your chance to survive is greater.".format(weapon))
        fight = textantasy_do_battle.do_battle(race, weapon, magic)
        fight = fight + bonus
        if fight == 100:
            fight = 99
        print('Your chance for success is: {}%.'.format(fight))
        print('\nYour roll [between 1 - 100] must be less than or equal to {} to succeed\n'.format(chance))
        r_roll = input("Please type 'roll' to continue: \n\n").lower()
        r_roll = textantasy_validators.universal_validator_1(r_roll, roll)
        r_roll = random.randint(1,100)
        print('\nYou rolled {}'.format(r_roll))
        if r_roll <= chance:
            print('\nYou defeat the vile beast with your {}.'.format(weapon))
            print('\nNow about that tree you thought you saw the little beast talking to ........\n')
        if r_roll > chance:
            print('\nYou fight valiantly with your {}, but the goblin smites you in battle!'.format(weapon))
            print('\nYour game is over.\n')
            quit()

    #print(race, weapon, magic)
