while True:
    try:
        a,b=map(int,input().split())
        ans=a/(b/100)**2
        ans=round(ans,2)
        print(ans)
    except:
        break