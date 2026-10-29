n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity

    if amount >= 1000:
        discount = 100
    else:
        discount = 0

    tax = amount * 0.05
    bill = amount + tax - discount

    print("product bill:", bill)

    total = total + bill

print("total bill:", total)