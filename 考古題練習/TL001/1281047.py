s=input().split()
key=1
while True:
        if key==False:
            break
        for i in range(0,len(s)-1):
            if s[i] == s[i+1]:
                a=s.pop(s[i])
                a=s.pop(s[i])
                key=True
                break
            key=False
print(s)