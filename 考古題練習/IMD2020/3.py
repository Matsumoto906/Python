s=list(map(int,input().split(',')))
a=s.pop(0)
b=s.pop(0)
num=[]
ans=[]
con=0
for i in range(a):
    num.append([])
for i in range(0,len(s),b):
    num[con]=s[i:i+b]
    con+=1

for i in range(0,a-2):
    for j in range(0,b-2):
        ans.append(num[i][j]+num[i][j+1]*-1+num[i][j+2]+
        num[i+1][j]*-1+num[i+1][j+1]+num[i+1][j+2]*-1+
        num[i+2][j]+num[i+2][j+1]*-1+num[i+2][j+2])
print(max(ans))