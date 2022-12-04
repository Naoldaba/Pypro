
""""
NAME- NAOL DABA
ID- UGR/4777/14
Question num-2
"""
while True:
    pi = 3.1415
    print(" " * 8 + "Welcome to volume calculator.")
    figure = input("Pls select shape of the solid figure: {prism, sphere, cone} \n  ")
    li = ["prism", "cone", "sphere"]
    def vol_calc():
        if figure.lower() in li:
            if figure.lower()=="prism":
                w=float(input("enter the width: "))
                l=float(input("enter the length: "))
                h=float(input("enter the height: "))
                return "volume = " + str(float(1/3*(w*l*h))) +" cubic units."
            elif figure.lower()=="cone":
                r = float(input("enter the base radius: "))
                h = float(input("enter the height: "))
                return "volume = " + str(float(1/3*(pi*r**2*h))) + " cubic units."
            elif figure.lower()=="sphere":
                r = float(input("enter the radius: "))
                return "volume = " + str(float(4/3*(pi*r**3))) + " cubic units."
        else:
            print("invalid!")
            quit()
    print(vol_calc())
    repeat=input("would you like to perform another operation? \n ('r' for repeat, 'q' to quit): ")
    if repeat.lower()=="r":
        continue
    elif repeat.lower()=="q":
        break
    else:
        print("invalid!")
        quit()

