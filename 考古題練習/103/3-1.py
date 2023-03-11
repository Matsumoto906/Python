for t in range(int(input())):
    s=list(map(int,input().split()))
    s.sort()
    n=[]
    k=0

    for i in range(0,5):#桐花順
        if s[i]+1==s[i+1]:
            k+=1
    if k==4:
        print(7)
        continue
    if 1 in s and 10 in s and 11 in s and 12 in s and 13 in s:
        k=5
    elif 14 in s and 23 in s and 24 in s and 25 in s and 26 in s:
        k=5
    elif 27 in s and 36 in s and 37 in s and 38 in s and 39 in s:
        k=5
    elif 40 in s and 49 in s and 50 in s and 51 in s and 52 in s:
        k=5
    if k==5:
        print(7)
        continue
    k=0
    for i in s:
        n.append(i%13)
    n.sort()
    for i in range(0,5):#四條
        if n[i]==n[i+1]:
            k+=1
        else:
            k=0
    if k==3:
        print(6)
        continue

