class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print(f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Disease: {self.disease}")

    def total_bill(self, medicine_cost=0):
        return self.consultation_fee + medicine_cost


patient_id = input("Enter patient ID: ")
name = input("Enter patient name: ")
age = int(input("Enter age: "))
disease = input("Enter disease: ")
consultation_fee = float(input("Enter consultation fee: "))

p1 = Patient(patient_id, name, age, disease, consultation_fee)
p1.display()

medicine_cost = float(input("Enter medicine cost: "))
print("Total Bill:", p1.total_bill(medicine_cost))
