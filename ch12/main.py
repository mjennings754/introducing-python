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

# Leap Year
import calendar
calendar.isleap(1900)
calendar.isleap(1996)

# datetime
from datetime import date
halloween = date(2019, 10, 31)
print(halloween)
print(halloween.isoformat())

from datetime import date
now = date.today()
print(now)

from datetime import datetime
now = datetime.now()
print(now)

from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
print(noon_today)

# time module
import time
now = time.time()
print(now)
print(time.ctime(now))