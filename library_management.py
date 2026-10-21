books = []

while True:
    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Add book\n2. View books\n3. Borrow book\n4. Return book\n5. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        title = input("Book title: ").strip()
        if title:
            books.append({"title": title, "available": True})
            print("Book added.")
        else:
            print("Title cannot be empty.")
    elif choice == "2":
        if not books:
            print("No books in the library.")
        for i, book in enumerate(books, start=1):
            status = "Available" if book["available"] else "Borrowed"
            print(f"{i}. {book['title']} - {status}")
    elif choice in ("3", "4"):
        title = input("Book title: ").strip().casefold()
        book = next((b for b in books if b["title"].casefold() == title), None)
        if book is None:
            print("Book not found.")
        elif choice == "3":
            if book["available"]:
                book["available"] = False
                print("Book borrowed.")
            else:
                print("That book is already borrowed.")
        else:
            if not book["available"]:
                book["available"] = True
                print("Book returned.")
            else:
                print("That book was not borrowed.")
    elif choice == "5":
        break
    else:
        print("Invalid option.")
