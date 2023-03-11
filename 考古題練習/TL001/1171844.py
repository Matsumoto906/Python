az=[]
ans=[]
num='123456789'
for i in range(97,123):
    az.append(chr(i))
s=input()
for i in range(0,len(s)):
    if s[i] in az:
        ans.append(s[i])
        if i != len(s)-1:
            if s[i+1] in num:
                k=int(s[i+1])
                ans.append(chr(ord(s[i])+k))
for i in ans:
    print(i,end='')