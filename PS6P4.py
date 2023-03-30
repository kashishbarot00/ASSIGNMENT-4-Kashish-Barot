numtickets = int(input("Enter the number of tickets: "))

if numtickets >= 25:
    price = 50
elif numtickets >= 10:
    price = 60
elif numtickets >= 5:
    price = 70
else:
    price = 75

total = numtickets * price

print("Number of Tickets: ", numtickets)
print("Price Per Ticket: ", price)
print("Total Cost: ", total)
