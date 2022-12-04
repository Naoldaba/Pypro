
def christmas(m):
    for i in range(m):
        print(" "* (m-i-1)+"*"*(2*i+1))
    for i in range(2):
        print(" "*(m-1) + "*")
christmas(int(input("how large do you want your christmas tree to be? ")))