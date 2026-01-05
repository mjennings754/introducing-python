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


# Add a method

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")
    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push()

# Get help from your parent with super()

class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

# Multiple inheritance

class Animal:
    def says(self):
        return 'I speak!'
    
class Horse(Animal):
    def says(self):
        return 'Neigh!'
    
class Donkey(Animal):
    def says(self):
        return 'Hee-haw!'
    
class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass

mule = Mule()
hinny = Hinny()
print(Mule.mro())
print(mule.says())

# Mixins

class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))

class Thing(PrettyMixin):
    pass
t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"

t.dump()

# Direct Access

class Duck:
    def __init__(self, input_name):
        self.name = input_name

fowl = Duck('Daffy')
print(fowl.name)