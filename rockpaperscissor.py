import random
print("What do u choose? type 0 for rock, 1 for paper or 2 for scissors")
human_user_input = int(input())
computer_choice_list= [0,1,2]
computer_choice = random.choice(computer_choice_list)
print("computer chose : " + str(computer_choice))
if(computer_choice== human_user_input):
    print("Its a draw! nobody loses")
elif (human_user_input == 0 ):
    if(computer_choice==1):
        print("computer wins, you lose")
    elif(computer_choice==2):
        print("you win ! computer loses") 
elif(human_user_input== 1):
    if(computer_choice == 2):
        print("computer wins, you lose")
    elif(computer_choice==0):
        print("you win ! computer loses")
elif(human_user_input == 2):
    if(computer_choice==1):
        print("you win ! computer loses") 
    elif(computer_choice==0):
        print("computer wins, you lose")
else:
    print("enter valid no")
