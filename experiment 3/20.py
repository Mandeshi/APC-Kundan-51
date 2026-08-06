books = ["Python", "Java", "C++"]

books.append("HTML")

search = "Python"

if search in books:
    print("Book Found")

books.remove("Java")

print("Books:", books)
print("Total Books:", len(books))