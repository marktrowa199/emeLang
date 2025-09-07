import random

print("Welcome to the number guessing game!")

# computer picks a random number between 1 and 100

secret_number = random.randint(1, 50)
attempts = 0

while True:
    guess = input("Enter your guess (1-50): ")

    #check if input is a number 
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too Low!, Try again")
    elif guess > secret_number:
        print("Too high Try again")
    else:
        print(f"Congratulations! You guessed it in {attempts} tries.")
        break