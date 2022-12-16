from gears.weapon import Weapon
from gears.armor import Armor
from characters.characters import Character
from characters.barbarian import Barbarian
from characters.wizard import *


Armure1 = Armor("Armure1", 35)
Armure2 = Armor("Armure2", 50)

Arme1 = Weapon("Arme1", 25)
Arme2 = Weapon("Arme2", 15)

# Perso1 = Character(110, "Perso1", Arme1, Armure1)
# Perso2 = Character(100, "Perso2", Arme2, Armure2)

Sort1=Spell("Sort1",50,50)


Barbare1=Barbarian(100,"Barbare1",Arme1,Armure1)
Sorcier1=Wizard(100,"Sorcier1",Arme2,Armure2,Sort1,50)






Barbare1.attack(Sorcier1)
print("Results: ")
print(Barbare1.name, Barbare1.hp, "HP")
print(Sorcier1.name, Sorcier1.hp, "HP")
input("------------------")
Sorcier1.attack(Barbare1)
print("Results: ")
print(Barbare1.name, Barbare1.hp, "HP")
print(Sorcier1.name, Sorcier1.hp, "HP")
input("------------------")
