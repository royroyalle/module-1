<<<<<<< HEAD
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
=======
text = str(input("Enter a string:"))
reverse = text [::-1]
text = reverse
print("Reversed form of the given string is")
print(text)
>>>>>>> 8f1b109adba34f91e7dad24f8cf80fed553c57bc
