import itertools
for t in range(int(input())):
    s,j,k=map(int,input().split(','))
    s = list(itertools.permutations(str(s)))
    a=0
    b=0
    j=s[j-1]
    k=s[k-1]
    for i in j:
        if i in k:
            if j.index(i)==k.index(i):
                a+=1
            else:
                b+=1
    print(a,'A',b,'B',sep='')