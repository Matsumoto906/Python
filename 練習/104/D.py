def gcd(x,y):
    a=max(x,y)
    b=min(x,y)
    if a%b==0:
        return b
    else:
        return gcd(a%b,b)
def f(x):
    for i in range(1,x+1):
        if x%i==0:
            num.append(i)

for t in range(int(input())):
    s=list(map(int,input().split(',')))
    num=[]
    f(gcd(max(s),min(s)))
    num.reverse()
    for i in num:
        key=True
        for j in s:
            if j%i!=0:
                key=False
                break
        if key==True:
            print(i)
            break