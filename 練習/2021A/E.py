while True:
    a=int(input())
    if a==0:
        break
    s=bin(a)[2:]
    ans=0
    for i in s:
        if i=='1':
            ans+=1
    print('The parity of ',a,' is ',s,' (mod 2).',sep='')