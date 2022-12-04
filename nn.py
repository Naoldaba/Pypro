'''
if __name__ == '__main__':
    n = int(input())
    string=""
    for i in range(1,n+1):
        string+=str(i)
    print(string)
for i in range(1,int(input())):
    print((10**i//9)*i)
'''
'''
x = int(input("enter"))
y = int(input(""))
z = int(input(""))
n = int(input(""))
general = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i + j + k != n:
                np=i,j,k
                general.append(list(np))
print(general)
'''
'''
n=int(input())
arr=list(map(int, input().split()))
arr.reverse()
Max=max(arr)
for i in arr:
    if i!=Max:
        print(i)
        break

name=""
score=""
st_mark={}
for _ in range(int(input())):
    name, *line=input().split()
    score=list(map(float, line))
    st_mark[name]=score
sm=0
op=input()
for j in st_mark:
    if j==op:
        for i in (st_mark[op]):
            sm+=i
jj=sm/len(st_mark[op])
print(f'{jj:.2f}')
'''
"""
def fibo_seq(n):
    if n<=1:
        return n
    else:
        return fibo_seq(n-1)+fibo_seq(n-2)

inp=int(input("enter: "))
if inp<=0:
    print("enter a valid entry")
else:
    print("fibonacci sequence")
    for i in range(inp):
        print(fibo_seq(i), end=" ")

"""
'''
def palindrome(a):
    term=a
    assert type(a)==int
    new_num=0
    while a>0:
        remain=a%10
        new_num*=10
        new_num+=remain
        a=a//10
    if new_num==term:
        return True
    else:
        return False
print(palindrome(777))
'''
'''
def is_amicable():
    x=int(input("enter num: "))
    y=int(input("enter num: "))
    sum1=0
    sum2=0
    for i in range(1,x):
        if x%i==0:
           sum1+=i
    for j in range(1,y):
        if y%j==0:
           sum2+=j
    if (sum1==y) and (sum2==x):
        return True
    return False
print(is_amicable())
'''
"""
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod
def a(x, y):
    x = x + 1
    return x * y
def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square
x = 1
y = x + 1
print(c(x, y+3, x+y))
"""
"""
def palindrome():
    x=input("endet the word")
    new_str=x[::-1]
    i=0
    count=0
    while i<=len(x)-1:
        if x[i]==new_str[i]:
            count+=1
        i+=1
    if count==len(x):
        print("the word is palindrome")
    else:
        print("the word is not palindrome")
print(palindrome())
"""
"""
num=65
hj=int(input(""))
n=0
ng=""
for i in range(1,hj):
    for j in range(i):
        print(chr(97+n), end="")
        n+=1
    print()
    """
"""
#diamond
n=3
for i in range(n):
    print(" "*(n-i)+"*"*(2*i+1))
for j in range(n,-1,-1):
    print(" "*(n-j)+"*"*(2*j+1))
    
    
    #final1
count=10
def nb(count):
    for i in range(10):
        if(i%2==0) or (i%3==0):
            continue
        else:
            while (count>=i):
                print(count, "-",i,"=",count-i)
                count=int((count/2))
        print(i,"+",count,"=",count+i)
print(nb(6))

     #final2
def man(n,m):
    b=len(n)
    v=len(m)
    count=0
    for i in range(b-v+1):
        if n[i:i+v]==m:
            count+=1
    return count
print(man("abbcybbcde","bbc"))

  #final3
def mag(n):
    result=0
    for i in str(n):
        if int(i)%2==0:
            result=result*10+int(i)
    return result
print(mag(12345))
"""
"""
  #nope
man=int(input())
line=input().split(" ")
line=tuple(map(int,line))
print(line)
print(hash(line))
"""

#elif jj=="insert":
#yu.insert()

"""
class Person:
    def __init__(self,name,age,school):
        self.name=name
        self.age=age
        self.school=school
per1=Person("naol", 19, "AAU")
print(per1.name)
print(per1.age)
print(per1.school)
"""

nice=int(input())
man=input().split("  ")
t=tuple(map(int,man))
print(t)
print(hash(t))











