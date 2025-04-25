# Start an infinite loop that will keep asking the user for input
while True:
    # Ask the user to enter a percentage, convert it to a float and If the user enters -1, the loop will exit
    percentage = float(input("Enter your percentage (-1 to exit): "))
    
    # Check if the user wants to exit
    if percentage == -1:
        print("Exiting program...")
        break  # Exit the loop when -1 is entered

    # Round the entered percentage to the nearest whole number
    rounded_percentage = round(percentage)

    # Determine the grade based on the rounded percentage
    if rounded_percentage >= 70:
        print("Distinction") # Top grade
    elif rounded_percentage >= 60:
        print("Merit") # Good grade
    elif rounded_percentage >= 50:
        print("Pass") # Minimum pass
    else:
        print("Fail") # Below passing grade
