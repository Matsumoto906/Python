s=list(map(int,input().split()))
s.sort()
num=[]
ans=[]

for i in s:
    num.append(str(i).zfill(2))
for i in range(0,len(num)-1):
    ans.append(num[i][1]+num[i+1][1])
ans.append(ans[-2]+ans[-1][1])
for i in ans:
    if i != ans[-1]:
        print(i,end=' ')
    else:
        print(i)