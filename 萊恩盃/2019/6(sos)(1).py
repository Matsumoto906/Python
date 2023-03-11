s=list(input())
num=[]
n=[]
for i in s:
    if i not in n:
        n.append(i)

for i in n:
    num.append(s.count(i))

for i in range(0,len(num)):
    print(num[i],n[i],sep='',end='')
    