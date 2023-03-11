def f(x):
    global num
    if x%n in p:
        num+=(p[x%n])
    else:
        num+=(str(x%n))
    if x//n==0:
        r=num[::-1]
        num=''
        return r
    else:
        return f(x//n)

def g(x):
    global key
    x=x[::-1]
    s=0
    for i in range(0,len(x)):
        if x[i] in turn:
            a=turn[x[i]]
            if a>=n:
                key=False
                break
            s+=a*n**i
        else:
            s+=int(x[i])*n**i
    return s
    
p={ 10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',
    18:'I',19:'J',20:'K',21:'L',22:'M',23:'N',24:'O'}
turn={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,
      'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'1':1,
      '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}

n,a,b=map(str,input().split())
n=int(n)
key=True
s1=g(a)
s2=g(b)
ans=s1*s2
num=''

if key==True:
    x=s1*turn[f(s2)[1]]
    y=s1*turn[f(s2)[0]]*n
    print(f(s1),f(s2),f(x),f(y),f(ans))
else:
    print('Error')