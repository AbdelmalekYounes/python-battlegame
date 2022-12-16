from gears.weapon import Weapon
from gears.armor import Armor


class Character:
    def __init__(self, hp: int, name: str, weapon: Weapon, armor: Armor):
        self.hp = hp
        self.name = name
        self.weapon = weapon
        self.armor = armor

    def attack(self, other):
        print(self.name+" attacks "+other.name+" with "+self.weapon.name)
        other.hp -= self.weapon.damage
