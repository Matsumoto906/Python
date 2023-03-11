s=str(input())
ans=0
for i in range(0,len((s))):
    ans += int(s[i])**len(s)
if int(s)==ans:
    print('True')
else:
    print('False')