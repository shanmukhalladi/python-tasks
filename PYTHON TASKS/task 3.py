n = int(input("Enter number of vehicles: "))
distance = int(input("Enter distance: "))
reserve = int(input("Enter reserve fuel: "))

low = 0

for i in range(n):
    mileage = int(input("Enter mileage: "))
    price = int(input("Enter fuel price: "))

    fuel = distance / mileage
    fuel = fuel + reserve
    cost = fuel * price

    print("fuel needed:", fuel)
    print("journey cost:", cost)

    if low == 0 or cost < low:
        low = cost

print("lowest cost:", low)