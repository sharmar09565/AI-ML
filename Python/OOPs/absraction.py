#  Abstraction:-hiding internal details and showing only essential features.
# Data hiding means defining access level of data. i.e data is private, protected or public.
# whereas abstraction means data hiding + showing only essential features

# Abstract classes:- blueprint of other classes. We don't create any object of these classes. We import it from abc module.
# module means the code written by another programmer and we directly use it by importing

from abc import ABC

class Animal(ABC):      # abstract class
    @classmethod
    def make_sound(self):   #abstract method- this method only declaring the func is parent class/abstract class and implementing it in the child class
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")


d = Dog()
d.make_sound()

c = Cat()
c.make_sound()