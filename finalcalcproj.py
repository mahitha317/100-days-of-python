import os
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

calculator = {
    "+" : add ,
    "-": subtract,
    "*":multiply,
    "/":divide,
}

print("whats the first number?: ")
n1 = float(input())
print("+")
print("-")
print("*")
print("/")
print("Pick an operation: ")
operator = (input())
print("whats the second number?: ")
n2 = float(input())
final = calculator[operator](n1,n2)
print(f"{n1} {operator} {n2} = {final}")

userdesc  = True
while(userdesc):
    userinput = input(f"Type 'y' to continue calculating with {final} or type 'n' to start a new calculation or'e' to exit: ")
    if(userinput.lower()=="y"):
        print("what is the next number: ")
        n3 = float(input())
        print("+")
        print("-")
        print("*")
        print("/")
        print("Pick an operation: ")
        operator = input()
        new = calculator[operator](final,n3)
        print(f"{final} {operator} {n3} = {new}")
        final = new
    elif(userinput.lower()=="n"):
        clear_screen()
        print("whats the first number?: ")
        n1 = float(input())
        print("+")
        print("-")
        print("*")
        print("/")
        print("Pick an operation: ")
        operator = (input())
        print("whats the second number?: ")
        n2 = float(input())
        final = calculator[operator](n1,n2)
        print(f"{n1} {operator} {n2} = {final}")
    elif userinput.lower() == "e":
        print("Exiting calculator. Goodbye!")
        userdesc = False
    else:
        print("Invalid input. Please type 'y', 'n', or 'e'.")
