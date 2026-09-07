import random

computer = random.choice([1,0,-1])
x=input("enter your choice :")
youdict = {"s": 1, "p": 0 , "sc":-1}
compdict ={1:"stone", 0:"paper",-1:"scissor"}
you = youdict[x]

print(f"computer choosed {compdict[computer]} and you choosed {compdict[you]}")

if computer == you:
    print("Draw")

else:
    if(computer == 1 and you== 0):
        print("you win")
    elif(computer == 1 and you == -1):
        print("computer wins")
    elif(computer==0 and you==1):
        print("computer win")
    elif(computer==0 and you==-1):
        print("you win")
    elif(computer==-1 and you==1):
        print("you win")
    elif(computer==-1 and you==0):
        print("computer win")
    else:
        print("wrong choice")