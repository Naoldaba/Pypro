while True:
    print("WILL YOU BE MY GIRLFRIEND FILEE?")
    ui=input("yes or no:- ")
    if ui!="yes" and ui!="no":
        print("wrong answer**. Pls try again")
    print("")
    def happy_heart():
        for row in range(6):
            for col in range(7):
                if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
                    print("❤",end="")
                else:
                    print(" ",end="")
            print()
    def write_feeling():
        print("\n I LOVE YOU")
    if ui=="yes":
        happy_heart(),write_feeling()
    def broken_heart():
        for row in range(6):
            for col in range(7):
                if(row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
                    print("💔", end="")
                else:
                    print(" ", end="")
            print()
    def write_sad_feeling():
        print("\n 😭😭😭😭😭😭😭😭😭😭\n  ")
    if ui=="no":
        broken_heart(),write_sad_feeling()
