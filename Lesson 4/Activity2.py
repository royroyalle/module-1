Amount = int(input("Enter the Amount to withdraw:"))
note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount%100)%50)//10

print("you can get-", note1 ,"notes of 100 rupees")
print("you can get-", note2 ,"notes of 50 rupees")
print("you can get-", note3 ,"notes of 10 rupees")