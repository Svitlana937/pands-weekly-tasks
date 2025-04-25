# Ask the user to input a positive integer
number = int(input("Enter a positive integer: "))

# Validate input: only proceed if the number is greater than 0
while number <= 0:
    print("Please enter a number greater than 0.")
    number = int(input("Enter a positive integer: "))

# Print the starting number
print("Collatz sequence:")

# Keep running the loop until the number becomes 1
while number != 1:
    print(number)  # Output the current number

    # If the number is even, divide it by 2
    if number % 2 == 0:
        number = number // 2  # Use integer division to avoid decimals
    else:
        # If the number is odd, multiply by 3 and add 1
        number = number * 3 + 1

# Print the final number (which is always 1)
print(1)
