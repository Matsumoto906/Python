ans=[]
for t in range(int(input())):
    s=int(input())
    s=(str(bin(s))[2:])
    n=0
    for i in s:
        if i == '1':
            n+=1
    ans.append(n)
for i in ans:
    print(i)