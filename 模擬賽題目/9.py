num=[2,3]
def f(x):
    key=True
    for i in range(0,len(num)):
        if x%num[i]==0:
            key=True
            break
    return key
for i in range(4,10001):
    if f(i)==True:
        num.append(i)

s=list(map(int,input().split(',')))
k=max(s)/2
n=[]
ans=[]
a=[]
for i in range(0,1024):
    ans.append([])
for i in range(0,len(num)):
    if num[i]>k:
        k=num[i-1]
        break
for i in s:
    n.append(i%k)
for i in range(0,len(n)):
    ans[n[i]].append(s[i])
    ans[n[i]].sort()

for i in ans:
    if i!=[]:
        for j in i:
            a.append(j)
for i in a:
    if i != a[-1]:
        print(str(i)+',',end='')
    else:
        print(str(i))
