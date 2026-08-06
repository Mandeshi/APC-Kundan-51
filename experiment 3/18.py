cart = ["Pen", "Book", "Pencil"]

cart.append("Eraser")
cart.remove("Pen")

item = "Book"

if item in cart:
    print("Item Found")

print("Cart:", cart)
print("Total Items:", len(cart))