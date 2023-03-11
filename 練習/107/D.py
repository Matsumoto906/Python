import itertools
for t in range(int(input())):
    s=list(map(int,input().split(',')))
    n=s.pop(0)
    k=s.pop(-1)
    a=''
    s=list(itertools.permutations(s))
    
    ans=str(s[k-1])[1:-1].split(', ')
    for i in ans:
        a+=(i)
    a.zfill(n)
    print(a)