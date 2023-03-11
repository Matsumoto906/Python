while True:
    try:
        s=list(map(int,input().split(', ')))
        s=sorted(s,reverse=True)
        print(s)
    except:
        break