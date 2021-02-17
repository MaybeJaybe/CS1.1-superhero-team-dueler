import random

class Hero:
    def __init__(self, name, starting_health=100):
        # need default starting health, can set it in header
        self.name = name
        self.starting_health = starting_health
        # current health is same as starting health cuz no damage yet
        self.current_health = starting_health

    def fight(self, opponent):
        # take turns fighting until a victor emerges
        # randomly choose winner for now
        hero_list = ["Wonder Woman", "Dumbledore"]
        print(str(random.choice(hero_list)) + " won the fight!")

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)
