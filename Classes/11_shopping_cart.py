class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []   # list of (name, price)

    def add_product(self, name, price):
        self.products.append((name, price))
        print(f"{name} added to cart")

    def remove_product(self, name):
        for item in self.products:
            if item[0] == name:
                self.products.remove(item)
                print(f"{name} removed from cart")
                return
        print(f"{name} not found in cart")

    def total_bill(self):
        return sum(price for name, price in self.products)

    def __del__(self):
        print(f"Shopping cart {self.cart_id} for {self.customer_name} is destroyed")


customer_name = input("Enter customer name: ")
cart_id = input("Enter cart ID: ")
cart = ShoppingCart(customer_name, cart_id)

n = int(input("How many products to add? "))
for i in range(n):
    name = input(f"Enter product {i+1} name: ")
    price = float(input(f"Enter product {i+1} price: "))
    cart.add_product(name, price)

remove_item = input("Enter a product name to remove (or press Enter to skip): ")
if remove_item:
    cart.remove_product(remove_item)

print("Total Bill:", cart.total_bill())

del cart   
