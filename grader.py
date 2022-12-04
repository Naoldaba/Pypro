
def _naM():
    while True:
        name=input("enter name pls: ")
        subject=input("enter subject name: ")
        score=int(input("enter score: "))
        grade=""
        if 0<=score<=100:
            if 90<=score:
                grade="A+"
            elif 83<=score:
                grade="A"
            elif 80<=score:
                grade="A-"
            elif 75<=score:
                grade="B+"
            elif 70<=score:
                grade="B"
            elif 60<=score:
                grade="C"
            elif 50<=score:
                grade="D"
            else:
                grade="invalid"
            maRk="student "+ name + " scored " + grade + " in "+subject + "."
            print(maRk)
        else:
          print("invalid")
_naM()