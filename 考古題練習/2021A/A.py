while True:
    try:
        a,b,c,d,e=map(int,input().split())
        ans=a*56+24*b+14*c+6*d+2*e
        print(ans)
    except:
        break