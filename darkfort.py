from random import randint
from random import choice


silver = 15 + randint(1, 6)
print(f'Your name is Kargunt. You begin with 15 hit points (hp) and {silver} silvers. You may carry unlimited items.')

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

inventory = []
inventory.append(choice(starting_items))
weapon = choice(starting_weapons)
inventory.append(weapon)

print(f'You own one weapon: a {weapon}, and one {inventory[0]}')

