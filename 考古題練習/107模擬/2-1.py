import itertools
for i in range(int(input())):
    s=list(map(int,input().split(',')))
    s.sort()
    s=list(itertools.permutations(s))
    for i in s[-2]:
        print(i,end='')
    print()