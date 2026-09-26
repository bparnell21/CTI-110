#Beverly Parnell
#September 25, 2026
#P2LAB2 - Dictionary
#This program calculautes the Cars MPG

#Create a dictionary contain8ing vehicles and their MPG values
vehicles= {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}   

# Create a variable that holds all the dictionary keys
keys = vehicles.keys()

## Display the available vehicles
print(keys)

# Ask the user to select a vehicle
vehicle = input("Enter a vehicle to see its mpg: ")

# Display the MPG of the selected vehicle
mpg = vehicles[vehicle]
print(f"The {vehicle} gets {mpg} MPG")

# Ask the user how many miles they plan to drive
miles = float(input(f"How many miles will youdrive the {vehicle}? "))

# Calculate the gallons og gas as needed
gallons = miles / mpg

#Display the result rounded to two decimal places
print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
      
