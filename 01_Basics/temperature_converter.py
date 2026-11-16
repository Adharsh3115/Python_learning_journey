
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit of the temperature (C/F):")

if unit =="C":
    temp = (temp * 9) / 5 + 32
    print(f"The temperature in farenheit is {round(temp,1)}°F")

elif unit == "F":
    temp = (temp-32)*5/9
    print(f"The temperature in celcius is{round(temp,1)}°C")


else:
    print(f"{unit} is not a valid unit")

