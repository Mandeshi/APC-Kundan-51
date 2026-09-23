class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Price: {self.price}")


books = []
for i in range(3):
    print(f"\nEnter details for book {i+1}")
    book_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    price = float(input("Price: "))
    books.append(Book(book_id, title, author, price))

print()
for book in books:
    book.display()
