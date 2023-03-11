s=input().split()
n=''
ans=[[],[],[],[],[],[],[],[],[]]
for i in range(0,len(s)):
    a=int(s[i][-1])-1
    ans[a]=s[i][0:-1]
for i in ans:
    if i != []:
        n+=i+' '
n=n.strip()
print(n)