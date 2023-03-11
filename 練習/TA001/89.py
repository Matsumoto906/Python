s=list(map(int,input().split()))
k=int(len(s)**0.5)
num=[]
for i in range(0,len(s),k):
    num.append(s[i:i+k])
for i in range(0,len(num)):
    for j in range(0,len(num)):
        if num[i][j]==num[j][i]:
            key=True
        else:
            key=False
            break
    if key==False:
        break
print(key)