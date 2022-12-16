from characters.characters import Character
from gears.armor import *
from gears.weapon import *


class Barbarian(Character):
    def __init__(self, hp, name: str, weapon: Weapon, armor: Armor):
        Character.__init__(self, hp, name, weapon, armor)

    def attack(self, other):
        print(self.name+" attacks twice "+other.name+" with "+self.weapon.name)
        other.hp -= 2*self.weapon.damage
