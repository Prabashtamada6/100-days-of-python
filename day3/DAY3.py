print("welcome to the rollercoaster")
height= int(input("what is your height in cm"))
bill=0
if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("what is your age"))
    if age<=12:
        bill=5
        print("pay $5")
    elif age<=18:
        print("pay $7")
        bill=7
    elif age >= 45 and age <= 55:
        print("you don't have pay")
        bill=0
    else:
        print("pay $12")
        bill=12
    wants_photos= input("do you want to have a photo take? Type y for yes and n for no.")
    if wants_photos == "y":
        bill+=3

    print(f"your final bill is ${bill}")
else:
    print("you can't ride the rollercoaster")
