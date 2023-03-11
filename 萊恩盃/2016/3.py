a,b=map(str,input().split())
A=0
B=0
an=[]
bn=[]
for i in a:
    an.append(i)
for i in b:
    bn.append(i)

for i in range(0,4):
    if an[i]==bn[i]:
        an[i]='x'
        bn[i]='o'
        A+=1

for i in range(0,len(bn)):
    if bn[i] in an:
        B+=1
        an[i]='x'
        bn[i]='o'
print(A,'A',B,'B',sep='')