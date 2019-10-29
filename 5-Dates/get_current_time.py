# To get current time we need to  use the datetime library.
from datetime import datetime

current_date = datetime.now()
# the now function return the current date and time as a datetime object


# You must convert datetime object to a string
# before you can concatelate it to another string 
print('Today is:', + str(current_date))

# Why the converted string has decimal places? 
