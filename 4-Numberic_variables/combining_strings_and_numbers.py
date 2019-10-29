days_in_feb=28

# The print function can accept numbers or strings
print(days_in_feb)

# The + operator can either add two numbers or it can concatenates two strings
# it does not know what to do when you pass it one number and one string
# This line of code will cause an error
print(days_in_feb + 'days in february')

# You need convert the number to a string to display the value
# This line of code will work
print(str(days_in_feb) + 'days in february')
