from secrets import choice
from unicodedata import name
from characters.character import Character
from gears.armor import Armor
from gears.weapon import Weapon


    
# class Spell:
#     def __init__(self, name:str, damage:int, mana:int):
        

    
class Wizard(Character):
    def __init__(self,hp,name,weapon,armor,spell, mana):
        Character.__init__(self,hp,name,weapon,armor)

        self.spell=spell
        self.mana=mana

    

    def attack(self, other):
        super().attack(other)


    def attack_with_spell(self,other):
        other.hp-=self.spell.damage
        self.mana=self.mana-self.spell.mana 