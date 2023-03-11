while True:
    try:
        s=list(map(int,input().split()))
        A=[]
        B=[]
        C=[]
        a=s[0]
        b=s[2]
        d=s[3]

        for i in range(0,a):
            A.append([])
        for i in range(0,b):
            B.append([])
        for i in range(0,a):
            C.append([])

        for i in range(0,a):
            s=list(map(int,input().split()))
            for j in s:
                A[i].append(j)

        for i in range(0,b):
            s=list(map(int,input().split()))
            for j in s:
                B[i].append(j)

        for i in range(0,a):
            for j in range(0,d):
                C[i].append('0')

        for i in range(0,a):
            for j in range(0,d):
                tot=0
                for n in range(0,b):
                    tot+=A[i][n]*B[n][j]
                C[i][j]=str(tot)
        for i in range(0,a):
            print(' '.join(C[i]))
    except:
        break