# AtlantaPizza.py - a simple pizza cost calculator

# Ask the person how many pizza they want, get the number with eval()
number_of_pizzas = eval(input("how many pizzas do you want? "))

cost_per_pizza = eval(input("how much does each pizza cost? "))
subtotal= number_of_pizzas * cost_per_pizza
tax_rate = 0.08
sales_tax = subtotal* tax_rate
total = subtotal+sales_tax
print("The total cost is $",subtotal)
print("This includes $", subtotal, "for the pizza and", end=' ')
print("$", sales_tax, " in sales tax.")