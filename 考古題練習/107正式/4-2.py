cyc=[]
k=[]
used=[]
data=[]
def f(n):
    cyc.append(n)
    used[n]=1
    if ip[n] not in cyc:
        f(ip[n])
for k in range(0,int(input())):
    s=input()
    s=s[1:len(s)-1]
    ip=list(map(int,s.split(',')))
    ip=[0]+ip
    k=[]
    used=[]
    data=[]
    for i in range(0,len(ip)):
        k.append(i)
        used.append(0)
    for i in range(1,len(k)):
        if used[i]==0:
            cyc=[]
            f(i)
            data.append(cyc)
    print(data)