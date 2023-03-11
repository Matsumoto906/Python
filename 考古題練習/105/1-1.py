az=[]
for i in range(65,123):
    az.append(chr(i))


for k in range(int(input())):
    s=input()
    s=s.lower()
    ans=1
    for i in range(0,len(s)-1):
        if s[i]==' ':
            if s[i+1] in az:
                ans+=1
        elif s[i]==',':
             if s[i+1] in az:
                ans+=1
        elif s[i]=='!':
            if s[i+1] in az:
                ans+=1
        elif s[i]==';':
            if s[i+1] in az:
                ans+=1
        elif s[i]=='.':
            if s[i+1] in az:
                ans+=1
    print(ans)