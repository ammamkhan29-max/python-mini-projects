import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

print("===== ROCK PAPER SCISSORS =====")
print("Type rock, paper, scissors, or quit.")

while True:
    user = input("\nYour choice: ").strip().lower()
    if user == "quit":
        break
    if user not in choices:
        print("Invalid choice.")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round.")
        computer_score += 1

    print(f"Score — You: {user_score} | Computer: {computer_score}")

print(f"\nFinal score — You: {user_score} | Computer: {computer_score}")
print("Thanks for playing!")
