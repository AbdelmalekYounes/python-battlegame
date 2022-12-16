from gears.armor import Armor
from gears.weapon import Weapon
from characters.character import Character
from characters.barbarian import Barbarian
from characters.wizard import Wizard
from characters.spell import Spell
from gears.arena import Arena


armuuure= Armor('Armuure',120)
warmog= Armor('Warmog',150)

sword=Weapon('sword',12)
axe=Weapon('Axe',8)

boule_de_feu=Spell('Boule de feu',50,35)
attaque_eclair=Spell('Attaque éclaire',70,40)

hades=Barbarian(200,'hades',axe,warmog)
ares=Wizard(180,'Ares',sword,armuuure,boule_de_feu,100)
arene=Arena(hades,ares)

arene.fight(hades,ares)

# while ares.hp >= 1 and hades.hp >= 1: 




# ares.attack(hades)
# print('Results: ')
# print(ares.name,ares.hp,'HP')
# print(hades.name,hades.hp,'HP')
# input('---------------')
    # if hades.hp<=1:
        # continue

# hades.attack(ares)
# print('Results: ')
# print(ares.name,ares.hp,'HP')
# print(hades.name,hades.hp,'HP')
# input('---------------')
# if ares.hp>=0:
    # print('Ares beated Hades')
# else :
    # print('Hades beated Ares with')