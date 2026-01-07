# create with str()
a = str(98.6)
print(type(a))

# combine using +
b = 'Release the kraken ' + 'No, wait!'
print(b)

# duplicate with *
start = 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)

# Get a character with []

letters = 'abcdefghijklmnopqrstuvwxyz'
letters[0]
letters[-1]
print(letters[::-1])

# Get a substring with slice
alpha = 'abcdefghijklmnopqrstuvwxyz'
print(alpha[:])
print(alpha[20:])
print(alpha[10:])
print(alpha[21:5])

# Get length with len()

print(len(alpha))

# Split with split()

tasks = 'get gloves,get mask,give dog vitamins,call ambulance'
print(tasks.split(','))

# Combine by using join()

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)

# Substitute by using replace()

setup = 'a duck goes into a bar...'
print(setup.replace('duck', 'marmoset'))

# Strip with strip()
world = '        earth.    '
print(world.strip())
print(world.strip(' '))
print(world.lstrip())
print(world.rstrip())

# Alignment
print(setup.center(30))

# Left justify
print(setup.ljust(30))

# Right justify
print(setup.rjust(30))

# formatting
thing = 'woodchuck'
print({thing})