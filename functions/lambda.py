"""
Anonymous Functions: lambda
A Python lambda function is an anonymous function expressed as a single
statement. You can use it instead of a normal tiny function.
"""

def send_item(items, func):
    for item in items:
        print(func(item))

products = ["down Jacket", "t-shirt", "merino Sweater", "denim Jeans"]

def capitalize(item):
    return item.capitalize()

#send_item(products, capitalize)


# Anonymous function
send_item(products, lambda item: item.capitalize())