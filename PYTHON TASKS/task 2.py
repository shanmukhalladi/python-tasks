n = int(input("Enter number of plans: "))
budget = int(input("Enter your budget: "))
usage = int(input("Enter required data in GB: "))

for i in range(n):
    print("Plan", i + 1)

    price = int(input("Enter plan price: "))
    data = int(input("Enter data limit in GB: "))
    validity = int(input("Enter validity in days: "))

    if data >= usage and validity >= 28 and price <= budget:
        print("eligible plan")
        print("plan price:", price)
    else:
        print("not eligible")