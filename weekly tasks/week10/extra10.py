def sqrt(number):
    # Start with a guess - any positive number will work
    guess = number / 2.0
    
    # Keep improving the guess until it's close enough
    # We'll stop when the difference is very small
    while abs(guess * guess - number) > 0.00001:
        # Improve the guess
        guess = (guess + number / guess) / 2.0

    return guess

# Ask the user for input
user_input = input("Enter a positive number: ")
number = float(user_input)

# Call our function and print the result
result = sqrt(number)
print("Approximate square root:", result)
