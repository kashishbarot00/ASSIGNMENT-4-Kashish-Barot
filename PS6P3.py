principle = float(input("Enter principle amount of CD: "))
maturity = int(input("Enter years to maturity of CD: "))

if principle > 100000 and maturity == 5:
    interest_rate = 0.06
elif principle >= 50000 and principle <= 100000 and maturity == 10:
    interest_rate = 0.05
elif principle >= 50000 and principle <= 100000 and maturity == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02

interest = principle * interest_rate

print("Principle: ", principle)
print("Interest Rate: ", interest_rate*100)
print("Interest for First Year: ", interest)
