star_num=[]
new_num=[]
ans=[]
n=[]

#建立二維矩陣並將值加入
s=list(map(str,input().split()))
l=len(s)
for i in range(3):
    star_num+=[[]]
k=0
for i in range(0,3):
    for j in range(0,int(len(s)//3)):
        star_num[i].append(s[k])
        k+=1

#
a=len(star_num[0])
for i in range(0,a):
    for j in range(0,3):
        new_num.append(int(star_num[j][i]))
k=0
for i in range(0,len(new_num)//3):
    n.append([new_num[k],new_num[k+1],new_num[k+2]])
    k+=3
#找出中間值
for i in range(0,len(n)):
    n[i].remove(max(n[i]))
    n[i].remove(min(n[i]))
    ans.append(n[i][0])
print([ans]*3)
