# Beverly Parnell
# October 10, 2026
# P3HW2
# This program calculates an employee's regular, overtime, and total pay.

# Ask the user to enter the employees name  
employee_name = input("Enter the employee's name: ")

# ask the user to enter the number of hours worked
hours_worked = float(input("Enter the number of hours worked: "))

# Ask the user to enter the employees pay rate 
pay_rate = float(input("Enter the employee's pay rate: "))

# Check if the employee worked more than 40 hours
if hours_worked > 40:

    # Calculate overtime hours
    overtime_hours = hours_worked - 40

    # Calculate overtime pay at 1.5 times the regular pay rate
    overtime_pay = overtime_hours * pay_rate * 1.5

    # Calculate reegular pay for 40 hours
    regular_pay = 40 * pay_rate

# Calculate total gross pay
gross_pay = regular_pay + overtime_pay

# Display employee's name
print("--------------------------------------")
print(f"Employee Name: {employee_name}")
print()

# Display column headers
print(f"{'Hours worked':<15}{'Pay Rate':<12}{'Overtime':<12}{'Overtime Pay':<17}{'Regular Pay':<17}{'Total Gross Pay':<12}")

# Display hours worked, pay rate, overtime, and gross pay
print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<17.2f}${regular_pay:<16.2f}${gross_pay:<.2f}")