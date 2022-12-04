

def laB_rim():
    end=int(input("enter the last digit: "))

    total_sum1=0
    total_sum2=0
    for _ in range(1,end+1):
        if _%2==0:
            total_sum1+=_
        elif _%2==1:
            total_sum2+=_
    print(total_sum1)
    print(total_sum2)
laB_rim()