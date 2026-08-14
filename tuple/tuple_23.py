prices = (150, 200, 350, 100, 500)

total_bill = sum(prices)
average_price = total_bill / len(prices)
highest = max(prices)
lowest = min(prices)

print("Total bill =", total_bill)
print("Average price =", average_price)
print("Highest priced item =", highest)
print("Lowest priced item =", lowest)