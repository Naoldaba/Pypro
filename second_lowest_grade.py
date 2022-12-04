nm = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    nm.append([name,score])
print(nm)
rr=[]
for i in range(len(nm)):
    jj=nm[i][1]
    rr.append(jj)
rr.sort()
Min=min(rr)
mm=""
for j in rr:
    if j!=Min:
       mm=j
       break
gh=[]
for p in range(len(nm)):
    if mm==nm[p][1]:
       gh.append(nm[p][0])
gh.sort()
for b in gh:
    print(b)