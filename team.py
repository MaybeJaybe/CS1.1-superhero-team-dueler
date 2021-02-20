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