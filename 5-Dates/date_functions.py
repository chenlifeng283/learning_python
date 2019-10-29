# To get current date and time you need to use the datetime library
from datetime import datetiem, timedelta

# The now function returns the current date and time
today = datetime.now()

print('Today is:' + str(today))
# You can use timedelta add or remove days, or weeks to a date
one_day = timedelta(days=1)
yestoday = today - one_day
print('Yestoday was:' + str(yestoday))

one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was:' + str(last_week))
