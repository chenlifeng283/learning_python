# import the datetime and timedelta moudules
from datetime import datetime, timedelta

# when you ask a user for a date tell them the desired date format.
birthday = input('When is your birthday(dd/mm/yyyy)?')

# When you convert the string containing the date into a date object
# you must specify the expected date format
# If the date is not expected format Python will raise the exception
birthday_date=datetime.strptime(birthday,'%d/%m/%Y')  
# the type of birthday_date is <class'datetime.datetime'>,such as datetime.datetime(2017,02,28,0,0)

print('Birthday' + str(birthday_date))
# Use 'str' function can output like '2017-02-28 00:00:00'.

# Because we converted the string into a date object
# We can use time and date functiong such as timedelta with the object.
one_day=timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before birthday"' + str(birthday_eve))
