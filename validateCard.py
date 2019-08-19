import re

cardNumber = input('Enter credit card number: ')
validPattern = re.match(r'^([4-6]\d{3}-?)(\d{12}|(-?\d{4}){3})$', cardNumber)

print('Valid' if validPattern else 'Invalid')
