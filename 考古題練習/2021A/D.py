s=list(map(int,input().split()))
k=input()
ans=''
for i in k:
    if i=='A':
        ans+=str(min(s))+' '
    elif i=='C':
        ans+=str(max(s))+' '
    else:
        for i in s:
            if i != max(s) and i != min(s):
                ans+=str(i)+' '
ans.strip()
print(ans) 