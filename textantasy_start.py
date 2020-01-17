import textantasy_validators
import textantasy_ravine
import random


magic_items = ['amulet', 'armor']

#easter egg can pick axe as weapon
weapons = ['wand', 'sword', 'axe']

#easter egg - can pick human as a race
races = ['human', 'dwarf', 'elf']

#design a function that take the player's name as input
#the player then picks  a fantasy race, a weapon, and a magic item
def start_game(n):
    print('\nHello ' + n.capitalize() + '\n')
    print("You look amazing today! Let's start the game!\n")
    race = input('Do you want to play an elf or a dwarf?\n\n').lower()
    race = textantasy_validators.universal_validator_1(race, races)
    if race == 'human':
        print('\nWelcome brave ' + race + '!' + '\n' + '\nYou found the first easter egg!' '\n')
    if race != 'human':
        print('\nWelcome brave ' + race + '!' + '\n')
    magic = input('Please choose your magical item:\n\namulet or armor\n\n').lower()
    magic = textantasy_validators.universal_validator_1(magic, magic_items)
    weapon = input('\nPlease choose your weapon:\n\nsword or wand\n\n').lower()
    if weapon == 'axe':
        print('\nGreat job finding the axe!' + '\n' + '\nYou found the second easter egg!')
    weapon = textantasy_validators.universal_validator_1(weapon, weapons)
    stats = {'race' : race, 'magic' : magic , 'weapon' : weapon}
    #return dictionary and start message
    print("""\nYou hail from a small village in the Kingdom of Zathruul. It is a land of wondrous beauty, but a dark cloud hangs
over it now. There has been much unrest in the kingom of late. Evil has struck the kingdom - townspeople have gone missing
missing. At first Captain Jarod, the captain of the guard, thought nothing of it. Then a rich merchant family went missing
- apparently disappeared right out of their home - no sign of them whatsoever. Then another rich merchant family. King Belgard
had enough of it. The king ordered Captain Jared to stifle the matter with a full investigation. The captain summoned a sorceress
to assist him. Using her magic she discovered a trail that could only be seen by magic-users. She and the captain followed the
trail to a ravine outside of town. They sent their messenger back to say they were crossing the ravine. It's been six months
and nobody has heard from them. Townspeople have continued to disappear and people are desperate for answers. Today """ + n.capitalize() +',\nbrave ' + race + ', it is your chance to be a hero!\n')
    return stats
