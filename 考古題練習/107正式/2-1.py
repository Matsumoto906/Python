def f(x):
    x=str(x)
    if x=='4':
        return 'F'
    a=0
    for i in x:
        a+=int(i)**2
    if a!=1:
        return f(a)
    else:
        return 'T'


for i in range(int(input())):
    s=(input())
    print(f(s))