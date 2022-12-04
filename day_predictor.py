



def day_add():
    magic=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",]
    dof = input("What is the day today? ")
    nof = int(input("Enter number of days after: "))
    for n in range(1000):
        c=7*n
        ui = magic.index(dof) + nof
        if ui==c:
            return "Sunday"
        elif ui==c+1:
            return "Monday"
        elif ui==c+2:
            return "Tuesday"
        elif ui==c+3:
            return "Wednesday"
        elif ui==c+4:
             return "Thursday"
        elif ui==c+5:
            return "Friday"
        elif ui==c+6:
            return "Saturday"
print(day_add())









