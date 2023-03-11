s=list(map(float,input().split()))
ans=[]
s.remove(s[-1])
for i in range(1,len(s)+1):
    k=0
    for j in range(0,i):
        k+=s[j]
    k=round(k/i,2)
    ans.append(k)
for i in ans:
    if i != ans[-1]:
        print('%.2f'%i,end=' ')
    else:
        print('%.2f'%i)