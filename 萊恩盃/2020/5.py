import itertools

def f(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        key=True
    else:
        key=False
    return key

input()
ans=0
num=list(map(int,input().split()))
a = list(itertools.permutations(num, r=3))
ans=0
for i in a:
    x=max(i)
    y=min(i)
    for j in i:
        if j !=x and j!=y:
            z=j
    if f(i[0],i[1],i[2]) == True and abs(180-x-z)>=y:
        if i[0]>90 or i[1]>90 or i[2]>90:
            if sum(i)>ans:
                ans=sum(i)
                
print(ans)