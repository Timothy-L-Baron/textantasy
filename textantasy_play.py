#main game play
import textantasy_start
import textantasy_validators
import textantasy_lists
import textantasy_play

magic_items = ['amulet', 'armor']
weapons = ['wand', 'sword']
races = ['human', 'dwarf', 'elf']

r_bridge_probs = { 'human' : 75, 'elf' : 90, 'dwarf' : 40 }
r_climb_probs = { 'human' : 75, 'elf' : 70, 'dwarf' : 85 }
r_bonus_penalties = [ ]





#play_stats = {}

def begin(name, race, weapon, magic):
    play_stats = {}
    play_stats['p_name'] = name
    play_stats['p_race'] = race
    play_stats['p_weapon'] = weapon
    play_stats['p_magic'] = magic
    return play_stats

def ravine(race, magic):
    print("""You stand before 'The Great Ravine', the last place where the sorceress and captain were last seen alive. You look down at
your feet and it looks as though the ravine was formed by a giant hand striking the ground from the sky, leaving a massive cut in the
ground before you. It stretches as far as the eye can see to your left and right  """)
    print(race, magic)
