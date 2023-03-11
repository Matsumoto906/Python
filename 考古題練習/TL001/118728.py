a=int(input())
b=int(input())
ans=[]
for k in range(a,b+1):
    key=True
    for i in str(k):
        if i =='0':
            key=False
            break
        if k % int(i) != 0:
            key=False
            break
    if key==True:
        ans.append(k)
print(ans)