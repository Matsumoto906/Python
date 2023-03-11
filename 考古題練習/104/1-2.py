h=int(input())
bi=input().split(',')
p=[]
for t in range(h):
    num=[]
    s=input().split(',')
    for i in s:
        a=s.copy()
        a.remove(i)
        num.append(a)
    ans=[]
    for i in num:
        k=0
        b=0
        for j in i:
            if j in bi:
                k+=1
        ans.append(k)
    a1=0
    a2=0
    a3=0
    a4=0
    for i in ans:
        if i==2:
            a1+=1
        elif i==3:
            a2+=1
        elif i==4:
            a3+=1
        elif i==5:
            a4+=1
    p.append((a1,a2,a3,a4))
for i in p:
    for j in range(4):
        if j != 3:
            print(i[j],end=',')
        else:
            print(i[j])