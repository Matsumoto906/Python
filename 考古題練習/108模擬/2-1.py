def f(x):
    ans=0
    x=str(x)
    for i in x:
        ans+=int(i)
    ans+=int(x)
    return ans

for t in range(int(input())):
    s=int(input())
    k=0
    for i in range(1,999999):
        if f(i)==s:
            print(i)
            k=1
            break
    if k==0:
        print(0)
        