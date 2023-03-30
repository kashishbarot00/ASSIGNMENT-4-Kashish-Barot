qty = int(input("Enter the quantity of widgets: "))

if qty > 10000:
    price = 10
elif qty >= 5000 and qty <= 10000:
    price = 20
else:
    price = 30

extended_price = qty * price
tax_amount = 0.07 * extended_price
total = extended_price + tax_amount

print("Extended Price: ", extended_price)
print("Tax Amount: ", tax_amount)
print("Total: ", total)
