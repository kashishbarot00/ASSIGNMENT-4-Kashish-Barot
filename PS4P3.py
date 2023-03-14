#input
meal_total = float(input("Enter the total for the meal: "))

#process 
tip_15 = meal_total * 0.15
total_15 = meal_total + tip_15

tip_18 = meal_total * 0.18
total_18 = meal_total + tip_18

tip_20 = meal_total * 0.20
total_20 = meal_total + tip_20

#output
print("With 15% Tip:")
print("Total:                 ", format(meal_total, ".2f"))
print("Tip:                    ", format(tip_15, ".2f"))
print("Total with Tip:  ", format(total_15, ".2f"), "\n")

print("With 18% Tip:")
print("Total:                 ", format(meal_total, ".2f"))
print("Tip:                    ", format(tip_18, ".2f"))
print("Total with Tip:  ", format(total_18, ".2f"), "\n")

print("With 20% Tip:")
print("Total:                 ", format(meal_total, ".2f"))
print("Tip:                    ", format(tip_20, ".2f"))
print("Total with Tip:  ", format(total_20, ".2f"))
