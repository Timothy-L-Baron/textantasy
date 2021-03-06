#main game play
import textantasy_start
import textantasy_validators
import random


#copies of lists
magic_items = ['amulet', 'armor']
weapons = ['wand', 'sword']
races = ['human', 'dwarf', 'elf']

#ravine info
r_bridge_probs = { 'human' : 85, 'elf' : 85, 'dwarf' : 50 }
r_climb_probs = { 'human' : 85, 'elf' : 50, 'dwarf' : 85 }
r_bonus_penalties = {'armor' : -10, 'amulet' : 10}
r_answers = ['bridge', 'climb']
roll = ['roll']

def ravine(race, magic):
    print("""You stand before 'The Great Ravine' facing north, the last place where the sorceress and captain were seen alive. You look down at
your feet and it looks as though the ravine was formed by a giant hand striking the ground from the sky, leaving a massive cut in the
ground before you 50 feet deep. It spans 50 feet and stretches as far as the eye can see to the east and west. On the other side of the ravine lies
Urchin Forest - many a parent has passed on storiesto their child about evil in the forest - but are they just stories? The captain's destination was
somewhere beyond the forest. There is a rickety bridge that's on it's last legs, but it will get you across the ravine quickly and before dark.
You could also climb down the ravine and climb back up the other side, but this will take all day. Elves are excellent at balancing on thngs like
ropes and bridges and dwarves are great climbers. Having the armo will make either route more difficult.""")
    choice = input("Do you want to walk across the bridge or climb down the ravine?\n - please  type 'bridge' or 'climb'\n\n").lower()
    choice = textantasy_validators.universal_validator_1(choice, r_answers)
    #calculate probabilities for success
    if choice == 'bridge':
            if race == 'elf':
                chance = r_bridge_probs['elf']
                if magic == 'armor':
                    chance = chance + r_bonus_penalties['armor']
                if magic == 'amulet':
                    chance = chance + r_bonus_penalties['amulet']
            if race == 'dwarf':
                chance = r_bridge_probs['dwarf']
                if magic == 'armor':
                    chance = chance + r_bonus_penalties['armor']
                if magic == 'amulet':
                    chance = chance + r_bonus_penalties['amulet']
            if race == 'human':
                chance = r_bridge_probs['human']
                if magic == 'armor':
                    chance = chance + r_bonus_penalties['armor']
                if magic == 'amulet':
                    chance = chance + r_bonus_penalties['amulet']
    if choice == 'climb':
            if race == 'elf':
                chance = r_climb_probs['elf']
                if magic == 'armor':
                    chance = chance + r_bonus_penalties['armor']
                if magic == 'amulet':
                    chance = chance + r_bonus_penalties['amulet']
            if race == 'dwarf':
                chance = r_climb_probs['dwarf']
                if magic == 'armor':
                    chance = chance + r_bonus_penalties['armor']
                if magic == 'amulet':
                    chance = chance + r_bonus_penalties['amulet']
            if race == 'human':
                chance = r_climb_probs['human']
                if magic == 'armor':
                    chance = chance + r_bonus_penalties['armor']
                if magic == 'amulet':
                    chance = chance + r_bonus_penalties['amulet']
    print('\nYour chance for success is {}%'.format(chance))
    print('\nYour roll [between 1 - 100] must be less than or equal to {} to succeed\n'.format(chance))
    r_roll = input("Please type 'roll' to continue: \n\n").lower()
    r_roll = textantasy_validators.universal_validator_1(r_roll, roll)
    r_roll = random.randint(1,100)
    print('\nYou rolled {}'.format(r_roll))
    if r_roll <= chance:
        print('\nCongratulations you made it across the ravine! A brooding forest now looms before you!!')
        print('\nStrange .... no animal sounds can be heard.')
    if r_roll > chance:
        print('\nYou died in your attempt to cross the ravine!')
        print('\nYour game is over.\n')
        quit()
