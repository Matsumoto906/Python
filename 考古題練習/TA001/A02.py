while True:
    try:
        a,b=map(int,input().split())
        ans=round(a/(b/100)**2,2)
        print(ans)
    except:
        break