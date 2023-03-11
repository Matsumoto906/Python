tree=[]
v=[]

def btree(x,ip):
    x=x.split()
    ipa=-1
    ipb=-1
    tree[ip]=int(x[0])

    for i in range(0,len(x)):#找到距離小於根最近的點
        if x[i]<x[0]:
            ipa=i
            break
    for i in range(0,len(x)):#找到距離大於跟最近的點
        if x[i]>x[0]:
            ipb=i
            break

    if ipa!=-1 and ipb!=-1:#有大有小
        sa=' '.join(x[ipa:ipb])
        btree(sa,ip*2+1)
        sb=' '.join(x[ipb:])
        btree(sb,ip*2+2)
    elif ipa!=-1:#只有小
        sa=' '.join(x[ipa:])
        btree(sa,ip*2+1)
    elif ipb!=-1:#只有大
        sa=' '.join(x[ipb:])
        btree(sa,ip*2+2)

def f(key,r):
    v.append(str(tree[r]))
    if key<tree[r]:
        f(key,r*2+1)
    elif key>tree[r]:
        f(key,r*2+2)

n,m=map(int,input().split(','))
for i in range(0,2**n): #填滿樹
    tree.append(-1)
s2=input()
btree(s2,0)
f(m,0)
print(len(v))
s3='>'.join(v)
v.clear()
f(max(tree),0)
print(len(v))
print(s3)