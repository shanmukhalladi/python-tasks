material = int(input("Enter material cost: "))
labour = int(input("Enter labour charges: "))
wastage = int(input("Enter wastage cost: "))
machine = int(input("Enter machine cost: "))
selling = int(input("Enter selling price: "))
target = int(input("Enter profit target: "))

cost = material + labour + wastage + machine
profit = selling - cost

print("total cost:", cost)
print("profit:", profit)

if profit >= target:
    print("profit target achieved")
else:
    print("profit target not achieved")