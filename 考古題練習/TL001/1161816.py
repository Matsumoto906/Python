s=input().split()
a=int(input())
ans=''
for i in range(0,a):
    ans+=s[i]+' '
ans=ans.strip()
print(ans)