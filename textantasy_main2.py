import textantasy_start
import textantasy_validators
import textantasy_ravine
import textantasy_forest
import textantasy_do_battle
import textantasy_tree_riddle
import random
import string


print('\nWelcome to Textantasy! Glad you could join us for a quick game!\n')

print("Textantasy is a 'choose your own adventure' styled text-based fantasy game.\n")

name = input("To start, please enter your name? \n\n").lower()

# initiate game with  start_game, return dictionary char_stats with 3 stats, add name to char_stats
# four stats are name, race, weapon, and magic
char_stats = textantasy_start.start_game(name)
char_stats['name'] = name

#make a function to determine how the player gets across the ravine.
textantasy_ravine.ravine(char_stats['race'],char_stats['magic'])


#make a function to determine how the player gets thru the forest.
textantasy_forest.forest(char_stats['race'], char_stats['weapon'], char_stats['magic'])


#make the player solve the tree riddle
textantasy_tree_riddle.tree_riddle(name, char_stats['race'])


#make a function to determine how the player gets thru the dungeon.



#make a function to determine how the player fights the evil king



#make a function to determine how the player games ends (for various endings)
