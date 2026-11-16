weight = float(input("Enter the weight: "))
unit = input("kilogram or pound (K 0r P)")

if unit == "K":
    weight = weight * 2.205
    symbol = "kgs"
    print(f"{weight} {symbol}")
elif unit =="L":
    weight = weight/2.205
    symbol = "lbs"
    print(f"{weight} {symbol}")
else:
    print("The entered unit is not valid")

