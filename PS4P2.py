#input
purchase_price = float(input("Enter purchase price per share:"))
current_price = float(input("Enter current price per share:"))
quantity = int(input("Enter quantity of stock:"))

#process
value_change = (current_price - purchase_price) * quantity

#output 
print("Increase (or decrease) in value of stock: $", value_change)
