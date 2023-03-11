def f(x,y):
    r.append(x)
    keya=(x*10)//y
    cb=(x*10)%y
    num2.append(str(keya))
    if cb != 0:
        if cb in r:
            s=''
            s=s.join(num2)
            n=r.index(cb)
            s=s[0:n]+'('+s[n:]+')'
            print(num1,'.',s,sep='')
        elif len(num2)<50:
            f(cb,y)
        elif len(num2)==50:
            s=''
            s=s.join(num2)
            print(num1,'.(',s,'...)',sep='')
        else:
            s=''
            s=s.join(num2)
            print(num1,'.',s,'(0)',sep='')
for i in range(int(input())):
    a,b=map(int,input().split())
    r=[]
    num1=a//b
    num2=[]
    f(a%b,b)