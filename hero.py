import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        # need default starting health, can set it in header
        self.name = name
        self.starting_health = starting_health
        # current health is same as starting health cuz no damage yet
        self.current_health = starting_health
        # abilities list and armors list
        self.abilities = list()
        self.armors = list()

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_ability(self, ability):
        # add ability objects
        self.abilities.append(ability)

    def defend(self):
        total_blocked = 0
        for armor in self.armors:
            total_blocked += armor.block()
        return total_blocked

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def take_damage(self, damage):
        final_damage = damage - self.defend()
        if final_damage > 0:
            self.current_health -= final_damage

    def fight(self, opponent):
        # take turns fighting until a victor emerges
        # randomly choose winner for now
        hero_list = [self.name, opponent.name]
        print(random.choice(hero_list) + " won the fight!")

    def is_alive(self):
        # check current health of hero, if <=0, return false, otherwise return true
        if self.current_health > 0:
            return True
        else: 
            return False


if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)

    ability1 = Ability("Great Debugging", 50)
    hero.add_ability(ability1)
    ability2 = Ability("Hopper Smash", 20)
    hero.add_ability(ability2)

    armor1 = Armor("Cloak of Shadows", 50)
    hero.add_armor(armor1)


    print(hero.current_health)
    hero.take_damage(50)
    print(hero.current_health)
    print(hero.is_alive())
    print("180 damage")
    hero.take_damage(180)
    print(hero.current_health)
    print(hero.is_alive())
    
    # print(hero.attack())
    # print(hero.defend())

    # print(hero.name)
    # print(hero.current_health)
    # print(hero.abilities)


    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")

    # hero1.fight(hero2)
