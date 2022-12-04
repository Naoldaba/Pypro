
""""
NAME- NAOL DABA
ID- UGR/4777/14
Question num-5
"""
while True:
    print(" " * 12 + "Quadratic equation solver")
    a = float(input("enter the value of 'a':  "))
    b = float(input("enter the value of 'b':  "))
    c = float(input("enter the value of 'c':  "))
    def solve_quadratic():
        descriminant= b**2-(4*a*c)
        if a!=0:
            if descriminant>=0:
                print("root 1 is " + str((-b+descriminant**0.5)/(2*a)))
                print("root 2 is " + str((-b-descriminant**0.5)/(2*a)))
            else:
                print("sorry your quadratic equation doesn't have a real root!!")
                quit()
        else:
            print("NOT QUADRATIC EQUATION! a=0")
    solve_quadratic()
    repeat=input("would you like to perform another operation? \n ('r' for repeat, 'q' to quit): ")
    if repeat.lower()=="r":
        continue
    elif repeat.lower()=="q":
        break
    else:
        print("invalid!")
        quit()


