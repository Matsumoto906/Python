for t in range(int(input())):
    a,b=map(str,input().split('/'))
    a=list(map(int,a.split('.')))
    b=list(map(int,b.split('.')))
    for i in range(0,3):
        print(a[i]&b[i],end='.')
    print(a[3]&b[3],end='/')
    for i in range(0,3):
        print(256+(a[i] | (~b[i])),end='.')
    print(256+(a[3] | (~b[3])))