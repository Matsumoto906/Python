tree=[]
def heap(x,node):
    if tree[node]==None:
        tree[node]=x
    elif x<tree[node]:
        heap(x,node*2+1)
    elif x>tree[node]:
        heap(x,node*2+2)

def f(node):
    if tree[node]!=None:
        ans.append(tree[node])
    if tree[2*node+1]!=None:
        f(2*node+1)
    if tree[2*node+2]!=None:
        f(2*node+2)

ans=[]
s=list(map(int,input().split(',')))
for i in range(0,len(s)**(2+1)):
    tree.append(None)
for i in s:
    heap(i,0)
f(0)
for i in ans:
    if i != ans[-1]:
        print(i,end=' ')
    else:
        print(i)