# print today's date
from datetime import datetime, timedelta
current_date = datetime.now()
print(current_date)

# print yestoday's date
one_day = timedelta(days=1)
yestoday = current_date - one_day
print('Yestoday was:' + str(yestoday))

# ask a user to enter a date
date_entered = input('enter a date(dd/mm/yyyy)?')
date_entered = datetime.strptime(date_entered,'%d%m%Y')

# print the date one week from the date entered
one_week = timedelta(weeks=1)
one_week_later = current_date + one_week
print('one week later it will be:' + str(one_week_later))
