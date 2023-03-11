for t in range(int(input())):
    a=input()
    b=input()
    ans=0
    for i in range(0,len(a)):
        if a[i]!=b[i]:
            ans+=1
    print(ans)