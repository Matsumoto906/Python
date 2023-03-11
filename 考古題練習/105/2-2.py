import itertools

def f(a,b):
    if a%b==0:
        return b
    else:
        return f(b,a%b)

for t in range(int(input())):
    s=map(int,input().split(','))
    s = list(itertools.permutations(s,2))
    s=list(set(s))
    ans=0
    for i in s:
        a=max(i)
        b=min(i)
        if a==0 or b==0:
            continue
        k=f(a,b)
        if k>ans:
            ans=k
    print(ans)