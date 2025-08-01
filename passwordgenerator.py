import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#input from users
number_of_letters = int(input("How many letters would you like in your password?"))
number_of_symbols = int(input("How many symbols would you like in your password?"))
number_of_numbers = int(input("How many numbers would you like in your password?"))
# creating an empty list to store all of it 
empty_list = []
#appending random elements to empty list
for i in range(0,number_of_letters):
    empty_list.append(random.choice(letters))
for i in range(0,number_of_symbols):
    empty_list.append(random.choice(symbols))
for i in range(0,number_of_numbers):
    empty_list.append(random.choice(numbers))

print(empty_list)
random.shuffle(empty_list)
print(empty_list)

final_password = ""
for i in empty_list:
    final_password += i

print("Your password is: " +final_password)

