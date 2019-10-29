# To get current date we need to use the datetime library
from datetime import datetime, timedelta

# The now function returns current date and time
today=datetime.now()

# Use day, month, year, hour, minute, second functions
# to display only part of the date
# All there functions return a integer
# convert them to string before concatenating them to  another string
print('Day:' + str(today.day))
print('Month:' + str(today.month))
print('Year:' + str(today.year))

print('hour:' + str(today.hour))
print('minute:' + str(today.minute))
print('Second:' + str(today.second))
