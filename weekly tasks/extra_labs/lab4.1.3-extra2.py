percentage = float(input("Enter your percentage: "))
rounded_percentage = round(percentage)

if rounded_percentage >= 70:
    print("Distinction")
elif rounded_percentage >= 60:
    print("Merit")
elif rounded_percentage >= 50:
    print("Pass")
else:
    print("Fail")