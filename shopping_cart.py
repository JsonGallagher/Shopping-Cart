print("""
WELCOME TO OUR USELESS STORE!
*************************
""")

item = input('What item are you purchasing? ')
price = input(f'What is the price of the {item}? ')
numItems = input(f'How many {item}(s) are you buying? ')
subtotal = (int(numItems) * int(price))
print()
print(f'Added {numItems} {item}(s) to the shopping cart')
print(f'Subtotal: ${subtotal}')