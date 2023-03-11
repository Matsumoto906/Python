s=int(input())
ans=0
while s != 1:
    ans+=1
    if s%2==0:
        s//=2
    else:
        s-=1
print(ans+1)