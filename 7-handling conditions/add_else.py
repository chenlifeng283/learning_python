price =  input('how much did you pay?')
price = float(price)

if price >= 1.00:
    #  Anything that costs $1.00 or more is charged 7% tax
    # All statement indented are only executed  if price more than $1.00
    tax = .07
    print('Tax rate is :' + str(tax))
else:
    # Anything else we do not charge any tax
    # All statement indented are only executed if price not >= 1
    tax = 0
    print('Tax rate is :' + str(tax))
    
