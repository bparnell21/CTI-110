# Beverly Parnell
# P4HW1
# 10/27/2026
# This program calculates the lowest grade and displays it along with the remaining grades


# Ask the user how many scores they want to enter
# create a empty list to store the scores
# Use a for loop to get the scores
# check if each score is between 0 and 100
# If invalid, ask the user to enter a valid score
# Add each valid score to the list
# Find and remove the lowest grade
# Calculate the average of the remaining scores
# Determine the letter grade
# Display the results

# Ask the user how many scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

# create a empty list 
score_list = []

# Use a for loop to get the scores
for i in range(num_scores):
        score = float(input(f"Enter score #{i + 1}: "))

        # Check for invalid scores
        while score < 0 or score > 100:
            print()
            print("INVALID Score entered!!!")
            print("Score should be between 0 and 100")
            score = float(input(f"Enter score #{i + 1} again: "))


        # Add valid score to the list
        score_list.append(score)

# Find the lowest score
lowest_score = min(score_list)

# Remove the lowest score
score_list.remove(lowest_score)

# Calculate the average 
average = sum(score_list) / len(score_list)

# Determine the letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Display the results
print("------------Results-------------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {score_list}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("--------------------------------")