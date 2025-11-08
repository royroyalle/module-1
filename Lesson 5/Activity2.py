ac = float(input("Please enter the cost of the object"))
sale = float(input("Please enter the price your selling for"))

if (sale > ac):
    amount = sale - ac 
    print("Total Profit = {0}".format(amount))
else:
    print("The object you sold has put you in a loss")