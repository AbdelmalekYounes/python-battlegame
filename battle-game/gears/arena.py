from characters.character import Character


class Arena(Character):
    def __init__(self, fighter_one,fighter_two):
        self.fighter_one=fighter_one
        self.fighter_two=fighter_two

    


    def fight(fighter_one,fighter_two):
        
        fighter_one.attack(fighter_two)
        print('Results: ')
        print(fighter_one.name,fighter_one.hp,'HP')
        print(fighter_two.name,fighter_two.hp,'HP')
        input('---------------')
