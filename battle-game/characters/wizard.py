from characters.characters import Character
from gears.armor import *
from gears.weapon import *


class Spell:
    def __init__(self, name: str, damage: int, mana: int):
        self.name = name
        self.damage = damage
        self.mana = mana


class Wizard(Character):
    def __init__(self, hp, name: str, weapon: Weapon, armor: Armor, spell: Spell, mana: Spell):
        Character.__init__(self, hp, name, weapon, armor)

    def attack(self, other):
        choice=input("Spell or Weapon ? ")
        if choice=="spell" or choice=="Spell":
            print(self.name+" attacks "+other.name+" with "+Spell.name)
            other.hp-=Spell.damage
        elif choice=="weapon" or choice=="Weapon":
            super().attack(other)
