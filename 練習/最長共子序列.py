num=[]
name=[]
s1=[[]]
s2=[[]]
a=input()
b=input()
for i in a:
    s1.append(i)
for i in b:
    s2.append(i)
for i in range(0,len(s2)):
    num.append([])
    name.append([])
    for j in range(0,len(s1)):
        num[i].append(0)
        name[i].append('')
for i in range(0,len(s2)):
    for j in range(0,len(s1)):
        if s2[i]==s1[j]:
            num[i][j]=num[i-1][j-1]+1
            name[i][j]=name[i-1][j-1]+s2[i]
        else:
            if num[i-1][j]>num[i][j-1]:
                num[i][j]=num[i-1][j]
                name[i][j]=name[i-1][j]
            else:
                num[i][j]=num[i][j-1]
                name[i][j]=num[i][j-1]
print(num)
print(name)