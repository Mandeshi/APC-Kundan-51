books = {
    1: ["Python", "ABC", True],
    2: ["Java", "XYZ", True]
}

while True:

    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Available Books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        id = int(input("Book ID: "))
        title = input("Title: ")
        author = input("Author: ")

        books[id] = [title, author, True]

    elif choice == 2:

        id = int(input("Book ID: "))

        if id in books:
            print(books[id])
        else:
            print("Book not found")

    elif choice == 3:

        id = int(input("Book ID: "))

        if id in books and books[id][2]:
            books[id][2] = False
            print("Book issued")
        else:
            print("Book unavailable")

    elif choice == 4:

        id = int(input("Book ID: "))

        if id in books:
            books[id][2] = True
            print("Book returned")

    elif choice == 5:

        for id in books:
            if books[id][2]:
                print(id, books[id])

    elif choice == 6:
        break