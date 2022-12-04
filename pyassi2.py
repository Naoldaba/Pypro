
def xomiang(m):
    sum=0
    div=0
    while m:
        m=input("enter: ")
        if m.isdigit():
            sum+=int(m)
            div+=1
        elif m=="done":
            break
        else:
            print("invalid!")
    print("Average is: ", sum/div)
xomiang(input("enter: "))






