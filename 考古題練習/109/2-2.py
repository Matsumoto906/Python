num=[2,3]
def g(x):
    key=True
    for i in range(0,len(num)):
        if x%num[i]==0:
            key=False
            break
    return key
for i in range(10,10001):
    if g(i)==True:
        num.append(i)
num.remove(2)
num.remove(3)
def f(x):
    if x in num:
        ans.clear()
        ans.append(-1)
        return ans
    if x==1:
        return ans
    for i in range(9,0,-1):
        if x%i==0:
            ans.append(i)
            break

    return f(x//i)


for j in range(0,int(input())):
    s=int(input())
    ans=[]
    
    f(s)
    for i in ans:
        s//=i

    ans.sort()
    for i in ans:
        print(i,end='')
    print()