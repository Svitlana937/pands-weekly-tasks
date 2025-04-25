import random

# Generate a random number between 0 and 100
random_number = random.randint(0, 100)

while True:
    guess = int(input("Guess the number (0-100) or enter -1 to exit: "))

    if guess == -1:
        print(f"You exited the game. The correct number was {random_number}.")
        break  # Exit the loop

    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number correctly. 🎉")
        break  # Exit the loop after a correct guess