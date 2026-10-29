balance = 1000
n = int(input("Enter number of transactions: "))

for i in range(n):
    print("1. deposit")
    print("2. withdraw")
    choice = int(input("Enter choice: "))
    amount = int(input("Enter amount: "))

    if amount <= 0:
        print("invalid amount")
    elif choice == 1:
        balance = balance + amount
        print("deposit successful")
    elif choice == 2:
        if amount <= balance and amount <= 5000:
            balance = balance - amount
            print("withdrawal successful")
        else:
            print("transaction rejected")
    else:
        print("invalid choice")

print("final balance:", balance)