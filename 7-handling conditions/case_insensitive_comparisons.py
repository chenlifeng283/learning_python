country = 'CANADA'
# by converting the string entered to lowercase and comparing it to a string
# that is all lowercase letters I make the case-insensitive
# If someone types CANADA  or Canada it will still be match
if country.lower() == 'canada':
    print('hello en')
else:
    print('hello')
    
