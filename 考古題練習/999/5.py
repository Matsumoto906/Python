while True:
    try:
        s=int(input())
        ans=0
        for i in range(1,s+1):
            if s%i==0:
                ans+=i
        print(ans)
    except:
        break