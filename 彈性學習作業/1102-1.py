n=1
ans=0
s=int(input())
while True:
    ans+=n
    if n==s:
        break
    n+=1

print(ans)