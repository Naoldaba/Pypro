def xomiang():
    yu=0
    while yu<=1:
        yu+=1
        j=int(input("Enter your number: "))
        for i in range(1,10):
            hu=j*i
            print(j,"*",i ,"=",hu, end=" ")
            if hu==j*j:
                print("it is the perfect square of ", j,"\n")
            elif hu==j*j*j:
                print("it is the perfect 3rd root of ", j,"\n")
            else:
                print("\n")
xomiang()










