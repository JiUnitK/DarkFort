from random import choice
from random import randint
import player
import items

class Skeleton:
    name = 'Blood-drenched Skeleton'
    points = 3
    hp = 6

    def damage(self):
        return randint(1, 4)
    
    def loot(self):
        if randint(1, 3) == 1:
            return items.Dagger()
        
class Cultist:
    name = 'Catacomb Cultist'
    points = 3
    hp = 6

    def damage(self):
        return randint(1, 4)
    
class Goblin:
    name = 'Goblin'
    points = 3
    hp = 5

    def damage(self):
        if randint(1, 3) == 1:
            return items.Rope()
        
class Hound:
    name = 'Undead Hound'
    points = 4
    hp = 6

    def damage(self):
        return randint(1, 4)
    
weak_monsters = [
    Skeleton,
    Cultist,
    Goblin,
    Hound,
]

strong_monsters = [
    'necro-sorcerer',
    'small stone troll',
    'medusa',
    'ruin basilisk',
]

def runBattle(enemy):
    enemy = enemy()
    input(f'You encounter a(n) {enemy.name}!')

    weapon = player.getCurrentWeapon()

    round = 1
    while (player.hp > 0 and enemy.hp > 0):
        print(f'Round {round}')
        round += 1

        print(f'   Your HP: {player.hp}')
        print(f'   Your weapon: {weapon.name} ({weapon.attack_str}, {weapon.damage_str})\n')

        print(f'   {enemy.name} HP: {enemy.hp}')
        print(f'   {enemy.name} Points: {enemy.points}\n')

        input(f'Hit Enter to strike!\n')

        attack = weapon.attack()
        msg = f'You strike with your {weapon.name}'
        if attack >= enemy.points:
            msg += f' and hit!\n'
        else:
            msg += f' but miss...\n'
        msg += f'Rolled {attack} ({weapon.attack_str}) vs monster\'s {enemy.points} points\n'
        print(msg)

        if attack >= enemy.points:
            damage = weapon.damage()
            input(f'You deal {damage} damage.\n')
            enemy.hp -= damage
        else:
            damage = enemy.damage()
            input(f'You receive {damage} damage\n')
            player.hp -= damage

    if player.hp < 0:
        print('You are dead\n\n')
        return False
    
    # Todo: Add loot mechanic

    print('You are victorious!')
    return True