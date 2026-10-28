# Beverly Parnell
# P4HW2
# 10/27/2026
# This program calculates regular, overtime, and gross pay for employees

# Set all pay totals to zero
# Set employee count to zero
# Ask the user to enter employee name
# While employee name is not "Done"
# Ask how many hours the employee worked
# Ask for the employee's pay rate
# If hours worked is greater than 40
# Calculate overtime hours
# Calculate overtime pay at 1.5 times the pay rate
# Calculate regular pay for 40 hours
# Else
# Set overtime hours and pay to zero
# Calculate regular pay
# Calculate gross pay
# Add employee pay to all totals
# Add one to employee count
# Display employee information
# Ask for another employee name
# Display total employees and total pay amounts


# Set starting totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Ask for employee name
employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# Use a while loop for multiple employees
while employee_name != "Done":

    # Ask for hours worked and pay rate    hours_worked
    hours_worked = float(input('Enter hours worked: '))
    pay_rate = float(input(f"what is {employee_name}'s pay rate? "))

    # Calculate overtime and regular pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        regular_pay = 40 * pay_rate

    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay

    # Add employee pay to totals
    total_overtime_pay = total_overtime_pay + overtime_pay
    total_regular_pay = total_regular_pay + regular_pay
    total_gross_pay = total_gross_pay + gross_pay

# Count employees
    employee_count = employee_count + 1

    # Display employee information
    print()
    print("Employee name:", employee_name)
    print()
    print("Hours Worked Pay Rate OverTime OverTime Pay RegHour Pay Gross Pay")
    print("------------------------------------------------------------------")
    print(f"{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}" 
          f"{overtime_pay:<14.2f}${regular_pay:<13.2f}${gross_pay:.2f}")
    print()

    # Ask for another employee
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

    # Display final totals
print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid for gross pay: ${total_gross_pay:.2f}")