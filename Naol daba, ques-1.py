
""""
NAME- NAOL DABA
ID- UGR/4777/14
Question num-1
"""
while True:
    print(" " * 12 + "Simple calculator")
    a = float(input("enter your number: "))
    c = input("choose operator: {+,-,%,*,/,^}: ")
    b = float(input("enter your number: "))
    def calculator():
        if c=="+":
            return str(a) + " + " + str(b) + " = " + str(a+b)
        elif c=="*":
            return str(a) + " * " + str(b) + " = " + str(a*b)
        elif c=="/":
            if b!=0:
               return str(a) + " / " + str(b) + " = " + str(a/b)
            else:
                return "can't divide by 0"
        elif c=="%":
            return str(a) + " % " + str(b) + " = " + str(a%b)
        elif c=="-":
            return str(a) + " - " + str(b) + " = " + str(a-b)
        elif c=="^":
            return str(a)+" ^ "+str(b)+" = " + str(a**b)
        else:
            return "invalid operator!!"
    print(calculator())
    repeat=input("would you like to perform another operation? \n ('r' for repeat, 'q' to quit): ")
    if repeat.lower()=="r":
        continue
    elif repeat.lower()=="q":
        break
    else:
        print("invalid!")
        quit()



