def f(x):
    return str(bin(int(x)))[2:]

def g(x):
    global cnt,ga
    if cnt == 5:
        return ga
    x='0.'+x
    x=float(x)*2
    ga+=str(x)[0]
    if x==0:
        ga+='0'*(5-cnt)
        return ga
    x=(str(x).split('.'))[1]
    cnt+=1
    return g(x)


for t in range(int(input())):
    a,b=map(str,input().split('.'))
    ans=''
    ga=''
    cnt=0
    ans+=f(a)+'.'+g(b)
    ans=float(ans)
    print('%.5f'%ans)