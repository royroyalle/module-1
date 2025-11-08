print ("\n Welcome to RK Travel Agencies! Please pick one type of transpot in the following")
print ("\n Bike")
print ("\n Car")
ans = input("Select your choice")
if ans == 'Bike':
    print("What type of bike transpot do you want?")
    print("\n Scooter")
    print("\n Cruiser")
elif ans == 'Car':
    print("What type of Car transpot do you want?")
    print("\n XUV")
    print("\n Sedan")
ans2 = input("Enter")
if ans2 == 'Scooter' or 'Cruiser':
    print("Alright", ans2, "is ordered")
else:
    print("Invaild")

if ans2 == 'XUV' or 'Sedan':
    print("Alright", ans2, "is ordered")

else:
    print("Invalid")