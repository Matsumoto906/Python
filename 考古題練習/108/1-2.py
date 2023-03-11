sc=[]
sp=[]
st=[]
ans=0
for t in range(int(input())):
    sp.clear()
    st.clear()
    b1=0
    b2=0
    con=0
    sc=[0]
    s=input().split()
    s=['0']+s
    for i in range(1,len(s)):
        if '9'>=s[i]>='0':
            sc.append(int(s[i]))
            con+=0.5
        elif s[i]=='/':
            sc.append(10-int(sc[i-1]))
            sp.append(i)
            con+=0.5
        elif s[i]=='X':
            sc.append(10)
            con+=1
            st.append(i)
    top=len(sc)-1
    for i in sp:
        if i<=top-1:
            b1+=sc[i+1]
    for i in st:
        if i<=top-2:
            b2+=sc[i+1]+sc[i+2]
    ans=sum(sc)+b1+b2
    if top-1 in sp and con > 10:
        ans-=sc[-1]
    if top-2 in st and con > 10:
        ans-=sc[-1]+sc[-2]
    print(ans)