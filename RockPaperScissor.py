
import random
pp=0;cp=0
def getWinner(pc,cc):
    if(pc=="Rock" and cc=="Paper"):
        return 'C'
    elif(pc=="Rock" and cc=="Scissor"):
        return 'P'
    elif(pc=="Paper" and cc=="Rock"):
        return 'P'
    elif(pc=="Paper" and cc=="Scissor"):
        return 'C'
    elif(pc=="Scissor" and cc=="Rock"):
        return 'C'
    elif(pc=="Scissor" and cc=="Paper"):
        return 'P'
    else:
        return 'D'

print("Rock_Paper_Scissor Game:\n")
max=int(input("enter max points:"))
print("enter 1 for Rock,2 for Paper , 3 for Scissor:\n")
item=["Rock","Paper","Scissor"]

s=input("Press 's' to start:")
while(s!="s"):
    s=input("Press 's' to start:")
while(pp!=max and cp!=max):
    try:
        pc=item[int(input("enter choice:"))-1]
    except IndexError:
        print("Invalid Choice...! ")
        continue

    cc=item[random.randint(0,2)]
    print("You:",pc," Computer:",cc)
    if(getWinner(pc,cc)=='C'):
        cp+=1
    elif(getWinner(pc,cc)=='P'):
        pp+=1
    else:
        print("Draw!")

    print("Your Score:",pp,"\nComputer's Score:",cp,"\n")
    if(pp==max):
       print("You Win!!!")
    elif(cp==max):
       print("Computer Wins...")
       

