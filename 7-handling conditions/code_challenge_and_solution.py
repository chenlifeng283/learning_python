# Fix the mistakes in this code and test based on the description below
# if I enter 2.00 I should see the message "The tax rate is: 0.07"
# if I enter 1.00 I should see the message "The tax rate is :0.07"
# if I enter 0.5 I should see the message "The tax rate is: 0"

price = input('How much did you pay?')
price = float(price) # Converting the string to a mumber

if price >= 1.00:
    tax = 0.07
    print('The tax rate is:' + str(tax))
else:  # Do not forget the ':'
    tax = 0
    print('The tax rate is:' +str(tax))
    
