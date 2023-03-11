a,b,c=map(int,input().split())
s1=max(a,b,c)
s2=min(a,b,c)
for i in (a,b,c):
    if i !=s1 and i!=s2:
        s3=i
s=input()
ans=[]
for i in s:
    if i=='C':
       ans.append(s1)
    elif i=='A':
        ans.append(s2)
    else:
        ans.append(s3)
print(ans[0],ans[1],ans[2])