# Name: Maderazo, Marshal Reign A.
# Section: BAET 2102
# Task 4 - Temperature Check

celsius = float(input("Enter temperature in °C: "))

fahrenheit = celsius * 9 / 5 + 32
between = celsius >= 20 and celsius <= 30

print("Fahrenheit:", fahrenheit)
print("Between 20 and 30 °C:", between)