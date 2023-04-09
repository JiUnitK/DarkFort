from random import randint
from random import choice

class Dagger:
    name = 'dagger'
    value = 6
    attack_str = 'd6 + 1 to hit'
    damage_str = 'd4 damage'
    description = f'{attack_str}. {damage_str}. Value = {value}'
    rank = 0
    
    def attack(self):
        return randint(1, 6) + 1
    
    def damage(self):
        return randint(1, 4)
    

class Warhammer:
    name = 'warhammer'
    value = 9
    attack_str = 'd6 to hit'
    damage_str = 'd6 damage'
    description = f'{attack_str}. {damage_str}. Value = {value}'
    rank = 1

    def attack(self):
        return randint(1, 6)
    
    def damage(self):
        return randint(1, 6)
    

class Sword:
    name = 'sword'
    value = 12
    attack_str = 'd6 + 1 to hit'
    damage_str = 'd6 damage'
    description = f'{attack_str}. {damage_str}. Value = {value}'
    rank = 2

    def attack(self):
        return randint(1, 6) + 1
    
    def damage(self):
        return randint(1, 6)
    

class Flail:
    name = 'flail'
    value = 15
    attack_str = 'd6 + 1 to hit'
    damage_str = 'd6 + 1 damage'
    description = f'{attack_str}. {damage_str}. Value = {value}'
    rank = 3

    def attack(self):
        return randint(1, 6) + 1
    
    def damage(self):
        return randint(1, 6) + 1
    

class MightyZweihander:
    name = 'Might Zweihander'
    value = 25
    attack_str = 'd6 + 2 to hit'
    damage_str = 'd6 + 2 damage'
    description = f'{attack_str}. {damage_str}. Value = {value}'
    rank = 4

    def attack(self):
        return randint(1, 6) + 2
    
    def damage(self):
        return randint(1, 6) + 2
    
class Rope:
    name = 'rope'
    value = 5
    description = '+1 on trap roll'

class Potion:
    name = 'potion'
    value = 4
    description = 'Heals d6 hp'

class Armor:
    name = 'armor'
    value = 10
    description = 'Reduce incoming damage by d4'

class CloakOfInvisibility:
    name = 'cloak of invisibility'
    charges = randint(1, 4)
    value = 15
    description = 'Avoid d4 fights while acquiring all monster points'
    disappears_on_use = True

class SummonDaemon:
    name = 'Summon Weak Daemon (scroll)'
    value = 7
    charges = randint(1, 4)
    description = 'The daemon helps you d4 fights, dealing d4 damage'
    disappears_on_use = True

class PalmsOpen:
    name = 'Palms Open the Southern Gate (scroll)'
    value = 7
    charges = randint(1, 4)
    description = 'Has d4 charges. Does d6 + 1 damage'

class AegisOfSorrow:
    name = 'Aegis of Sorrow'
    value = 7
    charges = randint(1, 4)
    description = 'Has d4 charges. Reduces incoming damage by d4'

class FalseOmen:
    name = 'False Omen'
    value = 7
    charges = 1
    description = 'Either: when exploring a room, you choose a result '\
        + 'on the Room table instead of rolling a d6, or reroll any die'


starting_weapons = [
    Warhammer,
    Dagger,
    Sword,
    Flail,
]
def getStartingWeapon():
    return choice(starting_weapons)()

starting_items = [
    Armor,
    Potion,
    SummonDaemon,
    CloakOfInvisibility,
]
def getStartingItem():
    item = choice(starting_items)()

    # Cloak of Invisibility and Summon Daemon scroll should not disappear 
    # after charges deplete if they are the starting items
    if hasattr(item, 'disappears_on_use'):
        item.disappears_on_use = False
        
    return item

random_scroll = [
    SummonDaemon,
    PalmsOpen,
    AegisOfSorrow,
    FalseOmen,
]
def getRandomScroll():
    return choice(random_scroll)()

def getRandomItem():
    random_items = [
        starting_weapons,
        Potion,
        Rope,
        random_scroll,
        Armor,
        CloakOfInvisibility,
    ]
    item = choice(random_items)
    if isinstance(item, list):
        item = choice(item)
    return item()