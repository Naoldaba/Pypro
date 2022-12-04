
""""
NAME- NAOL DABA
ID- UGR/4777/14
Question num-7
"""

def bMI():
    print(" "*12 + "Body Mass Index calculator")
    while True:
        w=float(input("what is your weight? (in Kg): "))
        h=float(input("what is your height? (in cm): "))
        print("your BMI is " + str(w/(h/100)**2),"\n")
        repeat = input("would you like to perform another operation? \n ('r' for repeat, 'q' to quit): ")
        if repeat.lower() == "r":
            continue
        elif repeat.lower() == "q":
            break
        else:
            print("invalid!")
            quit()
bMI()


