ans=[]
for i in range(0,int(input())):
    d1=input().split('/')
    d2=input().split('/')
    y=int(d1[2])-int(d2[2])
    if (d2[0])+(d2[1])<(d1[0])+(d1[1]):
        y-=1
    ans.append(y)
for i in ans:
    print(i)