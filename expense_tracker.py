expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense\n2. View expenses\n3. Show total\n4. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Expense name: ").strip()
        try:
            amount = float(input("Amount (Rs.): "))
            if name and amount > 0:
                expenses.append({"name": name, "amount": amount})
                print("Expense added.")
            else:
                print("Enter a name and an amount greater than zero.")
        except ValueError:
            print("Please enter a valid amount.")
    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            for index, expense in enumerate(expenses, start=1):
                print(f"{index}. {expense['name']}: Rs. {expense['amount']:.2f}")
    elif choice == "3":
        total = sum(item["amount"] for item in expenses)
        print(f"Total expenses: Rs. {total:.2f}")
    elif choice == "4":
        break
    else:
        print("Invalid option.")
