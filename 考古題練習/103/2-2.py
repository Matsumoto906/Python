ans=[]
for t in range(int(input())):
    a=input().split()
    b=input().split()
    num=[]
    a.remove(a[0])
    b.remove(b[0])
    for i in a:
        if i in b:
            num.append(i)
    num=list(set(num))
    ans.append(len(num))
    print(len(num))
#for i in ans:
 #   print(i)