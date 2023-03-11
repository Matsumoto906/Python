q=['q','w','e','r','t','y','u','i','o','p']
a=['a','s','d','f','g','h','j','k','l']
z=['z','c','x','v','b','n','m']
ans=0
s=(input().lower()).split()
for i in s:
    qn=0
    an=0
    zn=0
    for j in i:
        if j in q:
            qn+=1
        elif j in a:
            an+=1
        elif j in z:
            zn+=1
    if qn == len(i):
        ans+=1
    elif an == len(i):
        ans+=1
    elif zn == len(i):
        ans+=1
print(ans)