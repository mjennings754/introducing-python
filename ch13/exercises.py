"""
13.1 Write the current date as a string to the text file today.txt.
"""
from datetime import date
now = date.today()
now_str = now.isoformat()
with open('today.txt', 'wt') as output:
    print(now_str, file=output)

"""
13.2 Read the text file today.txt into the string today_string.
"""
with open('today.txt', 'rt') as input:
    today_string = input.read()

print(today_string)
"""
13.4 Create a date object of your day of birth.
"""
my_day = date(1988, 2, 19)

"""
13.5 What day of the week was your day of birth?
"""
print(my_day.weekday())

"""
13.6 When will you be (or when were you) 10,000 days old?
"""
from datetime import timedelta
party = my_day + timedelta(days=10000)
print(party)