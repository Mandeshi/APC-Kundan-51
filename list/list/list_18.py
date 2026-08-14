cart = []

cart.append("Milk")
cart.append("Bread")
cart.append("Toast")

cart.remove("Bread")

item = "Milk"
if item in cart:
    print(item, "found in cart")

print("Cart:", cart)
print("Total items =", len(cart))