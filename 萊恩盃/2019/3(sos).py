s=list(map(int,input().split()))
num=[[],[],[]]
for i in range(0,3):
    for j in range(3):
        num[i].append(0)
for i in range(0,3):
    for j in range(0,3):
        num[i][j]=s[i*3+j]
print(num)