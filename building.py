
def price_Building():
    p1=int(input("provide price per m^2: "))
    tf=int(input("pls provide the total number of floors: "))
    sum=0
    for i in range(1,tf+1):
        pb=int(input("enter area of floor number " +str(i) +":"))
        sum+=pb 
    print(sum)
    price=p1*sum 
    return price
print(price_Building())
        
