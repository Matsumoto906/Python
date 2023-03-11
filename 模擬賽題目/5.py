def f(x):
    global ans
    for i in s:
        if x >= i:
            x-=i
            ans+=1
            break
    if x==0:
        return ans
    else:
        return f(x)

s=list(map(int,input().split()))
a=s.pop(0)
b=s.pop(0)
n=a-b
s.sort()
s.reverse()
ans=0
print(f(n))