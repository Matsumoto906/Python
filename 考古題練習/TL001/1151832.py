az=[]
for i in range(97,123):
    az.append(chr(i))
s=input()
ans=[]
for i in s:
    if i not in ans and i in az:
        ans.append(i)

if len(ans) == len(az):
    print(True)
else:
    print(False)