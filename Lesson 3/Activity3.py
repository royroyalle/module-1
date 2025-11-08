numb = int(input("Please enter a number to check if it is an Armstrong Number"))
sum = 0
temp = numb
while temp > 0:
    digit = temp % 10
    sum += digit **3
    temp //= 10

if numb ==sum:
    print(numb, "is an Armstrong Number")
else:
    print(numb, "is not an Armstrong Number")
