from random import randint
from random import choice
import items

# String name to [object, charges] OR string name to [object, amount]
# Gives items with charges a unique name and lists the number of charges 
# in the item rather than the amount of items as value
# For charge-less items, the value is simply the amount of them
unique_id = 0
def addToInventory(item, amount=1):
    global inventory
    global unique_id

    if hasattr(item, 'charges'):
        inventory[f'{item.name}unique_id:{unique_id}'] = [item, item.charges]
        unique_id += 1
    else:    
        if item not in inventory:
            inventory[item.name] = [item, 0]
        inventory[item.name][1] += amount

# Returns the highest ranking weapon in inventory
def getCurrentWeapon():
    global inventory

    weapon = items.Dagger()
    for [item, _ ] in inventory.values():
        if hasattr(item, 'rank') and item.rank > weapon.rank:
            weapon = item
    return weapon

inventory = {}
silver = 15 + randint(1, 6)
hp = 15

addToInventory(items.getStartingItem())
addToInventory(items.getStartingWeapon())