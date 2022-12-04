import random
ty=input("Adios! how r u? Do u wanna Guess and win? yes/no: ")
if ty.lower()!="yes":
    print("fuck off")
    quit()
low_num=input("Type the minimum range of number..")
top_num=input("Type the maximum range of number..")

if low_num.isdigit():
    low_num=int(low_num)
    if low_num <0:
        print("enter a number that is greater than 0 next time")
        quit()
else:
    print("enter a number next time.")
if top_num.isdigit():
    top_num=int(top_num)
    if top_num <0:
        print("enter a number that is greater than 0 next time.")
else:
    print("enter a number next time.")

rand_num=random.randrange(low_num, top_num+1)
guess_num=0
while True:
    guess_num+=1
    user_guess=input("Guess the number...")
    if user_guess.isdigit:
        user_guess=int(user_guess)
    else:
        print("pls enter a number")
        continue
    if user_guess == rand_num:
        print("u got it right.")
        break
    elif user_guess < rand_num:
        print("ur guess is below the number")
    else:
        print("ur guess is above the number")
print("You got the number right in ",guess_num, "guesses." )




