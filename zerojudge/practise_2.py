while  True:
    try:
        a,b=map(str,input().split())
        x=[]
        y=[]
        n=[]
        for i in a:
            x.append(i)
        for i in b:
            y.append(i)
        for i in y:
            if i in x and i not in n:
                n.append(i)
        x=list(set(x))
        x.sort()
        y.sort()
        print(x)
        print(n)
        
    except:
        break