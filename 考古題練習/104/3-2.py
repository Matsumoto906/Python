for t in range(int(input())):
    a,b,c,d=map(int,input().split(','))
    A=[]
    B=[]
    C=[]
    for i in range(a):
        A.append([])
    for i in range(c):
        B.append([])
    for i in range(a):
        C.append([])
    
    for i in range(0,a):
        s=list(map(int,input().split()))
        A[i]=s
    for i in range(0,c):
        s=list(map(int,input().split()))
        B[i]=s
    for i in range(0,a):
        s=list(map(int,input().split()))
        C[i]=s

    for i in range(0,len(A)):
        for j in range(0,len(A[i])):
            if A[i][j]==9999:
                x=i
                y=j
                k=1
    for i in range(0,len(B)):
        for j in range(0,len(B[i])):
            if B[i][j]==9999:
                x=i
                y=j
                k=2

    m=0+x
    if k==1:
        n=0
        while B[y][m]==0:
            m+=1
        for i in range(0,b):
            if A[x][i]!=9999:
                n+=A[x][i]*B[i][m]
        n=C[x][m]+(n*(-1))
        ans=n // B[y][m]
        print(ans)

    elif k==2:
        n=0
        while A[m][x]==0:
            m+=1
        for i in range(0,b):
            if B[i][y]!=9999:
                n+=B[i][y]*A[m][i]
        n=C[m][y]+(n*(-1))
        ans=n // A[m][x]
        print(ans)