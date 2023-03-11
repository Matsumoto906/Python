f=[0,1]
for i in range(2,10001):
    f.append(f[i-1]+f[i-2])

def gcd(a,b):
    x=max(a,b)
    y=min(a,b)
    if x%y==0:
        return y
    else:
        return gcd(y,x%y)

def lcm(a,b):
    x=max(a,b)
    y=min(a,b)
    for i in range(x,x*y+1):
        if i%x==0 and i%y==0:
            return i

a,b=map(int,input().split())
a=f[a]
b=f[b]
print(gcd(a,b),lcm(a,b))