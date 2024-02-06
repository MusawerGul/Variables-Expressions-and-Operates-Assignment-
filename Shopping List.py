'''2. Shopping List: Write a program to manage a shopping list. Use variables to store item names, quantities, and prices. Calculate the total cost of items and check if you have enough budget.'''

item_names = []
quantities = []
prices = []
for i in range(3):
    item=input('Enter Item Name:')
    quantity=int(input('Enter Quantity:'))
    price=int(input('Enter Price:'))
    item_names.append(item)
    quantities.append(quantity)
    prices.append(price)
    
total_cost=sum([quantity * price for             quantity, price in zip(quantities, prices)])
print('Total Cost is:',total_cost)

budget =int(input('Enter your budget:'))  
if total_cost <= budget:
    print("You have enough budget to buy all the items!")
else:
    print("Oops! You don't have enough budget to buy all the items.")
