#Section 4.1
from datetime import datetime

#Section 4.2
from datetime import datetime

now = datetime.now()
print now

#Section 4.3
from datetime import datetime

now = datetime.now()
print now.year
print now.month
print now.day

#Section 4.4
from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.month, now.day, now.year)

#Section 4.5
from datetime import datetime
now = datetime.now()

print '%s:%s:%s' % (now.hour, now.minute, now.second)

#Section 4.6
from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
