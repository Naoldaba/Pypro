
""""
NAME- NAOL DABA
ID- UGR/4777/14
Question num-12
"""
while True:
    def tRIANGLE():
        print(" "*12 + "Triangle Constructor")
        row=int(input("Enter number of rows. Number must be between 1 and 10: "))
        if row>=1 and row<=10:
            for m in range(row):
                for n in range(row-m-1):
                    print(end=" ")
                for n in range(m+1):
                    print("*", end=" ")
                print()
        else:
            print("Pls enter a number between 1 and 10.")
    tRIANGLE()
    repeat=input("would you like to perform another operation? \n ('r' for repeat, 'q' to quit): ")
    if repeat.lower()=="r":
        continue
    elif repeat.lower()=="q":
        break
    else:
        print("invalid!")
        quit()




