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
        # super() will get Person() definition
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

# Getter and Setters

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

don = Duck('Donald')
print(don.get_name())
don.set_name('Donna')
print(don.get_name())

# Properties for Attribute Access

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

don = Duck('Donald')
print(don.name)
don.name = 'Donna'
print(don.name)

# Properties for Computed Values
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
    
# Static methods
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')


# Class and Object Attributes
class Fruit:
    color = 'red'

blueberry = Fruit()
Fruit.color
blueberry.color

blueberry.color = 'blue'

# Class methods

class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects")

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()

# Static methods

class CoyoteWeapon():
    @staticmethod
    def commercial():
        print("This CoyoteWeapon has been brought to you by Acme")

CoyoteWeapon.commercial()

# Duck Typing
class Quote():
     def __init__(self, person, words):
         self.person = person
         self.words = words
     def who(self):
         return self.person
     def says(self):
         return self.words + '.'
         
class QuestionQuote(Quote):
     def says(self):
         return self.words + '?'
              
class ExclamationQuote(Quote):
     def says(self):
         return self.words + '!'
     
hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())
