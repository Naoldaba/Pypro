

""""
NAME- NAOL DABA
ID- UGR/4777/14
Question num- 9
"""
while True:
    def bi_deci():
        print(" "*12 + "Binary to Decimal Converter")
        binary=int(input("Enter the binary number: "))
        sum, i= 0, 0
        while binary!=0:         # Using the doubling method
            if binary % 10 == 1:
                k=2**i
                sum+=k
                binary//=10
                i+=1
            elif binary % 10 == 0:
                binary//=10
                i+=1
                continue
            else:
                print("Pls enter a valid entry")
                quit()
        print(sum)
    bi_deci()
    repeat=input("would you like to perform another operation? \n ('r' for repeat, 'q' to quit): ")
    if repeat.lower()=="r":
        continue
    elif repeat.lower()=="q":
        break
    else:
        print("invalid!")
        quit()


