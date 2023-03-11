
def f(x):
    g=['0','1']
    for i in range(1,x):
        a=[]
        b=[]
        for j in g:
            a.append('0'+j)
        g.reverse()
        for j in g:
            b.append('1'+j)
        g=a+b
    return g

s=int(input())
a=(f(s))
for i in a:
    print(i)