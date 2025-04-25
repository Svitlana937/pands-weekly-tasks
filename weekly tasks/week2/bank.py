# Ask the user to input each amount in cents
amount1 = input("Enter amount1(in cent): ")
amount2 = input("Enter amount2(in cent): ")

# Convert both inputs from strings to integers and add them together
sum = int(amount1) + int(amount2)

print(f'The sum of these is \N{euro sign} {sum/100}')
