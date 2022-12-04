

p=74
while p!=1:
    print(p,end=", ")
    if p%2==0:
        p=p//2
    elif p%2==1:
        p=3*p+1
    print(p,end="\n")