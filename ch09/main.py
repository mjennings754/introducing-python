# FUNCTIONS

def do_nothing():
    pass

# Call a function with parentheses

do_nothing()

def make_a_sound():
    print('quack')

make_a_sound()

def agree():
    return True

if agree():
    print("Splendid!")
else:
    print('That was unexpected.')

# Arguments and parameters

def echo(anything):
    return anything + ' ' + anything

print(echo('Testing'))

def commentary(color):
    if color == 'red':
        return "It's a tomato"
    elif color == "green":
        return "It's a green pepper"
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it"
    else:
        return "I've never heard of the color " + color + "."
    
comment = commentary('blue')

print(comment)

# Positional Arguments

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken', 'cake'))

# Keyword arguments

print(menu(entree="beef", dessert="bagel", wine="bordeaux"))

# Specify default parameter values

def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chicken'))

# Explode/Gather positional arguments with *

def print_args(*args):
    print('Positional tuple:', args)

print_args()
print_args(3, 2, 1, 'wait', 'uh...')

def print_more(required1, required2, *args):
    print('Need this one', required1)
    print('Need this one too:', required2)
    print('All the rest', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

# Explode/Gather positional arguments with **

def print_kwargs(**kwargs):
    print('Keyword arguments', kwargs)

print_kwargs()
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

# Keyword only arguments

def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)

data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)

print_data(data, start=4)
print_data(data, end=2)

# Mutable and Immutable arguments

outside = ['one', 'fine', 'day']

def mangle(arg):
    arg[1] = 'terrible'

print(outside)

mangle(outside)
print(outside)

# Doc strings

def echo(anything):
    'echo returns its input argument'
    return anything

# You can also do rich formatting

# Functions are first-class citizens

def answer():
    print(42)

answer()

def run_something(func):
    func()

run_something(answer)

print(type(run_something))

# Inner functions

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(4, 7))

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

print(knights('Ni!'))


# Closures

def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(type(a))
print(type(b))

print(a())
print(b())

# Anonymous Functions: lambda

def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):
    return word.capitalize() + '!'

edit_story(stairs, enliven)

edit_story(stairs, lambda word: word.capitalize() + '!')

# Generators

print(sum(range(1, 101)))

# Generator Functions
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

print(my_range)

ranger = my_range(1, 5)
print(ranger)

for x in ranger:
    print(x)

for try_again in ranger:
    print(try_again)

genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
print(genobj)

for thing in genobj:
    print(thing)

# Decorators

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)

        return result
    return new_function

def add_ints(a, b):
    return a + b

add_ints(3, 5)

cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)

@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)

cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)

# Namespaces and Scope
animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)

print('at the top level:', animal)
print_global()

# To access the global variable rather than the local one within a function, use global

animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)

print(animal)
change_and_print_global()
print(animal)

# Uses of _ and __ in names

def amazing():
    '''
    This is the amazing function.
    Want to see it again?
    '''
    print('This function is named:', amazing.__name__)
    print("And its docstring is:", amazing.__doc__)

amazing()

# Recursion

def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item

lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
flatten(lol)
print(list(flatten(lol)))

# Handle errors with try and except

short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list)-1, ' but got',
          position)
    
# Make your own exceptions

class UppercaseException(Exception):
    pass

words = ['eenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)
    