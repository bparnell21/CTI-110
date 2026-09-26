# Beverly Parnell
# September 25, 2026
# P2HW2
# This program collects six module grades from the user and calculates the average

# Pseudocode :
# 1. Ask the user to enter six module grades
# 2. Store the six grades in a python list
# 3. Find the lowest grade in the list
# 4. Find the highest grade in the list
# 5. Calculate the sum of all six grades
# 6. Calculate the average of thegrades
# 7. Display the results in the required format

# Ask the user to enter grades for each module
module1 = float(input("Enter grade for module 1: "))
module2 = float(input("Enter grade for module 2: "))
module3 = float(input("Enter grade for module 3: "))
module4 = float(input("Enter grade for module 4: "))
module5 = float(input("Enter grade for module 5: "))
module6 = float(input("Enter grade for module 6: "))

# Store all six grades in a list
module_grades = [module1, module2, module3, module4, module5, module6]

# Calculate the lowest and highest grades
lowest_grade = min(module_grades)
highest_grade = max(module_grades)

# Calculate the sum and average of the grades
sum_grades = sum(module_grades)
average_grade = sum_grades / len(module_grades)

# Display the results
print()
print("---------------Results---------------")
print(f"Lowest grade:   {lowest_grade:.1f}")
print(f"Highest grade:  {highest_grade:.1f}")
print(f"Sum of grades:  {sum_grades:.1f}")
print(f"Average grade:  {average_grade:.2f}")
print("-----------------------------------")