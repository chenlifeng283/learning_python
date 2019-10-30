# Calculate the tax
# Anything purchased for more than $1.00 is charged a 7% tax 
price = input('How much did you pay?')

# Convert the string to a number
price = float(price)

# Check if the price is greater than 1.00
if price >= 1.00:
    tax = 0.07
    print('The tax is:' + str(tax))
