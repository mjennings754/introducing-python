# Objects

# Classes

class Dog():
    pass

a_dog = Dog()

print(a_dog)

a_dog.age = 4
a_dog.name = "Harry"
a_dog.nemesis = "Thunder"

# Methods

class Dog:
    def __init__(self, name):
        self.name = name

animal = Dog('Harry')

print("Our latest addition: ", animal.name)

# Inheritance

class Car():
    pass

class Yugo(Car):
    pass

print(issubclass(Yugo, Car))

# Create an object from each class
give_me_a_car = Car()
give_me_a_yugo = Yugo()

class Car():
    def exclaim(self):
        print("I'm a car!")

class Yugo(Car):
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()

# Override a method

class Car():
    def exclaim(self):
        print("I'm a car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yuog-ish")

give_me_a_car = Car()
give_me_a_yugo = Yugo()
