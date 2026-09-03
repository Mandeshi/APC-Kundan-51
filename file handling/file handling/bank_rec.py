f = open("transactions.txt", "r")

deposit = 0
withdrawal = 0
largest = 0

for line in f:

    type, amount = line.strip().split(",")

    amount = int(amount)

    if type == "Deposit":
        deposit += amount
    else:
        withdrawal += amount

    if amount > largest:
        largest = amount

f.close()

balance = deposit - withdrawal

print("Total Deposit:", deposit)
print("Total Withdrawal:", withdrawal)
print("Final Balance:", balance)
print("Largest Transaction:", largest)