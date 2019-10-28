# Python has to guess what datatypes a variable should be

# Since the input function return a string, the variable it populates will hold string type
first_num = input('enter first num')
last_num = input('enter last num')

# Because first_num and last_num are string variable the + operator can concatenates them just
#like concatenating first_name and last_name.
print(first_num + last_num)
