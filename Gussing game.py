import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("Welcome to the Number Guessing Game!")
print(f"You have {max_attempts} attempts to guess the number between 1 and 100.")

# Initialize a variable to control the game loop
guessed_correctly = False

while attempts < max_attempts and not guessed_correctly:
    try:
        # Ask the user for their guess
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        # Check the user's guess
        if user_guess == number_to_guess:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Check if the user ran out of attempts
if not guessed_correctly:
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}. Better luck next time!")
