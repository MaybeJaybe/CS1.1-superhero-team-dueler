from ability import Ability
from random import randint

class Weapon(Ability):
    def attack(self):
        # use // to find half of max_damage value
        half_max = self.max_attack // 2
        random_int = randint(half_max, self.max_attack)
        # return random int between that and max_damage
        return random_int