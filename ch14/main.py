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

fout = open('relativity', 'wt')
print(poem, file=fout)
fout.close()

fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
len(poem)

poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment

fin.close()
len(poem)

bdata = bytes(range(0,256))
print(len(bdata))

fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()

fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk
fout.close()

fin = open('bfile', 'rb')
bdata = fin.read()
len(bdata)
fin.close()

import os
os.path.exists('oops.txt')

name = 'oops.text'
os.path.isfile(name)

os.path.isdir(name)

os.path.isabs(name)
os.path.isabs('/big/fake/name')
os.path.isabs('big/fake/name/without/a/leading/slash')

import shutil
shutil.copy('oops.txt', 'ohno.txt')

import os
os.chdir('poems')
os.listdir('.')

os.path.abspath('oops.txt')
