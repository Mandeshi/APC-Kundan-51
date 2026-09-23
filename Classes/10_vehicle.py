class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate, available=True):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = available

    def rent_vehicle(self, days):
        if self.available:
            self.available = False
            charges = self.rental_rate * days
            print(f"Vehicle {self.vehicle_no} rented for {days} days. Charges: {charges}")
            return charges
        else:
            print("Vehicle not available")
            return 0

    def return_vehicle(self):
        self.available = True
        print(f"Vehicle {self.vehicle_no} returned")


vehicle_no = input("Enter vehicle number: ")
model = input("Enter model: ")
rental_rate = float(input("Enter rental rate per day: "))

v1 = Vehicle(vehicle_no, model, rental_rate)

days = int(input("Enter number of rental days: "))
v1.rent_vehicle(days)
v1.return_vehicle()
