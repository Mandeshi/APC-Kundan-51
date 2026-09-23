class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specs(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Price: {self.price}")

    def price_after_discount(self, discount_percent):
        discount = self.price * discount_percent / 100
        return self.price - discount


brand = input("Enter brand: ")
model = input("Enter model: ")
storage = input("Enter storage (in GB): ")
price = float(input("Enter price: "))

m1 = MobilePhone(brand, model, storage, price)
m1.display_specs()

discount = float(input("Enter discount percent: "))
print("Price after discount:", m1.price_after_discount(discount))
