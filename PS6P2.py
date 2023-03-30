partno = input("Enter the part number: ")
qty = int(input("Enter the quantity: "))

if partno == "10" or partno == "55":
    unitcost = 1.00
elif partno == "99":
    unitcost = 2.00
elif partno == "80" or partno == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00
   
total = qty * unitcost

print("Part Number: ", partno)
print("Cost per Unit: ", unitcost)
print("Total Cost: ", total)
