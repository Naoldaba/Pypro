
def add_er():
    n=[]
    list=input("enter numbers").split(",")
    n.extend(list)
    num=len(n)
    print(n)
    for i in range(num):
        if i<num-1:
            print(int(n[i])*int(n[i+1]))

        else:
            print(int(n[0])*int(n[i]))
add_er()









