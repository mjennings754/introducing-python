"""
12.1 Create a Unicode string called mystery and assign it the value
'\U0001f984'. Print mystery and its Unicode name.
"""
import unicodedata
mystery = '\U0001f984'
print(mystery)
print(unicodedata.name(mystery))

"""
12.2 Encode mystery, this time using UTF-8, into the bytes variable
popbytes. Print pop_bytes.
"""
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

"""
12.3 Using UTF-8, decode popbytes into the string variable pop_
string. Print pop_string. Is pop_string equal to mystery?
"""
pop_string = pop_bytes.decode('utf-8')
print(pop_string)
print(pop_string == mystery)