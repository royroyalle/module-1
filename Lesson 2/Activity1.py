num = int(input("Please enter a number whose sum you want to find"))
sum = 0

for i in range(1, num+1):
    sum = sum + i
    print("\n Sum =", sum)