import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        foundHero = False
        # loop thru each hero in list
        for hero in self.heroes:
            # if found remove from list
            if hero.name == name:
                print(name, hero.name)
                self.heroes.remove(hero)
                foundHero = True

        if not foundHero:
            return 0

    def view_all_heroes(self):
        # loop over list, print names to terminal
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name, kd))

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            current_hero = random.choice(living_heroes)
            current_opponent = random.choice(living_opponents)

            print("")
            current_hero.fight(current_opponent)

            if not current_hero.is_alive() and not current_opponent.is_alive():
                living_heroes.remove(current_hero)
                living_opponents.remove(current_opponent)
            elif not current_hero.is_alive():
                living_heroes.remove(current_hero)
            elif not current_opponent.is_alive():
                living_opponents.remove(current_opponent)
            else:
                living_heroes.remove(current_hero)
                living_opponents.remove(current_opponent)
