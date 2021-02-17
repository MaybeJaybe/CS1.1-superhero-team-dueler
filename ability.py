import random
# needs 
# init parameters: name:string, max_attack:int
# attack: no parameters

class Ability:
    def __init__(self, name, max_attack):
        self.name = name
        self.max_attack = max_attack

    def attack(self):
        # pick random value between 0 and max_attack
        random_value = random.randint(0, self.max_attack)
        return random_value

if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())