def f(x):
    a=[]
    b=[]
    g=['0','1']
    for i in range(1,x):
        a.clear()
        b.clear()
        for j in g:
            a.append('0'+j)
        g.reverse()
        for j in g:
            b.append('1'+j)
        g=a+b
    for i in g:
        print(i)
f(int(input()))