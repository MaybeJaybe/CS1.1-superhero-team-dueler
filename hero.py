import random

class Hero:
    # needs:
    # init parameters: name:string, starting_health:int=100
    # add_ability parameters: ability:Ability Object
    # attack: no parameters
    # defend: incoming_damage:int
    # take_damage parameters: damage
    # is alive: no parameters
    # fight parameters: opponent: Hero Class


    def __init__(self, name, starting_health=100):
        # need default starting health, can set it in header
        self.name = name
        self.starting_health = starting_health
        # current health is same as starting health cuz no damage yet
        self.current_health = starting_health

    def fight(self, opponent):
        # take turns fighting until a victor emerges
        # randomly choose winner for now
        hero_list = [self.name, opponent.name]
        print(random.choice(hero_list) + " won the fight!")

if __name__ == "__main__":
    # my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)
