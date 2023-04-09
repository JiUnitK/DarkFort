from random import randint
from random import choice
import player
import items
import combat

print(f'\nYour name is Kargunt. You begin with {player.hp} hit points (hp) and {player.silver} silvers. You may carry unlimited items.')
print(f'You own one weapon: a {player.getCurrentWeapon().name}, and one {list(player.inventory)[0]}.')
input(f'\n     Enter the catacombs (press Enter)\n')

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
    item = items.getRandomItem()
    player.addToInventory(item)
    input(f'You find a(n) {item.name}')
elif encounter == 2:
    # Encounter weak monster
    combat.runBattle(choice(combat.weak_monsters))
elif encounter == 3:
    # Random scroll
    scroll = choice(items.random_scroll)
    player.addToInventory(scroll)
    input(f'A dying mystic gives you {scroll.name}')
elif encounter == 4:
    # Room is empty
    input(f'The entrance is eerily quiet and desolate')
