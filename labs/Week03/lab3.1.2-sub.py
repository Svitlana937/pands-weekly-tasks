# Program to subtract on number from another
# input reads in a string so we need to convert it into an int
# so we can perfom mathematical operations

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))


# Perform subtraction
answer = x - y

# Display result

print(f"{x} minus {y} is {answer}".format(x, y, answer))


