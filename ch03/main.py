# Nonzero numbers are considered True:
print(bool(True))
print(bool(1))
print(bool(45))
print(bool(-45))

# Zero-valued ones are considered False:
print(bool(False))
print(bool(0))
print(bool(0.0))

# You can't have an initial 0 followed by a digit between 1 and 9:
# print(05)
"""
    print(05)
           ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
"""

# Use underscore for digit separation

million = 1_000_000
print(million)

# Addition and Subtraction
a = 5 + 9
print(a)
b = 100 - 7
print(b)
c = 4 - 10
print(c)

# Multiplication and Division
d = 6 * 7
print(d)
e = 9 / 5
print(e)

# Precedence (Multiplication has higher precendence than addition)
f = 2 + 3 * 4
print(f)

# Bases
# Base 2
print(0b10)
# Base 8
print(0o10)
# Base 16
print(0x10)

# Type Conversion
int(True)
int('99')

# How big is an int?

googol = 10**100
print(googol)

# Floats
print(5.)

print(5.0)

print(05.0)

print(5e0)

# Reassign a value to a variable
a = 95
temp = a - 3
a = temp
