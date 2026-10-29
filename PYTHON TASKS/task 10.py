n = int(input("patients: "))

for i in range(n):
    c = int(input("consultation: "))
    d = int(input("diagnostic: "))
    t = int(input("treatment: "))
    total = c + d + t

    if total < 0:
        print("invalid bill")
    else:
        if total >= 5000:
            total = total * 0.9

        print("bill:", total)

        if total <= 2000:
            print("low")
        elif total <= 5000:
            print("medium")
        else:
            print("high")