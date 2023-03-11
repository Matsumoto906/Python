def f(x):
    key=True
    for i in range(0,len(num)):
        if x%num[i]==0:
            key=False
            break
    return key
 
def g(x):
    ans=0
    for i in range(4,x+1):
        if f(i)==True:
            num.append(i)
    for i in num:
        for j in num:
            if i+j==x:
                ans+=1
    return ans

num=[2,3]
k=[]
a,b=map(int,input().split(','))
for i in range(a,b+1):
    if i%2==0:
        print(i,g(i))
        k.append(g(i))

if 0 not in k:
    print('哥德巴赫猜想可能是對的')
else:
    print('哥德巴赫猜想是錯的')