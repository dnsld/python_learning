datetime_library.py

from datetime import datetime
now = datetime.now()
print now


from datetime import datetime
now = datetime.now()

print '%02d-%02d-%04d' % (now.month, now.day, now.year)
# will print the current date as mm-dd-yyyy



from datetime import datetime
now = datetime.now()

print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
## 05/10/2018 02:47:10