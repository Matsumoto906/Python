for t in range(int(input())):
    a=input()
    b=input()
    n=[]
    for i in a:
        if i in b:
            n.append(i)
    if len(n)==0:
        print('N')
        continue
    n=list(set(n))
    n.sort()
    for i in n:
        print(i,end='')
    print()