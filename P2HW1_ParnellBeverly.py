 # Beverly Parnell
 # September 25, 2026
 # P2HW1
# This program calculates and displays travel expenses

# This program calculates and displays travel expenses
print("-------This program calculates and displays travel expenses-------")

# Ask for the user for their budget
budget = float(input("Enter budget: "))

# Ask user for their travel destination
destination = input ("Enter your travel destination: ")

# Ask user for their estimated gas expense
gas = float(input("How much do you think you will spend on gas? "))

#Ask user for their estimated accommodation expense
hotel = float(input("Approximately, how much will you need for accomodation/hotel?"))

# Ask user for their estimated food expense
food = float(input("Last, how much do you need for food? "))

# Add all expenses
total_expenses = gas + hotel + food

# Subtract total expenses from budget
remaining_balance = budget - total_expenses

# Display the results
print()
print("------------Travel Expenses------------")
print(f'{"Location:":<18}{destination}')
print(f'{"Initial Budget:":<18}${budget:.2f}')
print(f'{"Fuel:":<18}${gas:.2f}')
print(f'{"Accomodation:":<18}${hotel:.2f}')
print(f'{"Food:":<18}${food:.2f}')

print("----------------------------------------")
print()

print(f'{"Remaining Balance:":<18}${remaining_balance:.2f}')
