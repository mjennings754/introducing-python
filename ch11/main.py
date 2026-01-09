import itertools

for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

# Print nicely with pprint()
from pprint import pprint
quotes = OrderedDict([
    ('Moe', 'A wise gy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
    ])

