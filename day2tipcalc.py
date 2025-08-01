print("welcome to the tip calculator!")
price = float(input("what was the total bill? "))
tip = float(input("How much tip would you like to give? 10,12,or 15?"))
splitbill = float(input("how many people to split the bill?"))
total = (price + (tip*0.01*price))/splitbill
print("Each person should pay: $" + str(total))