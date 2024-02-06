'''3. Recipe Calculator: Design a recipe calculator that adjusts ingredient quantities based on the number of servings. Use variables to store recipe ingredients and amounts, and write expressions to calculate adjusted quantities.'''
ingredient1 =input('Enter 1st Ingrident:')
amount1 =int(input('Enter Amount of 1st Ingrident:'))  
ingredient2 =input('Enter 2nd Ingrident:')
amount2 =int(input('Enter Amount of 2nd Ingrident:'))
ingredient3 =input('Enter 3rd Ingrident:')
amount3 =int(input('Enter Amount of 3rd Ingrident:'))

servings =int(input('Enter Number of servings:'))

adjusted_amount1 = amount1 * servings
adjusted_amount2 = amount2 * servings
adjusted_amount3 = amount3 * servings

print("Adjusted quantities for", servings, "servings:")
print(ingredient1, ":", adjusted_amount1)
print(ingredient2, ":", adjusted_amount2)
print(ingredient3, ":", adjusted_amount3)

