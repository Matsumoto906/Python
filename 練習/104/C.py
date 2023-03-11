import itertools
for t in range(int(input())):
    a,b,c=map(int,input().split(','))
    a=str(a)
    k=list(itertools.permutations(a))
    x=''
    y=''
    for i in k[b-1]:
        x+=i
    for i in k[c-1]:
        y+=i
    print(int(x)+int(y))