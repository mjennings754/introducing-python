import csv
villians = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big']
]
with open('villians', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villians)


import csv
with open('villians', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villians = [row for row in cin]

print(villians)
