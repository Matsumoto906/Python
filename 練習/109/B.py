for t in range(int(input())):
    s=input()
    a=''
    b=[]
    ans=0
    for i in range(0,len(s)):
        if s[i] == '4':
            b.append('1'+'0'*(len(s)-i-1))
            a+='3'
        else:
            a+=s[i]
    for i in b:
        ans+=int(i)
    print(int(a),ans)