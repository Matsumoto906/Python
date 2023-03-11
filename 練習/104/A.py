for t in range(int(input())):
    input()
    ans=0
    num=list(map(int,input().split(',')))
    for i in range(0,len(num)-1):
        if num[i]>num[i+1]:
            ans+=10*(num[i]-num[i+1])
        elif num[i]<num[i+1]:
            ans+=20*(num[i+1]-num[i])
    print(ans)