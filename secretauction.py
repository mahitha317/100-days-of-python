print("Welcome to the secret auction program ")
# empty dictonary 
dict = {}
name = input("What is your name?: ")
bidamount = int(input("enter bid amount:$ "))
dict.update({name:bidamount})


user_desc = True 
while(user_desc):
    print("Are there any other bidders? Type 'yes' or 'no'\n")
    value = input()
    if(value.lower()=="yes"):
        print("\n"*100)
        name = input("What is your name?: ")
        bidamount = int(input("enter bid amount:$ "))
        dict.update({name:bidamount})
    else:
        break
maxbid =0
winner =""
for key in dict:
   bidvalue = dict[key]
   
   if maxbid < bidvalue:
        maxbid = bidvalue
        winner = key

print(f"The winner is {winner} with a bid of ${maxbid}")

