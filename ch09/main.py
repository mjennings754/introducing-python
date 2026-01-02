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