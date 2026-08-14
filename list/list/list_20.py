books = ["Python Basics", "Data Structures", "Algorithms"]

books.append("Machine Learning")

search = input("Enter book name to search: ")
if search in books:
    print("Book found")
else:
    print("Book not found")

books.remove("Algorithms")

print("All books:", books)
print("Total books =", len(books))