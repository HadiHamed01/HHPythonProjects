class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammals":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "birds":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        return f"{self.species} in {self.zoo_name}: {names} \nTotal animals: {total_animals}"


zoo_name = input()
count = int(input())