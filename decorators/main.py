"""
Decorators
Sometimes, you want to modify an existing function without changing its
source code. A common example is adding a debugging statement to see
what arguments were passed in.

A decorator is a function that takes one function as input and returns
another function.
"""

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)

def christmas_decorator(func):
    def tinsel(*args):
        print('Using function: ', func.__name__)
        print('Which branch?', args)
        result = func(*args)
        return result
    return tinsel

@christmas_decorator
def add_tinsel(a, b):
    return a + b

add_tinsel(43, 55)