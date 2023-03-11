#建立二維矩陣並將值加入
num=[]
s=list(map(str,input().split()))
for i in range(int(len(s)**0.5)):
    num+=[[]]
k=0
for i in range(0,int(len(s)**0.5)):
    for j in range(0,int(len(s)**0.5)):
        num[i]+=s[k]
        k+=1

#判斷num[i][j]是否=num[j][i]
key=True
for i in range(0,len(num)):
    for j in range(0,len(str(i))):
        if num[i][j]!=num[j][i]:
            key=False
            break
print(key)