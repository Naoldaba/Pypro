
def xomishag(n):
    yu=0
    for i in reversed(range(1,n+1)):
        for j in range(1,n+1):
            if j<=i:
               op=i*(j**i)
               yu+=op
            else:
                break 
    return yu
print(xomishag(int(input("Enter your number: "))))









