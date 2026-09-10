# Name: Maderazo, Marshal Reign A.
# Section: BAET 2102
# Task 1 - Change Calculator

amount = int(input("Enter amount in pesos: "))

hundreds = amount // 100
remaining = amount % 100

twenties = remaining // 20
remaining = remaining % 20

fives = remaining // 5
remaining = remaining % 5

ones = remaining

print("100 pesos:", hundreds)
print("20 pesos:", twenties)
print("5 pesos:", fives)
print("1 peso:", ones)
