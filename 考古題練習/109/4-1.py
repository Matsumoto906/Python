while True:
    try:
        s=list(map(int,input().split()))
        m=s[0]
        s.remove(s[0])
        s.remove(s[0])
        ans=0
        s=sorted(s,reverse=True)
        
        for i in s:
            tot=i
            for j in s:
                if i !=j:
                    tot+=j
                    if tot<=m and tot>ans:
                        ans=tot
                    if tot>m:
                        tot-=j
        print(ans)
    except:
        break