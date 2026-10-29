venue = int(input("Enter venue cost: "))
food = int(input("Enter food cost: "))
transport = int(input("Enter transport cost: "))

total = venue + food + transport

sponsor = int(input("Enter sponsorship amount: "))
fee = int(input("Enter registration fee per person: "))

balance = total - sponsor

print("total cost:", total)
print("remaining amount:", balance)

if fee > 0 and balance > 0:
    count = balance // fee
    if balance % fee != 0:
        count = count + 1
else:
    count = 0

print("minimum registrations:", count)