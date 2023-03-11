while True:
    try:
        a,b,c=map(int,input().split())
        ans=a*24+b*14+c*6
        print(ans)
    except:
        break