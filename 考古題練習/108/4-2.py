n=[]
a=0
b=0
def f(x,y):
    ans=0
    if x==a and y==b:
        ans=n[x][y]
    elif x==a and y<b:
        ans=n[x][y]+f(x,y+1)
    elif x<a and y==b:
        ans=n[x][y]+f(x+1,y)
    else:
        ans=n[x][y]+min(f(x+1,y),f(x,y+1))
    return ans

for k in range(0,int(input())):
    a=int(input())
    b=int(input())
    n.clear()
    for i in range(0,a+1):
        n.append([])
    for i in range(0,a+1):
        for j in range(0,b+1):
            n[i].append(0)
    for i in range(1,a+1):
        s=list(map(int,input().split()))
        for j in range(1,b+1):
            n[i][j]=s[j-1]
    print(f(1,1))