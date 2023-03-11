import itertools
for t in range(int(input())):
    s=list(map(int,input().split(',')))
    n=s.pop(len(s)-1)
    a=s.pop(0)
    s=list(itertools.permutations(s,r=a))
    s.sort()
    ans=(s[n-1])
    a=''
    for i in ans:
        a+=str(i)
    print(a)