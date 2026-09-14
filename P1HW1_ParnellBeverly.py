# Beverly Parnell
# September, 13, 2026
#P1HW1
# writing python code to calculate exponents

# Calculating exponents 

print("-------Calculating Exponents-------")
print()

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
result = base ** exponent
print(base, "raised to the power of", exponent, "is", result, "!!")

# Calculating addition and subtraction
print()
print("-------Addition and Subtraction-------")
print()

num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter a integer to add: "))
num3 = int(input("Enter a integer to subtract: "))

Sum_result = num1 + num2
Final_result = Sum_result - num3

print(num1, "+", num2, "-", num3, "is equal to", Final_result, "!!")
