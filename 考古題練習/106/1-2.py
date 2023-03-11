ro={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
for t in range(int(input())):
    s=(input())
    ans=0
    num=[]
    for i in s:
        num.append(ro[i])
    for i in range(0,len(num)):
        if num[i] == 0:
            continue
        elif num[i]!=num[-1]:
            if num[i] < num[i+1]:
                ans+=num[i+1]-num[i]
                num[i+1]=0
            else:
                ans+=num[i]
        else:
            ans+=num[i]
    print(ans)