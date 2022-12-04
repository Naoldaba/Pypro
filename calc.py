
def maV_ric():
    while True:
        x=int(input("enter number: "))
        y=int(input("enter another number: "))
        o=input("enter operation: ")
        if o=="/":
           print(x/y)
        elif o=="+":
           print(x+y)
        elif o=="-":
            print(x-y)
        elif o=="*":
            print(x*y)
        elif o=="%":
            print(x%y)
        elif o=="//":
            print(x//y)
        else:
            print("invalid")
maV_ric()
