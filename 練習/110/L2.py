tree=[]
def btree(key,node):
    x=list(map(int,key.split(',')))
    tree[node]=x[0]
    pa=-1
    pb=-1
    for i in range(1,len(x)):
        if x[i]<x[0]:
            pa=i
            break
    for i in range(1,len(x)):
        if x[i]>x[0]:
            pb=i
            break
    sa=[]
    sb=[]
    if pa!=-1 and pb!=-1:
        for i in range(pa,len(x)):
            if x[i]<=x[pa]:
                sa.append(str(x[i]))
        for i in range(pb,len(x)):
            if x[i]>=x[pb]:
                sb.append(str(x[i]))
        btree(','.join(sa),node*2+1)
        btree(','.join(sb),node*2+2)
    elif pa!=-1:
        for i in range(pa,len(x)):
            if x[i]<=x[pa]:
                sa.append(str(x[i]))
        btree(','.join(sa),node*2+1)
    elif pb!=-1:
        for i in range(pb,len(x)):
            if x[i]>=x[pb]:
                sb.append(str(x[i]))
        btree(','.join(sb),node*2+2)

def f(node):
    if tree[2*node+1]!=None:
        f(2*node+1)
    print(tree[node])
    if tree[2*node+2]!=None:
        f(2*node+2)

s1='9,4,1,5,12,11,10,15,2,3'
k=len(s1.split(','))
for i in range(0,2**k):
    tree.append(None)
btree(s1,0)
f(0)
