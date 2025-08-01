print("welcome to the treasure island. your misson is to find the treasure.")
direc = input("do u wanna fo left or right")
if(direc.lower()=="right"):
    print("Game over.")
elif(direc.lower()=="left"):
    print("do u wanna swim or wait")
    x = input()
    if(x.lower()=="swim"):
        print("Game over")
    else:
        print("which door, red, blue or yellow")
        y = input()
        if(y.lower()=="red"):
            print("Game Over")
        elif(y.lower() =="blue"):
            print("Game Over.")
        elif(y.lower() =="yellow"):
            print("Game over")
        else:
            print("enter valid color")

else:
    print("enter correct value")