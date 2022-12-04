

def maV_ric():
    start=int(input("pls enter a starting number: "))
    end=int(input("pls enter the ending number: "))

    total_sum=0
    for _ in range(start,end+1):
        total_sum+=_
    print(total_sum)
maV_ric()