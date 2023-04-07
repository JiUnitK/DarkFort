from random import randint
from random import choice
import os

inventory = {}
silver = 15 + randint(1, 6)

print(f'\nYour name is Kargunt. You begin with 15 hit points (hp) and {silver} silvers. You may carry unlimited items.')

starting_weapons = [
    'warhammer',
    'dagger',
    'sword',
    'flail',
]

starting_items = [
    'armor',
    'potion',
    'scroll',
    'cloak of invisibility',
]

random_scroll = [
    'Summon weak deamon (scroll)',
    'Palms Open the Southern Gate (scroll)',
    'Aegis of Sorrow (scroll)',
    'False Omen (scroll)',
]

def getRandomItem():
    random_items = [
        starting_weapons,
        'potion',
        'rope',
        random_scroll,
        'armor',
        'cloak of invisibility',
    ]
    item = choice(random_items)
    if isinstance(item, list):
        item = choice(item)
    return item

def addToInventory(item, amount=1):
    if item not in inventory:
        inventory[item] = 0
    inventory[item] += amount

item = choice(starting_items)
addToInventory(item, 1)
weapon = choice(starting_weapons)
addToInventory(weapon, 1)

print(f'You own one weapon: a {weapon}, and one {item}.')
input(f'\n     Enter the catacombs (press Enter)')

# Each key represents a room. The value is a list of connected rooms
dungeon = {}

# Entrance room will connect to 1 to 4 other rooms
connected_rooms = []
for room in range(randint(0, 3)):
    connected_rooms.append(room+1)
dungeon[0] = connected_rooms
current_room = 0

# Roll encounter
encounter = randint(1, 4)
if encounter == 1:
    # Random item
    item = getRandomItem()
    addToInventory(item)
    input(f'\nYou find a {item}')
elif encounter == 2:
    # Weak monster
    input(f'\nA weak monster stands guard. Attack!')
elif encounter == 3:
    # Random scroll
    scroll = choice(random_scroll)
    addToInventory(scroll)
    input(f'\nA dying mystic gives you {scroll}')
elif encounter == 4:
    # Room is empty
    input(f'\nThe entrance is eerily quiet and desolate')
