def lu(a,b):
    while a>=0 and b>=0:
        a-=1
        b-=1
        num.append([a,b])

def ru(a,b):
    while a>=0 and b<=8:
        a-=1
        b+=1
        num.append([a,b])

def ld(a,b):
    while a<=8 and b>=0:
        a+=1
        b-=1
        num.append([a,b])

def rd(a,b):
    while a<=8 and b<=8:
        a+=1
        b+=1
        num.append([a,b])

for t in range(int(input())):
    num=[]
    a,b,x,y=map(int,input().split())
    lu(a,b)
    ru(a,b)
    ld(a,b)
    rd(a,b)
    if [a,b] == [x,y]:
        print(0)
    elif [x,y] in num or a==x or b==y:
        print(1)
    else:
        print(2)