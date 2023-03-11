dic={'J':11,'Q':12,'K':13,'A':1}
ans=0
for i in range(5):
    s=input()
    if s in dic:
        ans+=dic[s]
    else:
        ans+=int(s)
print(ans)