#input
fixed_costs = float(input("Enter the fixed costs of your business: "))
priceper_unit = float(input("Enter the price per unit of your product: "))
costper_unit = float(input("Enter the cost per unit of your product: "))

#process
breakeven_point = fixed_costs / (priceper_unit - costper_unit)

#output
print("To break even, you must sell", breakeven_point, "units of your product.")
