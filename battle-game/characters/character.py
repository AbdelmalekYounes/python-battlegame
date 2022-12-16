from gears.armor import Armor
from gears.weapon import Weapon
from gears.arena import Arena

class Character:
    def __init__(self, hp:int, name:str, weapon:Weapon, armor:Armor):
        self.hp=hp
        self.name=name
        self.weapon=weapon
        self.armor=armor
    
    def attack(fighter_one,fighter_two):
        print(fighter_one.name+' attacks '+fighter_two.name+' with '+fighter_one.weapon.name)
        fighter_two.hp-=fighter_one.weapon.damage
        


        



