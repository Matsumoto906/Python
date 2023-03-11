s=list(map(int,input().split()))
num=[]
for i in range(0,len(s)-1):
    a=max(s[i+1:])
    num.append(a)
num+=[-1]
print(num)