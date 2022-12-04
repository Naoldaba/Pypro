import random
user_point=0
computer_point=0
op=input("welome to rock/paper/scissor game. \n do you wanna play?\n YES/NO: ").lower()
if op!="yes":
    quit()
name=input("type your name...").upper()
options=["rock","paper","scissor"]
while True:
    user_guess=input("type rock/ paper/ scissor or Q to quit ").lower()
    if user_guess=="q":
        break
    if user_guess not in options:
        print("pls enter a valid entry.")
        continue
    ran_dom=random.randint(0,2)
    computer_pick=options[ran_dom]
    print("computer picked " + computer_pick + ".")
    if user_guess=="scissor" and computer_pick=="paper":
        print("you won!")
        user_point+=1
    elif user_guess=="paper" and computer_pick=="rock":
        print("you won!")
        user_point+=1
    elif user_guess=="rock" and computer_pick=="scissor":
        print("you won!")
        user_point+=1
    else:
        print("computer won!")
        computer_point+=1
print(name+ "you won " + str(user_point) + " times.")
print("computer won " + str(computer_point) + " times.")
print("GOOD BYE!")

