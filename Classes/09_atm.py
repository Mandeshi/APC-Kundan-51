class ATM:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def display_details(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")


name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))
atm = ATM(name, balance)

while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Display Details\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        atm.check_balance()
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif choice == "4":
        atm.display_details()
    elif choice == "5":
        print("Thank you for using the ATM")
        break
    else:
        print("Invalid choice")
