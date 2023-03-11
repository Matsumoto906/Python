def f(x):
    global con
    con+=1
    a=0
    b=str(x)
    for i in b:
        a+=int(i)
    if str(a)=='9':
        return con
    else:
        return f(a)


con=0
s=int(input())
if s%9==0:
    print('Y',f(s))
else:
    print('N')
