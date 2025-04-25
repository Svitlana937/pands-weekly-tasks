while True:
    percentage = float(input("Enter your percentage (-1 to exit): "))
    
    if percentage == -1:
        print("Exiting program...")
        break  # Exit the loop when -1 is entered

    rounded_percentage = round(percentage)

    if rounded_percentage >= 70:
        print("Distinction")
    elif rounded_percentage >= 60:
        print("Merit")
    elif rounded_percentage >= 50:
        print("Pass")
    else:
        print("Fail")