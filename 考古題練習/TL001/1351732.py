ans=0
num=0
s=list(map(int,input().split()))
for i in s:
    num+=i
    if num>ans:
        ans=num
print(ans)