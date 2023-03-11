s=list(map(int,input().split()))
num=[]
n=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
ans=[]
k=int(len(s)/3)
for i in range(0,len(s),k):
    num.append(s[i:i+k])

for i in range(0,k):
    for j in range(0,3):
        n[i].append(num[j][i])

for i in n:
    for j in i:
        if j!=max(i) and j!=min(i):
            ans.append(j)
print([ans]*3)