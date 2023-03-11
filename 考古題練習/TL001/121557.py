s=(input().lower()).split()
ans=[]
for i in s:
    i=i[::-1]  
    ans.append(i)
for i in ans:
    if i != ans[-1]:
        print(i,end=' ')
    else:
        print(i)