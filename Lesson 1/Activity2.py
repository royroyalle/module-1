u = int(input("Please enter the consumed units"))

if (u < 50):
    at = u * 2.60
    se = 25
elif (u <= 100):
    at = 130 + ((u - 50) * 5.26)
    se = 35
elif (u <= 200):
    at = 130 + 162.50 + ((u - 100) * 5.26)
else:
    at = 130 + 162.50 + 526 + ((u - 200) * 8.45)
    se = 75
total = at + se
print("\n Your electricity bill is..", total)