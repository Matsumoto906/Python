while True:
    try:
        s=list(map(int,input().split(', ')))
        for j in range(0,2):
            for i in range(0,len(s)-1):
                if s[i] > s[i+1]:
                    k=s[i]
                    s[i]=s[i+1]
                    s[i+1]=k
        print(s)
    except:
        break