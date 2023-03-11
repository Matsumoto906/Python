num=[2,3]
def f(x):                   
    key=True
    for i in range(0,len(num)):
        if x % num[i]==0:
            key=False
            break
    return key

s=int(input())
for i in range(4,s+1):
    if f(i)==True:
        num.append(i)

ans=[]
ans.append(s)
def g(x):
    a=[]
    for i in range(0,len(num)):
        for j in range(0,len(num)):
            if num[i]+num[j]==x:
                a.append(abs(num[i]-num[j]))
    n=min(a)
    ans.append(n)
    if n==0 or n==2:
        return ans
    else:
        return g(n)
g(s)
for i in ans:
    print(i,end=',')