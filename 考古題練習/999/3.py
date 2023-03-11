a,b=map(int,input().split())
num=[]
for i in range(a):
    s=list(map(int,input().split()))
    num.append(max(s))
print(max(num))