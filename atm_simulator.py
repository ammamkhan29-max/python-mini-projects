balance = 5000.0
correct_pin = "1234"

print("===== ATM SIMULATOR =====")
pin = input("Enter your 4-digit PIN: ")

if pin == correct_pin:
    while True:
        print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Change PIN\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Current balance: Rs. {balance:.2f}")
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount (Rs.): "))
                if amount > 0:
                    balance += amount
                    print("Deposit successful.")
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Please enter a valid amount.")
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount (Rs.): "))
                if 0 < amount <= balance:
                    balance -= amount
                    print("Withdrawal successful.")
                else:
                    print("Invalid amount or insufficient balance.")
            except ValueError:
                print("Please enter a valid amount.")
        elif choice == "4":
            new_pin = input("Enter a new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                correct_pin = new_pin
                print("PIN changed for this session.")
            else:
                print("PIN must contain exactly 4 digits.")
        elif choice == "5":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option.")
else:
    print("Incorrect PIN.")
