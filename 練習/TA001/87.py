a,b=map(int,input().split())
a=bin(a)[2:].zfill(20)
b=bin(b)[2:].zfill(20)
ans=0
print(a)
print(b)
for i in range(0,len(a)):
    if a[i]!=b[i]:
        ans+=1
print(ans)