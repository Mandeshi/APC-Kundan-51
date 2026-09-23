class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        units = self.units
        if units <= 100:
            bill = units * 2
        elif units <= 300:
            bill = 100 * 2 + (units - 100) * 3
        else:
            bill = 100 * 2 + 200 * 3 + (units - 300) * 5
        return bill

    def display(self):
        print(f"Consumer No: {self.consumer_no}, Name: {self.consumer_name}")
        print(f"Units: {self.units}, Bill: {self.calculate_bill()}")


consumer_no = input("Enter consumer number: ")
consumer_name = input("Enter consumer name: ")
units = float(input("Enter units consumed: "))

e1 = ElectricityBill(consumer_no, consumer_name, units)
e1.display()
