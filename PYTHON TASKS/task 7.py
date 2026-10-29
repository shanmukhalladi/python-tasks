attended = int(input("Enter attended classes: "))
total = int(input("Enter total classes: "))
target = int(input("Enter required attendance: "))

percentage = attended / total * 100
print("current attendance:", percentage)

if percentage >= target:
    print("eligible")
else:
    extra = 0
    while percentage < target:
        attended = attended + 1
        total = total + 1
        extra = extra + 1
        percentage = attended / total * 100

    print("minimum extra classes required:", extra)