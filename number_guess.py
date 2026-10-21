import random

secret_number = random.randint(1, 100)
attempts = 0

print("===== NUMBER GUESSING GAME =====")
print("Guess a number from 1 to 100.")

while True:
    try:
        guess = int(input("Your guess: "))
        if not 1 <= guess <= 100:
            print("Choose a number between 1 and 100.")
            continue
        attempts += 1

        if guess < secret_number:
            print("Too low. Try again!")
        elif guess > secret_number:
            print("Too high. Try again!")
        else:
            print(f"Correct! You won in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a whole number.")
