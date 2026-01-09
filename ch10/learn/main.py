"""
Make a class with no contents and print it. Then, create an object called example
"""
class Nothing:
    pass

print(Nothing)
# Create the object
example = Nothing()
print(example)

"""
<class '__main__.Nothing'>
<__main__.Nothing object at 0x100b3a120>
"""

"""
Make a new class and assign a value to a class attribute letters. Print letters.
"""

class Nothing2:
    letters = 'ajnasdkjsandjksandjksn'

print(Nothing2.letters)

"""
Make another class, assign the value 'xyz' to an instance variable called letters.
"""

class Nothing3:
    def __init__(self):
        self.letters = 'xyz'

random = Nothing3()
print(random.letters)
