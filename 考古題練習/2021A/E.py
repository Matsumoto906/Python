while True:
    try:
        s=int(input())
        if s==0:
            break
        s=str(bin(s))[2:]
        ans=0
        for i in s:
            if i=='1':
                ans+=1
        print('The parity of ',s,' is ',ans,' (mod 2).',sep='')
    except:
        break