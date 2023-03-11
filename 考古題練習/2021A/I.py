while True:
    s=int(input())
    num=[]
    ans=0
    if s==0:
        break
    for i in range(s):
        num.append(int(input()))
    for i in range(0,len(num)):
        for j in range(0,len(num)):
            if num[i]>num[j] and i<j:
                ans+=1
    print(ans)