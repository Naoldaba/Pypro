#recieving z entries
jj="r"
while jj.lower()=="r":
    li=[]
    for i in range(1,4):
        print("insert row",i,":",end="")
        ip=list(map(int,input().split(",")))
        li.append(ip)
    #recieving the constants
    print("enter the constants(if any)")
    nope=list(map(int,input().split(",")))
    print("YOUR AUGMENTED MATRIX IS: ")
    p=-1
    for j in li:
        p+=1
        for m in j:
            print(f'{m:>5}',end=" ")
        print("|",nope[p])
    new=sum(li,[])
    print('''What did u wanna know dude??? 
           a)determinant
           b)inverse
           c)adjoint 
           d)solution ''',"\n")
    np=input("=>")
    #determinant
    def determ():
        fr1=new[0]*new[4]*new[8]
        fr2=new[1]*new[5]*new[6]
        fr3=new[2]*new[3]*new[7]
        ba1=new[6]*new[4]*new[2]
        ba2=new[5]*new[7]*new[0]
        ba3=new[8]*new[3]*new[1]
        global dt
        dt=(fr1+fr2+fr3)-(ba1+ba2+ba3)
        print("Determinant=",dt)

    #Adjoint
    def adjoint():
        print("Adjoint:")
        print(f'{new[4]*new[8]-(new[7]*new[5]):>5}' ,end=" ")
        print(f'{new[7]*new[2]-(new[1]*new[8]):>5}' ,end=" ")
        print(f'{new[1]*new[5]-(new[4]*new[2]):>5}' ,end=" ")
        print()
        print(f'{new[5]*new[6]-(new[8]*new[3]):>5}' ,end=" ")
        print(f'{new[8]*new[0]-(new[2]*new[6]):>5}' ,end=" ")
        print(f'{new[2]*new[3]-(new[5]*new[0]):>5}' ,end=" ")
        print()
        print(f'{new[3]*new[7]-(new[6]*new[4]):>5}' ,end=" ")
        print(f'{new[6]*new[1]-(new[0]*new[7]):>5}' ,end=" ")
        print(f'{new[0]*new[4]-(new[3]*new[1]):>5}' ,end=" ")
        print()

    #inverse
    inverto=[]
    def inverse():
        if dt!=0:
            print("inverse:")
            print(f'{round((new[4]*new[8]-(new[7]*new[5]))/dt,2):>5}' ,end=" ")
            inverto.append(round((new[4]*new[8]-(new[7]*new[5]))/dt,2))
            print(f'{round((new[7]*new[2]-(new[1]*new[8]))/dt,2):>5}' ,end=" ")
            inverto.append(round((new[7]*new[2]-(new[1]*new[8]))/dt,2))
            print(f'{round((new[1]*new[5]-(new[4]*new[2]))/dt,2):>5}' ,end=" ")
            inverto.append(round((new[1]*new[5]-(new[4]*new[2]))/dt,2))
            print()
            print(f'{round((new[5]*new[6]-(new[8]*new[3]))/dt,2):>5}' ,end=" ")
            inverto.append(round((new[5]*new[6]-(new[8]*new[3]))/dt,2))
            print(f'{round((new[8]*new[0]-(new[2]*new[6]))/dt,2):>5}' ,end=" ")
            inverto.append(round((new[8]*new[0]-(new[2]*new[6]))/dt,2))
            print(f'{round((new[2]*new[3]-(new[5]*new[0]))/dt,2):>5}' ,end=" ")
            inverto.append(round((new[2]*new[3]-(new[5]*new[0]))/dt,2))
            print()
            print(f'{round((new[3]*new[7]-(new[6]*new[4]))/dt,2):>5}' ,end=" ")
            inverto.append(round((new[3]*new[7]-(new[6]*new[4]))/dt,2))
            print(f'{round((new[6]*new[1]-(new[0]*new[7]))/dt,2):>5}' ,end=" ")
            inverto.append(round((new[6]*new[1]-(new[0]*new[7]))/dt,2))
            print(f'{round((new[0]*new[4]-(new[3]*new[1]))/dt,2):>5}')
            inverto.append(round((new[0]*new[4]-(new[3]*new[1]))/dt,2))
        else:
            print("Doesn't have inverse")
    sir1=[0,1,2]
    sir2=[3,4,5]
    sir3=[6,7,8]
    ss=[]
    x=0
    y=0
    z=0
    def solution():
        if dt!=0:
            global x, y, z
            for l in range(9):
                if l in sir1:
                    x+=inverto[l]*nope[l]
                elif l in sir2:
                    y+=inverto[l]*nope[l-3]
                elif l in sir3:
                    z+=inverto[l]*nope[l-6]
            ss.append(x)
            ss.append(y)
            ss.append(z)
            print("The solutions are",ss)
        else:
            print("Sorry this technique is not applicable for a matrix with ZERO determinant")
    if np.lower()=="determinant":
        determ()
    elif np.lower()=="adjoint":
        adjoint()
    elif np.lower()=="inverse":
        determ()
        inverse()
    elif np.lower()=="solution":
        determ()
        inverse()
        solution()
    jj=input('''DO YOU WANNA PERFORM ANOTHER OPERATION?? 
  PRESS 'Q' FOR QUIT AND 'R FOR REPEAT ''')