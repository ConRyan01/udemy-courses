import random
from replit import clear

import art
from game_data import data

def populate():
    """returns a dict entry from the data list"""
    entry = random.choice(data)
    return entry

def stringify(entry:dict):
    """returns a string of information from a dict input"""
    entry_text = f'{entry["name"]}, a {entry["description"]}, from {entry["country"]}'
    return entry_text

entry1 = None
should_continue = True
score = 0

while should_continue:

    print(art.logo)

    if entry1 == None:
        entry1 = populate()
    entry2 = populate()

    print(f'Compare A: {stringify(entry1)}')
    print(f'\n {art.vs}')
    print(f'Compare B: {stringify(entry2)}')

    answer = input('Who has more followers? A or B: ').lower()

    if entry1['follower_count'] > entry2['follower_count'] and answer == 'a':
        score += 1
        print(f'You\'re right! Current score: {score}')
    elif entry1['follower_count'] < entry2['follower_count'] and answer == 'b':
        score += 1
        print(f'You\'re right! Current score: {score}')
    else:
        should_continue = False

    entry1 = entry2
    
    clear()

print(art.logo)
print(f'Sorry, that\'s wrong. Final Score: {score}')
