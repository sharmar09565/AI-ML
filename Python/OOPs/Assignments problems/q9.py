class Herbivore:
    def eat(self):
        print("Eats grass")

class Carnivore:
    def eat(self):
        print("Eats flesh")

class Omnivore:
    def eat(self):
        print("Eats both grass and flesh")

class Bear(Herbivore, Carnivore, Omnivore):
    pass

b1 = Bear()
# b1.eat()

Herbivore.eat(b1)
Carnivore.eat(b1)
Omnivore.eat(b1)