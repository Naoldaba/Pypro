
print("Hello, Welcome to this quick astronomy quiz!")
race=input("Do you wanna play? ")
if race.lower() != "yes":
    print("fuck off!!!!!")
    quit()
print("well let go!\n Good luck!\n")
quiz=input(("Q1. What is the name of the planet nicknamed 'The hell planet'? " ))
score=0
if quiz.lower() == "venus":
    print("correct! you nailed it.")
    score+=1
else:
    print("incorrect!")
quiz=input("Q2. Which planet in our solarsystem is referred as 'The guardian planet'?" )
if quiz.lower() =="jupiter":
    print("hurahhh! you got it!")
    score+=1
else:
    print("sorry that's incorrect.")
quiz=input("Q3. Which moon of saturn has an ice covered surface?" )
if quiz.lower() == "enceladus":
    print("Correct. u seem unstoppable, ")
    score+=1
else:
    print("incorrect. How dumb could u be?")
quiz=input("Q4. What is the closest exo-planet to earth?" )
if quiz.lower() == "proxima b":
    print("incredible. that's correct")
    score+=1
else:
    print("U better die")
quiz=input("Q5. What is the celestial body known to currently have liquid on its surface other than earth?" )
if quiz.lower()=="titan":
    print("INDEED. YOU ARE GENIUS!")
    score+=1

else:
    print("how r u still alive??? pls go kill ur self.")
print("congratulations you scored " + str((score/5)*100) + "%")
print("Correct Answer")
print("Q1. venus")
print("Q2. jupiter")
print("Q3. enceladus")
print("Q4. proxima b")
print("Q5. titan")




