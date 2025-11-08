mc = input("Do you have a medical cause? Please answer with a Yes or No")
at = int(input("What is your attendence for this academic year? Please refrain from going above a 100"))
if mc =='Yes':
    print("You are allowed to take the medical examination for the respective year, please check with your attendence too")
    if at>= 75:
        print("Your attendence is meeting the current requirements for the current examination")
    if mc !='Yes':
        print("Apologies. You are restricted from attending this examination")
    if at <= 75:
        print("Apologies, your attendence seems to be below 75")
else:
    print("The given information is invalid. Please run this program again")