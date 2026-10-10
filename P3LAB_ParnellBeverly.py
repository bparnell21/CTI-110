# Beverly Parnell
# Octoberr 10, 2026
# P3LAB
# This program calculates the fewest number of bills and coins needed for a given amount of money

# Ask the user for the amount of money
amount = float(input("Enter the amount of money as a float: $"))

# Convert the amount to the whole cents
cents = int(round(amount * 100))

#   Calculate dollars and subtract their value
dollars = cents // 100
cents = cents - dollars * 100

# Calculate quarters and subtract their value
quarters = cents // 25
cents = cents - quarters * 25

# Calculate dimes and subtract their value
dimes = cents // 10
cents = cents - dimes * 10

# Calculate nickels and subtract their value
nickles = cents // 5
cents = cents - nickles * 5

# The remaining cents are the pennies
pennies = cents

# If the anount  is zero, display "No change"
if amount == 0:
    print("No change")

# Display dollars if needed, using singular or plural
if dollars > 0:
    if dollars == 1:
        print("1 Dollar")
    else:
        print(dollars, "Dollars")

# Display quarters if needed, using singular or plural
if quarters > 0:
    if quarters == 1:
        print("1 Quarter")
    else:
        print(quarters, "Quarters")

# Display dimes if needed, using singular or plural
if dimes > 0:
    if dimes == 1:
        print("1 Dime")
    else:
        print(dimes, "Dimes")

# Display nickels if needed, using singular or plural
if nickles > 0:
    if nickles == 1:
        print("1 Nickel")
    else:
        print(nickles, "Nickels")

# Display pennies if needed, using singular or plural
if pennies > 0:
    if pennies == 1:
        print("1 Penny")
    else:
        print(pennies, "Pennies")

