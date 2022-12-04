

def airplane(n,a,h):
    if a<=15:
        print("you are not allowed to sit in the window seat. pls take either the middle seat or aisle seat or middle seat.")

    elif a>=20 and h>=165:
        print("you are allowed to sit near the exit door or in the middle seat.")

    elif a>=15 or a<=60:
        print("you are allowed to sit in next to the exit door or in the middle seat,")

    elif a<=15 or a>=60:
        print("you are allowed to sit in the aisle seat.")

airplane(input("Enter name: "), int(input("Enter your age: ")), int(input("Enter your height (cm): ")))
