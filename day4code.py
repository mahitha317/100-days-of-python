#who will pay the bill program using the random module 
import random
friends = ["Alice","Bob","Charlie","David","Emaneul"]
print(random.choice(friends))
i = random.randint(0,len(friends)-1)
print(friends[i])
# two methods to do it !

#nested lists 
odd_no = [1,3,5,7,9]
even_no = [0,2,4,6,8,10]
lists_no = [odd_no,even_no] # seperated within a list
print(lists_no)