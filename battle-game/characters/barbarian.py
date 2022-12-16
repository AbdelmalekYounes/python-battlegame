from characters.character import Character


class Barbarian(Character):

    def __init__(self, hp:int,name:str,weapon,armor):
        Character.__init__(self,hp,name,weapon,armor)

        

    def attack(self, other):
        super().attack(other)
        super().attack(other)
        
