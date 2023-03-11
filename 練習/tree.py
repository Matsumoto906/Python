def heap(x,node):
    if tree[node]==None:
        tree[node]=x
    elif x>tree[node]:
        heap(x,node*2+2)
    elif x<tree[node]:
        heap(x,node*2+1)

def f(x):
    if tree[x*2+1]!=None:
        f(x*2+1)
    if tree[x*2+2]!=None:
        f(x*2+2)
    ans.append(tree[x])

for t in range(int(input())):
    input()
    tree=[]
    ans=[]
    s=list(map(int,input().split(',')))
    for i in range(0,2**(len(s)+1)):
        tree.append(None)
    for i in s:
        heap(i,0)
    f(0)
    print()
    for i in ans:
        if i != ans[-1]:
            print(i,end=' ')
        else:
            print(i)