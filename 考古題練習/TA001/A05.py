while True:
    try:
        x,y,z=map(int,input().split())
        tot=(x+y+z)//2
        j=tot-x
        a=tot-y
        b=tot-z
        print(a,b,j)
    except:
        break