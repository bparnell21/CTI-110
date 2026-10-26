# Beverly Parnell
# October 26, 2026
# P4LAB2
# This program displays a multiplication table using a for loop


# Start Program
# Set run again 
run_again = "yes"

# While run again 
while run_again == "yes":

# Ask user to enter number                                  
    num = int(input("Enter a number: "))

# If number is 0 or greater
    if num >= 0:

# For numbers 1 through 12
        for i in range(1, 13):

# Multiply the number
            answer = num * i

 # Display the result
            print(num, "*", i, "=", answer)

    # Else: 
    else: 

# Display message for negative numbers
                print("This program does not support negative numbers.")

# Ask user if they want to run the program again
    run_again = input("Do you want to run the program again? (yes/no): ")

# Display exit message
    print("Exiting the program.")

# End Program