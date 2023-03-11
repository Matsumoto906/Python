while True:
    s=int(input())
    num=[]
    ans=0
    if s == 0:
        break
    for i in range(s):
        a=int(input())
        num.append(a)
    for i in range(1,len(num)):
        for j in range(0,i):
            if num[i]<num[j]:
                ans+=1
    print(ans)