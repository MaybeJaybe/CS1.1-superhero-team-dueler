import random
from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team

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
    
    def add_weapon(self, weapon):
        # append weapon object passed as argument to self.abilities
        self.abilities.append(weapon)

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

    def is_alive(self):
        # check current health of hero, if <=0, return false, otherwise return true
        if self.current_health > 0:
            return True
        else: 
            return False

    def fight(self, opponent):
        print(f"{self.name} has these abilities:")
        for a in self.abilities:
            print(a.name)

        print(f"{opponent.name} has these abilities:")
        for a in opponent.abilities:
            print(a.name)
        # check if any heroes have abilities. if no hero has abilities, print draw
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("The battle is a draw, neither hero is able to attack.")
            return
        # else, start fighting loop until hero has won
        # while loop for this til someone dies
        while self.is_alive() and opponent.is_alive():
            # must attack and take damage from each other's attacks.
            self_damage = self.attack()
            opponent_damage = opponent.attack()

            print(self.current_health)
            print(opponent.current_health)

            print("Self Attacked Opponent")
            opponent.take_damage(self_damage)
            print("damage dealt to opponent")
            print(self_damage)
            print("opponent health")
            print(opponent.current_health)

            print(self.is_alive())
            print(opponent.is_alive())

            print("Opponent Attacked Self")
            self.take_damage(opponent_damage)
            print("damage dealt to self")
            print(opponent_damage)
            print("self health")
            print(self.current_health)

            print(self.is_alive())
            print(opponent.is_alive())

            print("----------------")

            # after each attack, check if self or opponent is alive
            # if one died, print "hero name won!"
            if not self.is_alive() and not opponent.is_alive():
                print("Stalemate, both heroes died from their wounds.")

            elif not self.is_alive():
                print(f"{opponent.name} won with {opponent.current_health} hp left.")

            elif not opponent.is_alive():
                print(f"{self.name} won with {self.current_health} hp left.")




        # hero_list = [self.name, opponent.name]
        # print(random.choice(hero_list) + " won the fight!")
        # while loop to continue attack til someone dies
        # if loop to check if any heroes have abilities. if none print draw



if __name__ == "__main__":

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Ground Breaker", 20)
    ability2 = Ability("Light Beam", 80)
    ability3 = Ability("Stupefy", 80)
    ability4 = Ability("Wingardium Leviosa", 20)
    weapon1 = Weapon("Lasso of Truth", 15)
    weapon2 = Weapon("Wand", 15)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.add_weapon(weapon1)
    hero2.add_weapon(weapon2)
    # hero_list.add_hero(hero1)
    # print(view_all_heroes)
    # print(hero1.attack())
    # print(hero2.attack())
    hero1.fight(hero2)



    # hero = Hero("Grace Hopper", 200)

    # ability1 = Ability("Great Debugging", 50)
    # hero.add_ability(ability1)
    # ability2 = Ability("Hopper Smash", 20)
    # hero.add_ability(ability2)

    # armor1 = Armor("Cloak of Shadows", 50)
    # hero.add_armor(armor1)


    # print(hero.current_health)
    # hero.take_damage(50)
    # print(hero.current_health)
    # print(hero.is_alive())
    # print("180 damage")
    # hero.take_damage(180)
    # print(hero.current_health)
    # print(hero.is_alive())
    
    # print(hero.attack())
    # print(hero.defend())

    # print(hero.name)
    # print(hero.current_health)
    # print(hero.abilities)


    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")

    # hero1.fight(hero2)
