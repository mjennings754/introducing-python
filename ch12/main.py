snowman = '\u2603'
ds = snowman.encode('utf-8')
print(len(ds))
print(ds)

place = 'caf\u00e9'
print(place)
print(type(place))

# HTML Entities
import html
html.unescape("&egrave;")
