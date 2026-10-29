entry = int(input("Enter entry hour (0-23): "))
exit = int(input("Enter exit hour (0-23): "))

if entry < 0 or entry > 23 or exit < 0 or exit > 23:
    print("invalid time")
elif exit < entry:
    print("overnight parking")
    hours = 24 - entry + exit
    fee = hours * 20
    if fee > 200:
        fee = 200
    print("parking fee:", fee)
else:
    hours = exit - entry
    fee = hours * 20

    if fee > 200:
        fee = 200

    print("parking fee:", fee)