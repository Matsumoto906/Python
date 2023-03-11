for t in range(int(input())):
    s=input()
    ans=0
    con=0
    for i in s:
        if i == 'O':
            con+=1
            ans+=con
        else:
            con=0
    print(ans)