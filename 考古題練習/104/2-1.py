import itertools
ans=[]
for t in range(int(input())):
    s,a,b=map(int,input().split(','))
    s = list(itertools.permutations(str(s)))
    num=[]
    for j in s:
        k=''
        for i in range(0,len(j)):
            k+=(j[i])
        num.append(str(k))
    n=(int(num[a-1])+int(num[b-1]))
    ans.append(n)
for i in ans:
    print(i)