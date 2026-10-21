contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add contact\n2. View contacts\n3. Search contact\n4. Delete contact\n5. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Name: ").strip()
        phone = input("Phone number: ").strip()
        if name and phone:
            contacts[name] = phone
            print("Contact saved.")
        else:
            print("Name and phone number cannot be empty.")
    elif choice == "2":
        if not contacts:
            print("No contacts saved.")
        else:
            for name, phone in sorted(contacts.items()):
                print(f"{name}: {phone}")
    elif choice == "3":
        name = input("Name to search: ").strip()
        phone = contacts.get(name)
        print(f"{name}: {phone}" if phone else "Contact not found.")
    elif choice == "4":
        name = input("Name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
