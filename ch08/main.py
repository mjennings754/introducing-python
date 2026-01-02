# Dictionaries

# Create with {}

empty_dict = {}
print(empty_dict)

# Create with dict()

acme_customer = {'first': 'Wile', 'middle':'E', 'last': 'Coyote'}
print(acme_customer)

# Using dict()

acme_customer2 = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer2)

# Convert with dict()

lol = [ [ 'a', 'b'], ['c', 'd'], ['e', 'f'] ]
print(dict(lol))

# Add or change an item by [ key ]

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael'
    }
pythons['Gilliam'] = 'Terry'
print(pythons)

# Get an item by [key] or with get()

print(pythons['Cleese'])

print(pythons.get('Cleese'))

# Get all keys with keys()

signals = {'green': 'go', 'yellow': 'slow down', 'red': 'stop'}
print(signals.keys())

# You can use list() to turn the results into normal python lists
print(list(signals.keys()))

# Get all values with values()
print(list(signals.values()))

# Combine dictionaries with {**a, **b}
first = {'a':'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
print({**first, **second})

# Delete all items with clear

pythons.clear()
print(pythons)

# copy with copy()

original_signals = signals.copy()
"""
This is a shallow copy, and works if the dictionary values are immutable
"""

print(original_signals)

# iterate with for and in
accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
              'person': 'Col. Mustard'}
for card in accusation:
    print(card)

# To iterate over the values rather than the keys, you use the dictionary's values() function:
for value in accusation.values():
    print(value)

# To return both the key and value as a tuple, use items()
for item in accusation.items():
    print(item)

# Sets

empty_set = set()
print(empty_set)
even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)

# Convery with set()
print(set( 'letters' ))

# when you give set() a dictionary, it uses only the keys
print(set({'apple': 'red', 'orange':'orange', 'cherry': 'red'}))

# Add an item with add()
s = set((1,2,3))
s.add(4)
print(s)

# Iterate with for and in
furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)

# Set comprehensions
a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)

# Create an immutable set with frozenset()

frozenset([3,2,1])