fout = open('oops.txt', 'wt')
print('Oops, I created a file', file=fout)
fout.close

poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.
'''
print(len(poem))
fout = open('relativity', 'wt')
fout.write(poem)
fout.close()