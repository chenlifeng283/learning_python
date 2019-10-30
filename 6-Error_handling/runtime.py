x = 42
y = 0
try:
    print(x / y)
except ZeroDivsionError as e:
    print('Sorry, something went wrong.')
except:
    print('Something really went wrong.')
finally:
    print('This always runs on success or failure')
