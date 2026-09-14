# Beverly Parnell
# September, 13, 2026
#P1HW2
# This program calculates and displays travel expenses

print("-------This program calculates and displays travel expenses-------")

# Ask for the user for their budget
budget = float(input("Enter budget: "))

# Ask user for their travel destination
destination = input ("Enter your travel destination: ")

# Ask user for their estimated  gas expense
gas = float(input("How much do you think you will spend on gas? "))

#Ask user for their estimated accommodation expense
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))

# Ask user for their estimated food expense
food = float(input("Last, how much do you need for food? "))

# Add all expenses
total_expenses = gas + hotel + food

# Subtract total expenses from budget
remaining_balance = budget - total_expenses

# Display the results
print()
print("------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation:", hotel)
print("Food:", food)
print()
print("Remaining Balance:", remaining_balance)
