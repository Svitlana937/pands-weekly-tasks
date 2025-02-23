# program that reads in two numbers and
# divides x by y and give the integer result and the reminder
# outputs the integer answer and remainder
x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

# Perform division
answer = x // y
remainder = x % y

# Display result
print(f"{x} divided by {y} is {answer} with a remainder of {remainder}".format(x, y, answer, remainder))
