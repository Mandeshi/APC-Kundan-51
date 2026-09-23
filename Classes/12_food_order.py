class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self, tax_percent=5):
        amount = self.quantity * self.price
        tax = amount * tax_percent / 100
        return amount + tax

    def __del__(self):
        print(f"Order {self.order_id} for {self.customer_name} completed")


order_id = input("Enter order ID: ")
customer_name = input("Enter customer name: ")
food_item = input("Enter food item: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

order = FoodOrder(order_id, customer_name, food_item, quantity, price)

tax_percent = float(input("Enter tax percent: "))
print("Total Bill (with tax):", order.total_bill(tax_percent))

del order   
